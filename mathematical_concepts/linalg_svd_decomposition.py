"""
Singular Value Decomposition (SVD) — Explanation and Examples

1) What is SVD?
SVD factors any real (or complex) m x n matrix A into three matrices:
    A = U Σ V^T
where:
  - U is an m x r matrix with orthonormal columns (left singular vectors).
  - Σ (Sigma) is an r x r diagonal matrix with non-negative singular values σ1 >= σ2 >= ... >= σr.
  - V is an n x r matrix with orthonormal columns (right singular vectors); V^T is r x n.
  - r = rank(A). If you compute full SVD, U is m x m, Σ is m x n, V^T is n x n.

Intuition:
  - V^T maps input coordinates into an orthonormal basis (right singular vectors).
  - Σ scales those coordinates by non-negative singular values.
  - U maps the scaled coordinates into the output space (left singular vectors).
So A acts like: rotate (V^T) -> scale (Σ) -> rotate (U).

2) Relationship to QR and spectral decomposition
  - QR factorization expresses A = Q R with Q orthonormal and R upper-triangular; it is primarily useful for solving linear systems and computing eigenvalues.
  - Spectral (eigendecomposition) is for square symmetric matrices: A = Q Λ Q^T where Λ is diagonal of eigenvalues.
  - For any A, A^T A is symmetric positive semi-definite; the eigen-decomposition of A^T A gives V and the squared singular values:
        A^T A = V Λ V^T   where Λ = Σ^2 (diagonal of σ_i^2).
    Thus computing eigenvectors/values of A^T A is a standard way to obtain V and σ_i.
  - SVD generalises spectral decomposition to non-square matrices and yields optimal low-rank approximations (Eckart–Young theorem).

3) How to compute SVD step-by-step (conceptually)
  1. Form B = A^T A (an n x n symmetric matrix).
  2. Find eigenvalues λ_i and orthonormal eigenvectors v_i of B. Arrange λ_i in descending order.
  3. Singular values σ_i = sqrt(λ_i) (non-negative).
  4. Set columns of V to the eigenvectors v_i.
  5. For each σ_i > 0, compute u_i = (1/σ_i) A v_i. These form columns of U.
  6. If you need full U (m x m), fill remaining u vectors to an orthonormal basis of R^m.

4) Applications (short list with brief notes)
  - Principal Component Analysis (PCA): compute PCA by SVD of mean-centered data matrix.
  - Low-rank approximation / compression: keep top k singular values/vectors to approximate A (best rank-k approximation).
  - Pseudoinverse (Moore–Penrose): A^+ = V Σ^+ U^T, where Σ^+ inverts non-zero singular values.
  - Solving linear least squares (including rank-deficient): use SVD to get stable solutions.
  - Image compression: approximate image matrix by low-rank SVD.
  - Latent Semantic Indexing (text): low-rank SVD of term-document matrix finds latent concepts.
  - Recommender systems: matrix factorization uses truncated SVD-like decompositions.
  - Condition number and numerical stability: cond(A) = σ_max / σ_min.

5) Numerical example (step-by-step with concrete numbers)
Matrix A (3 x 2):
[[1. 2.]
 [3. 4.]
 [5. 6.]]

Compute SVD numerically (using numpy.linalg.svd):

Singular values (σ_i):
  σ_1 = 9.52551809
  σ_2 = 0.51430058

Sigma (Σ) (diagonal):
[[9.52551809 0.        ]
 [0.         0.51430058]]

V^T (right singular vectors, rows are v_i^T):
[[-0.61962948 -0.78489445]
 [-0.78489445  0.61962948]]

V (columns are right singular vectors):
[[-0.61962948 -0.78489445]
 [-0.78489445  0.61962948]]

U (left singular vectors, columns are u_i):
[[-0.2298477   0.88346102]
 [-0.52474482  0.24078249]
 [-0.81964194 -0.40189603]]

Check reconstruction: U Σ V^T equals A (numerically):
[[1. 2.]
 [3. 4.]
 [5. 6.]]

Numerical check (max absolute error between A and reconstructed A):
  max_abs_error = 8.881784197001e-16

6) Low-rank approximation example (rank-1 truncation)
  - Keep only the largest singular value σ1 and corresponding u1, v1.
  - A_1 = σ1 * u1 * v1^T  (outer product)

A_1 (rank-1 approximation):
[[1.35662819 1.71846235]
 [3.09719707 3.92326845]
 [4.83776596 6.12807454]]

Frobenius norm errors:
  ||A - A||_F = 1.275549143318e-15
  ||A - A_1||_F = 5.143005806586e-01

7) Practical tips and notes
  - Use robust library implementations (LAPACK-backed numpy/scipy) rather than forming A^T A explicitly when numerical stability matters.
  - Small singular values indicate directions where A compresses information (near nullspace).
  - Truncating small singular values is a form of regularization (implicit denoising).
  - For very large sparse matrices, use iterative methods (e.g., randomized SVD, ARPACK) to compute only a few largest singular values/vectors.

8) References and further reading (keywords to search)
  - Eckart–Young theorem, Moore–Penrose pseudoinverse, randomized SVD, latent semantic indexing, PCA via SVD.

"""

"""
Singular Value Decomposition (SVD) — Formula, Proof, and Applications

1) Overview

The Singular Value Decomposition (SVD) is one of the most 
powerful and general matrix factorizations in linear algebra.
It works for any real (or complex) matrix A ∈ ℝᵐˣⁿ, regardless
of whether A is square, rectangular, invertible, or singular.

It expresses A as the product of three matrices:
    A = U Σ Vᵀ

where:
- U ∈ ℝᵐˣᵐ is orthogonal (UᵀU = Iₘ),
- V ∈ ℝⁿˣⁿ is orthogonal (VᵀV = Iₙ),
- Σ ∈ ℝᵐˣⁿ is diagonal (rectangular) with nonnegative diagonal entries:
      Σ = diag(σ₁, σ₂, ..., σ_r),  where σ₁ ≥ σ₂ ≥ ... ≥ σ_r > 0.
  These σᵢ are called *singular values* of A.

If m ≠ n, Σ contains extra rows or columns of zeros to match A’s shape.

---

2) Formula summary

A = U Σ Vᵀ, or equivalently:
  - Columns of U are *left singular vectors*
  (orthonormal basis of ℝᵐ).
  - Columns of V are *right singular vectors* 
  (orthonormal basis of ℝⁿ).
  - Singular values σᵢ describe how much A stretches
  the direction of each right singular vector vᵢ.

Equivalently:
  A vᵢ = σᵢ uᵢ
  Aᵀ uᵢ = σᵢ vᵢ

Hence:
  - uᵢ is an eigenvector of AAᵀ with eigenvalue σᵢ²
  - vᵢ is an eigenvector of AᵀA with eigenvalue σᵢ²

Thus:
  AᵀA = V Σ² Vᵀ
  AAᵀ = U Σ² Uᵀ


3) Proof (derivation of SVD)

Step 1 — Start with AᵀA: 
  AᵀA is always symmetric and positive semidefinite.

    Symmetry
    A matrix B is symmetric if it is equal to its own transpose, i.e.,
    Bᵀ = B. We can prove that AᵀA is symmetric using the property 
    that (XY)ᵀ = YᵀXᵀ and (Xᵀ)ᵀ = X: (AᵀA)ᵀ = Aᵀ (Aᵀ)ᵀ = AᵀA
    Since (AᵀA)ᵀ = AᵀA, the matrix AᵀA is always symmetric.

    Positive Semidefinite

    A symmetric matrix B is positive semidefinite 
    if for any non-zero vector x, the quadratic form xᵀBx ≥ 0.
    We can prove this for AᵀA: xᵀ (AᵀA) x = (xᵀAᵀ) A x = (Ax)ᵀ (Ax)
    The expression (Ax)ᵀ (Ax) represents the dot product 
    (or squared L2 norm) of the vector Ax with itself, 
    which is always greater than or equal to zero for 
    any real vector x. xᵀ AᵀA x = ||Ax||² ≥ 0
    Thus, AᵀA is always positive semidefinite.

    
By the spectral theorem, there exists an orthonormal basis 
{v₁, ..., vₙ} such that:
  AᵀA vᵢ = λᵢ vᵢ,  with λᵢ ≥ 0.

Let the eigenvalues be ordered λ₁ ≥ λ₂ ≥ ... ≥ λₙ ≥ 0.

Step 2 — Define singular values:
  σᵢ = √λᵢ.

Step 3 — Define left singular vectors:
  For each nonzero σᵢ, define
      uᵢ = (1/σᵢ) A vᵢ.

Then:
  - uᵢ are unit vectors, because
      ‖uᵢ‖² = (1/σᵢ²) vᵢᵀAᵀA vᵢ = (1/σᵢ²) λᵢ = 1.
  - uᵢ are orthonormal, because
      uᵢᵀ uⱼ = (1/σᵢσⱼ) vᵢᵀAᵀ. A vⱼ = 0 for i ≠ j.

    Explanation of why u_i are orthonormal 

        u_i = (1/σ_i) A v_i, where v_i are right singular vectors and σ_i > 0.
        We want to show that the u_i are orthonormal, i.e., u_i^T u_j = δ_ij (1 if i=j, 0 otherwise).

        Step 1: Write the inner product of u_i and u_j
        u_i^T u_j = ((1/σ_i) A v_i)^T ((1/σ_j) A v_j)
                    = (1/(σ_i σ_j)) (v_i^T A^T) (A v_j)
                    = (1/(σ_i σ_j)) v_i^T (A^T A) v_j

        Step 2: Use the eigen-decomposition property of A^T A
        - By definition, v_i are eigenvectors of A^T A:
                A^T A v_i = σ_i^2 v_i
        - Similarly, A^T A v_j = σ_j^2 v_j

        Step 3: Substitute into the inner product
        u_i^T u_j = (1/(σ_i σ_j)) v_i^T (σ_j^2 v_j)
                    = (σ_j / σ_i) v_i^T v_j

        Step 4: Use orthonormality of v_i
        - The v_i vectors are orthonormal: v_i^T v_j = δ_ij (1 if i=j, 0 if i≠j)
        - Therefore:
                u_i^T u_j = (σ_j / σ_i) δ_ij

        Step 5: For i = j, u_i^T u_i = (σ_i / σ_i) * 1 = 1
                For i ≠ j, u_i^T u_j = (σ_j / σ_i) * 0 = 0

        Conclusion: The u_i are orthonormal as claimed.


Step 4 — Form the matrices:
  Let V = [v₁ v₂ ... vₙ],  U = [u₁ u₂ ... uₘ], 
  and Σ be diagonal with entries σᵢ.

Then:
  A vᵢ = σᵢ uᵢ  for i = 1..r,
  and equivalently in matrix form:
      A V = U Σ.

Multiplying both sides by Vᵀ gives:
      A = U Σ Vᵀ.

This completes the proof.



4) Geometric interpretation

SVD describes A as a composition of three geometric transformations:

  x ⟶ (Vᵀ) ⟶ (Σ) ⟶ (U)

1. Vᵀ: rotates or changes coordinates to align with the right singular vectors.
2. Σ: scales each coordinate axis by its singular value σᵢ.
3. U: rotates the result into the space spanned by the left singular vectors.

Thus, A acts as a rotation, followed by anisotropic scaling,
followed by another rotation.

---

5) Applications of SVD


a) Dimensionality reduction / PCA
   - The top singular vectors capture 
   the directions of maximum variance in data.
   - In PCA, we use the SVD of the centered data matrix X:
         X = U Σ Vᵀ
    and project onto the top k singular vectors.

b) Low-rank approximation
   - Best rank-k approximation (in Frobenius or 2-norm) of A is:
         A_k = Σ_{i=1}^k σᵢ uᵢ vᵢᵀ.
   - Eckart–Young theorem: 
   A_k minimizes ‖A - B‖_F over all rank-k matrices B.

c) Solving least squares problems
   - For A x ≈ b, the minimum-norm least squares solution is:
         x = Σ_{i=1}^r (uᵢᵀ b / σᵢ) vᵢ.

d) Computing pseudo-inverses
   - The Moore–Penrose pseudoinverse is:
         A⁺ = V Σ⁺ Uᵀ,
     where Σ⁺ has reciprocals of nonzero σᵢ on the diagonal.

e) Data compression
   - In image or signal compression, 
   small singular values can be truncated to
   approximate data with fewer components.

f) Noise reduction
   - In signal processing or statistics,
    small singular values are often dominated by noise;
    truncating them denoises data.

---

6) Summary table
----------------

| Concept                 | Symbolic form           | Meaning / Description |
|--------------------------|-------------------------|------------------------|
| SVD formula              | A = U Σ Vᵀ             | Orthogonal–Diagonal–Orthogonal factorization |
| Singular values          | σᵢ = √λᵢ(AᵀA)         | Scaling factors of A |
| Left singular vectors    | uᵢ                     | Eigenvectors of A Aᵀ |
| Right singular vectors   | vᵢ                     | Eigenvectors of Aᵀ A |
| Pseudoinverse            | A⁺ = V Σ⁺ Uᵀ          | Solves least squares / underdetermined systems |
| Rank of A                | r = number of nonzero σᵢ | Dimension of column space |
| Best rank-k approximation| A_k = Σ_{i=1}^k σᵢ uᵢ vᵢᵀ | Optimal compression of A |

---

7) Key takeaways
----------------
- Eigen decomposition applies only to square matrices; SVD works for any matrix.
- SVD generalizes eigen decomposition: when A is symmetric and positive semidefinite, U = V and Σ = Λ.
- SVD reveals the geometric and numerical structure of A: directions, scaling, rank, and stability.
- In the eigenbasis of AᵀA, A acts by stretching space along orthogonal directions defined by V.

End of explanation.


"""







"""
Relation between Eigen Decomposition and Singular Value Decomposition (SVD)

1) Overview
Both eigen decomposition and SVD express a matrix in terms of 
simpler building blocks that reveal its geometric structure.
They are related but not identical — 
eigen decomposition applies to square matrices,
while SVD applies to any m×n matrix.

2) Eigen Decomposition

For a square matrix A ∈ ℝⁿˣⁿ (especially symmetric), 
if A is diagonalizable, there exist:
  - an orthogonal matrix Q whose columns are eigenvectors of A,
  - a diagonal matrix Λ of eigenvalues,
such that
  A = Q Λ Qᵀ.

Each eigenvector eᵢ defines a direction in which 
A acts by a scaling factor λᵢ:
  A eᵢ = λᵢ eᵢ.

Geometrically, A rotates vectors into the eigenbasis (via Qᵀ),
scales them by eigenvalues (Λ), and rotates them back (Q).

3) Singular Value Decomposition (SVD)

For *any* real matrix A ∈ ℝᵐˣⁿ 
(not necessarily square or symmetric), we can write:
  A = U Σ Vᵀ,
where:
  - U ∈ ℝᵐˣᵐ has orthonormal columns (left singular vectors),
  - V ∈ ℝⁿˣⁿ has orthonormal columns (right singular vectors),
  - Σ ∈ ℝᵐˣⁿ is diagonal (rectangular), with nonnegative entries
  σ₁ ≥ σ₂ ≥ … ≥ 0 called singular values.

The number of nonzero singular values equals the rank of A.

4) Connection between SVD and Eigen Decomposition

SVD can be derived from the eigen decomposition of AᵀA and AAᵀ:

- AᵀA = V Σ² Vᵀ
  (eigendecomposition of AᵀA, which is symmetric positive semidefinite)
- AAᵀ = U Σ² Uᵀ
  (eigendecomposition of AAᵀ)

Thus:
  - The right singular vectors (columns of V) are the eigenvectors of AᵀA.
  - The left singular vectors (columns of U) are the eigenvectors of AAᵀ.
  - The singular values σᵢ are the square roots of the nonzero eigenvalues of AᵀA (or AAᵀ).

So SVD generalizes eigen decomposition to rectangular or non-symmetric matrices.

5) Geometric Meaning

- Eigen decomposition: A acts by stretching vectors
along its eigenvector directions by possibly positive or negative λᵢ.
- SVD: A acts by rotating (Vᵀ), 
stretching by nonnegative singular values (Σ), and rotating again (U).

If A is symmetric and positive definite:
  - U = V = Q (same orthonormal basis)
  - Σ = Λ (eigenvalues are positive)
  - Then SVD reduces to the eigen decomposition A = Q Λ Qᵀ.

If A is symmetric but not necessarily positive definite,
the eigenvalues λᵢ can be negative.
SVD always uses nonnegative singular values σᵢ = |λᵢ|.

6) In summary
Eigen decomposition (for symmetric A):
  A = Q Λ Qᵀ
  Qᵀ Q = I, Λ diagonal (may have ± entries)

SVD (for any A):
  A = U Σ Vᵀ
  Uᵀ U = I, Vᵀ V = I, Σ diagonal with nonnegative entries.

Relation:
  If A = Aᵀ and A is symmetric positive semidefinite, then SVD = Eigen decomposition.

- Eigen decomposition: reveals how a square linear operator scales
 and rotates along special directions (eigenvectors).
- SVD: reveals how *any* linear transformation stretches and rotates space,
 even if it’s rectangular or not symmetric.
- Both describe A as “rotate → scale → rotate back,” 
but eigen decomposition uses possibly signed eigenvalues,
while SVD uses always nonnegative singular values.

"""


"""
Singular Values — Explanation

1) Definition:
  - In Singular Value Decomposition (SVD), any m x n matrix A can be decomposed as:
        A = U Σ V^T
    where Σ is a diagonal matrix containing the 
    singular values σ1 ≥ σ2 ≥ ... ≥ σr ≥ 0, with r = rank(A).
  - Each singular value σ_i represents the "stretching factor"
    along the corresponding singular vector direction:
    A maps the right singular vector v_i to the left singular vector u_i scaled by σ_i:
    A v_i = σ_i u_i

2) Intuition:
  - Think of A as a linear transformation of space.
      - V^T rotates the input space into an orthogonal basis (v_i directions).
      - Σ scales each direction by σ_i.
      - U rotates/scales into the output space.
  - The singular values tell you how much A stretches or compresses along each principal direction.
      - Large σ_i → direction is amplified.
      - Small σ_i → direction is nearly collapsed (close to nullspace).

3) Why they are called "singular values":
  - The term comes from classical matrix theory:
      - For a square matrix, eigenvalues characterize intrinsic scaling along eigenvectors.
      - For non-square matrices, there may not be eigenvalues, but we can still find intrinsic scaling factors.
      - These scaling factors (σ_i) are “special” or “singular” because they reveal the essential action of A on input space.
  - More formally:
      - Singular values are the square roots of the eigenvalues of A^T A (or AA^T):
            σ_i = sqrt(λ_i), where A^T A v_i = λ_i v_i
      - Since they arise from a symmetric positive semi-definite matrix (A^T A), they are always non-negative.

4) Properties:
  - Non-negative: σ_i ≥ 0
  - Ordered: σ1 ≥ σ2 ≥ ... ≥ σr
  - Number of non-zero σ_i = rank(A)
  - Condition number: cond(A) = σ_max / σ_min (measures numerical stability)
  - Frobenius norm: ||A||_F = sqrt(Σ σ_i^2)

5) Applications:
  - Low-rank approximation: keep top k singular values/vectors.
  - PCA: singular values indicate importance of each principal component.
  - Pseudoinverse: singular values used to invert A stably.
  - Image compression: smaller singular values can be dropped to reduce data.

---- End of explanation ----



"""