"""RMS error of the sampled value estimates against the exact v_pi, by episode.

Both runs are on lesson 1's grid (slip 0.2, gamma 0.9), with the model hidden
from the estimator. First-visit Monte Carlo uses the 1/N(s) running mean; TD(0)
uses the decaying step size alpha(s) = N(s) ** -0.7. Error is the root-mean-
square difference from the exact v_pi over the 14 non-terminal cells. The line
is the mean over 40 seeds and the band is the 10th-to-90th percentile across
those seeds. The numbers are the printed output of samples.py (uv run
samples.py), checkpoints 10, 20, 50, 100, 200, 500, 1000, 2000, 4000, 6000:

first-visit MC  mean 5.165 4.829 3.110 2.110 1.423 0.914 0.630 0.440 0.307 0.252
                p10  3.175 2.998 2.068 1.479 0.979 0.563 0.438 0.314 0.211 0.181
                p90  7.995 7.145 4.891 2.987 1.996 1.255 0.872 0.627 0.403 0.346
TD(0) N^-0.7    mean 3.437 3.112 2.086 1.663 1.190 0.797 0.548 0.424 0.324 0.287
                p10  1.903 1.708 1.261 1.052 0.647 0.542 0.364 0.300 0.226 0.176
                p90  5.655 4.609 2.994 2.466 1.558 1.083 0.742 0.567 0.429 0.387

TD's error is lower at every checkpoint out to 2,000 episodes; between 2,000 and
4,000 unbiased first-visit MC passes it, ending 0.252 against 0.287 at 6,000;
TD's band is tighter throughout. Both fall toward 0 because the step sizes decay.
"""

import plotly.graph_objects as go

episodes = [10, 20, 50, 100, 200, 500, 1000, 2000, 4000, 6000]

mc_mean = [5.165, 4.829, 3.110, 2.110, 1.423, 0.914, 0.630, 0.440, 0.307, 0.252]
mc_lo = [3.175, 2.998, 2.068, 1.479, 0.979, 0.563, 0.438, 0.314, 0.211, 0.181]
mc_hi = [7.995, 7.145, 4.891, 2.987, 1.996, 1.255, 0.872, 0.627, 0.403, 0.346]

td_mean = [3.437, 3.112, 2.086, 1.663, 1.190, 0.797, 0.548, 0.424, 0.324, 0.287]
td_lo = [1.903, 1.708, 1.261, 1.052, 0.647, 0.542, 0.364, 0.300, 0.226, 0.176]
td_hi = [5.655, 4.609, 2.994, 2.466, 1.558, 1.083, 0.742, 0.567, 0.429, 0.387]

MC_LINE = "#96640a"   # press --chart-1
TD_LINE = "#1c5cab"   # press --chart-2
MC_BAND = "rgba(150, 100, 10, 0.15)"
TD_BAND = "rgba(28, 92, 171, 0.15)"


def band(x, lo, hi, color):
    return [
        go.Scatter(x=x, y=hi, mode="lines", line={"width": 0},
                   hoverinfo="skip", showlegend=False),
        go.Scatter(x=x, y=lo, mode="lines", line={"width": 0}, fill="tonexty",
                   fillcolor=color, hoverinfo="skip", showlegend=False),
    ]


fig = go.Figure()
for trace in band(episodes, mc_lo, mc_hi, MC_BAND):
    fig.add_trace(trace)
for trace in band(episodes, td_lo, td_hi, TD_BAND):
    fig.add_trace(trace)
fig.add_trace(go.Scatter(
    name="first-visit Monte Carlo (1/N)", x=episodes, y=mc_mean,
    mode="lines+markers",
    line={"color": MC_LINE, "width": 2.5, "dash": "solid"},
    marker={"color": MC_LINE, "symbol": "circle", "size": 8},
))
fig.add_trace(go.Scatter(
    name="TD(0), decaying step", x=episodes, y=td_mean,
    mode="lines+markers",
    line={"color": TD_LINE, "width": 2.5, "dash": "dash"},
    marker={"color": TD_LINE, "symbol": "square", "size": 8},
))
fig.update_xaxes(
    title_text="episodes seen (log scale)", type="log",
    tickvals=[10, 20, 50, 100, 200, 500, 1000, 2000, 4000, 6000],
    ticktext=["10", "20", "50", "100", "200", "500", "1k", "2k", "4k", "6k"],
)
fig.update_yaxes(
    title_text="RMS error over the 14 cells (log scale)", type="log",
    tickvals=[0.2, 0.3, 0.5, 1, 2, 3, 5],
    ticktext=["0.2", "0.3", "0.5", "1", "2", "3", "5"],
)
fig.update_layout(
    legend={"yanchor": "bottom", "y": 1.02, "xanchor": "left", "x": 0},
)
