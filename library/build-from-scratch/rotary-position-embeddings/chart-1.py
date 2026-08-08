"""Attention-logit magnitude vs relative distance under RoPE, head dim d=128,
base 10000. Two series, each normalized to its own value at distance 0:

  aligned   query = key: the RoFormer Sec. 3.4.3 upper-bound construction,
            logit(r) = sum_i cos(r * theta_i). This is the envelope that decays.
  random    2000 independent standard-normal (q, k) pairs, mean |logit|. This
            is what arbitrary content sees: the decay is available, not imposed.

Provenance for chart-1.png. Reproduces from array math alone."""
import numpy as np
import plotly.graph_objects as go

def rope_freqs(d, base=10000.0):
    return base ** (-2.0 * np.arange(d // 2) / d)

def rope(x, pos, base=10000.0):
    ang = pos * rope_freqs(x.shape[-1], base)
    cos, sin = np.cos(ang), np.sin(ang)
    even, odd = x[..., 0::2], x[..., 1::2]
    out = np.empty_like(x)
    out[..., 0::2] = even * cos - odd * sin
    out[..., 1::2] = even * sin + odd * cos
    return out

d = 128
dist = np.arange(0, 513, 8)

aligned = np.array([np.sum(np.cos(r * rope_freqs(d))) for r in dist])
aligned = aligned / aligned[0]

rng = np.random.default_rng(0)
Q = rng.standard_normal((2000, d))
K = rng.standard_normal((2000, d))
q0 = rope(Q, 0)
rand = np.array([np.mean(np.abs(np.einsum("nd,nd->n", q0, rope(K, int(r))))) for r in dist])
rand = rand / rand[0]

fig = go.Figure()
fig.add_trace(go.Scatter(name="aligned query=key", x=dist, y=aligned, mode="lines"))
fig.add_trace(go.Scatter(name="random query, key (mean |logit|)", x=dist, y=rand, mode="lines"))
fig.update_layout(
    xaxis_title="relative distance between the two tokens (positions)",
    yaxis_title="logit magnitude, relative to distance 0",
)
