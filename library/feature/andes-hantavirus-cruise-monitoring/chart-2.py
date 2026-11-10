"""What a monitored group with zero infections can rule out.

The curve is the one-sided 95% upper bound on a per-contact attack rate p when
0 of n contacts are infected: the p at which (1 - p)^n = 0.05, so
p = 1 - 0.05^(1/n), close to the rule of three (3/n). This is the paper's own
arithmetic. It treats contacts as independent with comparable exposure, which
the 88 US contacts were not.

Counts:
- 88 US contacts, 40 of them high risk, none infected: CDC MMWR 2026;75(43),
  Table 2 and "Monitoring and Testing".
- Reference rates: Ferres et al., J Infect Dis 2007, prospective household
  contacts in Chile: 16 of 476 (3.4%) overall; 17.6% among sex partners;
  1.2% among other household contacts.
"""

import math

import plotly.graph_objects as go

n_values = [round(10 * 10 ** (k / 100), 3) for k in range(0, 201)]  # 10 to 1000
bound = [100 * (1 - 0.05 ** (1 / n)) for n in n_values]

us_n = [40, 88]
us_bound = [100 * (1 - 0.05 ** (1 / n)) for n in us_n]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="95% upper bound when 0 of n are infected",
        x=n_values,
        y=bound,
        mode="lines",
    )
)
fig.add_trace(
    go.Scatter(
        name="US contacts (CDC)",
        x=us_n,
        y=us_bound,
        mode="markers",
        marker=dict(size=18),
    )
)

for n_, b_, label, ax, ay in [
    (40, us_bound[0], f"40 high-risk US contacts: {us_bound[0]:.1f}%", 60, -60),
    (88, us_bound[1], f"all 88 US contacts: {us_bound[1]:.2f}%", 40, -110),
]:
    fig.add_annotation(
        x=math.log10(n_),  # log axes take annotation x in log10 units
        y=b_,
        text=label,
        showarrow=True,
        arrowhead=0,
        ax=ax,
        ay=ay,
        xanchor="left",
        font=dict(size=24),
    )

for rate, label in [
    (17.6, "Chile, sex partners 17.6%"),
    (16 / 476 * 100, "Chile, household 3.4%"),
    (1.2, "Chile, other household 1.2%"),
]:
    fig.add_hline(y=rate, line=dict(color="#555", width=1.5, dash="dot"))
    fig.add_annotation(
        x=3,
        xref="x",
        y=rate,
        text=label,
        showarrow=False,
        xanchor="right",
        yanchor="bottom",
        font=dict(size=24),
    )

fig.update_layout(
    font=dict(size=24),
    showlegend=False,
    xaxis=dict(
        tickfont=dict(size=22),
        title=dict(text="Contacts monitored, none infected (log scale)", font=dict(size=24)),
        type="log",
        range=[1, 3],
        tickvals=[10, 20, 40, 88, 250, 500, 1000],
    ),
    yaxis=dict(tickfont=dict(size=22), title=dict(text="Highest attack rate not ruled out (%)", font=dict(size=24)), range=[0, 26]),
    margin=dict(l=100, r=30, t=20, b=90),
)
