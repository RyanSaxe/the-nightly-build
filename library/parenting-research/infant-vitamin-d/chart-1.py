"""Gallo et al. (JAMA, 2013): share of healthy, term, breastfed infants
reaching each 25(OH)D threshold at 3 months, by daily vitamin D dose.

Data are read firsthand from the trial's structured abstract:
- >=50 nmol/L: reached in 97% of infants at 3 months across all four doses.
- >=75 nmol/L: 400 IU 55%, 800 IU 81%, 1200 IU 92%, 1600 IU 97.5%.
The point of the figure is that every dose clears the 50 nmol/L line the IOM
calls adequate, while only 1600 IU/day clears the higher 75 nmol/L target.
"""

import plotly.graph_objects as go

doses = ["400 IU", "800 IU", "1200 IU", "1600 IU"]
reach_50 = [97, 97, 97, 97]
reach_75 = [55, 81, 92, 97.5]

fig = go.Figure()
fig.add_trace(go.Bar(name="Reaching 50 nmol/L (IOM adequacy)", x=doses, y=reach_50))
fig.add_trace(go.Bar(name="Reaching 75 nmol/L (higher-dose target)", x=doses, y=reach_75))
fig.update_layout(
    barmode="group",
    yaxis_title="Infants reaching threshold at 3 months (%)",
    xaxis_title="Daily vitamin D dose",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
fig.update_yaxes(range=[0, 100])
