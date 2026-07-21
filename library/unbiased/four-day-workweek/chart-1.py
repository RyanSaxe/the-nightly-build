import plotly.graph_objects as go

# Reported revenue change during four-day-week trials, by who measured it and
# against which baseline. Numbers from the research log's Numbers section:
#  - 4 Day Week Global, US/Ireland/Australia 2022 pilot (the organizer's own
#    figures): +8.1% averaged over the trial period, and +38% against the same
#    period the prior year.
#  - Cambridge/Autonomy UK 2022 pilot (the peer-reviewed academic report): +1.4%
#    on average across the 23 organisations that supplied revenue data,
#    described as "broadly stable."
# The baselines differ, which is the point: the loudest figure and the
# peer-reviewed figure are an order of magnitude apart.

labels = [
    "4 Day Week Global<br>(avg over trial)",
    "4 Day Week Global<br>(vs prior-year period)",
    "Cambridge / Autonomy<br>(23 firms, avg)",
]
values = [8.1, 38.0, 1.4]
text = ["+8.1%", "+38%", "+1.4%"]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=labels,
        y=values,
        text=text,
        textposition="outside",
        cliponaxis=False,
    )
)
fig.update_layout(
    yaxis_title="Reported revenue change (%)",
    xaxis_title="Who measured it, and against which baseline",
    showlegend=False,
)
fig.update_yaxes(range=[0, 42])
