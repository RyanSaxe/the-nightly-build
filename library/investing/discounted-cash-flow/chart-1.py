import plotly.graph_objects as go

# This lesson's own computation on the illustrative firm (not a real company).
# Free cash flow to the firm of $100M in year 1, growing 8%/yr for a five-year
# explicit forecast, discounted at r, then capped with a stable-growth terminal
# value TV_5 = FCFF_5*(1+g)/(r-g). Enterprise value = PV(explicit) + PV(TV_5).
# The explicit forecast is identical across every point; only r and g move, so
# the whole spread below is the terminal value re-priced.
fcff = [100 * 1.08 ** i for i in range(5)]  # years 1..5: 100, 108, ... 136.05


def enterprise_value(r, g):
    pv_explicit = sum(cf / (1 + r) ** (t + 1) for t, cf in enumerate(fcff))
    tv5 = fcff[-1] * (1 + g) / (r - g)
    pv_tv = tv5 / (1 + r) ** 5
    return pv_explicit + pv_tv


g_grid = [0.015, 0.020, 0.025, 0.030, 0.035]
g_pct = [g * 100 for g in g_grid]
discount_rates = [0.08, 0.09, 0.10]

fig = go.Figure()
for r in discount_rates:
    fig.add_trace(
        go.Scatter(
            name=f"r = {int(r * 100)}%",
            x=g_pct,
            y=[enterprise_value(r, g) for g in g_grid],
            mode="lines+markers",
        )
    )

# Mark the base case (r = 9%, g = 2.5%): enterprise value ~ $1,845M.
fig.add_trace(
    go.Scatter(
        name="base case",
        x=[2.5],
        y=[enterprise_value(0.09, 0.025)],
        mode="markers",
        marker=dict(size=14, symbol="circle-open", line=dict(width=3)),
    )
)

fig.update_layout(
    xaxis_title="stable growth rate g (%, held below every discount rate)",
    yaxis_title="enterprise value (US$ millions)",
)
