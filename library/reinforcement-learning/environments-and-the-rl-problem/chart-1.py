import plotly.graph_objects as go

# State-value function v_pi of the equiprobable random policy on the running
# 4x4 gridworld at gamma = 0.9, computed by evaluate.py (direct solve
# v_pi = (I - gamma P_pi)^{-1} r_pi, confirmed by iterative policy evaluation
# to within 7e-10). Row 0 is the top row of the grid; cell (3,3) is the
# terminal goal, value 0. Values are the printed output rounded to one decimal
# for the labels; the color uses the same numbers.
values = [
    [-9.4, -9.2, -9.0, -8.8],
    [-9.2, -9.0, -8.5, -8.0],
    [-9.0, -8.5, -7.4, -5.8],
    [-8.8, -8.0, -5.8, 0.0],
]
n = 4
cols = list(range(n))
rows = list(range(n))

# Sequential single hue: most negative (most expected cost to reach the goal)
# is deep blue, the goal's 0 is near-white. zmin maps to colorscale 0.
colorscale = [[0.0, "#1c5cab"], [0.5, "#7ba2d4"], [1.0, "#eef3fa"]]

fig = go.Figure(
    go.Heatmap(
        z=values,
        x=cols,
        y=rows,
        colorscale=colorscale,
        zmin=-9.4,
        zmax=0.0,
        xgap=3,
        ygap=3,
        colorbar=dict(
            title=dict(text="v<sub>π</sub>", side="right"),
            tickvals=[0, -2, -4, -6, -8],
            outlinewidth=0,
        ),
        hovertemplate="row %{y}, col %{x}<br>v_pi = %{z}<extra></extra>",
    )
)

# Per-cell value labels, with font color chosen for contrast against the fill.
for r in rows:
    for c in cols:
        v = values[r][c]
        label = "0.0" if v == 0.0 else f"{v:.1f}"
        dark_fill = v <= -4.0
        fig.add_annotation(
            x=c, y=r, text=label, showarrow=False,
            font=dict(color="#ffffff" if dark_fill else "#1f2733", size=20),
        )

# Name the terminal goal cell.
fig.add_annotation(
    x=3, y=3, yshift=-26, text="goal (terminal)", showarrow=False,
    font=dict(color="#1f2733", size=13),
)

fig.update_layout(
    xaxis=dict(title="column", tickmode="array", tickvals=cols, constrain="domain"),
    yaxis=dict(
        title="row", tickmode="array", tickvals=rows,
        autorange="reversed", scaleanchor="x", scaleratio=1, constrain="domain",
    ),
    margin=dict(t=40, r=24, b=56, l=64),
)
