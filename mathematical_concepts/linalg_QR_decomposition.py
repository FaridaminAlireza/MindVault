"""
QR FACTORIZATION (ORTHOGONALIZATION)

PREREQUISITES
1. Basic linear algebra:
    * Vectors, inner product, norm, linear independence,
    span, subspaces, orthonormal bases.
2. Matrix algebra:
   * Matrix multiplication, transpose, invertibility, rank.
3. Concepts:
   * Orthogonal (or unitary) matrices Q where QᵀQ = I.
   * Triangular matrices.
   * Projection onto subspaces.
4. Optional but useful:
   * Numerical conditioning, rounding errors,
    and algorithmic stability.

---
WHAT IS QR FACTORIZATION

QR (or orthogonal) factorization expresses 
a matrix A (m×n, with m ≥ n) as:

A = Q R

where:
* Q is an m×n matrix with orthonormal columns (QᵀQ = I),
* R is an n×n upper triangular matrix.

Intuitively, QR expresses the columns of A as linear combinations
of an orthonormal basis (the columns of Q).

---
METHODS FOR QR FACTORIZATION

1. Classical Gram–Schmidt (CGS)

   * Sequential orthonormalization of columns.
   * Simple but numerically unstable.

2. Modified Gram–Schmidt (MGS)

   * Reordered form of CGS.
   * More numerically stable.

3. Householder Reflections

   * Uses orthogonal reflectors to zero subdiagonal entries.
   * Numerically stable and efficient for dense matrices.

4. Givens Rotations

   * Uses plane rotations to zero specific elements.
   * Useful for sparse matrices or incremental updates.

5. Pivoted QR

   * Adds column swaps to improve stability and reveal rank.

---
(GRAM–SCHMIDT CONSTRUCTION)

Let A = [a₁ a₂ ... a_n] have linearly independent columns.

We construct orthonormal vectors q₁,...,q_n and R (upper triangular).

Input: A (m x n) with columns a1,...,an
Output: Q (m x n) with orthonormal columns, R (n x n) upper triangular

for j = 1 to n:
    v = a_j                      # copy of j-th column
    for i = 1 to j-1:
        r[i,j] = q_i^T * a_j     # projection coefficient
        v = v - r[i,j] * q_i
    end
    r[j,j] = norm(v)             # positive scalar (assume v != 0)
    q_j = v / r[j,j]
end

Return Q = [q_1 ... q_n], R = [r[i,j]]


Then:
A = Q R
where Q = [q₁ ... q_n] and R contains the r_{i,j}.

Since q_i are orthonormal, QᵀQ = I and R is upper triangular.

Uniqueness:
If R has positive diagonal entries, the factorization is unique.

---
HOUSEHOLDER APPROACH (ALTERNATIVE PROOF)

Each step constructs a Householder matrix H_k = I − 2 v vᵀ / (vᵀv)
to zero all entries below the diagonal in column k.

After p steps:
H_p ... H_1 A = R
Let Q = H_1 ... H_p (orthogonal product).
Then:
A = Q R


KEY PROPERTIES

1. Q is orthogonal ⇒ QᵀQ = I.
2. R is upper triangular.
3. Columns of A are linear combinations of orthonormal columns of Q.
4. Orthogonal transformations preserve norms:
   ||Qx|| = ||x|| for all x.

---

 LEAST SQUARES APPLICATION

Problem:
minimize ||Ax − b||₂

If A = Q R (thin form):
||Ax − b|| = ||Q R x − b|| = ||R x − Qᵀ b||.

Solution:
Solve R x = Qᵀ b  (R is upper triangular).

This avoids forming AᵀA (which is numerically unstable).

---

NUMERICAL STABILITY

* CGS: Unstable for nearly dependent columns.
* MGS: Better stability.
* Householder: Most stable (preferred in practice).
* QR avoids squaring the condition number (unlike AᵀA).

---

 WORKED EXAMPLE (3×2 MATRIX)

Let:
A = [ 1  1
1  0
0  1 ]

Columns:
a₁ = [1,1,0]ᵀ
a₂ = [1,0,1]ᵀ

Step 1:
v₁ = a₁
r₁₁ = ||v₁|| = √2
q₁ = [1/√2, 1/√2, 0]ᵀ

Step 2:
r₁₂ = q₁ᵀ a₂ = 1/√2
v₂ = a₂ − r₁₂ q₁
= [1,0,1] − (1/√2)[1/√2,1/√2,0]
= [0.5, -0.5, 1]
r₂₂ = ||v₂|| = √(3/2)
q₂ = v₂ / r₂₂
≈ [0.408, -0.408, 0.816]

Final:
Q ≈ [[0.707, 0.408],
[0.707, -0.408],
[0,      0.816]]

```
R ≈ [[1.414, 0.707],
      [0,     1.225]]
```

Check:  Q R ≈ A

---

 HOUSEHOLDER METHOD (OUTLINE)

Each Householder reflection H = I − 2vvᵀ / (vᵀv) zeroes entries below diagonal.
Repeat for each column → A transformed to R.
Product of all H gives orthogonal Q such that A = Q R.

---

 APPLICATIONS OF QR FACTORIZATION

1. Linear least squares problems

   * Stable solution using R x = Qᵀ b.

2. Solving linear systems (square A)

   * Use Rx = Qᵀb instead of LU when orthogonality matters.

3. Eigenvalue computations

   * QR algorithm for eigenvalues uses repeated QR factorizations.

4. Basis construction

   * Build orthonormal bases for subspaces (e.g., Krylov, Arnoldi).

5. Rank detection

   * QR with column pivoting reveals numerical rank.

6. PCA and data analysis

   * Used to orthogonalize data before SVD or for low-rank approximations.

7. Control and signal processing

   * Recursive least squares, adaptive filtering.

8. Computer graphics and robotics

   * Re-orthogonalization of coordinate frames.

---

 NUMERICAL COMPLEXITY

For dense m×n (m ≥ n):
~ 2/3 * m n² operations.
Economy form (thin Q, n×n R) saves time and memory.

---

 PRACTICAL NOTES

* Use Householder QR for general dense problems.
* Use Givens for sparse or incremental systems.
* For rank-deficient matrices, use QR with column pivoting.
* In code: most libraries (NumPy, LAPACK, MATLAB) implement optimized QR routines.

---

 INTUITIVE INSIGHT

QR is the process of transforming your coordinate system into an orthonormal one.

Gram–Schmidt: subtract off projections to make each vector orthogonal to the previous ones.

Householder: reflect the space to eliminate unwanted components in one shot.

QR is fundamental in numerical linear algebra because orthogonal transformations
preserve length and are numerically stable.


"""



"""
The Gram–Schmidt process is fundamentally a method to produce 
an orthonormal basis of the column space of a matrix. 

1. Orthonormal basis → Q
  Each column of (Q) is a unit vector (q_j) that is orthogonal to all the previous (q_i) ((i<j)).
  So (Q) stores the orthonormal basis of the column space of (A).

2. Projections → R
  Each entry (r_{ij} = q_i^T a_j) is essentially the projection of (a_j) onto 
  the already computed orthonormal vectors.
  So (R) stores the “recipe” for reconstructing the original columns from the orthonormal basis.
  It is upper-triangular because when computing (q_j), we only need projections onto (q_1 . q_j).

3. Geometric intuition
   * Step by step, you take a vector (a_j),
    remove all components along the previously built orthonormal vectors 
    (those subtractions are encoded in (R)), 
    and normalize the residual to get the new orthonormal vector (q_j).
   * Hence, Q contains the basis, R contains the coordinates of the original vectors in that basis.

So in short:
* Q = orthonormal basis
* R = projections / coefficients that reconstruct the original matrix: (A = Q R).


QR decomposition

* In QR decomposition, we treat each **column of A** as a vector.
* Gram–Schmidt (or any QR method) constructs an orthonormal basis of the **column space** of A.
* Q contains columns that are orthonormal vectors, and R stores coefficients (projections)
 needed to reconstruct the original columns.
* Geometrically, we are projecting **columns** onto orthonormal directions.

LU decomposition:

* LU decomposition is conceptually **row-oriented**.
* It uses Gaussian elimination to transform A into an upper-triangular matrix U.
* Each **row of A** is expressed in terms of previous rows using multipliers stored in L.
* Geometrically, we are eliminating entries **row by row**.

**Intuition:**
* QR → “orthonormalize the columns” → think column vectors
* LU → “eliminate entries row by row” → think row operations

"""