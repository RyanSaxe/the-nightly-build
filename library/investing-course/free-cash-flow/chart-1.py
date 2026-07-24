"""Operating cash flow versus free cash flow, Costco and Micron, fiscal 2025.

Every value is a line of the Consolidated Statements of Cash Flows in each
company's Form 10-K, in US$ millions. Free cash flow is not a reported line;
it is computed here as net cash from operating activities minus capital
expenditure, so both bars in each pair come from cited line items and the
gap between them is the capital expenditure.

Costco (fiscal year ended August 31, 2025, accession 0000909832-25-000101):
    operating cash flow          13,335
    capital expenditure         - 5,498  ("Additions to property and equipment")
    free cash flow            =   7,837

Micron (fiscal year ended August 28, 2025, accession 0000723125-25-000028):
    operating cash flow          17,525
    capital expenditure        - 15,857  ("Expenditures for property, plant, and equipment")
    free cash flow            =   1,668

Micron reports more operating cash than Costco and leaves the owner far less.
"""

import plotly.graph_objects as go

companies = ["Costco", "Micron"]
operating = [13335, 17525]
free_cash = [7837, 1668]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Operating cash flow",
        x=companies,
        y=operating,
        text=[f"{v:,}" for v in operating],
        textposition="outside",
    )
)
fig.add_trace(
    go.Bar(
        name="Free cash flow (ops − capex)",
        x=companies,
        y=free_cash,
        text=[f"{v:,}" for v in free_cash],
        textposition="outside",
    )
)
fig.update_layout(
    barmode="group",
    yaxis_title="US$ millions",
    legend={"orientation": "h", "y": 1.12, "x": 0},
    margin={"t": 40},
)
fig.update_yaxes(range=[0, 19500])
