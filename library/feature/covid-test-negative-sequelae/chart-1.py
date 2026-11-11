# Outcomes attributable to COVID-19 (of 614) by follow-up window, under the
# two designs run on the same Komodo Health claims. Threshold: RR >= 1.1 and
# Bonferroni-corrected P < 0.05 within each window.
# Source: Nilforoshan et al., PNAS 123(44): e2604414123 (2026), Abstract and Fig. 1B.
import plotly.graph_objects as go

windows = ["Days 30–119<br>(1–4 mo)", "Days 120–359<br>(5–12 mo)", "Days 360–719<br>(13–24 mo)"]
unrestricted = [262, 286, 369]
test_based = [43, 5, 0]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Unrestricted control design",
        x=windows,
        y=unrestricted,
        mode="lines+markers+text",
        text=[str(v) for v in unrestricted],
        textposition="top center",
        textfont=dict(size=34),
    )
)
fig.add_trace(
    go.Scatter(
        name="Test-based control design",
        x=windows,
        y=test_based,
        mode="lines+markers+text",
        text=[str(v) for v in test_based],
        textposition="top center",
        textfont=dict(size=34),
    )
)
# The renderer exports at a fixed 1200 x 675 canvas, so type is set large
# enough to stay legible when the PNG is scaled down to a phone column.
fig.update_layout(
    font=dict(size=26),
    yaxis=dict(
        title=dict(text="Attributable outcomes (of 614)", font=dict(size=26)),
        tickfont=dict(size=26),
        range=[-25, 440],
        dtick=100,
    ),
    xaxis=dict(tickfont=dict(size=26), range=[-0.3, 2.3]),
    legend=dict(orientation="h", x=0, y=1.16, xanchor="left", font=dict(size=28)),
    margin=dict(l=110, r=30, t=80, b=100),
)
fig.update_traces(line_width=4, marker_size=13)
