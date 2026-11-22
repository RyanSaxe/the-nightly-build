# Chart 2: the 2025/26 change in graduate and OPT students, by place of origin.
# Data: IIE, Open Doors 2026, OD26_Intl-Student-Census-Tables_Website.xlsx,
# Table 8 (place of origin by academic level), rows India, China and WORLD
# TOTAL, columns 2024/25 and 2025/26. "Other places" is the world change
# minus India and China, computed below.
import plotly.graph_objects as go

table8 = {
    #            graduate 24/25, 25/26,  OPT 24/25, 25/26
    "India": (177_892, 116_609, 143_740, 182_201),
    "China": (120_229, 114_043, 61_981, 61_545),
    "World": (488_481, 423_078, 294_253, 335_785),
}

def change(row):
    g0, g1, o0, o1 = table8[row]
    return g1 - g0, o1 - o0

india, china, world = change("India"), change("China"), change("World")
other = (world[0] - india[0] - china[0], world[1] - india[1] - china[1])
assert india == (-61_283, 38_461) and world == (-65_403, 41_532)

groups = ["Graduate students", "Students on OPT"]
series = [
    ("India", india, "#a8332e"),
    ("China", china, "#1c5cab"),
    ("Other places", other, "#9aa3ad"),
]
fig = go.Figure()
for name, values, color in series:
    fig.add_trace(
        go.Bar(
            name=name,
            x=groups,
            y=list(values),
            marker_color=color,
            text=[f"{v:+,}" for v in values],
            textposition="outside",
            textfont={"size": 34},
            cliponaxis=False,
        )
    )
fig.update_layout(
    barmode="group",
    yaxis_title="Change in students",
    margin={"l": 200, "t": 110, "b": 120},
    font={"size": 32},
    yaxis={"title": {"standoff": 14, "font": {"size": 32}}, "tickfont": {"size": 30}, "tickformat": ",", "range": [-80_000, 58_000], "zeroline": True,
           "zerolinecolor": "#1f2733", "zerolinewidth": 1.5},
    legend={"orientation": "h", "yanchor": "bottom", "y": 1.0, "x": 0, "font": {"size": 30}},
    xaxis={"tickfont": {"size": 34}, "title": {"text": "2025/26 compared with 2024/25", "font": {"size": 32}}},
    bargap=0.3,
)
