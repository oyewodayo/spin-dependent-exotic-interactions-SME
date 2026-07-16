"""
pauli_matrices.py
=================
Symbolic and numeric Pauli matrix algebra for the nonrelativistic sector
of the FW-transformed Hamiltonians.

This module operates purely in 2x2 space (upper-component / NR limit).
It provides everything needed to verify the final nonrelativistic
Hamiltonians H^NR_{b_mu}, H^NR_{H_munu}, H^NR_{d_munu} symbolically.

Conventions
-----------
- sigma^i are the standard 2x2 Pauli matrices.
- Spin eigenstates: |+z> = (1,0)^T, |-z> = (0,1)^T.
- CPT conjugation rule implemented for SME coefficients.
- Natural units throughout.

References
----------
Dobrescu & Mocioiu, JHEP 0811:005 (2006).
Kostelecky & Lane, Phys. Rev. D 60, 116010 (1999).
"""

import sympy as sp
from sympy import (
    I, Matrix, symbols, sqrt, Rational, simplify, expand,
    zeros, eye, Symbol, Abs, conjugate, trace
)
import numpy as np

# ---------------------------------------------------------------------------
# Pauli matrices — symbolic
# ---------------------------------------------------------------------------

sigma_x = Matrix([[0, 1], [1, 0]])
sigma_y = Matrix([[0, -I], [I, 0]])
sigma_z = Matrix([[1, 0], [0, -1]])
I2 = eye(2)
Z2 = zeros(2, 2)

sigma = [sigma_x, sigma_y, sigma_z]  # sigma[0]=sx, sigma[1]=sy, sigma[2]=sz

# Pauli matrices — numeric (for numerical checks)
sx_num = np.array([[0, 1], [1, 0]], dtype=complex)
sy_num = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz_num = np.array([[1, 0], [0, -1]], dtype=complex)
I2_num = np.eye(2, dtype=complex)
sigma_num = [sx_num, sy_num, sz_num]

# ---------------------------------------------------------------------------
# Spin eigenstates
# ---------------------------------------------------------------------------

spin_up   = Matrix([1, 0])   # |+z>
spin_down = Matrix([0, 1])   # |-z>

# ---------------------------------------------------------------------------
# Basic 2x2 algebra
# ---------------------------------------------------------------------------

def comm2(A, B):
    """[A, B] = AB - BA  in 2x2."""
    return A * B - B * A


def acomm2(A, B):
    """{A, B} = AB + BA  in 2x2."""
    return A * B + B * A


def expectation(psi, M):
    """
    <psi | M | psi> for a normalised 2-component spinor psi (column Matrix).
    Returns scalar (SymPy expression).
    """
    return (psi.H * M * psi)[0, 0]


# ---------------------------------------------------------------------------
# Pauli product identity
# ---------------------------------------------------------------------------

def pauli_product(a_coeffs, b_coeffs):
    """
    Compute (a . sigma)(b . sigma) = (a . b) I + i (a x b) . sigma
    symbolically, where a_coeffs and b_coeffs are length-3 lists of
    SymPy symbols or expressions.

    Returns
    -------
    result : 2x2 Matrix
    dot_term : scalar  (a . b)
    cross_term : list  (a x b), length 3
    """
    a = a_coeffs
    b = b_coeffs

    # dot product
    dot = sum(a[i] * b[i] for i in range(3))

    # cross product
    cross = [
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0],
    ]

    # (a.sigma)(b.sigma) = (a.b) I + i(axb).sigma
    cross_mat = Z2.copy()
    for i in range(3):
        cross_mat = cross_mat + cross[i] * sigma[i]
    result = dot * I2 + I * cross_mat

    return simplify(result), dot, cross


# ---------------------------------------------------------------------------
# Levi-Civita symbol (3D)
# ---------------------------------------------------------------------------

def levi_civita(i, j, k):
    """Return epsilon_{ijk} for i,j,k in {0,1,2}."""
    indices = (i, j, k)
    if len(set(indices)) < 3:
        return 0
    even_perms = {(0,1,2), (1,2,0), (2,0,1)}
    return 1 if indices in even_perms else -1


# ---------------------------------------------------------------------------
# SME nonrelativistic Hamiltonians (2x2, upper-component sector)
# ---------------------------------------------------------------------------

def H_NR_bmu(b_spatial, b0=0, p=None):
    """
    NR Hamiltonian from the b_mu SME coefficient (CPT-odd).

        H^NR_{b} = -b_i sigma^i + b0 * (sigma . p) / m   [to O(1/m)]

    Parameters
    ----------
    b_spatial : list of 3 SymPy expressions  [b1, b2, b3]
    b0        : SymPy expression, the temporal component (default 0)
    p         : list of 3 SymPy expressions [p1, p2, p3], needed for b0 term.
                If None, the b0/m term is omitted.

    Returns
    -------
    H : 2x2 SymPy Matrix
    description : str
    """
    H = Z2.copy()
    for i in range(3):
        H = H - b_spatial[i] * sigma[i]

    if b0 != 0 and p is not None:
        m = symbols('m', positive=True)
        H = H + b0 * sum(p[i] * sigma[i] for i in range(3)) / m

    return simplify(H), (
        "H^NR_b = -b.sigma  [CPT-odd; sign flips for antimatter]"
    )


def H_NR_Hmunu(H_B, H_E=None, p=None):
    """
    NR Hamiltonian from the H_{mu nu} SME coefficient (CPT-even).

        H^NR_{H} = -H_B^k sigma^k - (1/m) sigma.(p x H_E)   [to O(1/m)]

    Parameters
    ----------
    H_B : list of 3 SymPy expressions  [H_B1, H_B2, H_B3]
          Magnetic-like components: H_B^k = (1/2) epsilon^{ijk} H_{ij}
    H_E : list of 3 SymPy expressions  [H_{01}, H_{02}, H_{03}]
          Electric-like components (optional; needed for 1/m term).
    p   : list of 3 SymPy expressions [p1, p2, p3] (optional).

    Returns
    -------
    H : 2x2 SymPy Matrix
    description : str
    """
    H = Z2.copy()
    for i in range(3):
        H = H - H_B[i] * sigma[i]

    if H_E is not None and p is not None:
        m = symbols('m', positive=True)
        # p x H_E
        pxH = [
            p[1]*H_E[2] - p[2]*H_E[1],
            p[2]*H_E[0] - p[0]*H_E[2],
            p[0]*H_E[1] - p[1]*H_E[0],
        ]
        pxH_mat = Z2.copy()
        for i in range(3):
            pxH_mat = pxH_mat + pxH[i] * sigma[i]
        H = H - pxH_mat / m

    return simplify(H), (
        "H^NR_H = -H_B.sigma - (1/m) sigma.(p x H_E)  "
        "[CPT-even; same sign for antimatter]"
    )


def H_NR_dmunu(d_i0, d_ij, p, include_mass_term=True):
    """
    NR Hamiltonian from the d_{mu nu} SME coefficient (CPT-even).

        H^NR_{d} = d_{i0} m sigma^i + d_{ij} p^j sigma^i + d_{00} sigma.p

    Parameters
    ----------
    d_i0 : list of 3 SymPy expressions  [d_{10}, d_{20}, d_{30}]
    d_ij : 3x3 list of SymPy expressions  d_ij[i][j] = d_{i+1, j+1}
    p    : list of 3 SymPy expressions [p1, p2, p3]
    include_mass_term : bool  (default True)
        If True, includes the d_{i0} * m * sigma^i term.

    Returns
    -------
    H : 2x2 SymPy Matrix
    description : str
    """
    m = symbols('m', positive=True)

    # d_{i0} m sigma^i term
    H = Z2.copy()
    if include_mass_term:
        for i in range(3):
            H = H + m * d_i0[i] * sigma[i]

    # d_{ij} p^j sigma^i term
    for i in range(3):
        for j in range(3):
            H = H + d_ij[i][j] * p[j] * sigma[i]

    return simplify(H), (
        "H^NR_d = d_{i0} m sigma^i + d_{ij} p^j sigma^i  "
        "[CPT-even; velocity-dependent; same sign for antimatter]"
    )


# ---------------------------------------------------------------------------
# CPT conjugation of NR Hamiltonians
# ---------------------------------------------------------------------------

def cpt_conjugate(H_NR, cpt_sign):
    """
    Apply CPT conjugation to a 2x2 NR Hamiltonian.

    For CPT-odd coefficients (cpt_sign = -1):
        H^NR_antiparticle = -H^NR_particle

    For CPT-even coefficients (cpt_sign = +1):
        H^NR_antiparticle = +H^NR_particle

    Parameters
    ----------
    H_NR : 2x2 SymPy Matrix
    cpt_sign : +1 or -1

    Returns
    -------
    2x2 SymPy Matrix
    """
    return cpt_sign * H_NR


# ---------------------------------------------------------------------------
# Asymmetry parameter
# ---------------------------------------------------------------------------

def asymmetry(g_matter, g_antimatter):
    """
    Compute the asymmetry parameter A_alpha = (g_f - g_fbar) / (g_f + g_fbar).

    Parameters
    ----------
    g_matter, g_antimatter : SymPy expressions or floats

    Returns
    -------
    A : SymPy expression
    """
    return (g_matter - g_antimatter) / (g_matter + g_antimatter)


# ---------------------------------------------------------------------------
# Consistency checks
# ---------------------------------------------------------------------------

def _run_checks():
    print("Running Pauli algebra consistency checks...")

    # Clifford algebra in 2D: {sigma^i, sigma^j} = 2 delta^{ij} I
    for i in range(3):
        for j in range(3):
            ac = simplify(acomm2(sigma[i], sigma[j]))
            expected = 2 * (1 if i == j else 0) * I2
            assert ac == expected, f"{{sigma[{i}], sigma[{j}]}} failed"

    # [sigma^i, sigma^j] = 2i epsilon^{ijk} sigma^k
    for i in range(3):
        for j in range(3):
            c = simplify(comm2(sigma[i], sigma[j]))
            expected = Z2.copy()
            for k in range(3):
                expected = expected + 2 * I * levi_civita(i, j, k) * sigma[k]
            assert simplify(c - expected) == Z2, \
                f"[sigma[{i}], sigma[{j}]] failed"

    # Pauli product identity
    ax, ay, az = symbols('ax ay az')
    bx, by, bz = symbols('bx by bz')
    result, dot, cross = pauli_product([ax,ay,az], [bx,by,bz])
    # Verify trace(result) = 2*(a.b)
    tr = simplify(trace(result) - 2*dot)
    assert tr == 0, "Pauli product trace check failed"

    # CPT: b_mu (CPT-odd) flips sign
    b1, b2, b3 = symbols('b1 b2 b3', real=True)
    H_mat, _ = H_NR_bmu([b1, b2, b3])
    H_anti = cpt_conjugate(H_mat, -1)
    assert simplify(H_mat + H_anti) == Z2, "CPT flip for b_mu failed"

    # CPT: H_munu (CPT-even) does not flip
    hb1, hb2, hb3 = symbols('hb1 hb2 hb3', real=True)
    H_mat2, _ = H_NR_Hmunu([hb1, hb2, hb3])
    H_anti2 = cpt_conjugate(H_mat2, +1)
    assert simplify(H_mat2 - H_anti2) == Z2, "CPT preservation for H_munu failed"

    print("All checks passed.")


if __name__ == "__main__":
    _run_checks()

    print("\n--- Pauli matrices ---")
    for i, name in enumerate(['sigma_x', 'sigma_y', 'sigma_z']):
        print(f"\n{name}:")
        sp.pprint(sigma[i])

    print("\n--- Example: H^NR for b_mu ---")
    b1, b2, b3 = symbols('b_1 b_2 b_3', real=True)
    H, desc = H_NR_bmu([b1, b2, b3])
    print(desc)
    sp.pprint(H)

    print("\n--- Eigenvalues (spin splitting in b-field) ---")
    eigs = H.eigenvals()
    for val, mult in eigs.items():
        print(f"  E = {val}  (multiplicity {mult})")

    print("\n--- Example: H^NR for H_munu ---")
    hb1, hb2, hb3 = symbols('H_B1 H_B2 H_B3', real=True)
    H2, desc2 = H_NR_Hmunu([hb1, hb2, hb3])
    print(desc2)
    sp.pprint(H2)

    print("\n--- Asymmetry parameter: naive signed substitution (b_mu, CPT-odd) ---")
    # For an EXACT CPT-odd sign flip, a hypothetical *signed* coupling would
    # satisfy g_fbar = -g_f, so the denominator g_f + g_fbar vanishes
    # identically. This is a genuine divergence, not a bounded value --
    # verified here with sympy's own limit(), rather than asserted by hand.
    gm_sym = symbols('g_f', positive=True)
    eps_sym = symbols('epsilon', positive=True)
    A_signed = asymmetry(gm_sym, -gm_sym + eps_sym)
    print(f"  A(g_fbar -> -g_f + eps) = {sp.simplify(A_signed)}")
    limit_val = sp.limit(A_signed, eps_sym, 0, dir='+')
    print(f"  sympy limit as eps -> 0+: {limit_val}")
    assert limit_val is sp.oo, "Expected divergence, not saturation at 1"
    print("  => DIVERGES. A CPT-odd sign flip does NOT predict |A_alpha| -> 1")
    print("     when substituted directly as a signed coupling in this formula.")

    print("\n--- What SPINDEP actually computes: ratio of two independent bounds ---")
    # SPINDEP's `coupling_abs` columns (see spindep/README.md) are always-
    # positive experimental UPPER BOUNDS from independent experiments, not
    # signed measured values. Their ratio saturates near +/-1 whenever one
    # bound is far tighter than the other, with NO dependence on whether the
    # underlying physics is CPT-odd or CPT-even -- a generic property of
    # comparing two positive numbers of very different size, i.e. a
    # sensitivity-gap effect, not evidence of a sign flip.
    g_loose = symbols('g_loose', positive=True)
    ratio = symbols('r', positive=True)  # r = g_tight / g_loose
    A_bounds = sp.simplify(asymmetry(g_loose, ratio * g_loose))
    print(f"  A(g_tight = r * g_loose) = {A_bounds}")
    print(f"  limit as r -> 0+ (bounds differ by orders of magnitude): "
          f"{sp.limit(A_bounds, ratio, 0, dir='+')}")
    print("  => |A_alpha| -> 1 purely from a large sensitivity gap between two")
    print("     positive bounds. This is indistinguishable from a real CPT-odd")
    print("     signal using bound magnitudes alone -- observing |A_alpha| ~ 1")
    print("     in SPINDEP output is therefore NOT, by itself, evidence of the")
    print("     b_mu sign-flip mechanism (see potential_match_table.md).")