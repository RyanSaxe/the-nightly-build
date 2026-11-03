"""Figure 2: the $115 billion enterprise value divided by Lumentum revenue.

Provenance (every input is a published figure; the division is the paper's):
  Numerator  $115 billion implied enterprise value, Marvell/Lumentum joint press
             release, 2 November 2026 (value at Marvell's 28 October price).
  Revenue, $ millions, Lumentum earnings releases (8-K Exhibit 99.1) and 10-K:
    FY2026 net revenue                        3,014.0   (10-K, Item 7)
    Q2 FY26 to Q1 FY27, four quarters sum     665.5 + 808.4 + 1,006.3 + 1,262.6
    Q1 FY27 net revenue, times 4              1,262.6   (Q1 FY27 release)
    Q2 FY27 guidance 1,575 to 1,625, mid 1,600, times 4
    Target model, $2 billion a quarter        8,000     (OFC investor briefing,
                                              17 March 2026, slide 38; "not guidance")
  Marvell reference line: equity 925.7 million shares x $251.56 = $232.9 billion
    (Merger Agreement Section 4.2(c)(i) share counts excluding warrants; Marvell
    undisturbed price ~$252 on 28 October, deal deck slide 9, and 4.5 x $251.56 =
    $1,132) plus net debt $4,962.9M - $3,932.8M = $1.03 billion (Marvell 10-Q,
    1 August 2026) = $233.9 billion. Divided by Q3 FY27 guidance midpoint
    $3,150 million x 4 = $12,600 million gives 18.6 times.
"""
import plotly.graph_objects as go

EV = 115_000  # $ millions
MARVELL_MULTIPLE = 233.9 / 12.6  # 18.56

points = [
    # label, revenue $M, basis
    ("FY2026, reported", 3014.0, "Reported"),
    ("Last 4 quarters, reported", 665.5 + 808.4 + 1006.3 + 1262.6, "Reported"),
    ("Sept. quarter x 4", 1262.6 * 4, "One quarter, annualized"),
    ("Dec. guidance x 4", 1600.0 * 4, "One quarter, annualized"),
    ("Target, 2B a quarter", 8000.0, "Lumentum target, not guidance"),
]

xs = [x / 1000 for x in range(2500, 9001, 100)]
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=xs,
        y=[EV / 1000 / x for x in xs],
        mode="lines",
        name="$115B / revenue",
        line=dict(color="#8a8f98", width=1.5),
        hoverinfo="skip",
        showlegend=False,
    )
)
fig.add_hline(
    y=MARVELL_MULTIPLE,
    line=dict(color="#a24935", width=1.5, dash="dash"),
    annotation_text="Marvell itself, 28 Oct.: 18.6x",
    annotation_position="top right",
    annotation_yshift=4,
    annotation_font=dict(size=28, color="#a24935"),
)

styles = {
    "Reported": dict(symbol="circle", color="#2f6f8f"),
    "One quarter, annualized": dict(symbol="square", color="#2f6f8f"),
    "Lumentum target, not guidance": dict(symbol="diamond", color="#2f6f8f"),
}
placement = {
    "FY2026, reported": "top right",
    "Last 4 quarters, reported": "top right",
    "Sept. quarter x 4": "top right",
    "Dec. guidance x 4": "bottom left",
    "Target, 2B a quarter": "bottom center",
}
seen = set()
for label, rev, basis in points:
    m = EV / rev
    fig.add_trace(
        go.Scatter(
            x=[rev / 1000],
            y=[m],
            mode="markers+text",
            name=basis,
            legendgroup=basis,
            showlegend=False,
            marker=dict(size=16, **styles[basis]),
            text=[f"{label}<br>${rev/1000:.2f}B, {m:.1f}x"],
            textposition=placement[label],
            textfont=dict(size=27),
        )
    )
    seen.add(basis)

fig.update_layout(
    font=dict(size=27),
    showlegend=False,
    xaxis=dict(
        title="Lumentum annual revenue, $ billions (linear)",
        range=[2.4, 9.4],
        title_font=dict(size=26),
        tickfont=dict(size=26),
    ),
    yaxis=dict(
        title="$115B / revenue, times (linear)",
        range=[8, 46],
        title_font=dict(size=26),
        tickfont=dict(size=26),
    ),
    margin=dict(l=100, r=15, t=15, b=95),
)
