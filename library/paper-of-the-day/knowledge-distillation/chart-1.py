"""Student-teacher top-1 agreement across distillation settings.

Data read firsthand from Stanton et al., "Does Knowledge Distillation Really
Work?" (NeurIPS 2021, arXiv:2106.05945):
  - LeNet-5 self-distillation on MNIST reaches "over 99%" test agreement
    (Fig. 2, section 4.1, p. 4). Plotted as 99.0.
  - ResNet-56 ensemble distilled into a ResNet-56 on CIFAR-100, best fidelity
    policy MixUp at temperature 4: 86.0% test agreement (Fig. 3, section 5.1,
    p. 7).
  - Same setting, Baseline crops+flips at temperature 4: 84.5% test agreement
    (Fig. 3, section 5.1, p. 7).
Reference line at 100 marks perfect fidelity (student matches teacher exactly).
"""

import plotly.graph_objects as go

settings = [
    "ResNet-56, CIFAR-100<br>(crops + flips, T=4)",
    "ResNet-56, CIFAR-100<br>(MixUp, T=4)",
    "LeNet-5, MNIST<br>(self-distillation)",
]
agreement = [84.5, 86.0, 99.0]
labels = ["84.5%", "86.0%", ">99%"]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=agreement,
        y=settings,
        orientation="h",
        text=labels,
        textposition="outside",
        cliponaxis=False,
        showlegend=False,
    )
)
fig.add_vline(
    x=100,
    line_dash="dash",
    annotation_text="perfect fidelity",
    annotation_position="top",
)
fig.update_xaxes(
    title_text="Student–teacher top-1 agreement on held-out data (%)",
    range=[0, 108],
)
fig.update_yaxes(title_text="", automargin=True)
fig.update_layout(margin=dict(l=240))
