# Solving Systems of Linear Equations — Pivoting Approaches and Algorithms
# =======================================================================

# 1. Introduction
# ---------------
# When solving a system of linear equations Ax = b, numerical stability is crucial.
# Gaussian elimination is the standard algorithm, but to avoid dividing by small
# or zero numbers (pivots), different forms of *pivoting* are used. Pivoting improves
# both accuracy and stability by reordering rows and/or columns so that the pivot 
# element is well-chosen.

# 2. Gaussian Elimination (basic idea)
# ------------------------------------
# Gaussian elimination converts a system of equations into an
# equivalent upper-triangular system, then performs back-substitution.

# Algorithm steps:
# 1. For each column k = 1..n-1:
#    - Choose a pivot element (the diagonal A[k,k] after previous eliminations).
#    - Eliminate entries below the pivot using row operations.
# 2. Solve the upper-triangular system by back-substitution.

# The key question: *How do we choose the pivot element?*
# This is where pivoting strategies come in.

# 3. Types of Pivoting
# --------------------

# A. No Pivoting
#    - Rows and columns remain fixed.
#    - Simple but can be numerically unstable if the pivot element is very small.
#    - Only acceptable for well-conditioned or special matrices 
#    (e.g., diagonally dominant or symmetric positive definite).

# B. Partial Pivoting (Row Pivoting)
#    - Swap rows so that the pivot element (A[k,k]) is the largest by magnitude in its column (from row k to n).
#    - Eliminates divisions by very small numbers and reduces rounding errors.
#    - Very stable for most practical problems.
#    - Used in all standard numerical libraries.

# C. Full Pivoting (Row + Column Pivoting)
#    - Swap both rows and columns so that the pivot element is the largest by magnitude in the remaining submatrix.
#    - Maximizes numerical stability but requires additional bookkeeping (because variable order changes).
#    - Rarely needed in practice; mostly used in symbolic or exact arithmetic systems.

# Comparison Table
# ----------------
# | Type             | Swaps        | Reorders Variables | Stability | Cost | Common Use |
# |------------------|--------------|--------------------|------------|------|-------------|
# | No Pivoting      | None         | No                 | Poor       | Lowest | Special cases |
# | Partial Pivoting | Rows only    | No                 | Very good  | Low  | Default everywhere |
# | Full Pivoting    | Rows + cols  | Yes                | Excellent  | Higher | Rare, symbolic math |

# 4. Gaussian Elimination with Partial Pivoting (Algorithm)

# for k = 1 to n-1:
#     # Find pivot (row with max |A[i,k]| for i >= k)
#     p = argmax(|A[i,k]|)
#     if p != k:
#         swap rows A[k] <-> A[p]
#         swap b[k] <-> b[p]

#     # Eliminate below pivot
#     for i = k+1 to n:
#         m = A[i,k] / A[k,k]
#         for j = k to n:
#             A[i,j] = A[i,j] - m*A[k,j]
#         b[i] = b[i] - m*b[k]

# # Back substitution
# x[n] = b[n] / A[n,n]
# for i = n-1 downto 1:
#     s = b[i] - sum(A[i,j]*x[j] for j=i+1..n)
#     x[i] = s / A[i,i]

# This version uses partial pivoting and is stable for most systems.

# 5. Example (Partial Pivoting)
# ------------------------------
# Solve:
#     2x + 3y - z = 5
#     4x + y + 2z = 6
#    -2x + 5y + 3z = -4

# Step 1: Choose pivot in column 1: values are [2, 4, -2];
# largest is 4 → swap row 1 and row 2. 
# Continue elimination → get upper-triangular → back-substitute 
# to get solution:
#     x = 7/4, y = 2/7, z = -9/14

# If no pivoting were done and the first pivot were very small
# rounding errors could destroy accuracy. Partial pivoting 
# fixes this automatically.

# 6. Full Pivoting (Conceptual Example)
# -------------------------------------
# At step k, find largest element in entire submatrix A[k:n, k:n].
# Swap both row and column so that it becomes A[k,k].
# Track column swaps to recover correct variable order at the end.

# Example matrix:
#     [[0.001, 1000],
#      [1, 2]]
# Partial pivoting → pivot = 1 (swap rows).
# Full pivoting → pivot = 1000 (swap rows + columns).

# 7. What Do Software Libraries Use?
# ----------------------------------
# All professional numerical linear algebra libraries implement
# *partial pivoting by default* because it offers excellent balance
# between stability and efficiency.

# - NumPy:        numpy.linalg.solve(A, b) → Uses LAPACK routines
#                 (LU factorization with partial pivoting).
# - SciPy:        scipy.linalg.lu(A) → Returns L, U, and permutation matrix P (for row swaps).
# - MATLAB:       A\\b → Uses Gaussian elimination with partial pivoting (LU decomposition).
# - LAPACK:       dgetrf, sgetrf → LU factorization with partial pivoting.
# - Julia:        \\ operator and lu() → LU factorization with partial pivoting.

# Full pivoting is supported optionally in some libraries (e.g., SymPy, 
# MATLAB's `lu(...,'vector')` options) but rarely used in numeric contexts.

# 8. Summary
# -----------
# - Pivoting = swapping rows/columns to choose a good pivot.
# - Partial pivoting (row swaps) is the standard technique used in nearly all software.
# - Full pivoting (row+col swaps) gives slightly better stability but higher cost.
# - Without pivoting, algorithms are fast but potentially unstable.
# - Gaussian elimination with partial pivoting (GEPP) is the standard 
#  practical algorithm for solving systems of linear equations.

# 9. Python Implementation — Gaussian Elimination with Partial Pivoting
# ---------------------------------------------------------------------
# Below is a simple educational implementation of Gaussian elimination
# with partial pivoting in pure Python. For real applications, you should always 
# use NumPy’s built-in `numpy.linalg.solve` which uses optimized LAPACK routines.

import numpy as np

def gaussian_elimination_partial_pivot(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    # Forward elimination with partial pivoting
    for k in range(n-1):
        # Find pivot row
        pivot = np.argmax(np.abs(A[k:, k])) + k
        if pivot != k:
            A[[k, pivot]] = A[[pivot, k]]
            b[[k, pivot]] = b[[pivot, k]]

        # Eliminate entries below pivot
        for i in range(k+1, n):
            if A[k, k] == 0:
                raise ValueError("Zero pivot encountered!")
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]

    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        s = np.dot(A[i, i+1:], x[i+1:])
        x[i] = (b[i] - s) / A[i, i]
    return x

# Example usage
A = np.array([[2, 3, -1],
              [4, 1, 2],
              [-2, 5, 3]], dtype=float)
b = np.array([5, 6, -4], dtype=float)

x = gaussian_elimination_partial_pivot(A, b)
print("Solution:", x)
