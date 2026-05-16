"""
dirac_algebra.py
================
Symbolic Dirac algebra for the Foldy-Wouthuysen derivations.

Provides the standard 4x4 Dirac matrices in the Dirac/Pauli representation,
the metric convention (+,-,-,-), and all utilities needed for FW reduction
of the SME-modified Dirac Hamiltonian.

Conventions
-----------
- Dirac/Pauli representation throughout (block structure manifest).
- Metric: g^{mu nu} = diag(+1, -1, -1, -1).
- Natural units: hbar = c = 1.
- gamma^5 = i * gamma^0 * gamma^1 * gamma^2 * gamma^3.
- sigma^{mu nu} = (i/2) [gamma^mu, gamma^nu].

References
----------
Bjorken & Drell, Relativistic Quantum Mechanics (1964), Chapter 4.
Kostelecky & Lane, Phys. Rev. D 60, 116010 (1999).
"""

import sympy as sp
from sympy import I, Matrix, zeros, eye, symbols, sqrt, Rational, simplify, expand

# ---------------------------------------------------------------------------
# 2x2 building blocks
# ---------------------------------------------------------------------------

def _zero2():
    return zeros(2, 2)

def _eye2():
    return eye(2)

# Pauli matrices (symbolic)
sigma_x = Matrix([[0, 1],
                  [1, 0]])

sigma_y = Matrix([[0, -I],
                  [I,  0]])

sigma_z = Matrix([[1,  0],
                  [0, -1]])

sigma = [sigma_x, sigma_y, sigma_z]   # sigma[i] = sigma_{i+1}

# Identity
I2 = eye(2)
I4 = eye(4)
Z4 = zeros(4, 4)

# ---------------------------------------------------------------------------
# Dirac matrices — Dirac/Pauli representation
# ---------------------------------------------------------------------------

def _block(A, B, C, D):
    """Assemble a 4x4 matrix from four 2x2 blocks."""
    top = A.row_join(B)
    bot = C.row_join(D)
    return top.col_join(bot)


# beta = gamma^0
beta = _block(I2, _zero2(), _zero2(), -I2)

# gamma^i  (i = 1,2,3)
gamma = [None]  # placeholder so gamma[mu] works for mu=0..3
gamma[0] = beta  # gamma^0 = beta

for s in sigma:
    gamma.append(_block(_zero2(), s, -s, _zero2()))

# gamma^5 = i gamma^0 gamma^1 gamma^2 gamma^3
gamma5 = _block(_zero2(), I2, I2, _zero2())

# Verify: (gamma5)^2 = I4
assert simplify(gamma5 * gamma5 - I4) == Z4, "gamma5^2 != 1"

# alpha^i = gamma^0 gamma^i  (i=1,2,3; stored at alpha[0..2])
alpha = []
for i in range(1, 4):
    alpha.append(beta * gamma[i])  # = _block(0, sigma_i, sigma_i, 0)

# Sigma^i = block-diag(sigma_i, sigma_i)  — spin matrices in 4-component space
Sigma = []
for s in sigma:
    Sigma.append(_block(s, _zero2(), _zero2(), s))

# sigma^{mu nu} = (i/2)[gamma^mu, gamma^nu]
def sigma_munu(mu, nu):
    """Compute sigma^{mu nu} = (i/2)[gamma^mu, gamma^nu]."""
    gmu = gamma[mu]
    gnu = gamma[nu]
    return Rational(1, 2) * I * (gmu * gnu - gnu * gmu)


# ---------------------------------------------------------------------------
# Classification utilities
# ---------------------------------------------------------------------------

def is_even(M, tol=True):
    """
    Return True if M is even: beta * M = M * beta.
    Uses symbolic equality after simplification.
    """
    return simplify(beta * M - M * beta) == Z4


def is_odd(M):
    """
    Return True if M is odd: beta * M = -M * beta.
    """
    return simplify(beta * M + M * beta) == Z4


def even_part(M):
    """Extract the even part of M: E = (M + beta M beta) / 2."""
    return Rational(1, 2) * (M + beta * M * beta)


def odd_part(M):
    """Extract the odd part of M: O = (M - beta M beta) / 2."""
    return Rational(1, 2) * (M - beta * M * beta)


# ---------------------------------------------------------------------------
# Commutator and anticommutator
# ---------------------------------------------------------------------------

def comm(A, B):
    """[A, B] = AB - BA."""
    return A * B - B * A


def acomm(A, B):
    """{A, B} = AB + BA."""
    return A * B + B * A


# ---------------------------------------------------------------------------
# FW commutator expansion (BCH) — symbolic, to a given order
# ---------------------------------------------------------------------------

def bcf_expansion(S, H, order=4):
    """
    Compute e^{iS} H e^{-iS} via BCH to the given order of nested commutators.

    Returns
    -------
    terms : list of Matrix
        terms[n] = (i^n / n!) [S,[S,...[S,H]...]]   (n commutators)
        terms[0] = H
    total : Matrix
        Sum of all terms.
    """
    terms = [H]
    current = H
    factorial = 1
    for n in range(1, order + 1):
        factorial *= n
        current = comm(S, current)
        # multiply by i^n / n!
        prefactor = (I ** n) * sp.Rational(1, factorial)
        terms.append(prefactor * current)

    total = sum(terms)
    return terms, simplify(total)


# ---------------------------------------------------------------------------
# Upper-component projection (nonrelativistic limit)
# ---------------------------------------------------------------------------

def upper(M):
    """
    Project onto upper 2x2 block (particle sector, beta -> +1).
    Returns 2x2 matrix.
    """
    return M[:2, :2]


def lower(M):
    """
    Project onto lower 2x2 block (antiparticle sector, beta -> -1).
    Returns 2x2 matrix.
    """
    return M[2:, 2:]


# ---------------------------------------------------------------------------
# Consistency checks
# ---------------------------------------------------------------------------

def _run_checks():
    print("Running Dirac algebra consistency checks...")

    # {gamma^mu, gamma^nu} = 2 g^{mu nu} I4
    g = [1, -1, -1, -1]  # metric
    for mu in range(4):
        for nu in range(4):
            expected = 2 * g[mu] * (1 if mu == nu else 0) * I4
            result = simplify(acomm(gamma[mu], gamma[nu]) - expected)
            assert result == Z4, f"Clifford algebra failed at mu={mu}, nu={nu}"

    # alpha^i anti-commutes with beta
    for i, ai in enumerate(alpha):
        assert is_odd(ai), f"alpha[{i}] is not odd"

    # Sigma^i commutes with beta (even)
    for i, Si in enumerate(Sigma):
        assert is_even(Si), f"Sigma[{i}] is not even"

    # gamma5 anti-commutes with all gamma^mu
    for mu in range(4):
        result = simplify(acomm(gamma[mu], gamma5))
        assert result == Z4, f"{{gamma^{mu}, gamma5}} != 0"

    # sigma^{0i} = i alpha^i
    for i in range(1, 4):
        s0i = sigma_munu(0, i)
        expected = I * alpha[i - 1]
        assert simplify(s0i - expected) == Z4, f"sigma^{{0{i}}} != i alpha^{i}"

    # sigma^{ij} = epsilon^{ijk} Sigma^k
    import itertools
    eps = {(0,1,2):1, (1,2,0):1, (2,0,1):1,
           (2,1,0):-1, (0,2,1):-1, (1,0,2):-1}
    for i, j in itertools.combinations(range(3), 2):
        sij = sigma_munu(i + 1, j + 1)
        k = 3 - i - j  # the remaining index in {0,1,2}
        e = eps.get((i, j, k), 0)
        expected = e * Sigma[k]
        assert simplify(sij - expected) == Z4, f"sigma^{{{i+1}{j+1}}} mismatch"

    print("All checks passed.")


if __name__ == "__main__":
    _run_checks()

    print("\n--- Dirac matrices (Dirac/Pauli representation) ---")
    print("beta (gamma^0):")
    sp.pprint(beta)
    for i in range(3):
        print(f"\nalpha[{i}] (= gamma^0 gamma^{i+1}):")
        sp.pprint(alpha[i])
    print("\ngamma5:")
    sp.pprint(gamma5)
    for i in range(3):
        print(f"\nSigma[{i}]:")
        sp.pprint(Sigma[i])