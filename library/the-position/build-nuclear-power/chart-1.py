"""LCOE cost curve, indexed to 2009 = 100.

Data: Lazard, Levelized Cost of Energy+ (LCOE) Version 17.0, June 2024, p.16,
"Selected Historical Average LCOE Values." Lazard reports the cumulative change
in mean unsubsidized LCOE between its 2009 (v3.0) and 2024 (v17.0) estimates:
U.S. new-build nuclear +49%, utility-scale solar PV -83%, onshore wind -65%.
The two endpoints are indexed to 100 at 2009 so the divergence reads directly;
the intermediate path is not implied. Source owns the numbers plotted here.
"""

import plotly.graph_objects as go

years = ["2009", "2024"]

# Endpoints from Lazard v17.0 p.16 cumulative % change, indexed to 2009 = 100.
nuclear = [100, 149]  # +49%
solar = [100, 17]     # -83%
wind = [100, 35]      # -65%

fig = go.Figure()
fig.add_trace(go.Scatter(name="Nuclear (new build)", x=years, y=nuclear, mode="lines+markers"))
fig.add_trace(go.Scatter(name="Utility solar PV", x=years, y=solar, mode="lines+markers"))
fig.add_trace(go.Scatter(name="Onshore wind", x=years, y=wind, mode="lines+markers"))

fig.update_layout(
    yaxis_title="Mean unsubsidized LCOE (2009 = 100)",
    xaxis_title="Lazard estimate year",
)
fig.update_yaxes(rangemode="tozero")
