"""Time against accelerator-minutes for NVIDIA's three same-chip, same-backend
scaling series on MLPerf Training v6.1 qwen35_397b_grpo (closed, GBS 512,
10 GRPO steps per scored run).

Minutes: official scores from results.mlcommons.org/training (v6.1, model
"Qwen3.5 397B GRPO"). Accelerator-minutes: the printed (two-decimal) score x
accelerator count, rounded to a whole number, so a reader can reproduce each
one from the table (a derived figure, not an official MLPerf metric).
"""

import plotly.graph_objects as go

series = [
    # name, [(accelerators, result ID, minutes, accelerator-minutes), ...]
    (
        "GB300, vLLM (Theia)",
        [
            (64, "6.1-0035", 42.48, 2719),
            (256, "6.1-0040", 20.11, 5148),
            (512, "6.1-0043", 14.52, 7434),
            (1024, "6.1-0031", 13.78, 14111),
        ],
    ),
    (
        "Rubin, vLLM (Hecate)",
        [
            (64, "6.1-0122", 32.18, 2060),
            (256, "6.1-0131", 14.33, 3668),
            (1024, "6.1-0118", 10.94, 11203),
        ],
    ),
    (
        "Rubin, TensorRT-LLM (Hecate)",
        [
            (56, "6.1-0119", 28.47, 1594),
            (64, "6.1-0121", 25.93, 1660),
            (1024, "6.1-0117", 10.44, 10691),
        ],
    ),
]

# Label positions chosen so the GPU-count tags do not collide.
positions = {
    ("GB300, vLLM (Theia)", 64): "top center",
    ("GB300, vLLM (Theia)", 256): "top center",
    ("GB300, vLLM (Theia)", 512): "middle right",
    ("GB300, vLLM (Theia)", 1024): "middle right",
    ("Rubin, vLLM (Hecate)", 64): "bottom center",
    ("Rubin, vLLM (Hecate)", 256): "bottom right",
    ("Rubin, vLLM (Hecate)", 1024): "top left",
    ("Rubin, TensorRT-LLM (Hecate)", 56): "bottom center",
    ("Rubin, TensorRT-LLM (Hecate)", 64): "bottom left",
    ("Rubin, TensorRT-LLM (Hecate)", 1024): "middle left",
}

fig = go.Figure()
for name, points in series:
    fig.add_trace(
        go.Scatter(
            name=name,
            x=[p[2] for p in points],
            y=[p[3] for p in points],
            mode="lines+markers+text",
            text=["" if (name, p[0]) == ("GB300, vLLM (Theia)", 512) else f"{p[0]:,}" for p in points],
            textposition=[positions[(name, p[0])] for p in points],
            textfont=dict(size=24),
            marker=dict(size=14),
            customdata=[p[1] for p in points],
        )
    )

fig.update_layout(
    font=dict(size=22),
    xaxis_title="Score (minutes)",
    yaxis_title="Accelerator-minutes",
    legend=dict(orientation="v", yanchor="top", y=0.99, x=0.45, xanchor="left", font=dict(size=22)),
    margin=dict(t=30, r=30, l=140, b=100),
)
fig.update_xaxes(range=[5, 46], dtick=5, tickfont=dict(size=22), title_font=dict(size=22), automargin=True)
fig.update_yaxes(range=[0, 15500], tickformat=",", tickfont=dict(size=22), title_font=dict(size=22), title_standoff=16, automargin=True)
# The 512-GPU GB300 label sits on a white chip so the crossing lines do not obscure it.
fig.add_annotation(x=14.52, y=7434, text="512", showarrow=False, xshift=34, font=dict(size=24), bgcolor="white")
