"""Attack rate and number of patients behind it, lonvo-z integrated analysis.

Source: Intellia investor deck "Readying Lonvo-z for Patients with HAE", 12 Nov
2026 (SEC Exhibit 99.1), slide 31. 93 patients given one 50 mg dose in Phase 1/2
or HAELO; no control arm; one month = 28 days.

Mean monthly attack rate was read from the slide's plot: 3.3 at baseline, about
0.3 at month 6, 0.2 at month 12, 0.1 at month 24, 0.0 from month 35 (shown at
month 36). Patients who had reached each month come from the slide's at-risk
row: 93 at baseline and month 1, 81 at month 2, 71 at month 6, 24 at month 12,
16 at month 24, 10 at month 36, 4 at month 41 and later.
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots

rate_x = [0, 6, 12, 24, 36]
rate_y = [3.3, 0.3, 0.2, 0.1, 0.0]
risk_x = [0, 2, 6, 12, 24, 36, 41]
risk_y = [93, 81, 71, 24, 16, 10, 4]

fig = make_subplots(
    rows=2,
    cols=1,
    shared_xaxes=True,
    vertical_spacing=0.12,
    row_heights=[0.5, 0.5],
    subplot_titles=(
        "Mean attacks per month (approximate, read from slide 31)",
        "Patients who have reached each month",
    ),
)
fig.add_trace(
    go.Scatter(
        x=rate_x,
        y=rate_y,
        mode="lines+markers+text",
        text=["3.3"] + [f"~{v:g}" for v in rate_y[1:]],
        textposition="top right",
        textfont={"size": 34},
        marker={"size": 16},
        line={"width": 4},
        showlegend=False,
    ),
    row=1,
    col=1,
)
fig.add_trace(
    go.Bar(
        x=risk_x,
        y=risk_y,
        width=[1.6] * len(risk_x),
        text=[str(v) for v in risk_y],
        textposition="outside",
        constraintext="none",
        cliponaxis=False,
        textfont={"size": 34},
        marker={"color": "#1c5cab"},
        showlegend=False,
    ),
    row=2,
    col=1,
)
fig.update_layout(
    font={"size": 34},
    margin={"t": 60, "r": 30, "b": 90, "l": 90},
)
fig.update_annotations(font={"size": 34})
fig.update_yaxes(range=[-0.25, 4.2], tickfont={"size": 32}, row=1, col=1)
fig.update_yaxes(range=[0, 118], tickfont={"size": 32}, row=2, col=1)
fig.update_xaxes(
    tickmode="array",
    tickvals=[0, 2, 6, 12, 24, 36, 41],
    ticktext=["0", "2", "6", "12", "24", "36", "41+"],
    range=[-2, 46],
    tickfont={"size": 32},
    title={"text": "Months since the 50 mg dose (28-day months)", "font": {"size": 34}},
    row=2,
    col=1,
)
