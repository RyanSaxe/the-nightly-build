import plotly.graph_objects as go

# Two thefts, two compositions, two freeze rates (% of the haul).
# Binance, 29 Oct 2026 (Elliptic, updated 1 Nov): stablecoins $3.46B of $6.43B
#   stolen = 53.8%; frozen or seized $2.85B of $6.43B = 44.3%.
# Bybit, 21 Feb 2025: haul was 401,346.77 ETH, 90,375.55 stETH, 8,000 mETH and
#   15,000 cmETH with no stablecoin (Block Scholes, from on-chain data) = 0%.
#   Frozen share 3% (4 Mar 2025) to 3.84% (21 Apr 2025), Bybit CEO Ben Zhou as
#   reported by Decrypt; a share of roughly 500,000 ETH, not of dollars.
# Bars show the latest figures; the Bybit range is labeled.

measures = ["Stablecoin<br>share of haul", "Frozen or seized<br>share of haul"]
binance = [53.8, 44.3]
bybit = [0.0, 3.84]

fig = go.Figure()
fig.add_trace(go.Bar(name="Binance 2026", y=measures, x=binance, orientation="h",
                     text=["54%", "44%"], textposition="outside", cliponaxis=False, marker_color="#2b3140"))
fig.add_trace(go.Bar(name="Bybit 2025", y=measures, x=bybit, orientation="h",
                     text=["0%", "3% to 3.84%"], textposition="outside", cliponaxis=False, marker_color="#9aa3b2"))
fig.update_layout(
    barmode="group",
    xaxis_title="Percent of the haul",
    xaxis_range=[0, 70],
    yaxis_autorange="reversed",
    yaxis_ticklabelstandoff=14,
    yaxis_tickfont=dict(size=24),
    xaxis_tickfont=dict(size=20),
    xaxis_title_font=dict(size=20),
    legend=dict(orientation="h", y=-0.3, x=0, traceorder="normal", font=dict(size=19)),
    margin=dict(l=230, r=40, t=20, b=110),
    font=dict(size=20),
)
