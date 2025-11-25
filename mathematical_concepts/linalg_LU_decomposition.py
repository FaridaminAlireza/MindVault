"""LU Decomposition 


We want to decompose a given square matrix A into two matrices L and U, such that:
    A = L * U
where
- L = lower-triangular (1’s on diagonal,
 values below diagonal = elimination multipliers)
- U = upper-triangular (values above and on diagonal
 after elimination)


Example: 3×3 System

Let’s use a simple matrix:
    A = [[2,  3,  1  ],
         [4,  7,  7  ],
         [-2, 4,  5  ]]

We’ll find L and U manually, by mimicking Gaussian elimination.

----
Step 1 — Initialization

L = I (identity matrix)
U = A


Step 2 — Eliminate below first pivot (row 1)

Pivot: U[1,1] = 2
Eliminate below it (row 2 and row 3).

m21 = 4/2 = 2
m31 = -2/2 = -1

Row 2 = Row 2 - 2*Row 1  => [4,7,7] - 2*[2,3,1] = [0,1,5]
Row 3 = Row 3 + Row 1     => [-2,4,5] + [2,3,1] = [0,7,6]

U becomes:
[[2, 3, 1],
 [0, 1, 5],
 [0, 7, 6]]

L stores multipliers:
[[1,  0,  0],
 [2,  1,  0],
 [-1, 0,  1]]

----
Step 3 — Eliminate below pivot (row 2)

Pivot: U[2,2] = 1
Eliminate below it (row 3).

m32 = 7/1 = 7
Row 3 = Row 3 - 7*Row 2 => [0,7,6] - 7*[0,1,5] = [0,0,-29]

U becomes:
[[2, 3, 1  ],
 [0, 1, 5  ],
 [0, 0, -29]]

L becomes:
[[1,  0, 0],
 [2,  1, 0],
 [-1, 7, 1]]

----
Step 4 — Final L and U

L = [[1,  0, 0],
     [2,  1, 0],
     [-1, 7, 1]]

U = [[2, 3, 1],
     [0, 1, 5],
     [0, 0, -29]]

Check: L * U = A 
----
Step 5 — Interpretation

Pivot division (m = a_ij / a_jj), Stored in L
Result of elimination is Upper-triangular matrix stored in U
Identity diagonal in L: Because we don't eliminate the pivot row

----
Step 6 — Algorithm (no pivoting)

Given A (n×n):

Initialize L = I, U = A
for k = 0..n-2:
    for i = k+1..n-1:
        m = U[i,k] / U[k,k]
        L[i,k] = m
        U[i,:] = U[i,:] - m * U[k,:]

----
Step 7 — Python Implementation
"""
import numpy as np

def lu_factorization(A):
    A = A.astype(float)
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()

    for k in range(n - 1):
        for i in range(k + 1, n):
            m = U[i, k] / U[k, k]
            L[i, k] = m
            U[i, :] = U[i, :] - m * U[k, :]
    return L, U

A = np.array([[2, 3, 1],
              [4, 7, 7],
              [-2, 4, 5]], dtype=float)

L, U = lu_factorization(A)
print("L =\n", L)
print("U =\n", U)
print("Check L@U = A:", np.allclose(L @ U, A))

"""
Step 8 — With Pivoting (for Stability)

When the pivot element (U[k,k]) is small or zero,
we swap rows to keep the system stable. That’s called 
LU decomposition with partial pivoting: P A = L U

Example (SciPy):

from scipy.linalg import lu
P, L, U = lu(A)
print("P:\n", P)
print("L:\n", L)
print("U:\n", U)
print("Check PA=LU:", np.allclose(P @ A, L @ U))

----
Intuitive Analogy

Think of LU decomposition like recording your Gaussian elimination process:
- Each time you eliminate a number → you store 
how much of one row was subtracted from another in L.
- The matrix you get at the end of elimination is U.
- Together, they reconstruct the exact operations that
 turned A into U.

"""


