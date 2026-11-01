"""Value of cell 13 as policy iteration and value iteration converge.

Both runs are on lesson 1's grid (slip 0.2, gamma 0.9) from the hand-drawn
policy's starting point (value iteration starts from v = 0). The numbers are the
printed output of control.py (uv run control.py):

Value iteration, v(13) after each sweep 0..18:
  0.0000, -1.0000, -1.9000, -2.7100, -3.4390, -1.9863, -1.3345, -0.9811,
  -0.8355, -0.7668, -0.7377, -0.7245, -0.7188, -0.7162, -0.7151, -0.7146,
  -0.7144, -0.7143, -0.7143

Policy iteration, v(13) after each evaluate-and-improve round 0..3:
  -2.0055, -1.8412, -0.7142, -0.7142

A policy-iteration round solves the full linear system once and takes one greedy
step; a value-iteration sweep is one cheap max pass over the 14 cells. The two
x-axes are plotted together as iteration count, not equal cost. The optimal
value is v_*(13) = -0.7142.
"""

import plotly.graph_objects as go

vi = [
    0.0000, -1.0000, -1.9000, -2.7100, -3.4390, -1.9863, -1.3345, -0.9811,
    -0.8355, -0.7668, -0.7377, -0.7245, -0.7188, -0.7162, -0.7151, -0.7146,
    -0.7144, -0.7143, -0.7143,
]
pi = [-2.0055, -1.8412, -0.7142, -0.7142]
v_star = -0.7142

fig = go.Figure()
fig.add_hline(
    y=v_star,
    line={"width": 1, "dash": "dot"},
    annotation_text="v*(13) = -0.71",
    annotation_position="bottom right",
)
fig.add_trace(
    go.Scatter(
        name="Value iteration (per sweep)",
        x=list(range(len(vi))),
        y=vi,
        mode="lines+markers",
    )
)
fig.add_trace(
    go.Scatter(
        name="Policy iteration (per round)",
        x=list(range(len(pi))),
        y=pi,
        mode="lines+markers",
    )
)
fig.update_layout(
    xaxis_title="iteration (value-iteration sweep, or policy-iteration round)",
    yaxis_title="value of cell 13",
    legend={"yanchor": "bottom", "y": 0.04, "xanchor": "right", "x": 0.98},
    margin={"t": 12},
)
fig.update_xaxes(dtick=2)
