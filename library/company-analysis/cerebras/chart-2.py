import plotly.graph_objects as go

# Cerebras revenue concentration by lettered customer, first half of the
# fiscal year, percent of six-month GAAP revenue. Customer A and Customer D
# are disclosed as related parties to each other; Customer B first appears
# as a separately disclosed customer in the H1 2026 table.
# Source: Cerebras Form 10-Q for the quarter ended June 30, 2026, Note 3
# (Revenue) -- the H1 2026 column and its H1 2025 comparative.
halves = ["H1 2025", "H1 2026"]
customer_a = [47, 49]
customer_b = [0, 20]
customer_d = [41, 10]

fig = go.Figure()
fig.add_trace(go.Bar(name="Customer A", x=halves, y=customer_a))
fig.add_trace(go.Bar(name="Customer B", x=halves, y=customer_b))
fig.add_trace(go.Bar(name="Customer D", x=halves, y=customer_d))
fig.update_layout(
    barmode="stack",
    yaxis_title="Share of six-month revenue (%)",
    xaxis_title="Period",
)
fig.update_yaxes(rangemode="tozero")
