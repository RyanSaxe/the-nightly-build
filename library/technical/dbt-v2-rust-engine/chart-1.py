# Data: the Nightly Build's own timing runs, 3,000 synthetic DuckDB models
# (each a one-line join of two earlier models by ref), 4-core Linux machine,
# wall-clock seconds including process start, default one thread. Parse: 3 runs
# per engine, full parse with target/ deleted (and --no-partial-parse on v1).
# Compile: 2 runs per engine. No --static-analysis strict in any timing run.
import plotly.graph_objects as go
from plotly.subplots import make_subplots

engines = ["dbt-core 1.12.5", "dbt OSS 2.0.5", "dbt 2.0.6"]
parse = {
    "dbt-core 1.12.5": [15.8, 15.2, 15.8],
    "dbt OSS 2.0.5": [2.1, 2.2, 2.0],
    "dbt 2.0.6": [2.3, 2.3, 2.6],
}
compile_ = {
    "dbt-core 1.12.5": [32.2, 32.5],
    "dbt OSS 2.0.5": [4.0, 4.2],
    "dbt 2.0.6": [4.4, 4.2],
}

colors = {"dbt-core 1.12.5": "#8f6410", "dbt OSS 2.0.5": "#1f5aa6", "dbt 2.0.6": "#00876c"}
fig = make_subplots(rows=1, cols=2, subplot_titles=("Parse (3 runs each)", "Compile (2 runs each)"))
for col, data in ((1, parse), (2, compile_)):
    for e in engines:
        ys = data[e]
        mean = sum(ys) / len(ys)
        fig.add_trace(go.Bar(x=[e], y=[mean], marker_color=colors[e], opacity=0.35,
                             showlegend=False, width=0.5), row=1, col=col)
        fig.add_trace(go.Scatter(x=[e] * len(ys), y=ys, mode="markers", showlegend=False,
                                 marker=dict(size=10, color=colors[e], symbol="circle",
                                             line=dict(width=1.5, color="#212730"))),
                      row=1, col=col)
fig.update_yaxes(title_text="Wall-clock seconds (linear scale; bar = mean, dots = runs)", rangemode="tozero", row=1, col=1)
fig.update_yaxes(rangemode="tozero", row=1, col=2)
fig.update_layout(width=1100, height=520, margin=dict(t=70, b=60))
