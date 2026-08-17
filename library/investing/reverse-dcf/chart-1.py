import plotly.graph_objects as go

# Two-stage reverse DCF for Mastercard, computed from the verified inputs:
# FCF base $16,433M (FY2025 10-K), 876.0M shares (Q2 2026 10-Q cover),
# 9% cost of equity, ten explicit years, then a perpetuity at the terminal rate.
# Each point is the implied value per share the price would have to reproduce.
FCF0 = 16433.0      # US$M, FY2025 free-cash-flow base
SHARES = 876.0      # millions
R = 0.09            # cost of equity
N = 10              # explicit-forecast years
PRICE = 569.29      # last close, 2026-08-14


def implied_price(g, terminal):
    pv = 0.0
    fcf = FCF0
    for t in range(1, N + 1):
        fcf = FCF0 * ((1 + g) ** t)
        pv += fcf / ((1 + R) ** t)
    tv = fcf * (1 + terminal) / (R - terminal)
    pv += tv / ((1 + R) ** N)
    return pv / SHARES


growth = [g / 1000.0 for g in range(30, 121)]   # 3.0% .. 12.0%
g_pct = [g * 100 for g in growth]
curve_4 = [implied_price(g, 0.04) for g in growth]
curve_3 = [implied_price(g, 0.03) for g in growth]

fig = go.Figure()
fig.add_trace(go.Scatter(name="4% terminal growth", x=g_pct, y=curve_4, mode="lines"))
fig.add_trace(go.Scatter(name="3% terminal growth", x=g_pct, y=curve_3, mode="lines"))

# Today's price: the horizontal line the model output must cross.
fig.add_trace(
    go.Scatter(
        name="Price, 2026-08-14 ($569)",
        x=[g_pct[0], g_pct[-1]],
        y=[PRICE, PRICE],
        mode="lines",
    )
)

# The crossing under the 4% terminal case: 8.8% implied growth.
fig.add_trace(
    go.Scatter(
        name="Implied growth (8.8%)",
        x=[8.8],
        y=[PRICE],
        mode="markers",
        marker=dict(size=15, symbol="circle-open", line=dict(width=3)),
    )
)

fig.update_layout(
    xaxis_title="Assumed free-cash-flow growth, years 1-10 (% per year)",
    yaxis_title="Implied value per share (US$)",
)
