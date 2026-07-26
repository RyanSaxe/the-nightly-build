import plotly.graph_objects as go

# Source: He, Zhang, Ren, Sun, "Deep Residual Learning for Image
# Recognition" (arXiv:1512.03385), Table 2 (18/34-layer plain vs. ResNet,
# 10-crop testing on ImageNet validation) and Table 3 (ResNet-34 option A,
# and ResNet-50/101/152, option B for dimension-matching shortcuts). Every
# value is the paper's own reported top-1 error; none is fitted or
# estimated. The paper never trains a plain network past 34 layers, so the
# plain series stops there.
depths_plain = [18, 34]
top1_plain = [27.94, 28.54]

depths_resnet = [18, 34, 50, 101, 152]
top1_resnet = [27.88, 25.03, 22.85, 21.75, 21.43]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Plain",
        x=depths_plain,
        y=top1_plain,
        mode="lines+markers",
    )
)
fig.add_trace(
    go.Scatter(
        name="ResNet",
        x=depths_resnet,
        y=top1_resnet,
        mode="lines+markers",
    )
)
fig.update_layout(
    xaxis_title="Depth (layers)",
    yaxis_title="ImageNet top-1 error (%, 10-crop testing)",
    xaxis=dict(type="linear", tickvals=[18, 34, 50, 101, 152]),
)
