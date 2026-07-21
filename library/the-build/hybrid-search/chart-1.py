import plotly.graph_objects as go

# BEIR nDCG@10, zero-shot (Thakur et al., 2021, Table 4). A lexical retriever
# (BM25) against a dense bi-encoder (ANCE), on eight BEIR datasets. Datasets are
# ordered by (ANCE - BM25): BM25 wins on the left, dense wins on the right.
# Neither retriever dominates, and where they disagree is corpus-specific.
datasets = [
    "SciFact",
    "Touche-2020",
    "NFCorpus",
    "DBPedia",
    "TREC-COVID",
    "FiQA-2018",
    "Quora",
    "ArguAna",
]
bm25 = [0.665, 0.367, 0.325, 0.313, 0.656, 0.236, 0.789, 0.315]
ance = [0.507, 0.240, 0.237, 0.281, 0.654, 0.295, 0.852, 0.415]

fig = go.Figure()
fig.add_trace(go.Bar(name="BM25 (lexical)", x=datasets, y=bm25))
fig.add_trace(go.Bar(name="ANCE (dense)", x=datasets, y=ance))
fig.update_layout(
    barmode="group",
    yaxis_title="nDCG@10 (zero-shot)",
    xaxis_title="BEIR dataset (ordered: BM25 wins → dense wins)",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
fig.update_yaxes(range=[0, 0.9])
