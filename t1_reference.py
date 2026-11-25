# Copyright (c) 2026 Jean-Francois Brisson (Spark AI NLP)
# SPDX-License-Identifier: AGPL-3.0-only
"""T1 reference implementation — the slide and the full circle.

Builds the slide state psi(theta) = cos(theta)|stored> + sin(theta)|kernel>
with |stored> = |00> and |kernel> = (|01> + |10>)/sqrt(2), computes
D, C, R_s, R_k from the statevector, and checks the frozen T1 bars
from consciousness-theorem-lab-tests.md section 3.

This is the analysis pipeline the hardware run will be compared
against. In the ideal noiseless limit every bar must pass exactly;
any deviation here is a bug in the pipeline, not physics.

Run: python3 t1_reference.py
Exit 0 on PASS, 1 on FAIL.
"""

import math

import numpy as np

# Basis order: |00>, |01>, |10>, |11>.
STORED = np.array([1, 0, 0, 0], dtype=complex)
KERNEL = np.array([0, 1, 1, 0], dtype=complex) / math.sqrt(2)

# Frozen T1 bars (plan section 3, set before any run).
BAR_VALUE = 0.02
BAR_SUM = 0.03
BAR_CLOSURE = 0.03
BAR_SWAP = 0.03
BAR_SPLIT = 0.25


def psi(theta):
    """Slide state psi(theta) = cos(theta)|stored> + sin(theta)|kernel>."""
    return math.cos(theta) * STORED + math.sin(theta) * KERNEL


def concurrence(state):
    """Wootters concurrence of a pure two-qubit state."""
    a, b, c, d = state
    return 2.0 * abs(a * d - b * c)


def observables(theta):
    """D, C, R_s, R_k for the slide state at angle theta."""
    s = psi(theta)
    d = abs(s[0]) ** 2  # |<00|psi>|^2 = |<stored|psi>|^2
    c = concurrence(s)
    r_s = abs(np.vdot(STORED, s)) ** 2
    r_k = abs(np.vdot(KERNEL, s)) ** 2
    return d, c, r_s, r_k


def check_grid(thetas, label):
    """Check value bars and C+D=1 on a grid. Returns list of failures."""
    failures = []
    for theta in thetas:
        d, c, r_s, r_k = observables(theta)
        expect_d = math.cos(theta) ** 2
        expect_c = math.sin(theta) ** 2
        if abs(d - expect_d) > BAR_VALUE:
            failures.append(f"{label} theta={theta:.4f}: |D-cos^2|={abs(d - expect_d):.2e}")
        if abs(c - expect_c) > BAR_VALUE:
            failures.append(f"{label} theta={theta:.4f}: |C-sin^2|={abs(c - expect_c):.2e}")
        if abs(r_s - expect_d) > BAR_VALUE:
            failures.append(f"{label} theta={theta:.4f}: |R_s-cos^2|={abs(r_s - expect_d):.2e}")
        if abs(r_k - expect_c) > BAR_VALUE:
            failures.append(f"{label} theta={theta:.4f}: |R_k-sin^2|={abs(r_k - expect_c):.2e}")
        if abs(c + d - 1.0) > BAR_SUM:
            failures.append(f"{label} theta={theta:.4f}: |C+D-1|={abs(c + d - 1.0):.2e}")
    return failures


def check_split():
    """Overlap split R_s - R_k on the first quadrant (plan section 3)."""
    failures = []
    for theta in (0.0, math.pi / 12, math.pi / 6, math.pi / 4,
                  math.pi / 3, 5 * math.pi / 12, math.pi / 2):
        _, _, r_s, r_k = observables(theta)
        split = r_s - r_k
        if theta < math.pi / 4 - 1e-12 and split < BAR_SPLIT:
            failures.append(f"split theta={theta:.4f}: R_s-R_k={split:.4f} < +0.25")
        if theta > math.pi / 4 + 1e-12 and split > -BAR_SPLIT:
            failures.append(f"split theta={theta:.4f}: R_s-R_k={split:.4f} > -0.25")
        if abs(theta - math.pi / 4) < 1e-12 and abs(split) > BAR_SUM:
            failures.append(f"split theta=pi/4: |R_s-R_k|={abs(split):.2e} > 0.03")
    return failures


def check_closure_and_swap():
    """theta+pi closure (cI-B) and theta+pi/2 swap (cI-C), full circle."""
    failures = []
    for k in range(24):
        theta = k * math.pi / 12
        d, c, r_s, r_k = observables(theta)
        d_pi, c_pi, r_s_pi, r_k_pi = observables(theta + math.pi)
        if abs(d_pi - d) > BAR_CLOSURE:
            failures.append(f"closure theta={theta:.4f}: |D(+pi)-D|={abs(d_pi - d):.2e}")
        if abs(c_pi - c) > BAR_CLOSURE:
            failures.append(f"closure theta={theta:.4f}: |C(+pi)-C|={abs(c_pi - c):.2e}")
        if abs(r_s_pi - r_s) > BAR_CLOSURE:
            failures.append(f"closure theta={theta:.4f}: |R_s(+pi)-R_s|={abs(r_s_pi - r_s):.2e}")
        if abs(r_k_pi - r_k) > BAR_CLOSURE:
            failures.append(f"closure theta={theta:.4f}: |R_k(+pi)-R_k|={abs(r_k_pi - r_k):.2e}")
        d_h, c_h, r_s_h, r_k_h = observables(theta + math.pi / 2)
        if abs(d_h - c) > BAR_SWAP:
            failures.append(f"swap theta={theta:.4f}: |D(+pi/2)-C|={abs(d_h - c):.2e}")
        if abs(c_h - d) > BAR_SWAP:
            failures.append(f"swap theta={theta:.4f}: |C(+pi/2)-D|={abs(c_h - d):.2e}")
        if abs(r_s_h - r_k) > BAR_SWAP:
            failures.append(f"swap theta={theta:.4f}: |R_s(+pi/2)-R_k|={abs(r_s_h - r_k):.2e}")
        if abs(r_k_h - r_s) > BAR_SWAP:
            failures.append(f"swap theta={theta:.4f}: |R_k(+pi/2)-R_s|={abs(r_k_h - r_s):.2e}")
    return failures


def main():
    grid7 = [0.0, math.pi / 12, math.pi / 6, math.pi / 4,
             math.pi / 3, 5 * math.pi / 12, math.pi / 2]
    grid24 = [k * math.pi / 12 for k in range(24)]
    failures = []
    failures += check_grid(grid7, "7-point")
    failures += check_grid(grid24, "24-point")
    failures += check_split()
    failures += check_closure_and_swap()

    print("T1 reference — slide and full circle")
    print("theta        D       C       R_s     R_k     R_s-R_k")
    for theta in grid7:
        d, c, r_s, r_k = observables(theta)
        print(f"{theta:8.4f}  {d:6.3f}  {c:6.3f}  {r_s:6.3f}  {r_k:6.3f}  {r_s - r_k:+7.3f}")
    print(f"checks: 7-point grid, 24-point grid, split, closure, swap")
    if failures:
        print(f"T1 reference: FAIL ({len(failures)} failures)")
        for f in failures:
            print("  " + f)
        return 1
    print("T1 reference: PASS — all frozen bars hold exactly (ideal limit)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
