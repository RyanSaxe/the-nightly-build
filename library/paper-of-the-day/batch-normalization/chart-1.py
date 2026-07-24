import plotly.graph_objects as go

# Source: Ioffe & Szegedy 2015, "Batch Normalization: Accelerating Deep
# Network Training by Reducing Internal Covariate Shift" (arXiv:1502.03167),
# Sec. 4.2.2 / Fig. 3. Training steps needed to reach Inception's own
# published top-5-complement accuracy of 72.2% on ImageNet (single crop).
# Every value is read directly from the paper's reported figures; none is
# fitted or estimated.
models = ["Inception", "BN-Baseline", "BN-x5"]
steps_millions = [31.0, 13.3, 2.1]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Steps to 72.2% accuracy",
        x=models,
        y=steps_millions,
        text=[f"{v}M" for v in steps_millions],
        textposition="outside",
    )
)
fig.update_layout(
    yaxis_title="Training steps to reach 72.2% accuracy (millions)",
    showlegend=False,
)
