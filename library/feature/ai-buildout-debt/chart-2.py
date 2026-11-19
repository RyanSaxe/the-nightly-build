"""Fig. 2: what the filings itemize inside the Fed's "guarantees & contract commitments".

Top bar: Federal Reserve Board, Financial Stability Report, November 2026,
Box 2.2, figure C (p. 24), 2026:Q2 value for seven firms, read from the
vector geometry of the published chart (about +/- $5 billion); the Fed has
published no data table and no split of this total.

Lower bars: the companies' own Forms 10-Q, undiscounted, at their own dates.
  Purchase commitments
    Meta Platforms, non-cancelable contractual commitments, 30 Sep 2026, p. 21: 454.52
    Nvidia, supply and capacity commitments, 26 Jul 2026, p. 18: 279
    Oracle, unconditional purchase obligations, 31 Aug 2026: 34.15
  Credit guarantees that pay a lender or lessor on a default or shortfall
    Nvidia, maximum gross exposure under data center lease guarantees, 26 Jul 2026, p. 19: 108.5
    Alphabet, credit-derivative notional backstopping data center lease and
      energy payments, 30 Sep 2026, p. 21: 48.012
    Meta Platforms, maximum residual value guarantees, 30 Sep 2026, p. 18: 41.493
Dates differ from the Fed's 2026:Q2 cut-off, and the Fed does not say whether
it nets commitments between firms in its set, so the bars are a scale
comparison, not a reconciliation.
"""

import plotly.graph_objects as go

fed_total = 2068
purchase = {"Meta": 454.52, "Nvidia": 279.0, "Oracle": 34.15}
guarantees = {"Nvidia": 108.5, "Alphabet": 48.012, "Meta": 41.493}

rows = [
    ("Fed: guarantees & contract commitments, 2026:Q2", fed_total, "#008a74",
     "seven firms; value read from the Fed's published chart"),
    ("Purchase commitments named in three filings", sum(purchase.values()), "#1c5cab",
     " · ".join(f"{k} {v:,.0f}" for k, v in purchase.items())),
    ("Credit guarantees named in three filings", sum(guarantees.values()), "#a8332e",
     " · ".join(f"{k} {v:,.0f}" for k, v in guarantees.items())),
]

ys = [2, 1, 0]
fig = go.Figure()
for (label, value, color, detail), y in zip(rows, ys):
    fig.add_trace(
        go.Bar(
            x=[value], y=[y], orientation="h", width=0.42,
            marker_color=color, showlegend=False,
        )
    )
    # Row label above the bar, total at its end, components under it.
    fig.add_annotation(x=0, y=y + 0.24, text=f"<b>{label}</b>", xanchor="left",
                       yanchor="bottom", showarrow=False, font={"size": 30})
    fig.add_annotation(x=value, y=y, text=f"${value:,.0f}bn", xanchor="left",
                       xshift=10, showarrow=False, font={"size": 30})
    fig.add_annotation(x=0, y=y - 0.24, text=detail, xanchor="left", yanchor="top",
                       showarrow=False, font={"size": 26, "color": "#68727f"})

fig.update_layout(
    barmode="overlay",
    font={"size": 28},
    margin={"t": 30, "r": 40, "b": 80, "l": 40},
    xaxis={
        "title": {"text": "US$ billions, undiscounted", "font": {"size": 26}},
        "tickfont": {"size": 26},
        "range": [0, 2500],
        "dtick": 500,
        "tickformat": ",",
    },
    yaxis={"visible": False, "range": [-0.7, 2.75]},
)
