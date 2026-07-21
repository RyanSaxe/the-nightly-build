import plotly.graph_objects as go

# GPT-3 175B adaptation on WikiSQL: validation accuracy (%) against the number
# of trainable parameters, per method. Numbers from Hu et al. 2021, Table 4.
# Trainable parameters are in millions; the x-axis is logarithmic because the
# methods span from ~3M to ~175,000M trainable parameters.

# (label, trainable params in millions, WikiSQL accuracy %)
points = [
    ("Full fine-tuning", 175255.8, 73.8),
    ("PrefixEmbed", 3.2, 63.1),
    ("BitFit", 14.2, 71.3),
    ("PrefixLayer", 20.2, 70.1),
    ("Adapter (7.1M)", 7.1, 71.9),
    ("Adapter (40.1M)", 40.1, 73.2),
    ("LoRA (4.7M)", 4.7, 73.4),
    ("LoRA (37.7M)", 37.7, 74.0),
]

lora = [p for p in points if p[0].startswith("LoRA")]
other = [p for p in points if not p[0].startswith("LoRA")]

fig = go.Figure()

other_textpos = {
    "Full fine-tuning": "middle left",
    "PrefixEmbed": "top center",
    "BitFit": "top center",
    "PrefixLayer": "top center",
    "Adapter (7.1M)": "top center",
    "Adapter (40.1M)": "bottom center",
}

fig.add_trace(
    go.Scatter(
        name="Other methods",
        x=[p[1] for p in other],
        y=[p[2] for p in other],
        mode="markers+text",
        text=[p[0] for p in other],
        textposition=[other_textpos[p[0]] for p in other],
    )
)

fig.add_trace(
    go.Scatter(
        name="LoRA",
        x=[p[1] for p in lora],
        y=[p[2] for p in lora],
        mode="markers+text",
        text=[p[0] for p in lora],
        textposition=["middle left", "top center"],
    )
)

fig.update_layout(
    xaxis_title="Trainable parameters (millions, log scale)",
    yaxis_title="WikiSQL validation accuracy (%)",
    showlegend=True,
)
fig.update_xaxes(type="log")
fig.update_yaxes(range=[61, 76])

