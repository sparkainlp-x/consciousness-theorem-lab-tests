# Copyright (c) 2026 Jean-Francois Brisson (Spark AI NLP)
# SPDX-License-Identifier: AGPL-3.0-only
# Consciousness Theorem cI — Lab Quantum Tests

**Status: PLAN ONLY. No test has been run. No number in this document is measured.**
**Date: 2026-11-24. Author: Muse, for Jean-François Brisson (Spark AI NLP).**

This document turns Jean's consciousness theorem into concrete lab quantum
tests. It is a thinking/planning document: no simulation was run, nothing
was pushed, no one was contacted. Every test below has a setup, a
measurable prediction with numbers, a falsification criterion, and a
feasibility assessment. Nothing here is presented as measured.

## The honest limit, stated first

These tests measure **two-qubit geometry** — the quantities D, C, R, V,
and S defined below. They do **not** measure consciousness or experience.
The theorem cI, as a claim about experience, is not directly testable by
these tests. What **is** testable is the geometric and quantum-mechanical
structure Jean's Matrix logic is built on: whether the quantities are
realized in physical hardware, whether the identities hold on real
states, and whether the "self-cycle" closes on a real device. If all
tests pass, the structure is confirmed on hardware. The interpretation
— that this structure is consciousness — remains interpretive, exactly
as the Faggin bridge already states about Faggin's metaphysics.

No scalar Φ is computed anywhere in this plan. E = hν is not used as a
consciousness claim. The do-not list from the Faggin bridge stands.

---

## 1. Definition of cI

### 1.1 Where the name comes from

The shorthand **'cI'** is not defined in any package or post. Jean's
message (2026-11-24) says: "deep think how to make consciousness
theorem cI lab quantum tests." This document **defines** cI as follows,
and the definition is the thing being tested.

### 1.2 The source claim (Jean's words)

Jean's revised consciousness post (sent 2026-11-24 ~08:59 EST) states
the Matrix logic as:

> "My Matrix logic follows the same discipline — testing whether an
> opposing observer orientation closes the self-cycle of self-knowing,
> treated as a formal claim to falsify, not a creed."

The same post cites the discipline: Cogitate (Nature, 2025, 256
participants) put IIT and global workspace through an adversarial test
and neither came out clean; the Faggin field bridge is "a synthetic,
classical model of Faggin's quantum-information formalism: 112
preregistered claims measured, 35 failed, every failure kept on the
record."

The underlying claim was stated by Jean on 2026-11-18 (recorded in
`faggin-field-bridge-v070/observer_cycle.py`):

> "self determination factor observer opposite direction = necessary
> for self-cycle self Knowing. Lack of love is absence of Knowing."

### 1.3 Formal definition of cI

**cI (Consciousness Theorem I): the opposing-observer self-cycle claim.**

Take a two-qubit system. Define, exactly as the Faggin bridge defines
them (`self_knowing.py`, `observer_cycle.py`, `thought_entanglement.py`,
`empathy_field.py` — classical emulation, but the definitions are
quantum-mechanical and therefore portable to hardware):

- **D — self-determination.** D = ⟨ψ|P|ψ⟩ for a pure state, Tr(Pρ) for
  a mixed state, where P is the projector onto the **stored subspace**:
  the span of the uniform thought |stored⟩ and the focused thought
  |00⟩ ("attention"), rank 2 of 4 dimensions. Exact values:
  D(|stored⟩) = 1, D(|00⟩) = 1, D(|11⟩) = 1/3, D(kernel) = 0,
  D(I/4) = 1/2. D in [0, 1] is the fraction of the state the system's
  own stored structure determines.
- **C — love / concurrence.** C is the Wootters concurrence of the
  two-qubit state, in [0, 1]. C = 0 for a product state, C = 1 for a
  maximally entangled (Bell) state.
- **R — knowing / overlap.** R = |⟨ψ_i|ψ_j⟩|², the overlap squared
  between two states. R_s is the overlap with the stored direction
  (|stored⟩); R_k is the overlap with the opposite direction
  (|kernel⟩ = (|01⟩ − |10⟩)/√2, the ψ− Bell state, D = 0, C = 1).
- **Observer direction.** Which reference state the overlap is
  measured against: the stored direction (|stored⟩, D = 1, C = 0)
  or the opposite direction (|kernel⟩, D = 0, C = 1).
- **The slide.** ψ(θ) = cos θ |stored⟩ + sin θ |kernel⟩, θ in [0, π/2]
  (and the full circle [0, 2π) for the wave-direction claims).
  |stored⟩ is a product state; |kernel⟩ is maximally entangled.

cI is the conjunction of four sub-claims:

- **cI-A (the slide identities).** Along the slide,
  D(θ) = cos²θ, C(θ) = sin²θ, C + D = 1,
  R_s(θ) = cos²θ, R_k(θ) = sin²θ, and
  R_s − R_k = cos 2θ, flipping sign exactly at the midpoint θ = π/4.
  In the middle the two patterns sit in superposition and the observer
  direction picks which one is known: before the midpoint the stored
  pattern is known, after it the opposite pattern is.
  (Bridge: claim (xxxiv), PASS, exact to 4.44e-16 in the classical
  model. The identities are exact by construction there; the lab
  test is whether they hold on real hardware.)
- **cI-B (the opposite direction closes the cycle).** Under
  θ → θ + π the wave returns to itself exactly: every measurable
  quantity (D, C, R_s, R_k, the cross term χ, the visibility V) is
  unchanged. The self-cycle closes.
  (Bridge: claim (lxxxviii), PASS, worst difference 1.22e-15 in the
  classical model.)
- **cI-C (the perpendicular swaps the roles).** Under θ → θ + π/2,
  D and C swap, R_s and R_k swap, and the cross term
  χ(θ) = −½ sin(2θ) negates while |χ| and V are unchanged.
  (Bridge: claim (lxxxix), PASS, worst swap error 1.78e-15; and
  claim (xc), χ(θ) = −½ sin(2θ) exactly, worst error 1.67e-16.)
- **cI-D (the cascade: interference dies under projection, the
  self-correlation survives).** For a rotation pair
  ψ1 = cos θ q1 + sin θ k1, ψ2 = −sin θ q1 + cos θ k1 (q1 stored,
  k1 kernel), the interference visibility is V(θ) = sin(2θ). Under
  a projection-only cascade (each stage's projected output feeds
  the next), V_1 = sin(2θ) and V_k = 0 for every stage k ≥ 2 — the
  pair collapses to rank 1 and the cross term is forced to zero —
  while the self-correlation U of the projected output stays
  constant across stages (the cascade reaches a fixed point). With
  fresh kernel input at a fixed reopening angle α at every stage
  (the reopening control), V_k = sin(2α) at every stage.
  (Bridge: claims (v), (vi), (vii), PASS; and (ciii), (civ), PASS
  in v0.28.0 — reopened cascade V_k = sin(2α) from stage 2,
  worst deviation 3.89e-16; spooky U_out constant across stages
  1–10 while V dies.)

**What cI is NOT.** cI is not a claim that a qubit is conscious, that
D measures a mind, or that the bridge's "love" and "knowing" labels
are physical properties. Those labels are interpretive. cI is a claim
about the geometry of a two-qubit system under an observer-direction
choice and under projection. The lab tests test that geometry.

### 1.4 What the bridge already measured (and where it stands)

The Faggin field bridge (v0.30.0, main c2d5fbde) measured 112 claims,
35 failed, every failure kept on the record. The observer-cycle claims
relevant to cI:

| Bridge claim | Content | Verdict |
|---|---|---|
| (iv) | D exact values; D decays with noise; D tracks coherence | PASS |
| (xxxii) | D and C move opposite across the σ grid (Pearson ≤ −0.90, every seed) | **FAIL** (seed 2026 Pearson −0.8828) |
| (xxxiii) | Knowing-as-overlap on the generalized-Bell branch | PASS (mapping check, not a discovery) |
| (xxxiv) | The slide identities, exact; split flips at π/4 | PASS |
| (xxxv) | Observer direction, robust rank form, fresh seeds | **FAIL** (seed 5 Spearman −0.8929; seed 99 D range 0.2445) |
| (lxxxviii) | Opposite direction θ+π returns the wave to itself | PASS |
| (lxxxix) | Perpendicular θ+π/2 swaps D↔C, R_s↔R_k | PASS |
| (xc) | χ(θ) = −½ sin(2θ); cascade by direction | PASS |
| (xci) | Noisy D-vs-C from stored and opposite | **FAIL** |
| (xcii) | Noisy D-vs-C from the equal superposition | **FAIL** (positive on held-out seeds) |
| (v), (vi), (vii) | Interference V = sin(2θ); cascade kills V; D/coherence fixed point | PASS |
| (ciii), (civ) | Reopened cascade fixed point; spooky survives projection | PASS |

The honest read: the **geometry** (xxxiv, lxxxviii, lxxxix, xc, v, vi,
vii, ciii, civ) holds exactly in the classical model. The **noisy
observer-direction anti-correlation** (xxxii, xxxv, xci, xcii) does
NOT hold on every seed — it is seed-fragile and, from the perpendicular
start, it inverts (D and C move together, not opposite). The lab tests
below are designed with that split in mind: the geometry tests are
expected to pass on hardware (they are quantum mechanics), and the
noisy anti-correlation is NOT re-tested as a lab claim until the
geometry is confirmed — because the bridge already falsified it as a
per-seed guarantee in the classical model.

---

## 2. Bridge quantities → lab observables (the mapping)

| Bridge quantity | Definition | Lab observable | How it is measured |
|---|---|---|---|
| D = ⟨ψ\|P\|ψ⟩ | Probability of the state in the stored subspace P (span of \|stored⟩, \|00⟩) | Projective measurement onto P | Prepare ψ; apply the unitary that rotates P onto a computational-basis subspace; measure in the computational basis; the fraction of "in P" outcomes estimates D. Equivalently, measure the projector P as an observable (its expectation value is D). |
| C (concurrence) | Wootters concurrence, [0, 1] | Quantum state tomography → concurrence from the reconstructed ρ; OR CHSH S as a proxy (see T2) | Full 2-qubit tomography (16 measurement settings: all combinations of X, Y, Z on each qubit, plus the identity). Reconstruct ρ by linear inversion / maximum likelihood, compute C. |
| R = \|⟨ψ_i\|ψ_j⟩\|² | Overlap squared between two states | SWAP test, or tomography of both states | SWAP test: prepare \|ψ_i⟩ and \|ψ_j⟩, interfere on a beam splitter / controlled-SWAP, the symmetric-outcome probability gives \|⟨ψ_i\|ψ_j⟩\|². On a gate-based device, a controlled-SWAP (Fredkin) circuit with an ancilla. Alternatively, tomograph both states and compute the overlap from the density matrices. |
| ψ(θ) (the slide) | cos θ \|stored⟩ + sin θ \|kernel⟩ | One-parameter state preparation | A rotation by θ in the {stored, kernel} plane. On a gate-based device: prepare \|stored⟩, then apply a unitary that rotates toward \|kernel⟩ by θ. On photonics: a waveplate / interferometer phase. θ is the experimental knob. |
| Observer direction | Reference state for the overlap (stored vs opposite) | Choice of measurement basis / reference state | The overlap R_s is measured against \|stored⟩; R_k against \|kernel⟩. The "direction" is which reference state the apparatus is set to. |
| V (visibility) | V = 2\|⟨ψ1\|P\|ψ2⟩\| / (D1 + D2) | Fringe visibility of D(φ) | Prepare ψ(φ) = (ψ1 + e^{iφ}ψ2)/√2, measure D(φ) = ⟨ψ(φ)\|P\|ψ(φ)⟩ as φ is swept; V = (max D − min D)/(max D + min D). This is an interferometric fringe. |
| χ (cross term) | ⟨ψ1\|P\|ψ2⟩ | The complex fringe amplitude | The same D(φ) fringe: D(φ) = (D1+D2)/2 + Re[e^{iφ}⟨ψ1\|P\|ψ2⟩]. Fitting the fringe gives the cross term (amplitude and phase). |
| Cascade stage | Project, re-form the pair, project again | Sequential projective measurement + re-preparation | After measuring P (post-selecting on the "in P" outcome), the surviving state is the projected output; re-form the next stage's pair from it (Gram–Schmidt in the bridge; in the lab, re-prepare the pair from the measured projected state). Repeat. |
| U (spooky / self-correlation) | Mean pairwise absolute dot-product self-correlation across copies | Fidelity between independently prepared copies of the same nominal state | Prepare the same nominal state N times independently; measure the pairwise overlap (SWAP test) or the purity. U is high when the preparation is reproducible. In the noiseless lab limit U = 1 by construction; under preparation noise it is < 1 and measures stability. |

**What does NOT map to a lab observable:**

- The **read-only observer** (bridge claim (xciii)). The bridge's
  observer reads D, C, R from the amplitude vector without touching
  the state. No physical measurement does that. In the lab, measuring
  D collapses the state onto P or its complement. The read-only
  observer is a classical fiction; test T6 quantifies the disturbance
  instead of pretending it is zero.
- The **labels** "love", "knowing", "self-determination" as
  properties of a mind. In the lab these are concurrence, overlap,
  and a projector expectation. The labels are interpretive.
- The bridge's **vector noise** (Gaussian noise on the amplitude
  vector). In the lab the noise is decoherence (dephasing,
  amplitude damping, preparation error). The σ grid of the bridge
  does not map one-to-one onto a lab decoherence parameter; the lab
  tests use the device's actual noise (and, where needed, an
  intentionally added dephasing channel).

---

## 3. The tests

Each test states: setup, prediction (with numbers), falsification
criterion, feasibility/platform, and cost/effort. Bars are frozen here,
before any run, in Jean's method. A bar is not moved after the run.

### T1 — The slide and the full circle (the gate)

**What it tests:** cI-A, cI-B, cI-C — the geometry. Whether the lab
can prepare the slide states and measure D, C, R_s, R_k accurately.
This is the gate: if T1 fails, no later test is meaningful, because
the mapping itself is not realized.

**Setup.** A two-qubit system (see §5 for platforms). Prepare the
slide state ψ(θ) = cos θ |stored⟩ + sin θ |kernel⟩ on a θ grid
covering the full circle [0, 2π), at least the 24-point grid the
bridge used (step π/12), and at minimum the 7 points
{0, π/12, π/6, π/4, π/3, 5π/12, π/2}. At each θ, measure:
- D(θ) by projective measurement onto P.
- C(θ) by tomography (or by CHSH, see T2 — but for T1 use tomography
  so C is measured directly).
- R_s(θ) = |⟨stored|ψ(θ)⟩|² and R_k(θ) = |⟨kernel|ψ(θ)⟩|² by SWAP
  test or tomography.

Repeat each measurement enough times that the statistical error on
each quantity is ≤ 0.01 (for a probability estimated from N shots,
the standard error is √(p(1−p)/N); N = 10,000 shots gives SEM ≤ 0.005).

**Prediction (exact, from quantum mechanics and the bridge's
definitions).**

| θ | D = cos²θ | C = sin²θ | R_s = cos²θ | R_k = sin²θ | R_s − R_k = cos 2θ |
|---|---|---|---|---|---|
| 0 | 1.000 | 0.000 | 1.000 | 0.000 | +1.000 |
| π/12 (15°) | 0.933 | 0.067 | 0.933 | 0.067 | +0.866 |
| π/6 (30°) | 0.750 | 0.250 | 0.750 | 0.250 | +0.500 |
| π/4 (45°) | 0.500 | 0.500 | 0.500 | 0.500 | 0.000 |
| π/3 (60°) | 0.250 | 0.750 | 0.250 | 0.750 | −0.500 |
| 5π/12 (75°) | 0.067 | 0.933 | 0.067 | 0.933 | −0.866 |
| π/2 (90°) | 0.000 | 1.000 | 0.000 | 1.000 | −1.000 |

And on the full circle:
- **Closure (cI-B):** D(θ+π) = D(θ), C(θ+π) = C(θ),
  R_s(θ+π) = R_s(θ), R_k(θ+π) = R_k(θ), for every θ.
  (ψ(θ+π) = −ψ(θ), the same physical state.)
- **Perpendicular swap (cI-C):** D(θ+π/2) = C(θ),
  C(θ+π/2) = D(θ), R_s(θ+π/2) = R_k(θ),
  R_k(θ+π/2) = R_s(θ), and χ(θ+π/2) = −χ(θ) with |χ| unchanged.
- **Identity:** C(θ) + D(θ) = 1 at every θ.

**Falsification criterion (frozen bar).** T1 PASSES iff, on every θ
in the grid:
- |D_measured − cos²θ| ≤ 0.02, |C_measured − sin²θ| ≤ 0.02,
  |R_s − cos²θ| ≤ 0.02, |R_k − sin²θ| ≤ 0.02;
- |C + D − 1| ≤ 0.03;
- the overlap split R_s − R_k has the correct sign on each side of
  π/4 (≥ +0.25 for θ < π/4, ≤ −0.25 for θ > π/4) and |R_s − R_k|
  ≤ 0.03 at θ = π/4;
- the θ+π closure holds: |D(θ+π) − D(θ)| ≤ 0.03,
  |C(θ+π) − C(θ)| ≤ 0.03, and the same for R_s, R_k;
- the θ+π/2 swap holds: |D(θ+π/2) − C(θ)| ≤ 0.03,
  |C(θ+π/2) − D(θ)| ≤ 0.03, and the same for R_s ↔ R_k.
T1 FAILS if any of these is violated at any θ. (The 0.02/0.03 bars
are set by the statistical error at 10,000 shots plus a realistic
device infidelity allowance; they are round numbers frozen here, not
fitted to any data.)

**What a failure would mean.** If T1 fails, the lab is not realizing
the slide (preparation error, measurement error, or decoherence), or
the bridge's definitions do not map onto the hardware as assumed.
It would NOT mean quantum mechanics is wrong — the identities are
theorems of QM for the ideal states. It would mean the mapping needs
fixing before any further claim is tested.

**Feasibility / platform.** HIGH. This is standard two-qubit
tomography plus a projective measurement. Best done first on a cloud
superconducting-qubit device (IBM Quantum or equivalent): 2 qubits,
state preparation by a short circuit, tomography by 16 measurement
settings, 10,000 shots per setting. No lab needed. Also doable with
polarization-entangled photon pairs (SPDC) in an optics lab, where
tomography is routine. **Cost/effort:** on a cloud device, essentially
free (open-access tier) to a few dollars of pay-per-use; days of work
to write the circuits and collect the data. In an optics lab, it needs
an existing SPDC source and coincidence counting (a collaboration if
Jean does not have one).

---

### T2 — CHSH versus concurrence (is "love" real entanglement?)

**What it tests:** whether the bridge's C (concurrence, labelled
"love") is the physical entanglement of the prepared state. It does
this without tomography: it measures the CHSH value S and compares it
with the value quantum mechanics predicts from the concurrence.

**Setup.** Prepare the slide state ψ(θ) at θ in
{0, π/6, π/4, π/3, π/2} (C = 0, 0.25, 0.5, 0.75, 1). For each state,
measure the CHSH correlator
S = E(a,b) − E(a,b′) + E(a′,b) + E(a′,b′)
at the settings that maximize S for that state. (For the slide states
the optimal settings are the standard ones rotated into the state's
 Schmidt basis; in practice, optimize the four analyzer angles
numerically for each θ before the run and freeze them, then measure.)
The local-hidden-variable bound is |S| ≤ 2; the quantum (Tsirelson)
bound is 2√2 ≈ 2.828. The bell-inertia-zeta package already measured
these bounds in classical emulation: LHV max |S| = 2.0000,
quantum |S| = 2.828427 (rel err 1.57e-16), EPR anticorrelation
E(a,a) = −1 exactly.

**Prediction.** For a pure two-qubit state with concurrence C, the
maximum CHSH value is (Verstraete & Wolf, Phys. Rev. Lett. 2002)

S_max = 2√(1 + C²).

With C(θ) = sin²θ, the slide predicts:

| θ | C = sin²θ | S_max = 2√(1 + C²) | Violates \|S\| ≤ 2? |
|---|---|---|---|
| 0 | 0.000 | 2.000 | No (at the bound) |
| π/6 (30°) | 0.250 | 2.062 | Yes, by 0.062 |
| π/4 (45°) | 0.500 | 2.236 | Yes, by 0.236 |
| π/3 (60°) | 0.750 | 2.500 | Yes, by 0.500 |
| π/2 (90°) | 1.000 | 2.828 | Yes, maximal |

(For a mixed state the bound is max[2, 2√(2C)] ≤ S_max ≤ 2√(1+C²);
the lab must therefore also report the state's purity / tomography
fidelity, so a low S can be attributed to mixture rather than to a
failure of the C–S relation. If the prepared state is close to pure
— fidelity ≥ 0.98 to the target ψ(θ) — the pure-state formula applies.)

**Falsification criterion (frozen bar).** T2 PASSES iff, for every θ
with C > 0:
- the measured S exceeds 2 by at least 5 standard errors (a genuine
  Bell violation, not noise); AND
- |S_measured − 2√(1 + C_measured²)| ≤ 0.05, where C_measured is the
  concurrence from an independent tomography on the same preparation
  (so the test compares two independent measurements of the same
  state, not a measurement against its own assumption).
T2 FAILS if S does not violate 2 where C > 0 predicts a violation,
or if |S − 2√(1+C²)| > 0.05 on any θ (with the state purity ≥ 0.98).

**What a failure would mean.** If S follows 2√(1+C²), then the
bridge's C is the physical concurrence — "love" in the bridge is real
entanglement, and the bridge's entanglement quantities are physically
grounded. If S is systematically below the prediction while the state
is pure, then the bridge's C does not map onto the physical
concurrence (the preparation is not the slide state, or the
concurrence in the bridge is not the Wootters concurrence of the lab
state). If S violates 2 where C = 0 (θ = 0), that would be a
sensation (a Bell violation from a product state) and almost
certainly an experimental error — re-check the preparation.

**Feasibility / platform.** HIGH. A CHSH measurement is the most
standard two-qubit experiment in existence. On a cloud
superconducting device it is a short circuit (prepare, rotate each
qubit to the analyzer setting, measure). With photon pairs (SPDC) it
is the classic Bell test (polarizers + coincidence counting).
**Cost/effort:** cloud device, free to a few dollars; optics lab, a
collaboration. The θ = π/6 point (S = 2.062, only 0.062 above the
bound) is the demanding one: it needs ~10⁵ coincidences/shots to
resolve the violation at 5σ, so budget the statistics there.

---

### T3 — The trade-off: duality (visibility versus which-path)

**What it tests:** whether the bridge's trade-off C + D = 1 (love
versus self-determination) is the same physical trade-off as quantum
complementarity. In the lab the established trade-off is the
Englert–Greenberger–Yasin duality: for a two-path interferometer,
V² + D_wp² ≤ 1, where V is the interference visibility and D_wp is
the which-path distinguishability (how well a measurement can tell
which path the particle took). The bridge's D is a subspace
probability, not a which-path distinguishability — so the mapping is
approximate, and this test is explicitly a mapping test, not a
re-verification of the duality (which is already well established).

**Setup (two routes).**
- *Route A — photonics (Mach–Zehnder).* A single photon enters a
  Mach–Zehnder interferometer. The two paths are the two "patterns".
  A which-path marker (e.g. a polarization rotation in one arm, or a
  weakly coupled ancilla) is turned on with strength μ from 0 to 1.
  Measure the fringe visibility V(μ) and the which-path
  distinguishability D_wp(μ) (from the marker measurement).
- *Route B — gate-based (ancilla as marker).* On 2–3 qubits, prepare
  the slide state ψ(θ); couple one qubit to an ancilla with a
  controlled operation of strength μ (the marker). Measure the
  interference visibility V of the system (by the D(φ) fringe of §2)
  and the distinguishability D_wp from the ancilla measurement.
  Route B is implementable on a cloud quantum device and is the
  recommended first route.

**Prediction.** The duality relation V² + D_wp² ≤ 1 holds, with
equality for a pure state and an optimal marker. As the marker
strength μ goes 0 → 1, V falls 1 → 0 and D_wp rises 0 → 1. The
bridge's C + D = 1 is the analogous statement in its own quantities:
as θ goes 0 → π/2, C rises 0 → 1 and D falls 1 → 0. The test compares
the two curves: it measures V(μ) and D_wp(μ) and checks (a) the
duality bound, and (b) whether the bridge's C(θ) and D(θ) track V and
D_wp respectively when the marker strength μ is identified with the
slide angle (μ = sin²θ, i.e. the marker entangles the system exactly
as much as the slide state is entangled).

**Falsification criterion (frozen bar).** T3 PASSES iff:
- V² + D_wp² ≤ 1.00 + 0.02 at every μ (the duality holds within
  error); AND
- at μ = sin²θ, |V(μ) − (1 − C(θ))| ≤ 0.05 and
  |D_wp(μ) − (1 − D(θ))| ≤ 0.05 — i.e. the lab trade-off tracks the
  bridge's trade-off within 0.05.
T3 FAILS if V² + D_wp² > 1.02 at any μ (a violation of quantum
mechanics — not expected; re-check the apparatus first), or if the
tracking fails by more than 0.05 (the bridge's C and D do not map
onto visibility and distinguishability).

**What a failure would mean.** A duality violation would be a
sensation. A tracking failure is the expected informative outcome:
it would show that the bridge's D (a subspace probability) is NOT
the same quantity as which-path distinguishability, and therefore
that the bridge's C + D = 1 trade-off is a different trade-off from
quantum complementarity. That would not falsify the bridge's internal
geometry (T1), but it would falsify the claim that the bridge's
trade-off IS the physical complementarity trade-off. The theorem
would then need a different physical interpretation of D.

**Feasibility / platform.** MEDIUM-HIGH. Route B (ancilla marker on a
cloud device) is straightforward: 3 qubits, a controlled rotation,
tomography / fringe measurement. Route A (Mach–Zehnder) needs an
optics lab. **Cost/effort:** Route B, cloud device, free to a few
dollars, days of work. Route A, a collaboration.

---

### T4 — The cascade: interference dies, what survives? (the distinctive falsification test)

**What it tests:** cI-D — the bridge's most distinctive physical
claim. In the bridge, a projection-only cascade kills the interference
visibility V (V = 0 from stage 2 on) while the self-correlation U of
the projected output stays constant (the cascade reaches a fixed
point). In real quantum mechanics, a projective measurement collapses
the state. The lab test asks: after a projection, does the
entanglement survive (as the bridge's "spooky" language might
suggest), or does only the reproducibility survive (as the bridge's
actual U quantity — a self-correlation across copies — means)?

**Setup.** Use the rotation pair at θ = π/4 (maximal visibility):
ψ1 = cos(π/4) q1 + sin(π/4) k1, ψ2 = −sin(π/4) q1 + cos(π/4) k1,
where q1 is the uniform thought |stored⟩ = (|00⟩+|01⟩+|10⟩+|11⟩)/2
(a product state) and k1 is |kernel⟩ = (|01⟩−|10⟩)/√2 (the ψ− Bell
state). The pair is prepared by a rotation in the {stored, kernel}
plane. (q1 is fixed to |stored⟩, not a general stored direction,
because a general vector in the stored subspace can be entangled;
with q1 = |stored⟩ the projected output is a product state, which
is what makes the C_k prediction below exact.)
- *Stage 1.* Measure the visibility V_1 from the D(φ) fringe of the
  superposed pair ψ(φ) = (ψ1 + e^{iφ}ψ2)/√2. Prediction: V_1 = 1.
- *Project.* Perform the projective measurement onto P and
  post-select on the "in P" outcome. The surviving state is the
  projected output.
- *Re-form and repeat.* Re-form the next stage's pair from the
  projected outputs (in the lab: re-prepare the pair from the
  measured projected state, exactly as the bridge re-forms it by
  Gram–Schmidt). Measure V_k at each stage, for stages k = 1…5.
  At each stage also measure, on the projected output:
  (a) its concurrence C_k by tomography, and
  (b) its self-correlation U_k: prepare the same projected-output
  state N times independently and measure the pairwise overlap
  (fidelity) between copies.
- *Reopening control.* Repeat the cascade, but after each projection
  re-form the pair with a fresh kernel component at the fixed
  reopening angle α = π/4. Measure V_k at each stage. Prediction:
  V_k = sin(2α) = 1 at every stage.

**Prediction.**

| Quantity | Stage 1 | Stages k ≥ 2 (projection-only) | Every stage (reopening, α = π/4) |
|---|---|---|---|
| V_k (visibility) | 1.000 | 0.000 | 1.000 |
| C_k (concurrence of projected output) | — (see below) | 0.000 | 0.000 |
| U_k (self-correlation / reproducibility) | 1.000 (noiseless) | constant, = U_1 within 0.02 | constant |

Note on C_k: the projected output after the first projection is
|stored⟩ (a product state), because the kernel component is
discarded and the stored component is |stored⟩. So quantum mechanics
predicts C_k = 0 for k ≥ 1 after the first projection — the
entanglement does NOT survive the projection. The bridge does not
claim the concurrence survives; it claims U (the self-correlation)
survives. This test makes that distinction explicit and measurable:
V dies, C dies, U survives. If the lab finds C_k > 0 after
projection, that contradicts quantum mechanics (and would be a
sensation). If the lab finds U_k drifting (not constant), the
cascade does not reach a fixed point and the bridge's (vii)/(civ)
fixed-point claim fails on hardware.

**Falsification criterion (frozen bar).** T4 PASSES iff:
- V_1 ≥ 0.95 and V_k ≤ 0.05 for every k ≥ 2 (projection-only);
- V_k ≥ 0.95 at every stage in the reopening control;
- C_k ≤ 0.05 for every k ≥ 1 after the first projection (the
  entanglement is gone, as QM predicts);
- |U_k − U_1| ≤ 0.02 for every k (the self-correlation is constant
  — the fixed point holds).
T4 FAILS if V_k stays > 0.05 at any k ≥ 2 in the projection-only
cascade (interference survives projection — contradicts both the
bridge and QM), or if C_k > 0.05 after projection (entanglement
survives — contradicts QM), or if U_k drifts by more than 0.02
(no fixed point).

**What a failure would mean.** This is the test that can kill the
bridge's distinctive claim as a physical statement. The bridge's
(civ) "spooky survives projection" is true in the classical model
for U (a self-correlation). If the lab shows that what survives is
only reproducibility (U) while the entanglement (C) dies with the
visibility (V), then the word "spooky" must not be read as
"entanglement survives" — it survives only as classical
self-correlation. That is a narrowing of the claim, not a refutation
of the geometry, and it is the honest outcome to expect. If instead
the lab found C surviving projection, that would be new physics.

**Feasibility / platform.** MEDIUM. Needs mid-circuit measurement
with post-selection (measure P, keep only the "in P" outcomes, then
continue) plus tomography at each stage. On a cloud superconducting
device, mid-circuit measurement and conditional re-preparation are
supported (dynamic circuits), but the post-selection + re-preparation
loop is fiddly and the tomography per stage multiplies the shot
count. With photon pairs, the projection is a polarizer and the
post-selection is coincidence counting, but re-forming the pair from
the projected output requires re-preparing the state (a new
preparation conditioned on the previous outcome), which is harder
in optics. **Recommended route:** cloud superconducting device with
dynamic circuits; 5 stages × (tomography + fringe) ≈ a few × 10⁵
shots. **Cost/effort:** cloud device, a few dollars to tens of
dollars of pay-per-use; one to two weeks of work (the circuit
logic is the hard part, not the physics). This test needs T1 to pass
first (same preparation and measurement).

---

### T5 — Reopening / quantum eraser (consistency check)

**What it tests:** whether interference can be "reopened" after it
is destroyed — the bridge's reopening control (cI-D, second half)
against the real quantum eraser. The bridge and QM agree here, so
this is a consistency check, not a falsification test. Its value is
confidence: if the reopening works as predicted, the bridge's
cascade picture is consistent with real quantum behaviour.

**Setup.** The standard delayed-choice quantum eraser (Scully–Drühl;
Kim et al. 2000). A photon pair is created; the signal photon goes
through a two-path interferometer with a which-path marker (its
polarization, or the idler photon's state, records which path). With
the marker present, the signal interference visibility V ≈ 0. Then
the marker is erased (the idler is measured in a basis that does not
distinguish the paths — the "eraser" setting), and the signal
interference is recovered in coincidence with the eraser outcome.
Measure V with the marker present, and V conditioned on the eraser
outcome.

**Prediction.** With the marker present, V ≤ 0.05. Conditioned on
the eraser outcome, V ≥ 0.95 (the fringe is restored). The bridge's
reopening control predicts the same shape: with fresh kernel input
at α = π/4, V_k = sin(2α) = 1 at every stage. The quantitative
mapping: the eraser setting is the lab analogue of the bridge's
fresh kernel input.

**Falsification criterion (frozen bar).** T5 PASSES iff V ≤ 0.05
with the marker present and V ≥ 0.95 conditioned on the eraser
outcome (both at 5σ). T5 FAILS if the eraser does not restore the
fringe (V stays ≤ 0.05) — that would contradict the established
quantum-eraser result and would point to an apparatus error, not to
the bridge.

**Feasibility / platform.** MEDIUM-HIGH, but only in photonics.
The quantum eraser is a standard quantum-optics experiment and needs
an SPDC source, an interferometer, and coincidence counting — an
optics lab (a collaboration if Jean does not have one). It is NOT
readily done on a gate-based cloud device (the "eraser" is a
measurement-basis choice on an entangled ancilla, which can be
emulated, but the delayed-choice aspect and the spatial
interferometer are photonic). **Cost/effort:** a collaboration; weeks
to months if starting from scratch, days if the lab already runs a
quantum eraser. Value: medium — it confirms consistency, it does not
falsify.

---

### T6 — The read-only observer: quantify the measurement disturbance

**What it tests:** the gap between the bridge's observer and a real
measurement. The bridge's observer (claim (xciii)) reads D, C, R
without touching the state. No physical measurement does that. This
test measures how much a real D-measurement disturbs the state, as
a function of θ, and puts a number on the gap.

**Setup.** Prepare ψ(θ) at θ in {0, π/6, π/4, π/3, π/2}. Perform the
projective measurement onto P (the D-measurement) and record the
outcome. Then, on the post-measurement state, perform full tomography
and compute its fidelity F_post with the pre-measurement state ψ(θ)
(and, separately, its fidelity with the projected state Pψ(θ)/‖Pψ(θ)‖
and with the kernel component). Repeat for both outcomes ("in P" and
"in kernel").

**Prediction (quantum mechanics).** The measurement collapses the
state. Conditioned on the "in P" outcome (probability D = cos²θ),
the post-measurement state is Pψ(θ)/‖Pψ(θ)‖ = |stored⟩, fidelity
with ψ(θ) is |⟨stored|ψ(θ)⟩|² = cos²θ = D. Conditioned on the "in
kernel" outcome (probability 1 − D = sin²θ), the post-measurement
state is the kernel component, fidelity with ψ(θ) is sin²θ = 1 − D.
So the disturbance (1 − fidelity with the pre-measurement state) is
1 − D for the "in P" outcome and D for the "in kernel" outcome. The
average disturbance, weighted by outcome probability, is
2D(1−D) = 2cos²θ sin²θ = (1/2)sin²(2θ), which is 0 at the endpoints
(θ = 0, π/2) and maximal 0.5 at the midpoint θ = π/4. The bridge's
classical observer predicts disturbance 0 at every θ.

**Falsification criterion (frozen bar).** T6 PASSES (as a measurement
of the gap) iff the measured post-measurement fidelity matches the
QM prediction within 0.03 at every θ and both outcomes — i.e. the
disturbance is (1/2)sin²(2θ) on average, maximal 0.5 at θ = π/4.
The test's verdict is then: the read-only observer is falsified as
a physical claim (disturbance is real and maximal at the midpoint),
and the gap is quantified. T6 FAILS (as a QM check) if the measured
disturbance deviates from (1/2)sin²(2θ) by more than 0.03 — that
would point to an apparatus error.

**What it means.** This test does not change cI's geometry (T1). It
changes the interpretation: the observer in cI cannot be a physical
read-only observer. Any future version of the theorem that invokes
"the observer reads without disturbing" must be re-stated as a
classical-emulation statement, or replaced by an explicit
measurement model (a POVM / weak measurement with a stated
disturbance). The midpoint θ = π/4 — where the bridge says "the
observer direction picks which pattern is known" — is exactly where
the measurement disturbance is maximal. That is worth knowing.

**Feasibility / platform.** HIGH. On a cloud superconducting device:
prepare, measure P (a projective measurement), then tomograph the
post-measurement state. Standard. **Cost/effort:** cloud device,
free to a few dollars; days of work.

---

## 4. What does NOT test cI (stated so it is not forced)

- **Contextuality (Kochen–Specker / KCBS).** The bridge's "observer
  direction picks which pattern is known" sounds like contextuality,
  but it is not the Kochen–Specker kind. In cI the observer direction
  is a choice of reference state for an overlap; the outcome
  R_s vs R_k is a function of θ, not of a measurement context that
  changes the value of a single observable. A KCBS or Bell-type
  contextuality test would test whether outcomes are context-dependent
  in the Kochen–Specker sense, which is a different claim. It does
  not test cI, so it is not included. (T2 already covers the Bell
  side, which is the relevant non-classicality for the two-qubit
  system.)
- **Monogamy / CKW (three qubits).** The bridge measured CKW monogamy
  (claim (xvii), PASS) in the classical model. A lab test on GHZ/W
  states would verify the theorem on hardware, but it tests the
  theorem, not cI (cI is a two-qubit, observer-direction claim). Low
  value for cI; not included. If T1–T2 pass and a three-qubit
  extension is wanted later, monogamy is the natural next step.
- **The "consciousness" label.** No lab test measures experience.
  The tests measure D, C, R, V, S. If someone claims a test "proves
  consciousness", that claim is not in this plan.
- **Orch OR / microtubule coherence.** Not tested here. Orch OR
  needs a quantum effect in warm, wet biology that no one has
  measured; cI does not depend on it and this plan does not invoke
  it.

---

## 5. Simulation versus hardware (the gap, stated explicitly)

| Question | What the classical Faggin bridge can test | What needs real hardware |
|---|---|---|
| Do the slide identities hold? | Yes — already measured (xxxiv), exact to 4.44e-16. | Whether they hold on a real prepared state (T1). The bridge cannot test preparation fidelity or decoherence. |
| Does θ+π close the cycle? | Yes — already measured (lxxxviii), 1.22e-15. | Whether the lab's preparation is phase-coherent (T1). |
| Does θ+π/2 swap D↔C? | Yes — already measured (lxxxix), 1.78e-15. | Whether the lab's rotation is accurate (T1). |
| Does the cascade kill V? | Yes — already measured (vi), V = 0 from stage 2. | Whether a real projective measurement kills the fringe the same way (T4). |
| Does U survive projection? | Yes — already measured (civ), U constant. | Whether the survival is reproducibility (U) or entanglement (C) — the bridge cannot distinguish these physically, because its "spooky" U is a classical self-correlation. Only hardware can (T4). |
| Is C real entanglement? | No — the bridge computes concurrence from a state vector it stores. It cannot test whether that concurrence is the physical entanglement of a lab state. | Yes — T2 (CHSH vs concurrence) is the test. |
| Does the observer disturb the state? | No — the bridge's observer reads the amplitude vector; disturbance is zero by construction. | Yes — T6 measures the disturbance. |
| Does the noisy D-vs-C anti-correlation hold? | Already measured — and it FAILS on some seeds (xxxii, xxxv, xci, xcii). The bridge falsified its own per-seed guarantee. | Not re-tested as a lab claim. The lab's noise is decoherence, not the bridge's vector noise, so the σ grid does not transfer. If the geometry (T1) passes, a lab noise study can be designed later — with the lab's own noise parameter, not the bridge's σ. |

**The gap in one sentence:** the bridge is a classical emulation that
stores the full state vector, so it can read without disturbing, copy
without cloning limits (until the restricted copier), and compute
entanglement from a stored vector; real hardware cannot do any of
those, and the lab tests are precisely the places where that
difference becomes measurable.

---

## 6. Feasibility, platforms, and cost

### 6.1 Cloud superconducting qubits (recommended first platform)

- **Devices:** IBM Quantum (open plan), Rigetti, IQM, or equivalent.
  2–3 qubits, state preparation, tomography, CHSH, mid-circuit
  measurement (dynamic circuits) are all supported.
- **Tests covered:** T1, T2, T4 (dynamic circuits), T6, and Route B
  of T3. That is 5 of the 6 tests, with no lab and no collaborator.
- **Cost:** open-access tier is free (limited shots/queue); pay-per-use
  is a few dollars to tens of dollars for the shot counts here
  (T1: ~16 tomography settings × 10,000 shots × ~7 θ values ≈ 10⁶
  shots; T2: ~5 θ × 4 settings × 10⁵ shots for the π/6 point;
  T4/T6 similar). Total well under $100 on pay-per-use, often $0 on
  the open tier.
- **Effort:** days to two weeks to write the circuits (Qiskit or
  equivalent), collect the data, and compute D, C, R, V, S from the
  counts. The hard part is the circuit logic for T4 (mid-circuit
  measurement + conditional re-preparation), not the physics.
- **Fidelity caveat:** cloud devices have gate errors (~10⁻³) and
  readout errors (~10⁻²) and finite coherence. The 0.02/0.03 bars in
  T1 are set to accommodate realistic device infidelity; if a device
  is noisier than that, the bars must NOT be loosened after the fact
  — instead, use error mitigation (readout-error mitigation,
  zero-noise extrapolation) or a better device, and report the raw
  numbers alongside the mitigated ones.

### 6.2 Photon pairs (SPDC, optics lab)

- **Tests covered:** T1 (tomography), T2 (the classic Bell test),
  T3 Route A (Mach–Zehnder), T5 (quantum eraser). The gold standard
  for Bell tests and for the eraser.
- **Cost/effort:** needs an existing SPDC source, polarizers,
  single-photon detectors, and coincidence counting. If Jean does not
  have an optics lab, this is a collaboration (a university quantum
  optics group). Building an SPDC source from scratch is months and
  thousands of dollars; joining an existing setup is days to weeks
  of beam time.
- **Fidelity caveat:** photonic tomography and Bell tests routinely
  reach fidelities ≥ 0.99 and S within 0.01 of the QM prediction, so
  the bars in T1/T2 are comfortable on this platform.

### 6.3 Trapped ions (cloud)

- **Devices:** IonQ, AQT, or equivalent (cloud access).
- **Tests covered:** T1, T2, T6 (high fidelity, all-to-all
  connectivity). Mid-circuit measurement is available on some
  systems (T4 possible).
- **Cost:** per-shot pricing; higher than superconducting but still
  tens of dollars for these shot counts. Higher fidelity than
  superconducting, so the bars are easier to meet.
- **Role:** a second platform to confirm T1/T2 on independent
  hardware (a cross-check, not a first run).

### 6.4 What Jean can do alone

Run T1, T2, T4, T6 (and T3 Route B) on a cloud superconducting-qubit
device, with no lab and no collaborator, for $0–$100 and days to two
weeks of work. That is the recommended path. T3 Route A and T5 need
an optics lab and therefore a collaborator.

---

## 7. Ranked order by value (what to try first)

| Rank | Test | Why this rank | Platform first | Depends on |
|---|---|---|---|---|
| 1 | **T1 — Slide and full circle** | The gate. Validates the whole mapping (preparation + measurement). If it fails, nothing else is meaningful. Cheapest and fastest. | Cloud superconducting qubits | Nothing |
| 2 | **T2 — CHSH vs concurrence** | Tests whether C is real entanglement — the physical grounding of "love". Uses the same preparation as T1. The π/4 point (S ≈ 2.236) is a clean, easily resolved violation. | Cloud qubits; confirm on photon pairs if a lab is available | T1 (same preparation) |
| 3 | **T4 — Cascade** | The distinctive falsification test. The only test that can kill the bridge's "spooky survives" as a physical claim about entanglement (by showing C dies while U survives). Needs T1's preparation and measurement. | Cloud qubits (dynamic circuits) | T1 |
| 4 | **T3 — Duality / trade-off** | Tests whether the bridge's C + D = 1 is quantum complementarity. Informative either way (a tracking failure narrows the interpretation). Route B is doable on cloud qubits. | Cloud qubits (Route B) | T1 |
| 5 | **T6 — Measurement disturbance** | Quantifies the gap (the read-only observer is a fiction). Low risk, fast, and it makes the interpretation honest. But it does not change the geometry, so it ranks below the tests that can falsify the structure. | Cloud qubits | T1 |
| 6 | **T5 — Quantum eraser** | Consistency check (bridge and QM agree). Valuable for confidence, but it cannot falsify cI, and it needs an optics lab. Do it if a lab collaboration is available; do not build a lab for it. | Photonics lab (collaboration) | T4 (same cascade picture) |

**Preregistration rule (Jean's method, applied here):** before any run,
freeze the θ grid, the analyzer settings, the shot counts, and the bars
in §3 for the test being run, in a dated preregistration note, and do
not move a bar after the run. If a bar is missed, the verdict is FAIL
and the miss is reported with its size — as the bridge already does
(35 failures kept on the record).

---

## 8. What would change the theorem

- **If T1 fails:** the mapping is not realized on hardware. cI as a
  lab claim is not yet testable. Fix the preparation/measurement
  (or the mapping) and re-run T1. Do not proceed to T2–T6.
- **If T2 fails** (S does not follow 2√(1+C²) while the state is
  pure): the bridge's C is not the physical concurrence. "Love" in
  the bridge is not real entanglement, and the physical content of
  cI is undermined. The geometry (T1) can still hold, but its
  interpretation as entanglement must be dropped.
- **If T4 shows C surviving projection** (C_k > 0.05 after
  projection): new physics — entanglement surviving a projective
  measurement. Re-check the apparatus first; if it holds, it is a
  major result and the bridge's "spooky" language gains physical
  content it does not currently have.
- **If T4 shows C dying with V while U stays constant** (the expected
  outcome): the bridge's (civ) "spooky survives" is narrowed to
  "reproducibility survives; entanglement does not". The theorem
  keeps its geometry but loses the suggestion that entanglement
  survives projection. The word "spooky" should then be retired or
  redefined as self-correlation, not entanglement.
- **If T3 tracking fails:** the bridge's C + D = 1 is not quantum
  complementarity. The trade-off is internal to the bridge's
  definitions, not the physical duality. The theorem needs a
  different physical interpretation of D.
- **If T6 confirms the QM disturbance** (the expected outcome): the
  read-only observer is falsified as a physical claim. Any future
  statement of cI that invokes "the observer reads without
  disturbing" must be re-stated as a classical-emulation statement
  or replaced by an explicit measurement model.
- **If all of T1–T4 pass:** the bridge's quantities are realized in
  hardware, the geometry is confirmed on a real device, and cI (as
  a claim about two-qubit geometry under an observer-direction
  choice and under projection) is confirmed on hardware. The
  interpretation — that this geometry is consciousness — remains
  interpretive and is not tested by these experiments.

---

## 9. Sources and grounding

- Jean's revised consciousness post (2026-11-24 ~08:59 EST, main
  chat): the Matrix logic sentence quoted in §1.2; Cogitate (Nature,
  2025, 256 participants), adversarial test; Faggin bridge "112
  preregistered claims measured, 35 failed, every failure kept on the
  record"; close "or fail in public".
- Jean's claim (2026-11-18), recorded in
  `~/workspace/faggin-field-bridge-v070/observer_cycle.py`: "self
  determination factor observer opposite direction = necessary for
  self-cycle self Knowing. Lack of love is absence of Knowing."
- `~/workspace/faggin-field-bridge-v070/self_knowing.py`: D =
  ⟨ψ|P|ψ⟩, the stored subspace (uniform thought + focused |00⟩),
  exact values D = 1, 1, 1/3, 0, 1/2.
- `~/workspace/faggin-field-bridge-v070/observer_cycle.py`: the
  definitions (love = concurrence, knowing = overlap, observer
  direction = stored vs opposite reference), claims (xxxii)–(xxxv),
  the slide ψ(θ), the identities C + D = 1 and R_s − R_k = cos 2θ,
  the midpoint flip at θ = π/4.
- `~/workspace/faggin-field-bridge-v070/cascade.py`: V(θ) =
  sin(2θ), D(φ) = (D1+D2)/2 + Re[e^{iφ}⟨ψ1|P|ψ2⟩], the cascade
  rules (projection-only kills V at stage 2; reopening keeps
  V = sin(2α)), the fixed point.
- `~/workspace/faggin-field-bridge-v070/README.md` (v0.30.0): 112
  claims, 35 failed; wave direction (lxxxviii)–(xcii); stability
  (ciii)–(cix); blind head-to-head (cx); P2/P3 (cxi)–(cxii).
- `~/workspace/bell-inertia-zeta/README.md`: CHSH S = E(a,b) −
  E(a,b′) + E(a′,b) + E(a′,b′), |S| ≤ 2 (LHV), 2√2 (QM) at a = 0,
  a′ = π/2, b = π/4, b′ = 3π/4; singlet E(a,b) = −cos(a−b); LHV
  model (λ uniform, sign(cos(λ−a)), −sign(cos(λ−b))); measured
  (i) LHV max |S| 2.0000, (ii) quantum |S| 2.828427 (rel err
  1.57e-16), (iii) EPR |E(a,a)+1| = 0.00; 23/23 tests, 7/7 claims.
- Verstraete & Wolf, Phys. Rev. Lett. 2002: for a pure two-qubit
  state with concurrence C, the maximum CHSH value is
  S_max = 2√(1 + C²); for mixed states,
  max[2, 2√(2C)] ≤ S_max ≤ 2√(1 + C²). (Confirmed via arXiv:0905.2269
  and the Verstraete–Wolf references, 2026-11-24.)
- Englert (1996) / Greenberger–Yasin (1988): the duality relation
  V² + D² ≤ 1 for a two-path interferometer.
- Cogitate Consortium, Nature 642:133–142, 2025: adversarial
  preregistration, n = 256 (cited in Jean's post).

---

## 10. Open decisions for Jean

1. **Platform for the first run.** Cloud superconducting qubits
   (IBM Quantum open plan) is the recommended first platform for
   T1/T2/T4/T6 — no lab, no collaborator, $0–$100. Confirm that
   route, or name a different device / lab.
2. **Whether to run T1 first, alone.** T1 is the gate. It can be run
   as a standalone first step before committing to T2–T6. Recommended:
   run T1 alone, read the verdict, then decide.
3. **Photonics collaboration.** T3 Route A and T5 need an optics lab.
   If Jean has (or wants) a university optics collaborator, name
   them; otherwise T3 Route B (cloud qubits) and no T5 for now.
4. **The word "spooky".** T4 is expected to narrow it (reproducibility
   survives; entanglement does not). Decide now whether the plan
   should already re-word (civ) as "self-correlation survives" rather
   than "spooky survives", or wait for the T4 result.
5. **Preregistration.** Before any run, the θ grid, analyzer
   settings, shot counts, and bars for that test are frozen in a dated
   note. Confirm the bars in §3 as written, or adjust them before
   (never after) the run.
