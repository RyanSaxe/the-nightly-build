# Chart 1: fluorosis risk/odds ratios and 95% CIs for the three "exposure"
# questions Wong et al. 2024 (Cochrane CD007693.pub3) asked about topical
# fluoride and dental fluorosis of the permanent teeth. Figures are the
# review's own point estimates, taken verbatim from research.md's Numbers
# section:
#   Starting age, at/before 12mo vs. after: RR 0.98 (95% CI 0.81-1.18),
#     2 cohort studies, 260 children, very-low certainty.
#   Amount used, case-control design: OR 0.77 (95% CI 0.41-1.46),
#     258 children, very-low certainty.
#   Amount used, cross-sectional design: OR 0.92 (95% CI 0.66-1.28),
#     2,037 children, very-low certainty.
#   Concentration, 550 ppm vs. 1000 ppm: RR 0.75 (95% CI 0.57-0.99),
#     959 children, 1 RCT, moderate certainty.
#   Concentration, 440 ppm vs. 1450 ppm: RR 0.72 (95% CI 0.58-0.89),
#     1,009 children, 1 RCT, moderate certainty.
# Each ratio compares the lower-exposure arm (earlier-or-later start recoded
# so "at/before 12 months" is the numerator, less toothpaste, or lower
# concentration) against the higher-exposure arm. No number here is
# estimated; all are the review's own reported RR/OR and CI bounds.
import plotly.graph_objects as go

labels = [
    "440 vs. 1450 ppm",
    "550 vs. 1000 ppm",
    "Amount, cross-sectional",
    "Amount, case-control",
    "Starting age, ≤12mo vs. after",
]
point = [0.72, 0.75, 0.92, 0.77, 0.98]
ci_low = [0.58, 0.57, 0.66, 0.41, 0.81]
ci_high = [0.89, 0.99, 1.28, 1.46, 1.18]
certainty = ["moderate", "moderate", "very low", "very low", "very low"]

upper = [hi - p for p, hi in zip(point, ci_high)]
lower = [p - lo for p, lo in zip(point, ci_low)]

fig = go.Figure()
for group in ["moderate", "very low"]:
    idx = [i for i, c in enumerate(certainty) if c == group]
    fig.add_trace(
        go.Scatter(
            name=f"{group.capitalize()} certainty",
            x=[point[i] for i in idx],
            y=[labels[i] for i in idx],
            mode="markers",
            error_x=dict(
                type="data",
                array=[upper[i] for i in idx],
                arrayminus=[lower[i] for i in idx],
                thickness=1.5,
                width=7,
            ),
            marker=dict(size=10),
        )
    )

fig.add_vline(x=1, line_dash="dot", line_width=1)
fig.update_layout(
    xaxis_title="Risk ratio / odds ratio, lower exposure vs. higher (1.0 = no difference)",
    yaxis_title=None,
    margin=dict(l=220),
)
fig.update_xaxes(range=[0.15, 1.75])
