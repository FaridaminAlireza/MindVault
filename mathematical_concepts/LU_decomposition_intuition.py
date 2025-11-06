"""
LU Decomposition — Intuition and Reasoning
Goal: Understand L * U = A and why the multipliers in Gaussian elimination go into L


1. Gaussian elimination = a sequence of linear transformations
When you perform Gaussian elimination on A, you’re doing row operations
to eliminate entries below the diagonal. Each of those row operations can
be represented by multiplying A by a special matrix.

Example of a single elimination step:
Suppose you eliminate a21 (a(row=2)(column=1)) using the first row. 

Compute m21 = a21/a11 and do:
    R2 ← R2 - m21 * R1

That’s equivalent to multiplying A on the left by an elimination matrix E1:
    E1 = [[ 1,    0,   0  ],
          [-m21,  1,   0  ],
          [0,     0,   1  ]
          ]

Then:
    E1 * A = A(1)   (after eliminating the first column below the pivot)

----------
2. Elimination matrices are invertible — and their inverses are easy
The inverse of E1 reverses the elimination:
    E1⁻¹ = [[1,    0,  0  ],
            [m21,  1,  0  ],
            [0,    0,  1  ]]

This inverse matrix has exactly the structure of L.

----------
3. Chaining all elimination steps
For a 3×3 matrix, you perform two elimination steps:

    E2 * E1 * A = U

Rearrange to get:
    A = E1⁻¹ * E2⁻¹ * U

Let:
    L = E1⁻¹ * E2⁻¹

Then:
    A = L * U

So, L is the product of the inverses of the elimination matrices 
— which encode the multipliers used in elimination.

----------
4. Why L has the multipliers
Each inverse elimination matrix E_k⁻¹ looks like:
E_k⁻¹ = I + m_ik * e_ik

where e_ik has 1 at (row i, column k) (and 0 elsewhere).
When you multiply all such inverses, their product accumulates
the multipliers m_ik below the diagonal — exactly the entries stored in L.

Thus, L records how much of one row was subtracted from another
 during elimination.

----------
5. Checking what happens when we multiply L × U
Example:

L = [[1,  0,  0   ],
     [2,  1,  0   ],
     [-1, 7,  1   ]]

U = [[2,  3,  1   ],
     [0,  1,  5   ],
     [0,  0,  -29 ]]

Compute L * U:

Step 1: First row of A

Row1(L) = [1, 0, 0] → Picks Row1(U) → [2, 3, 1]
→ Matches A’s first row.

Step 2: Second row of A

Row2(L) = [2, 1, 0]
Row2(A) = 2×Row1(U) + 1×Row2(U) = [4,7,7]
→ Matches A’s second row.

Step 3: Third row of A

Row3(L) = [-1, 7, 1]
Row3(A) = -1×Row1(U) + 7×Row2(U) + 1×Row3(U)
         = [-2,4,5]
→ Matches A’s third row.

Therefore, L * U reconstructs A exactly.

----------
6. Intuitive Summary
Gaussian elimination: Turns A into upper-triangular U by subtracting multiples of rows
Multipliers: How much of a row was subtracted — stored in L
L is Product of inverse elimination matrices (records elimination history)
U is the result after elimination
A = L × U , Applying all elimination inverses (L) to U reconstructs A

7. Another way to see it
When you multiply L × U, you’re reapplying the same combinations of rows
that you did during elimination — but in reverse — to rebuild A exactly.
Each row of A is formed as a linear combination of rows of U,
with the coefficients (multipliers) stored in L.
That’s why L * U = A.
"""