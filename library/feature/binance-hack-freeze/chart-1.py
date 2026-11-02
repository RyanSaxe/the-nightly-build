import plotly.graph_objects as go

# What happened to the Binance haul, by asset type, $ billions.
# Source: Elliptic, "Binance: the largest hack in history" (updated 1 Nov 2026).
#   stolen at theft-time prices          $6.43B
#   stablecoins stolen                   $3.46B   (Elliptic)
#   frozen or seized                     $2.85B   (Elliptic), 94% stablecoin
#   stablecoins converted before freezes ~$0.786B (Elliptic: into ETH and TRX)
# Derived here (writer's arithmetic, +/- $0.03B because the 94% is rounded):
#   frozen stablecoin       = 0.94 * 2.85            = 2.68
#   stolen, not stablecoin  = 6.43 - 3.46            = 2.97
#   frozen, not stablecoin  = 2.85 - 2.68            = 0.17
#   not frozen, not stable  = 2.97 - 0.17            = 2.80
# The frozen amount is priced at 1 Nov, the stolen amount at theft time, so
# the ratios mix two price dates.

rows = ["Stablecoins<br>$3.46B stolen", "Everything else<br>$2.97B stolen"]
frozen = [2.68, 0.17]
swapped = [0.79, 0.0]
not_frozen = [0.0, 2.80]

fig = go.Figure()
fig.add_trace(go.Bar(name="Frozen or seized", y=rows, x=frozen, orientation="h",
                     text=["$2.68B", ""], textposition="inside",
                     insidetextanchor="middle"))
fig.add_trace(go.Bar(name="Swapped out before freeze", y=rows, x=swapped,
                     orientation="h", text=["$0.79B", ""], textposition="inside",
                     insidetextanchor="middle"))
fig.add_trace(go.Bar(name="Not frozen", y=rows, x=not_frozen,
                     orientation="h", text=["", "$2.80B"], textposition="inside",
                     insidetextanchor="middle"))
fig.add_annotation(x=3.55, y=rows[0], text="77% frozen", showarrow=False, xanchor="left")
fig.add_annotation(x=3.05, y=rows[1], text="6% frozen", showarrow=False, xanchor="left")
fig.update_layout(
    barmode="stack",
    xaxis_title="US$ billions (stolen at theft-time prices)",
    xaxis_range=[0, 4.4],
    yaxis_autorange="reversed",
    yaxis_ticklabelstandoff=14,
    yaxis_tickfont=dict(size=24),
    xaxis_tickfont=dict(size=20),
    xaxis_title_font=dict(size=20),
    legend=dict(orientation="h", y=-0.28, x=0, traceorder="normal", font=dict(size=19)),
    margin=dict(l=230, r=40, t=20, b=110),
    font=dict(size=20),
)
