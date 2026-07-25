"""Adam+L2 vs. AdamW: does the same weight-decay rate shrink every parameter
by the same amount?

Reconstructs the mechanism Loshchilov & Hutter, "Decoupled Weight Decay
Regularization" (arXiv:1711.05101), identify: folding an L2 penalty into the
gradient before Adam's per-parameter scaling makes the realized decay depend
on a parameter's own gradient history, while applying the decay term directly
to the weight (AdamW) does not. Both optimizers are implemented here from
their defining update rules (Kingma & Ba, arXiv:1412.6980, for the moment
estimates and bias correction; Loshchilov & Hutter for the two decay
placements) and run on two synthetic scalar parameters that share every
hyperparameter and differ only in the size of the gradient signal they saw
before the signal stopped.

Two phases, one weight decay rate (lambda = 0.05) throughout:
  1. Steps 1-50: each parameter receives a constant task gradient ("hot" =
     0.5, "quiet" = 0.02), building up Adam's second-moment estimate the way
     a frequently- vs. rarely-active weight would in training. No decay yet.
  2. Steps 51-250: the task gradient stops (as if that input pattern went
     quiet), and weight decay is switched on for both methods. What happens
     next is driven entirely by the decay term and by the second-moment
     history each parameter carries in from phase 1.

The trajectories are normalized to 1.0 at step 50 so the two methods can be
compared on the same axis regardless of where the burn-in left them.
"""

import math

import plotly.graph_objects as go

BETA1, BETA2, EPS = 0.9, 0.999, 1e-8
ALPHA = 0.05
LAMBDA = 0.05
BURN_IN = 50
TOTAL_STEPS = 250
THETA0 = 1.0


def simulate(method: str, burn_in_gradient: float) -> list[float]:
    """Run Adam-with-L2 ("l2") or AdamW ("adamw") for TOTAL_STEPS steps."""
    theta, m, v = THETA0, 0.0, 0.0
    trajectory = [theta]
    for t in range(1, TOTAL_STEPS + 1):
        task_gradient = burn_in_gradient if t <= BURN_IN else 0.0
        decay_active = LAMBDA if t > BURN_IN else 0.0
        if method == "l2":
            # L2 penalty folded into the gradient before Adam ever sees it:
            # the moment estimates below cannot tell the penalty apart from
            # the task signal.
            g = task_gradient + decay_active * theta
            m = BETA1 * m + (1 - BETA1) * g
            v = BETA2 * v + (1 - BETA2) * g * g
            m_hat = m / (1 - BETA1**t)
            v_hat = v / (1 - BETA2**t)
            theta = theta - ALPHA * m_hat / (math.sqrt(v_hat) + EPS)
        else:
            # AdamW: moments see only the task gradient; decay is a separate
            # term applied straight to the weight.
            g = task_gradient
            m = BETA1 * m + (1 - BETA1) * g
            v = BETA2 * v + (1 - BETA2) * g * g
            m_hat = m / (1 - BETA1**t)
            v_hat = v / (1 - BETA2**t)
            theta = theta - ALPHA * m_hat / (math.sqrt(v_hat) + EPS) - ALPHA * decay_active * theta
        trajectory.append(theta)
    return trajectory


series = {
    "Adam + L2, quiet parameter": simulate("l2", 0.02),
    "Adam + L2, hot parameter": simulate("l2", 0.5),
    "AdamW, quiet parameter": simulate("adamw", 0.02),
    "AdamW, hot parameter": simulate("adamw", 0.5),
}

steps_after_signal = list(range(0, TOTAL_STEPS - BURN_IN + 1))

fig = go.Figure()
for name, trajectory in series.items():
    baseline = trajectory[BURN_IN]
    normalized = [value / baseline for value in trajectory[BURN_IN:]]
    fig.add_trace(
        go.Scatter(
            name=name,
            x=steps_after_signal,
            y=normalized,
            mode="lines",
        )
    )

fig.update_layout(
    xaxis_title="steps after the task gradient stops (decay switched on here)",
    yaxis_title="θₜ / θ at signal-stop (fraction of value remaining)",
)
