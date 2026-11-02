"""What first-visit Monte Carlo learned: the estimated value grid over episodes.

One run (seed 0) on lesson 1's grid (slip 0.2, gamma 0.9) with the model hidden.
Each panel is the first-visit MC estimate V(s) after a given number of episodes,
laid out on the 4x4 grid (cell 0 top-left, cell 15 bottom-right); the last panel
is lesson 1's exact v_pi. The numbers are the printed output of samples.py
(uv run samples.py, "heatmap panels (seed 0)" and "exact"):

V @ 100   : -0.39  0.50  4.39 goal / -0.36 -0.89  pit  6.12
            -1.41 -5.36 -2.46 3.33 / -4.56 -9.88 -7.73 6.20
V @ 1000  :  2.78  4.44  7.12 goal /  1.19  1.01  pit  6.39
            -0.13 -0.47 -0.99 3.68 / -1.13 -2.45 -3.10 1.48
V @ 6000  :  2.29  4.31  6.83 goal /  0.81  0.35  pit  6.56
            -0.61 -1.15 -0.14 3.97 / -2.02 -2.14 -1.07 2.20
exact v_pi:  2.16  4.04  6.48 goal /  0.61  0.06  pit  6.48
            -0.72 -1.03 -0.10 4.02 / -1.86 -2.01 -1.08 1.98

At 100 episodes the estimate is far off and noisy (cell 13 reads -9.88); by
6,000 it has settled onto lesson 1's grid, with cell 13 at -2.14 against the
exact -2.01.
"""

from plotly.subplots import make_subplots
import plotly.graph_objects as go

GOAL, PIT = 3, 6
panels = [
    ("after 100 episodes",
     [-0.39, 0.50, 4.39, 0.0, -0.36, -0.89, 0.0, 6.12,
      -1.41, -5.36, -2.46, 3.33, -4.56, -9.88, -7.73, 6.20]),
    ("after 1,000 episodes",
     [2.78, 4.44, 7.12, 0.0, 1.19, 1.01, 0.0, 6.39,
      -0.13, -0.47, -0.99, 3.68, -1.13, -2.45, -3.10, 1.48]),
    ("after 6,000 episodes",
     [2.29, 4.31, 6.83, 0.0, 0.81, 0.35, 0.0, 6.56,
      -0.61, -1.15, -0.14, 3.97, -2.02, -2.14, -1.07, 2.20]),
    ("exact v_pi (lesson 1)",
     [2.16, 4.04, 6.48, 0.0, 0.61, 0.06, 0.0, 6.48,
      -0.72, -1.03, -0.10, 4.02, -1.86, -2.01, -1.08, 1.98]),
]

fig = make_subplots(rows=1, cols=4, horizontal_spacing=0.035,
                    subplot_titles=[title for title, _ in panels])

for i, (_title, flat) in enumerate(panels, start=1):
    z = [flat[4 * r:4 * r + 4] for r in range(4)]
    text = [["" for _ in range(4)] for _ in range(4)]
    for s in range(16):
        r, c = s // 4, s % 4
        if s == GOAL:
            text[r][c] = "goal"
        elif s == PIT:
            text[r][c] = "pit"
        else:
            text[r][c] = f"{flat[s]:.1f}"
    fig.add_trace(
        go.Heatmap(
            z=z, text=text, texttemplate="%{text}",
            textfont={"size": 12}, coloraxis="coloraxis",
            xgap=2, ygap=2, hoverinfo="skip",
        ),
        row=1, col=i,
    )
    fig.update_yaxes(autorange="reversed", showticklabels=False, row=1, col=i)
    fig.update_xaxes(showticklabels=False, row=1, col=i)

fig.update_layout(
    coloraxis={
        "colorscale": [[0.0, "#a8332e"], [0.5, "#f1ece1"], [1.0, "#1c5cab"]],
        "cmin": -7, "cmid": 0, "cmax": 7,
        "colorbar": {"title": {"text": "value", "side": "right"},
                     "thickness": 14, "len": 0.9},
    },
    margin={"t": 40, "r": 24, "b": 12, "l": 12},
)
fig.update_annotations(font_size=14)
