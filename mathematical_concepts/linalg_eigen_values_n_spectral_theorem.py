"""
Eigenvalues and eigenvectors and also of symmetric matrices.
Spectral theorem for real symmetric matrices (a real symmetric 
matrix S has an orthonormal basis of eigenvectors and real eigenvalues.

---
What are eigenvalues and eigenvectors?

Let A be an n×n matrix (real or complex). 
A scalar λ and a non-zero vector v ∈ R^n (or C^n) 
are called an eigenvalue and eigenvector of A if
A v = λ v.
Interpretation: applying the linear map A to v 
just stretches (by λ) and possibly flips it 
— it does not change the direction of v.

To compute them:
1. Solve (A−λI)v=0 for nonzero v.
2. Nontrivial solutions exist only when det(A−λI)=0.
This is because if (A−λI) has inverse, after mulitplying both sides
to inverse of (A−λI), v = 0 ,will have the trivial solution.

The polynomial p(λ)=det(A−λI) is the characteristic polynomial;
its roots are the eigenvalues.

3. For each eigenvalue λ, solve (A−λI)v=0 to get the eigenspace 
(all eigenvectors for that λ), whose dimension is the geometric 
multiplicity.
The multiplicity of λ as a root of p(λ) is its algebraic multiplicity.
Always: geometric multiplicity ≤ algebraic multiplicity.

---
# Special case: real symmetric matrices

A real matrix S is symmetric if S^T = S. These matrices have special properties:

Spectral theorem (real symmetric case) — statement (informal):
If S is a real symmetric n×n matrix, then:
- All eigenvalues of S are real.
- There exists an orthonormal basis of R^n consisting of eigenvectors of S.
Equivalently, there exists an orthogonal matrix Q 
(i.e. Q^T Q = I) and a real diagonal matrix Λ such that
S = Q Λ Q^T,
where Λ contains the eigenvalues of S on the diagonal.

Consequences:
- S is diagonalizable by an orthogonal change of basis.
- S is symmetric ⇒ "nice" spectral decomposition;
 eigenvectors for distinct eigenvalues are orthogonal.
- Quadratic form x^T S x is easy to analyze in eigenbasis;
 signs of eigenvalues tell you definiteness.

---
Example 1: 3x3 SYMMETRIC matrix (step-by-step)

Matrix:
S = [[2, 0, 0],
     [0, 3, 4],
     [0, 4, 9]]

1) Form A - λI:
S - λI = [[2-λ, 0,   0  ],
          [0,   3-λ, 4  ],
          [0,   4,   9-λ]]

2) Characteristic polynomial p(λ) = det(S - λI).
Expand along first row (since two zeros):
p(λ) = (2-λ) * det([[3-λ, 4],
                   [4,   9-λ]])
     = (2-λ) * ((3-λ)(9-λ) - 16)
     = (2-λ) * ( (27 - 12λ + λ^2) - 16 )
     = (2-λ) * (λ^2 - 12λ + 11)

Set p(λ) = 0:
(2-λ)(λ^2 - 12λ + 11) = 0

Solve factors:
- From first factor: λ = 2
- From quadratic: λ = [12 ± sqrt(144 - 44)]/2 = [12 ± sqrt(100)]/2 = (12 ± 10)/2
  => λ = 11 and λ = 1

Eigenvalues:
λ1 = 2, λ2 = 11, λ3 = 1  (all real, as expected for symmetric S)

3) Eigenvectors (solve (S - λI)v = 0):

- For λ = 2:
  S - 2I = [[0, 0, 0],
            [0, 1, 4],
            [0, 4, 7]]
  Equations:
    1*y + 4*z = 0
    4*y + 7*z = 0
  From first: y = -4z. 
  Substitute: 4(-4z) + 7z = 
  -16z + 7z = -9z = 0 => z = 0 => y = 0.
  x is free. Choose x = 1.
  Eigenvector v1 = (1, 0, 0)^T.
  S = [[2, 0, 0],
       [0, 3, 4],
       [0, 4, 9]]
  (Check: S v1 = (2,0,0)^T = 2 v1)

- For λ = 11:
  S - 11I = [[-9, 0, 0],
             [0, -8, 4],
             [0, 4, -2]]
  System (ignore first row -> x=0):
    -8 y + 4 z = 0  => -8y + 4z = 0  => z = 2y
    4 y - 2 z = 0   => same relation
  Choose y = 1 => z = 2
  Eigenvector v2 = (0, 1, 2)^T.
  (Check: S v2 = (0, 3*1 + 4*2, 4*1 + 9*2)^T = (0, 11, 22)^T = 11 v2)

- For λ = 1:
  S - I = [[1, 0, 0],
           [0, 2, 4],
           [0, 4, 8]]
  From first row: x = 0.
  From second: 2 y + 4 z = 0 => y = -2 z
  Third: 4 y + 8 z = 0 => same relation.
  Choose z = 1 => y = -2
  Eigenvector v3 = (0, -2, 1)^T. (Or multiply by -1 -> (0, 2, -1)^T)
  (Check: S v3 = (0, 3*(-2)+4*1, 4*(-2)+9*1)^T = (0, -6+4, -8+9)^T = (0, -2, 1)^T = 1 * v3)

4) Multiplicities:
- Each eigenvalue appears once as a root of p(λ): algebraic multiplicity (AM) = 1 for λ=2,11,1.
- Eigenspaces each found to be 1-dimensional: geometric multiplicity (GM) = 1 for each eigenvalue.
- For symmetric matrices, AM = GM for all eigenvalues; matrix is diagonalizable.

5) Orthonormal eigenvectors and spectral decomposition:
Normalize vectors:

v1 = (1,0,0)          -> q1 = (1,0,0)

v2 = (0,1,2)          -> norm = sqrt(1^2 + 2^2) = sqrt(5) => q2 = (0, 1/√5, 2/√5)

v3 = (0,2,-1)         -> norm = sqrt(4 + 1) = sqrt(5) => q3 = (0, 2/√5, -1/√5)

Note: q2 and q3 are orthogonal to each other and to q1.

Assemble Q = [q1 q2 q3], Λ = diag(2,11,1), then
S = Q Λ Q^T.

---
Example 2: 3x3 NON-SYMMETRIC matrix (Jordan upper-triangular example)

Matrix:
A = [[2, 1, 0],
     [0, 2, 1],
     [0, 0, 2]]

This is an upper-triangular (Jordan block-like) matrix.
Its eigenvalues are the diagonal entries (2,2,2).

1) Characteristic polynomial:
p(λ) = det(A - λI) = (2 - λ)^3
Eigenvalue: λ = 2 with algebraic multiplicity AM = 3.

2) Solve (A - 2I)v = 0 to find eigenspace:

A - 2I = [[0, 1, 0],
          [0, 0, 1],
          [0, 0, 0]]

Let v = (x, y, z)^T. Then (A - 2I)v = 0 gives:
  0*x + 1*y + 0*z = 0  => y = 0
  0*x + 0*y + 1*z = 0  => z = 0
  0 = 0  (third row)

Thus y = 0, z = 0; x is free. 
So eigenspace consists of vectors (x, 0, 0)^T (one-dimensional).

Geometric multiplicity GM = 1.

Conclusion about diagonalizability:
- Algebraic multiplicity AM(2) = 3.
- Geometric multiplicity GM(2) = 1.
Because GM < AM, A is not diagonalizable. In particular, 
A has a single independent eigenvector v = (1,0,0)^T (up to scaling).
This matrix is similar to a Jordan block of size 3.

General check:
Compute A v for v = (1,0,0)^T:
A v = (2,0,0)^T = 2 v  => valid eigenvector.

For completeness, generalized eigenvectors exist 
(solve (A - 2I)w = v) and form a Jordan chain,
but they are not eigenvectors.
---

# If A is symmetric then eigenvectors corresponding to
distinct eigenvalues are always orthogonal.

Orthogonality of eigenvectors for symmetric (real) matrices — Step-by-step proof

1) Statement (what we want to show)
   Let A be a real symmetric matrix (A = A^T). Show that eigenvectors belonging
   to *distinct* eigenvalues are orthogonal. Also explain what happens when eigenvalues
   are equal, and how to obtain an orthonormal basis of eigenvectors.

2) Setup (definitions and notation)
   - A is an n×n real matrix with A = A^T.
   - v and w are two eigenvectors of A with eigenvalues λ and μ respectively:
       A v = λ v,     A w = μ w.
   - We use the standard real inner product: x · y = x^T y.
   - Goal: show v · w = 0 when λ ≠ μ.

3) Key property of symmetric matrices (used in the proof)
   For any vectors x and y in R^n, if A = A^T then
       x^T (A y) = (A x)^T y.
   This follows because x^T (A y) is a scalar and equals its transpose:
       x^T (A y) = (x^T (A y))^T = y^T A^T x = y^T A x = (A x)^T y.
   So for symmetric A we may interchange A between the two slots of the inner product.

4) The proof (distinct eigenvalues)
   Start from the two eigen-equations:
       A v = λ v        (1)
       A w = μ w        (2)
   Take the inner product of v with (2):
       v^T (A w) = v^T (μ w) = μ (v^T w).        (3)
   Take the inner product of (1) with w (equivalently the inner product of A v with w):
       (A v)^T w = (λ v)^T w = λ (v^T w).       (4)
   Use the symmetry property to equate the left-hand sides of (3) and (4):
       v^T (A w) = (A v)^T w.
   Therefore from (3) and (4) we get:
       μ (v^T w) = λ (v^T w).
   Rearranging gives:
       (μ − λ) (v^T w) = 0.
   If λ ≠ μ then μ − λ ≠ 0, hence v^T w = 0.
   That is, v and w are orthogonal.

5) What if λ = μ (repeated eigenvalue)
   If two eigenvectors share the same eigenvalue, the above argument
   gives no information (it only yields 0 = 0).
   In that case the eigenvectors lie in the same eigenspace (a subspace).
   Any basis of that eigenspace is valid, and we can apply the 
   Gram–Schmidt process (or orthonormal diagonalization theory)
   to choose an orthonormal basis of that eigenspace. Therefore for 
   symmetric matrices we can always choose a full set of n orthonormal eigenvectors
   (one for each dimension), i.e., A is diagonalizable by an orthogonal matrix:
   A = Q D Q^T with Q^T Q = I.

6) Complex case (Hermitian matrices)
   For complex matrices A with A = A*, i.e. A equals 
   its conjugate transpose (Hermitian), the same proof works
   using the complex inner product ⟨x,y⟩ = x* y 
   (conjugate transpose of x times y). The key identity becomes
   ⟨x, A y⟩ = ⟨A x, y⟩ and leads to orthogonality of eigenvectors
   for distinct eigenvalues. Repeated eigenvalues again allow orthonormalization
   within each eigenspace, so a Hermitian matrix has an orthonormal eigenbasis and
   is unitarily diagonalizable: A = U D U*.

7) Short numeric example (real symmetric 2×2)
   Let A = [[2, 1], [1, 2]]. Its eigenvalues are λ1 = 3 and λ2 = 1.
   Corresponding eigenvectors: v1 = [1, 1]^T, v2 = [1, -1]^T.
   Their dot product: v1^T v2 = 1*1 + 1*(−1) = 0 ⇒ orthogonal (as predicted).

8) Final remarks
   - Distinct eigenvalues ⇒ eigenvectors are orthogonal for symmetric (or Hermitian) matrices.
   - Repeated eigenvalues ⇒ eigenvectors need not be orthogonal automatically,
   but we can choose an orthonormal basis inside each eigenspace.
   - Therefore every real symmetric matrix has a complete orthonormal set
   of eigenvectors and can be diagonalized by an orthogonal matrix.

---
# The eigenvalues in symmetric matrix are real

Realness of eigenvalues:
If S is real symmetric and Sv=λ v with possibly complex v,
take conjugate transpose v* S = overline{λ} v* (because S^T=S). Now compute:
v* S v = v* (λ v) = λ (v* v).
But also
v* S v = (v* S v)* = overline{v* S v} = overline{λ} (v* v).
So λ (v* v) = overline{λ}(v* v). Since v≠0 implies v* v>0, we get λ = overline{λ}, i.e. λ real.
---

These two facts are central to proving the spectral theorem.

---
Spectral Decomposition of a Real Symmetric Matrix

1) Setup and notation

Let S be a real symmetric matrix, i.e. S = S^T.
We know from the spectral theorem that any real symmetric matrix
can be diagonalized by an orthogonal matrix.

That means there exists an orthogonal matrix Q
and a diagonal matrix Λ (Greek letter "Lambda") such that

    S = Q Λ Q^T

Here:
- Q = [q₁ q₂ ... qₙ] is the matrix whose columns are the eigenvectors of S.
- Each qᵢ is a unit-length (normalized) eigenvector.
- Λ = diag(λ₁, λ₂, ..., λₙ) is a diagonal matrix
  containing the eigenvalues of S on the diagonal.

The term "orthogonal matrix" means Q satisfies Q^T Q = I,
i.e., its columns are orthonormal:
    qᵢ^T qⱼ = 0 if i ≠ j,
    qᵢ^T qᵢ = 1 for all i.


2) What S = Q Λ Q^T really means

If we expand this expression, we can write S in terms of its
eigenvectors and eigenvalues as a sum:

    S = λ₁ q₁ q₁^T + λ₂ q₂ q₂^T + ... + λₙ qₙ qₙ^T

This is equivalent to writing

    S = Σ (from i=1 to n) λᵢ qᵢ qᵢ^T.

Each term qᵢ qᵢ^T is a matrix formed by the *outer product*
of qᵢ with itself.

- The matrix qᵢ qᵢ^T is called an *orthogonal projection matrix*.
  It projects any vector onto the direction of qᵢ.
- Because the qᵢ are orthonormal, these projections are
  mutually orthogonal — each acts independently on its subspace.
- Each projection is *scaled* by the corresponding eigenvalue λᵢ.

So S can be thought of as a sum of "scaled projections"
onto its eigenvector directions.

This expression is called the **spectral decomposition**
or **eigendecomposition** of S.


3) Interpreting Q^T S Q = Λ
Multiplying both sides of S = Q Λ Q^T by Q^T on the left
and Q on the right, we get:

    Q^T S Q = Λ

This means that in the *coordinate system defined by the eigenvectors*
(the "eigenbasis"), the matrix S acts as a purely diagonal matrix Λ.
That is, in this basis, S simply scales each coordinate by λᵢ
without mixing them.

So in the standard basis, S might "mix" components,
but in the eigenbasis, it acts in a perfectly simple way.


4) Connection with positive definiteness

If all eigenvalues λᵢ are positive (λᵢ > 0 for all i),
then for any nonzero vector x, we have:

    x^T S x = x^T (Q Λ Q^T) x
            = (Q^T x)^T Λ (Q^T x)
            = Σ λᵢ (yᵢ)²,
      where y = Q^T x (a rotated version of x).

Since λᵢ > 0 and (yᵢ)² ≥ 0, the sum is strictly positive
for any nonzero x.

Therefore, S is **positive definite**.


5) key takeaways

- The columns of Q are orthonormal eigenvectors of S.
- Λ is the diagonal matrix of eigenvalues.
- The relation S = Q Λ Q^T is called the spectral decomposition.
- It shows that S can be represented as a weighted sum
  of orthogonal projections onto its eigenvectors.
- Q^T S Q = Λ means the matrix becomes diagonal
  when expressed in its eigenbasis.
- If all eigenvalues are positive, S is positive definite.

This decomposition is fundamental in many areas:
principal component analysis (PCA), quadratic forms,
optimization, and numerical linear algebra.


---
# How to compute numerically (practical recipe)

For a real symmetric matrix S:
1. Use a reliable algorithm: 
QR algorithm specialized to symmetric matrices 
(or divide-and-conquer, or tridiagonalization + QR) 
— these exploit symmetry for numerical stability.
2. If you compute by hand (small n):
- Form characteristic polynomial, find eigenvalues.
- For each eigenvalue, solve (S−λI)v=0.
- Apply Gram–Schmidt only if an eigenspace has dimension > 1 
(to produce orthonormal eigenvectors inside that eigenspace).
3. Normalize all eigenvectors to length 1;
assemble Q. Then check Q^T Q = I and Q^T S Q is diagonal.

"""

