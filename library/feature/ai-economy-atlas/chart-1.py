import plotly.graph_objects as go

# Task saturation by major occupation group, ATLAS v1.0 global rows.
# Source: atlas_v1_work_occupations.csv (GLOBAL rows), April 2026.
# "Any observed use" = non_negligible_ai_use: the share of the group's O*NET
# tasks with AI use observed above the dataset's reporting threshold.
# "Intensive use" = intensive_ai_use: the stricter threshold.
# This is depth of use inside a job, a different quantity from the usage-volume
# shares (the 30% headline) the piece discusses. The 14 groups below are the
# ones carried in the evidence record.

# (group, non_negligible_ai_use %, intensive_ai_use %)
rows = [
    ("Computer & mathematical", 46.36, 30.26),
    ("Business & financial ops.", 42.99, 28.35),
    ("Sales & related", 38.96, 19.35),
    ("Office & admin. support", 38.45, 23.87),
    ("Arts, design & media", 37.63, 23.11),
    ("Management", 32.50, 17.10),
    ("Architecture & engineering", 27.95, 13.75),
    ("Life, physical & social science", 25.07, 11.79),
    ("Legal", 22.76, 16.26),
    ("Installation, maint. & repair", 18.96, 9.81),
    ("Healthcare practitioners", 17.18, 6.65),
    ("Healthcare support", 11.57, 4.48),
    ("Production", 11.04, 3.34),
    ("Building & grounds cleaning", 9.52, 1.19),
]

# Sort ascending so the highest-saturation group sits at the top of a
# horizontal bar chart.
rows = sorted(rows, key=lambda r: r[1])

labels = [r[0] for r in rows]
any_use = [r[1] for r in rows]
intensive = [r[2] for r in rows]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Any observed use",
        y=labels,
        x=any_use,
        orientation="h",
    )
)
fig.add_trace(
    go.Bar(
        name="Intensive use",
        y=labels,
        x=intensive,
        orientation="h",
    )
)
fig.update_layout(
    barmode="group",
    xaxis_title="Share of the group's tasks with observed AI use (%)",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    margin=dict(l=320),
)
fig.update_xaxes(range=[0, 50])
fig.update_yaxes(automargin=True)
