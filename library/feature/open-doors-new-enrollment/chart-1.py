# Chart 1: the year-on-year change in IIE's total, split by component.
# Data: IIE, Open Doors 2026, Census_Academic-Level_OD26_Website.xlsx,
# sheet "Broad Academic Levels" (counts by academic year). The four levels sum
# to IIE's total (Census_Overall-Enrollment_OD26_Website.xlsx). Each bar is the
# difference of two consecutive years' counts, computed below.
import plotly.graph_objects as go

years = ["2021/22", "2022/23", "2023/24", "2024/25", "2025/26"]
counts = {
    "Undergraduate": [344_532, 347_602, 342_875, 357_231, 356_165],
    "Graduate": [385_097, 467_027, 502_291, 488_481, 423_078],
    "Non-degree": [34_131, 43_766, 38_742, 37_801, 31_135],
    "OPT": [184_759, 198_793, 242_782, 294_253, 335_785],
}
totals = [948_519, 1_057_188, 1_126_690, 1_177_766, 1_146_163]

for i, total in enumerate(totals):
    assert sum(series[i] for series in counts.values()) == total

labels = years[1:]
change = {k: [v[i] - v[i - 1] for i in range(1, len(v))] for k, v in counts.items()}
total_change = [totals[i] - totals[i - 1] for i in range(1, len(totals))]

fig = go.Figure()
order = ["Graduate", "Undergraduate", "Non-degree", "OPT"]
colors = {
    "Graduate": "#1c5cab",
    "Undergraduate": "#96640a",
    "Non-degree": "#9aa3ad",
    "OPT": "#a8332e",
}
for name in order:
    fig.add_trace(
        go.Bar(
            name=name,
            x=labels,
            y=change[name],
            marker_color=colors[name],
            hovertemplate="%{y:+,}",
        )
    )
fig.add_trace(
    go.Scatter(
        name="Total change",
        x=labels,
        y=total_change,
        mode="markers",
        marker={"symbol": "diamond", "size": 28, "color": "#1f2733",
                "line": {"color": "#ffffff", "width": 2}},
        showlegend=True,
    )
)
# Label each total outside its stack, so no label sits on a bar.
for i, label in enumerate(labels):
    parts = [change[name][i] for name in order]
    top, bottom = sum(p for p in parts if p > 0), sum(p for p in parts if p < 0)
    below = total_change[i] < 0
    fig.add_annotation(
        x=label,
        y=bottom if below else top,
        yshift=-42 if below else 46,
        text=f"Total {total_change[i]:+,}",
        showarrow=False,
        font={"size": 30, "color": "#1f2733"},
    )
fig.update_layout(
    barmode="relative",
    xaxis_title="Academic year",
    font={"size": 32},
    yaxis_title="Change from prior year",
    yaxis={"title": {"standoff": 14, "font": {"size": 32}}, "tickfont": {"size": 30}, "tickformat": ",", "zeroline": True, "zerolinecolor": "#1f2733",
           "zerolinewidth": 1.5, "range": [-125_000, 160_000]},
    legend={"orientation": "h", "yanchor": "bottom", "y": 1.0, "x": 0, "font": {"size": 26}},
    xaxis={"tickfont": {"size": 32}, "title": {"font": {"size": 32}}},
    margin={"l": 200, "t": 90, "b": 120},
    bargap=0.3,
)
