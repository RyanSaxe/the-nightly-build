"""Cumulative share of Andes virus incubations completed by a given day.

Data:
- Epuyen, Argentina, 2018-19 person-to-person outbreak, incubation binned as
  extracted from Martinez et al., NEJM 2020, by the UKHSA evidence summary
  (Annexe D): <=15 d: 5; 16-21 d: 10; 22-28 d: 13; >=29 d: 6; n = 34; overall
  range 9-40 d. Cumulative shares are plotted at each bin's upper edge, with the
  last bin closed at the 40-day maximum. Points are not joined, because the
  bins say nothing about the shape between their edges.
- WHO Disease Outbreak News 2026-DON604 (28 May 2026): "probability of safe
  release from quarantine of 96% at 42 days, reducing to 91% at 35 days".
- Windows: 45 days (WHO DON599, 4 May; UKHSA until 2 June), 42 days (WHO
  DON600, CDC, ECDC), 35 days (WHO's comparison point).
"""

import plotly.graph_objects as go

bin_upper = [15, 21, 28, 40]
bin_counts = [5, 10, 13, 6]
n = sum(bin_counts)
cumulative = []
running = 0
for count in bin_counts:
    running += count
    cumulative.append(round(100 * running / n, 1))

who_days = [35, 42]
who_share = [91, 96]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Epuyén 2018–19, 34 cases, at each bin's end",
        x=bin_upper,
        y=cumulative,
        mode="markers+text",
        textfont=dict(size=24),
        text=[f"{v:.0f}%" for v in cumulative],
        textposition=["middle right", "middle right", "middle right", "top center"],
        marker=dict(size=16),
    )
)
fig.add_trace(
    go.Scatter(
        name="WHO estimate, 28 May 2026",
        x=who_days,
        y=who_share,
        mode="markers+text",
        textfont=dict(size=24),
        text=["91%", "96%"],
        textposition=["bottom right", "bottom left"],
        marker=dict(size=18, symbol="diamond"),
    )
)

for day, label, dash in [
    (35, "35 d", "dot"),
    (42, "42 d window", "solid"),
    (45, "45 d", "dot"),
]:
    fig.add_vline(x=day, line=dict(color="#555", width=1.5, dash=dash))
    fig.add_annotation(
        x=day,
        y=60,
        text=label,
        showarrow=False,
        textangle=-90,
        xshift=-10,
        font=dict(size=24),
    )

fig.update_layout(
    font=dict(size=24),
    xaxis=dict(tickfont=dict(size=22), title=dict(text="Days from exposure to symptom onset", font=dict(size=24)), range=[0, 50], dtick=7),
    yaxis=dict(tickfont=dict(size=22), title=dict(text="Cases with onset by this day (%)", font=dict(size=24)), range=[0, 112]),
    legend=dict(x=0.02, y=0.98, xanchor="left", yanchor="top", orientation="v", font=dict(size=22)),
    margin=dict(l=100, r=30, t=20, b=90),
)
