# Chart 2: Trailing and forward P/E multiples, Vertiv against its two named
# electrical-infrastructure peers and the sector average. Vertiv and the
# sector-average figures are as of 2026-07-22 (GuruFocus/Yahoo Finance
# valuation data); Eaton and Schneider Electric forward multiples are from an
# independent analyst comparison published in June 2026 (Investing.com).
import plotly.graph_objects as go

labels = ["Vertiv\n(trailing)", "Vertiv\n(forward)", "Sector avg\n(forward)",
          "Eaton\n(forward)", "Schneider Electric\n(forward)"]
pe = [76.71, 44.02, 29.03, 30.5, 28.0]

fig = go.Figure()
fig.add_trace(go.Bar(x=labels, y=pe, text=[f"{v:g}x" for v in pe],
                     textposition="outside"))

fig.update_layout(
    yaxis_title="Price / earnings multiple",
    xaxis_title="",
    showlegend=False,
    yaxis=dict(range=[0, 90]),
)
