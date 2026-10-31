"""Accuracy against cost per problem for the AstaBench leaderboard (test split).

Data: Ai2's live AstaBench leaderboard, "AstaBench Overall Leaderboard
(Aggregate)", Test Set tab, retrieved 2026-10-31 from
https://allenai.org/asta/leaderboard. Score is the board's Overall Score (0-1,
shown here x100); cost is its Overall Cost in USD per problem. The 23 agents
that attempt all four categories; the 24th costed row (Smolagents Coder with
Llama 4 Scout, 3 of 4 categories) is left out. `frontier` marks the 11 agents
the board flags with its Pareto icon.
"""

import math

import plotly.graph_objects as go

# (scaffold, model, score 0-1, cost USD per problem, on board frontier)
ROWS = [
    ("ReAct", "claude-opus-4-7", 0.5804, 3.5422, True),
    ("ReAct", "claude-opus-4-6", 0.5533, 2.1851, True),
    ("ReAct", "claude-sonnet-4-6", 0.5447, 2.0755, True),
    ("ReAct", "gpt-5.5", 0.5287, 1.6104, True),
    ("Asta v0", "mixture, Claude Sonnet 4 and 6 others", 0.5090, 3.3950, False),
    ("ReAct", "gemini-3.1-pro", 0.4958, 1.2551, True),
    ("ReAct", "gpt-5.4", 0.4648, 0.7006, True),
    ("ReAct", "GPT-5", 0.4332, 0.3090, True),
    ("ReAct", "o3", 0.3783, 0.1635, True),
    ("ReAct", "Claude Sonnet 4", 0.3746, 0.3965, False),
    ("Smolagents Coder", "GPT-5", 0.3535, 0.1265, True),
    ("Smolagents Coder", "Claude Sonnet 4", 0.3494, 1.0239, False),
    ("ReAct", "GPT-5 Mini", 0.3136, 0.0366, True),
    ("ReAct", "GPT-4.1", 0.3040, 0.1985, False),
    ("Smolagents Coder", "GPT-4.1", 0.2998, 0.3212, False),
    ("Smolagents Coder", "GPT-5 Mini", 0.2704, 0.0648, False),
    ("Smolagents Coder", "Gemini 2.5 Flash", 0.2450, 0.7088, False),
    ("ReAct", "Claude 3.5 Haiku", 0.2140, 0.0359, True),
    ("ReAct", "GPT-4o", 0.1617, 0.1223, False),
    ("ReAct", "Gemini 2.5 Flash", 0.1524, 0.7107, False),
    ("Smolagents Coder", "GPT-4o", 0.1311, 0.3588, False),
    ("Smolagents Coder", "Claude 3.5 Haiku", 0.1214, 0.2974, False),
    ("ReAct", "Llama 4 Scout 17B", 0.0774, 0.6784, False),
]

SYMBOL = {"ReAct": "circle", "Smolagents Coder": "diamond", "Asta v0": "square"}

front = sorted((r for r in ROWS if r[4]), key=lambda r: r[3])

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        name="Frontier (11 agents)",
        x=[r[3] for r in front],
        y=[r[2] * 100 for r in front],
        mode="lines",
        line=dict(width=2, dash="dot", color="#3a6f8f"),
        hoverinfo="skip",
    )
)

for kind, on_front, label in [
    (True, True, "On the frontier"),
    (False, False, "Dominated"),
]:
    for scaffold in ("ReAct", "Smolagents Coder", "Asta v0"):
        pts = [r for r in ROWS if r[4] == on_front and r[0] == scaffold]
        if not pts:
            continue
        fig.add_trace(
            go.Scatter(
                name=f"{scaffold}, {label.lower()}",
                x=[r[3] for r in pts],
                y=[r[2] * 100 for r in pts],
                mode="markers",
                text=[f"{r[0]} / {r[1]}" for r in pts],
                hovertemplate="%{text}<br>score %{y:.1f}<br>$%{x:.4f} per problem<extra></extra>",
                marker=dict(
                    symbol=SYMBOL[scaffold],
                    size=12,
                    color="#3a6f8f" if on_front else "rgba(0,0,0,0)",
                    line=dict(width=2, color="#3a6f8f" if on_front else "#a24935"),
                ),
            )
        )

# (model key, label, ax, ay) offsets in pixels
LABELS = {
    ("ReAct", "claude-opus-4-7"): ("ReAct claude-opus-4-7", -40, -28),
    ("ReAct", "gpt-5.5"): ("ReAct gpt-5.5", -60, -26),
    ("Asta v0", "mixture, Claude Sonnet 4 and 6 others"): ("Asta v0", 40, 24),
    ("ReAct", "gpt-5.4"): ("ReAct gpt-5.4", -62, -22),
    ("ReAct", "GPT-5"): ("ReAct GPT-5", -52, -22),
    ("ReAct", "GPT-5 Mini"): ("ReAct GPT-5 Mini", -10, -34),
    ("ReAct", "Llama 4 Scout 17B"): ("ReAct Llama 4 Scout", 10, 28),
    ("ReAct", "Gemini 2.5 Flash"): ("ReAct Gemini 2.5 Flash", 54, 26),
}
for r in ROWS:
    key = (r[0], r[1])
    if key in LABELS:
        text, ax, ay = LABELS[key]
        fig.add_annotation(
            x=math.log10(r[3]),  # annotations on a log axis take log10 values
            y=r[2] * 100,
            xref="x",
            yref="y",
            text=text,
            showarrow=True,
            arrowhead=0,
            arrowwidth=1,
            ax=ax,
            ay=ay,
            font=dict(size=16),
        )

fig.update_layout(
    xaxis=dict(
        type="log",
        title="Overall cost per problem (USD, log scale)",
        tickvals=[0.03, 0.1, 0.3, 1, 3],
        ticktext=["$0.03", "$0.10", "$0.30", "$1", "$3"],
        range=[-1.6, 0.7],
    ),
    yaxis=dict(title="Overall score (points, board's 0-1 scale x 100)", range=[0, 66]),
    legend=dict(orientation="h", y=-0.24, x=0, font=dict(size=14)),
    font=dict(size=16),
    width=1100,
    height=720,
    margin=dict(l=80, r=30, t=20, b=170),
)
