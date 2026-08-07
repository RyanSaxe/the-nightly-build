"""GLUE dev score against pre-training compute (FLOPs).

Data read firsthand from Clark, Luong, Le & Manning, "ELECTRA: Pre-training
Text Encoders as Discriminators Rather Than Generators" (ICLR 2020,
arXiv:2003.10555), Tables 1 and 2 (GLUE dev score; approximate training FLOPs):
  BERT-Small       75.1 @ 1.4e18   (masked LM)
  ELECTRA-Small    79.9 @ 1.4e18   (replaced-token detection, same compute)
  ELECTRA-400K     89.0 @ 7.1e20   (RTD, the 1x compute baseline in Table 2)
  ELECTRA-1.75M    89.5 @ 3.1e21   (RTD)
  RoBERTa-500K     88.9 @ 3.2e21   (masked LM, ~4.5x the ELECTRA-400K compute)
  XLNet-LARGE      89.1 @ 3.9e21   (permutation LM, ~5.4x)
The three ELECTRA points are joined as one training-compute frontier; the
masked-LM and permutation-LM baselines are plotted as single points. FLOPs axis
is logarithmic.
"""

import plotly.graph_objects as go

electra_flops = [1.4e18, 7.1e20, 3.1e21]
electra_glue = [79.9, 89.0, 89.5]
electra_text = ["ELECTRA-Small", "ELECTRA-400K", "ELECTRA-1.75M"]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="ELECTRA (replaced-token detection)",
        x=electra_flops,
        y=electra_glue,
        mode="lines+markers+text",
        text=electra_text,
        textposition=["bottom center", "bottom center", "top center"],
    )
)
fig.add_trace(
    go.Scatter(
        name="BERT-Small (masked LM)",
        x=[1.4e18],
        y=[75.1],
        mode="markers+text",
        text=["BERT-Small"],
        textposition="top center",
    )
)
fig.add_trace(
    go.Scatter(
        name="RoBERTa-500K (masked LM)",
        x=[3.2e21],
        y=[88.9],
        mode="markers+text",
        text=["RoBERTa-500K"],
        textposition="bottom center",
    )
)
fig.add_trace(
    go.Scatter(
        name="XLNet-LARGE (permutation LM)",
        x=[3.9e21],
        y=[89.1],
        mode="markers+text",
        text=["XLNet-LARGE"],
        textposition="middle right",
    )
)
fig.update_layout(
    xaxis_title="Pre-training compute, FLOPs (log scale)",
    yaxis_title="GLUE dev score",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
fig.update_xaxes(type="log", range=[17.9, 22.0])
fig.update_yaxes(range=[72, 92])
