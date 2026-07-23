# Chart 1: CoreWeave revenue against the cost of owning its fleet, by fiscal year.
# Data owned by CoreWeave's FY2025 Form 10-K (filed 2026-03-02), tied out against
# the SEC XBRL company-facts extract for CIK 0001769628. Dollars in millions.
import plotly.graph_objects as go

years = ["FY2023", "FY2024", "FY2025"]
revenue = [229, 1915, 5131]
depreciation = [103, 863, 2454]
interest = [27, 349, 1148]

fig = go.Figure()
fig.add_trace(go.Bar(name="Revenue", x=years, y=revenue))
fig.add_trace(go.Bar(name="Depreciation & amortization", x=years, y=depreciation))
fig.add_trace(go.Bar(name="Interest expense", x=years, y=interest))

fig.update_layout(
    barmode="group",
    yaxis_title="US$ millions",
    xaxis_title="Fiscal year",
    legend_title_text="",
)
