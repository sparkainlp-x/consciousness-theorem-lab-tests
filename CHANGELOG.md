# Copyright (c) 2026 Jean-Francois Brisson (Spark AI NLP)
# SPDX-License-Identifier: AGPL-3.0-only
# Changelog

## 0.1.1 (2026-11-24)

- Adds `t1_reference.py`: the T1 analysis pipeline as runnable code.
  Builds ψ(θ) = cos θ |00⟩ + sin θ (|01⟩+|10⟩)/√2, computes D, C,
  R_s, R_k from the statevector, and checks every frozen T1 bar
  (value ±0.02, C+D−1 ±0.03, split, θ+π closure, θ+π/2 swap) on
  the 7-point and 24-point grids. **Measured: PASS** — the table
  reproduces the plan's predictions exactly (D=cos²θ, C=sin²θ,
  flip at π/4, closure, swap), exit 0. This validates the pipeline
  the hardware run will be compared against; it is not a hardware
  result. No plan text or bar changed.

## 0.1.0 (2026-11-24)

- Plan only. No test has been run; no number in this repository is measured.
- Defines cI explicitly as the opposing-observer self-cycle claim, from Jean's Matrix logic, formalized with the Faggin bridge's quantities (D self-determination, C concurrence/"love", R overlap/"knowing").
- Six lab quantum tests (T1–T6), each with setup, measurable prediction, frozen falsification bar, and feasibility: T1 slide and full circle (the gate, cloud qubits), T2 CHSH vs concurrence, T3 duality, T4 cascade (the falsification test), T5 quantum eraser, T6 read-only observer / measurement disturbance.
- Ranked order by value: T1 → T2 → T4 → T3 → T6 → T5.
- Honest limit stated up front: the tests measure two-qubit geometry, not consciousness or experience; the interpretation remains interpretive.
- Five open decisions for Jean: platform (IBM Quantum open plan), T1 alone first, optics-lab collaborator, re-wording "spooky survives", confirming frozen bars before any run.
