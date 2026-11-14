"""Reduction in attack rate versus placebo, primary endpoint of each pivotal trial.

Data (all percent reduction in the drug arm's attack rate relative to placebo,
with the 95% CI the owner reports):
  HAELO, lonvo-z 50 mg once: 87 (78, 93). NEJM 2026 abstract; Intellia 12 Nov 2026
    deck slide 23. Counted weeks 5-28.
  HELP, lanadelumab 300 mg every 2 weeks: 87 (76, 93). TAKHZYRO label section 14,
    Table 3; JAMA 2018 abstract. Counted days 0-182.
  VANGUARD, garadacimab 200 mg monthly: 89.2 (75.6, 95.2). ANDEMBRY label section
    14, Table 4 (FDA analysis; the Lancet 2023 paper reports 87, CI 58 to 96).
  OASIS-HAE, donidalorsen 80 mg every 4 weeks: 81 (65, 89). DAWNZERA label section
    14, Table 4.
  APeX-2, berotralstat 150 mg daily: 44.2 (23.0, 59.5). ORLADEYO label section 14,
    Table 3; JACI 2021 abstract.
  COMPACT (C1-INH SC) is not plotted: the HAEGARDA label reports its primary result
    as a within-subject difference (-3.5 attacks a month) and its percentage as a
    median per-patient reduction (95%), neither of which is a rate ratio like the
    others, so a derived 1 - 0.52/4.03 would not compare like for like.
"""

import plotly.graph_objects as go

rows = [
    # name, reduction, lo, hi
    ("Lonvo-z", 87.0, 78.0, 93.0),
    ("Lanadelumab", 87.0, 76.0, 93.0),
    ("Garadacimab", 89.2, 75.6, 95.2),
    ("Donidalorsen", 81.0, 65.0, 89.0),
    ("Berotralstat", 44.2, 23.0, 59.5),
]
order = [r[0] for r in rows]

fig = go.Figure()
lonvo = rows[0]
others = rows[1:]

fig.add_trace(
    go.Scatter(
        x=[lonvo[1]],
        y=[lonvo[0]],
        mode="markers+text",
        cliponaxis=False,
        text=[f"{lonvo[1]:.0f}"],
        textposition="top center",
        textfont={"size": 36},
        marker={"symbol": "diamond", "size": 20},
        error_x={
            "type": "data",
            "symmetric": False,
            "array": [lonvo[3] - lonvo[1]],
            "arrayminus": [lonvo[1] - lonvo[2]],
            "thickness": 4,
            "width": 9,
        },
        name="Lonvo-z",
        showlegend=False,
    )
)
fig.add_trace(
    go.Scatter(
        x=[r[1] for r in others],
        y=[r[0] for r in others],
        mode="markers+text",
        cliponaxis=False,
        text=[f"{r[1]:g}" for r in others],
        textposition="top center",
        textfont={"size": 36},
        marker={"symbol": "circle", "size": 18},
        error_x={
            "type": "data",
            "symmetric": False,
            "array": [r[3] - r[1] for r in others],
            "arrayminus": [r[1] - r[2] for r in others],
            "thickness": 4,
            "width": 9,
        },
        name="Chronic prophylaxis",
        showlegend=False,
    )
)
fig.update_layout(
    font={"size": 36},
    margin={"t": 70, "r": 40, "b": 130, "l": 300},
    xaxis={
        "range": [0, 100],
        "title": {"text": "Attack-rate reduction vs placebo, % (bars: 95% CI)", "font": {"size": 36}},
        "tickfont": {"size": 36},
        "dtick": 20,
    },
    yaxis={
        "categoryorder": "array",
        "categoryarray": order[::-1],
        "tickfont": {"size": 38},
        "gridcolor": "#f3f5f8",
    },
)
