"""Absolute RSV risk over one season, with and without nirsevimab.

Data are the control (placebo / no-intervention) and nirsevimab event rates,
expressed as cases per 100 infants through ~150 days, from each trial's own
registered results:

- MELODY (healthy term / late-preterm, >=35 wk GA), NCT03979313, primary cohort:
    medically-attended RSV LRTI  placebo 25/496 = 5.0%, nirsevimab 12/994 = 1.2%
    RSV hospitalization          placebo  8/496 = 1.6%, nirsevimab  6/994 = 0.6%
- Griffin Phase 2b (preterm 29-<35 wk GA), NCT02878330:
    medically-attended RSV LRTI  placebo 46/484 = 9.5%, nirsevimab 25/969 = 2.6%
    RSV hospitalization          placebo 20/484 = 4.1%, nirsevimab  8/969 = 0.8%
- HARMONIE (infants <12 mo, >=29 wk GA), NCT05437510:
    RSV hospitalization          control 64/4019 = 1.6%, nirsevimab 11/4038 = 0.3%
"""

import plotly.graph_objects as go

groups = [
    "Term / late-preterm<br>medically attended<br>(MELODY)",
    "Term / late-preterm<br>hospitalized<br>(MELODY)",
    "Preterm 29–35 wk<br>medically attended<br>(Griffin)",
    "Preterm 29–35 wk<br>hospitalized<br>(Griffin)",
    "Infants &lt;12 mo<br>hospitalized<br>(HARMONIE)",
]

without = [5.0, 1.6, 9.5, 4.1, 1.6]
with_ = [1.2, 0.6, 2.6, 0.8, 0.3]

fig = go.Figure()
fig.add_trace(go.Bar(name="Without nirsevimab", x=groups, y=without))
fig.add_trace(go.Bar(name="With nirsevimab", x=groups, y=with_))
fig.update_layout(
    barmode="group",
    yaxis_title="Cases per 100 infants, one RSV season (~150 days)",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
)
fig.update_yaxes(range=[0, 10])
