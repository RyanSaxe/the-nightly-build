import plotly.graph_objects as go

# GSM8K solve rate (%), standard vs. chain-of-thought prompting, by model
# scale. Source: Wei et al. 2022 (arXiv:2201.11903), Table 2 (Appendix).
gpt3_params = [0.35, 1.3, 6.7, 175]
gpt3_standard = [2.2, 2.4, 4.0, 15.6]
gpt3_cot = [0.5, 0.5, 2.4, 46.9]

palm_params = [8, 62, 540]
palm_standard = [4.9, 9.6, 17.9]
palm_cot = [4.1, 29.9, 56.9]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="GPT-3, standard",
        x=gpt3_params,
        y=gpt3_standard,
        mode="lines+markers",
        line=dict(dash="dot"),
    )
)
fig.add_trace(
    go.Scatter(
        name="GPT-3, chain-of-thought",
        x=gpt3_params,
        y=gpt3_cot,
        mode="lines+markers",
    )
)
fig.add_trace(
    go.Scatter(
        name="PaLM, standard",
        x=palm_params,
        y=palm_standard,
        mode="lines+markers",
        line=dict(dash="dot"),
    )
)
fig.add_trace(
    go.Scatter(
        name="PaLM, chain-of-thought",
        x=palm_params,
        y=palm_cot,
        mode="lines+markers",
    )
)
fig.update_layout(
    xaxis_title="Model scale (billions of parameters, log scale)",
    yaxis_title="GSM8K solve rate (%)",
)
fig.update_xaxes(type="log")
