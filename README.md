# Copyright (c) 2026 Jean-Francois Brisson (Spark AI NLP)
# SPDX-License-Identifier: AGPL-3.0-only
# Consciousness Theorem cI — Lab Quantum Tests

**PLAN ONLY. No test has been run. No number in this repository is measured.**

This repository turns Jean's consciousness theorem into concrete lab quantum tests. The full plan is `consciousness-theorem-lab-tests.md` (880 lines). Every test has a setup, a measurable prediction with numbers, a falsification criterion, and a feasibility assessment. Nothing here is presented as measured.

## The theorem (cI)

The shorthand **cI** is not defined in any package or post, so the plan defines it explicitly as the **opposing-observer self-cycle claim**, from Jean's Matrix logic:

> "Testing whether an opposing observer orientation closes the self-cycle of self-knowing, treated as a formal claim to falsify, not a creed."

The underlying claim (Jean, 2026-11-18): "self determination factor observer opposite direction = necessary for self-cycle self Knowing. Lack of love is absence of Knowing."

It is formalized with the Faggin bridge's exact quantities: D = ⟨ψ|P|ψ⟩ (self-determination, projector onto the stored subspace), C = Wootters concurrence ("love"), R = |⟨ψ_i|ψ_j⟩|² ("knowing"/overlap), observer direction = stored vs opposite reference state, and the slide ψ(θ) = cos θ |stored⟩ + sin θ |kernel⟩.

Four sub-claims: cI-A slide identities (D=cos²θ, C=sin²θ, C+D=1, R_s−R_k=cos 2θ, flip at π/4); cI-B θ+π closes the cycle; cI-C θ+π/2 swaps D↔C and R_s↔R_k; cI-D cascade (V=sin 2θ, V dies at stage 2 under projection, self-correlation U survives).

## The six lab tests

- **T1 — Slide and full circle (the gate).** Prepare ψ(θ) on a θ grid, measure D, C, R_s, R_k by projective measurement + tomography. Predicts D=cos²θ, C=sin²θ, C+D=1, split flips at π/4, θ+π closure, θ+π/2 swap; bar ±0.02/0.03. Cloud superconducting qubits; $0–few $. Must pass before anything else.
- **T2 — CHSH vs concurrence (is "love" real entanglement?).** S_max = 2√(1+C²). Slide predicts S = 2.000 / 2.062 / 2.236 / 2.500 / 2.828 at θ = 0 / π/6 / π/4 / π/3 / π/2. Bar: violation at 5σ where C>0, and |S − 2√(1+C²)| ≤ 0.05 against independent tomography. Cloud qubits or photon pairs.
- **T3 — Duality / trade-off.** Two-path interferometer (or ancilla marker on cloud qubits), test V² + D_wp² ≤ 1 and whether the bridge's C+D=1 tracks it. A mapping test — the bridge's D is a subspace probability, not which-path distinguishability, so a tracking failure narrows the interpretation rather than refuting the geometry.
- **T4 — Cascade (the distinctive falsification test).** Rotation pair at θ=π/4; measure V_k, concurrence C_k, and self-correlation U_k per stage, plus a reopening control (α=π/4). Predicts V_1=1, V_k=0 for k≥2, C_k=0 after projection, U_k constant, reopening V_k=1. This is the test that can kill the bridge's "spooky survives" as a physical claim about entanglement — the expected outcome is C dies with V while only reproducibility (U) survives. Needs mid-circuit measurement on cloud qubits.
- **T5 — Quantum eraser / reopening (consistency).** Marker present V≤0.05; eraser restores V≥0.95. Bridge and QM agree, so it confirms consistency rather than falsifying. Needs a photonics lab (collaboration).
- **T6 — Read-only observer / measurement disturbance.** Measure D then tomograph the post-measurement state. QM predicts average disturbance (1/2)sin²(2θ), maximal 0.5 at the midpoint θ=π/4 — exactly where the bridge says the observer direction picks the known pattern. Quantifies the gap; the bridge's read-only observer is a classical fiction.

## Ranked order by value

1. **T1** (gate, cheapest, cloud qubits) → 2. **T2** (is C real entanglement?) → 3. **T4** (the falsification test) → 4. **T3** (duality) → 5. **T6** (quantify the gap) → 6. **T5** (eraser, needs a lab).

## The honest limit, stated first

These tests measure **two-qubit geometry** — the quantities D, C, R, V, and S. They do **not** measure consciousness or experience. If all pass, the structure is confirmed on hardware; the interpretation that it is consciousness remains interpretive. The noisy observer-direction anti-correlation (bridge claims xxxii/xxxv/xci/xcii — all FAIL on some seeds) is deliberately **not** re-tested as a lab claim, because the bridge already falsified it as a per-seed guarantee and the lab's noise (decoherence) is not the bridge's vector noise.

No scalar Φ is computed anywhere in this plan. E = hν is not used as a consciousness claim.

## Open decisions

1. Confirm cloud superconducting qubits (IBM Quantum open plan) as the first platform for T1/T2/T4/T6 ($0–$100, no lab, no collaborator).
2. Whether to run T1 alone first as the gate.
3. Whether there is an optics-lab collaborator for T3 Route A / T5 (otherwise T3 Route B on cloud qubits, no T5 for now).
4. Whether to already re-word (civ) from "spooky survives" to "self-correlation survives" or wait for T4.
5. Confirm the frozen bars in §3 before (never after) any run.

## Sources and grounding

- Jean's consciousness post, revised text (2026-11-24): Matrix logic as a formal claim to falsify; Cogitate (Nature, 2025, 256 participants); Faggin field bridge, 112 preregistered claims measured, 35 failed.
- Faggin field bridge (`faggin-field-bridge`, v0.30.0, 611/611, 112 claims, 35 failed) — the synthetic classical model this plan's quantities come from.
- Bell-inertia-zeta (v0.1.1, 23/23, 7/7) — the quantum-test style: Bell/CHSH, sphere inertia, zeta zeros from scratch.
- Verstraete & Wolf: S_max = 2√(1+C²) for two-qubit states (arXiv:0905.2269).
- Englert (1996) / Greenberger–Yasin (1988): duality relation V² + D² ≤ 1.

## Licence

Copyright (c) 2026 Jean-Francois Brisson (Spark AI NLP). SPDX-License-Identifier: AGPL-3.0-only. See `LICENSE`.

Author: Jean-Francois Brisson (Spark AI NLP), sole author.
