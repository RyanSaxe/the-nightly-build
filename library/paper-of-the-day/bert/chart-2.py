"""RoBERTa's controlled input-format / NSP ablation (Table 2).

Data read firsthand from Liu, Ott, Goyal, Du, Joshi, Chen, Levy, Lewis,
Zettlemoyer & Stoyanov, "RoBERTa: A Robustly Optimized BERT Pretraining
Approach" (arXiv:1907.11692), Table 2, dev-set scores on matched data (SQuAD
2.0 F1; MNLI-m and SST-2 accuracy; RACE accuracy):
  SEGMENT-PAIR + NSP    SQuAD2.0 78.7, MNLI-m 84.0, SST-2 92.9, RACE 64.2
  SENTENCE-PAIR + NSP   SQuAD2.0 76.2, MNLI-m 82.9, SST-2 92.1, RACE 63.0
  FULL-SENTENCES        SQuAD2.0 79.1, MNLI-m 84.7, SST-2 92.5, RACE 64.8
  DOC-SENTENCES         SQuAD2.0 79.7, MNLI-m 84.7, SST-2 92.7, RACE 65.6
The two no-NSP rows (FULL-SENTENCES, DOC-SENTENCES) drop the loss AND switch to
a single contiguous span; the two NSP rows keep the concatenated-segment input.
"""

import plotly.graph_objects as go

metrics = ["SQuAD 2.0 F1", "MNLI-m", "SST-2", "RACE"]
seg_pair_nsp = [78.7, 84.0, 92.9, 64.2]
sent_pair_nsp = [76.2, 82.9, 92.1, 63.0]
full_sent = [79.1, 84.7, 92.5, 64.8]
doc_sent = [79.7, 84.7, 92.7, 65.6]

fig = go.Figure()
fig.add_trace(go.Bar(name="SEGMENT-PAIR + NSP", x=metrics, y=seg_pair_nsp))
fig.add_trace(go.Bar(name="SENTENCE-PAIR + NSP", x=metrics, y=sent_pair_nsp))
fig.add_trace(go.Bar(name="FULL-SENTENCES (no NSP)", x=metrics, y=full_sent))
fig.add_trace(go.Bar(name="DOC-SENTENCES (no NSP)", x=metrics, y=doc_sent))
fig.update_layout(
    barmode="group",
    yaxis_title="Dev score",
    xaxis_title="Task",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
fig.update_yaxes(range=[60, 95])
