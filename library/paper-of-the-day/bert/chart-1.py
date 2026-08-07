"""BERT's Section 5.1 pre-training-task ablation (Table 5).

Data read firsthand from Devlin, Chang, Lee & Toutanova, "BERT: Pre-training of
Deep Bidirectional Transformers for Language Understanding" (NAACL 2019,
aclanthology.org/N19-1423), Table 5, dev-set scores (SQuAD is F1, the rest are
accuracies):
  BERT-BASE      MNLI-m 84.4, QNLI 88.4, MRPC 86.7, SST-2 92.7, SQuAD 88.5
  No NSP         MNLI-m 83.9, QNLI 84.9, MRPC 86.5, SST-2 92.6, SQuAD 87.9
  LTR & No NSP   MNLI-m 82.1, QNLI 84.3, MRPC 77.5, SST-2 92.1, SQuAD 77.8
"No NSP" keeps the segment-pair input and only removes the next-sentence loss;
"LTR & No NSP" additionally replaces the masked LM with a left-to-right LM, so
each token conditions only on its left context. All dev numbers, one benchmark.
"""

import plotly.graph_objects as go

tasks = ["MNLI-m", "QNLI", "MRPC", "SST-2", "SQuAD F1"]
bert_base = [84.4, 88.4, 86.7, 92.7, 88.5]
no_nsp = [83.9, 84.9, 86.5, 92.6, 87.9]
ltr_no_nsp = [82.1, 84.3, 77.5, 92.1, 77.8]

fig = go.Figure()
fig.add_trace(go.Bar(name="BERT-BASE (masked LM + NSP)", x=tasks, y=bert_base))
fig.add_trace(go.Bar(name="No NSP (masked LM, loss removed)", x=tasks, y=no_nsp))
fig.add_trace(
    go.Bar(name="LTR & No NSP (left-to-right LM)", x=tasks, y=ltr_no_nsp)
)
fig.update_layout(
    barmode="group",
    yaxis_title="Dev score (SQuAD F1; others accuracy)",
    xaxis_title="GLUE / SQuAD task",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
fig.update_yaxes(range=[70, 95])
