"""Change in global fossil CO2 from 2025 to the 2026 projection, by fuel.

Data: Global Carbon Budget 2026 dataset (doi:10.18160/GCP-2026), file
Global_Carbon_Budget_2026_v0.1.xlsx. Fuel rows: sheet "Fossil Emissions by
Category", rows 285 (2025) and 286 (2026), columns C-F (coal, oil, gas,
cement); flaring and other are carried unchanged (0.0). Cement carbonation
sink: sheet "Global Carbon Budget", rows 89-90, column G. GtC x 3.664 = GtCO2.
Values are 2026 minus 2025, in MtCO2, as recorded in the evidence record.
"""

import plotly.graph_objects as go

labels = ["Coal", "Oil", "Gas", "Cement", "Carbon-<br>ation", "Net"]
values = [89.6, -243.1, -27.3, -8.2, 31.3, -157.8]
measure = ["relative"] * 5 + ["total"]
text = ["+90", "−243", "−27", "−8", "+31", "−158"]

fig = go.Figure(
    go.Waterfall(
        x=labels,
        y=values,
        measure=measure,
        text=text,
        textposition="outside",
        textfont=dict(size=36),
        connector=dict(line=dict(color="#8a8f98", width=1, dash="dot")),
        increasing=dict(marker=dict(color="#a24935")),
        decreasing=dict(marker=dict(color="#3f6f8f")),
        totals=dict(marker=dict(color="#4a4f57")),
    )
)
fig.add_hline(y=0, line_width=1, line_color="#4a4f57")
fig.update_layout(
    showlegend=False,
    yaxis_title="Change from 2025, Mt CO2",
    yaxis=dict(range=[-235, 130], dtick=50, tickfont=dict(size=26), title=dict(font=dict(size=26))),
    xaxis=dict(tickfont=dict(size=28)),
    margin=dict(t=20, b=90, l=120, r=10),
    font=dict(size=28),
)
