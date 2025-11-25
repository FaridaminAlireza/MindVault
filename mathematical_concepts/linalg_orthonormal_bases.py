"""
Mapping coordinates into an orthonormal basis

if {e₁,…,eₖ} is an orthonormal basis, the coordinates of a vector v
in that basis are simply the dot products cᵢ = v·eᵢ. 
If you start with some other basis, use Gram–Schmidt to make it orthonormal first.

---
1) Problem setup (example)

Work in ℝ³. Start with a non-orthonormal basis of a 2-dimensional subspace:
u₁ = (1, 1, 0)
u₂ = (1, 0, 1)
and take the input vector
v = (2, 1, 1)

Goal: find coordinates of v in an orthonormal basis for span{u₁, u₂}.

-------------------------------------------------------------------------------------
2) Orthonormalize the basis (Gram–Schmidt)
-------------------------------------------------------------------------------------
Step 2.1 — first orthonormal vector e₁:
‖u₁‖ = √2
e₁ = (1/√2, 1/√2, 0)

Step 2.2 — make u₂ orthogonal to e₁:
projₑ₁(u₂) = (u₂·e₁)e₁ = (1/√2)e₁
v₂ = u₂ - projₑ₁(u₂) = (1,0,1) - (½,½,0) = (½, -½, 1)

Step 2.3 — normalize v₂ to get e₂:
‖v₂‖ = √(3/2) = √6 / 2
e₂ = (1/√6, -1/√6, 2/√6)

Now {e₁, e₂} is an orthonormal basis.

-------------------------------------------------------------------------------------
3) Compute coordinates of v in the orthonormal basis
-------------------------------------------------------------------------------------
c₁ = v·e₁ = 3/√2
c₂ = v·e₂ = 3/√6

Coordinates of v relative to {e₁, e₂}:
[v]_(e₁,e₂) = [3/√2, 3/√6]^T

Reconstruction check: (3/√2)e₁ + (3/√6)e₂ = (2, 1, 1) = v

-------------------------------------------------------------------------------------
4) Matrix viewpoint
-------------------------------------------------------------------------------------
Matrix Q = [e₁ e₂]

Then:
c = Qᵀv
Projection onto the span: proj(v) = Q Qᵀ v (reconsturction of V)

If Q is square and orthonormal, Q⁻¹ = Qᵀ.

-------------------------------------------------------------------------------------
5) Orthogonal projection explained
-------------------------------------------------------------------------------------
Projection means finding the point v_S inside the subspace S = span{e₁, e₂, …}
that is closest to v, such that v - v_S ⟂ S.

For orthonormal basis:
proj_S(v) = (v·e₁)e₁ + (v·e₂)e₂ + … = Q Qᵀ v

Example (same as before):
v = (2,1,1)
c₁ = 3/√2, c₂ = 3/√6
proj_S(v) = c₁ e₁ + c₂ e₂ = (2,1,1)

Since v already lies in the span, projection equals v.

-------------------------------------------------------------------------------------
6) Matrix computation example for QQᵀv
-------------------------------------------------------------------------------------
Q =
[ 0.7071   0.4082 ]
[ 0.7071  -0.4082 ]
[ 0.0000   0.8165 ]

v = [2, 1, 1]^T

Step 1: Qᵀv = [2.1213, 1.2247]^T

Step 2: Q(Qᵀv) =
[ 0.7071  0.4082 ] [2.1213]
[ 0.7071 -0.4082 ] [1.2247]
[ 0.0000  0.8165 ]
= (2, 1, 1)

v lies entirely in the plane spanned by e₁ and e₂.

-------------------------------------------------------------------------------------
7) Interpretation of coordinates c₁, c₂ and relation to eigenvalues
-------------------------------------------------------------------------------------
- cᵢ = v·eᵢ are the coordinate scalars — they tell how much v points along each orthonormal direction.
- They are **not eigenvalues** by themselves.

Eigenvalues appear only when there is a linear operator A such that
A eᵢ = λᵢ eᵢ.
Then, projecting v along each eigenvector 𝑒𝑖 gives the decomposition
of v in the eigenbasis.

cᵢ = v·eᵢ

A eᵢ = λᵢ eᵢ.

Applying A to v scales each component cᵢ by the corresponding eigenvalue λᵢ:

A v = Σ cᵢ λᵢ eᵢ.

So eigenvalues describe how the operator scales eigenvectors,
while cᵢ describe how v is composed of those directions.


General proof: Why A v = Σ_i c_i λ_i e_i holds

Assume:
- A is a diagonalizable (or symmetric) linear operator on ℝ^n.
- { e₁, e₂, …, eₙ } are orthonormal eigenvectors of A.
- The corresponding eigenvalues are { λ₁, λ₂, …, λₙ }, meaning A eᵢ = λᵢ eᵢ for all i.

Let any vector v ∈ ℝⁿ be expressed as a linear combination of these eigenvectors:
  v = Σ_i cᵢ eᵢ
where cᵢ = v · eᵢ are the coordinates of v in the eigenbasis.

Goal: Prove that A v = Σ_i cᵢ λᵢ eᵢ.

Proof:
1) Start from the linearity of A:
   A(v) = A(Σ_i cᵢ eᵢ) = Σ_i A(cᵢ eᵢ)

2) Constants can be factored out of linear maps:
   Σ_i A(cᵢ eᵢ) = Σ_i cᵢ A(eᵢ)

3) Use the eigenvector property A eᵢ = λᵢ eᵢ:
   Σ_i cᵢ A(eᵢ) = Σ_i cᵢ (λᵢ eᵢ)

4) Simplify notation:
   A v = Σ_i cᵢ λᵢ eᵢ

This completes the proof.

Interpretation:
- Each component of v in the eigenbasis (the cᵢ)
 is scaled by its corresponding eigenvalue λᵢ when A acts on v.
- So A acts as a *diagonal operator* in the eigenbasis.

Matrix form equivalence:
Let Q = [ e₁ e₂ ... eₙ ] and Λ = diag(λ₁, ..., λₙ).

Then for any v:
  v = Q c  where  c = Qᵀ v.
  A v = Q Λ Qᵀ v = Q Λ c = Σ_i λᵢ cᵢ eᵢ.

Hence the identity holds both in vector and matrix form.

Geometric meaning:
A simply stretches or compresses v along each eigenvector direction eᵢ by factor λᵢ.


Why A = Q Λ Qᵀ? 
Spectral decomposition (A = Q Λ Q^T)
--------------------------------------
- Suppose A is a real symmetric matrix 
(or more generally diagonalizable with an orthonormal eigenbasis).
- Let e_1,...,e_n be orthonormal eigenvectors of A and 
λ_1,...,λ_n their eigenvalues, so A e_i = λ_i e_i.
- Put the eigenvectors as columns of Q: Q = [ e_1 e_2 ... e_n ].
Then Q is orthogonal: Q^T Q = I.
- Let Λ = diag(λ_1,...,λ_n). The eigen-equations for all columns
can be written together as: A Q = Q Λ.
- Multiply on the right by Q^T and use Q Q^T = I to get:
A = Q Λ Q^T.
This is the spectral (eigendecomposition) of A.

Interpretation: write A as: 
rotate to eigenbasis (Q^T), scale each coordinate by Λ, rotate back (Q).

--
Coordinates in eigenbasis, and effect of A:

- Coordinates of a vector v in the eigenbasis are given by c = Q^T v. So v = Q c and c_i = v · e_i.
- Apply A:
    A v = (Q Λ Q^T) v = Q Λ (Q^T v) = Q Λ c.
- Λ c = (λ_1 c_1, λ_2 c_2, ..., λ_n c_n)^T.
- Therefore:
    A v = Q (Λ c) = Σ_i (λ_i c_i) e_i.
  So, in the eigenbasis, coordinates are simply scaled: c'_i = λ_i c_i.
  In other words, A multiplies the coefficient along each eigenvector e_i by the eigenvalue λ_i.

Geometric intuition
- Q^T: change coordinates from standard basis to eigenbasis (express vector in eigen-directions).
- Λ: scale each eigen-coordinate independently by λ_i.
- Q: convert scaled coordinates back to the original coordinate system.
- So A acts by "rotate → scale → rotate back".


-------------------------------------------------------------------------------------
8) Summary formulas
-------------------------------------------------------------------------------------
Coordinates:   c = Qᵀv
Projection:    v_proj = Q Qᵀ v
Residual:      r = v - v_proj  (orthogonal to subspace)

If basis vectors are eigenvectors of a symmetric matrix A:
A v = Q Λ Qᵀ v = Σ λᵢ cᵢ eᵢ


"""


"""
eigenvectors are not always normalized by default. 
An eigenvector v multiplied by any non-zero scalar c (i.e., cv) 
is still an eigenvector for the same eigenvalue. 
The length of an eigenvector is arbitrary by definition, 
although they can be scaled (normalized) to unit length for convenience.
 Furthermore, eigenvectors do not always form an orthonormal basis 
(a set of mutually orthogonal unit vectors) for the entire vector space.

This depends on the specific matrix: 

General Matrices: For most matrices, eigenvectors are neither necessarily
orthogonal nor do they always form a complete basis. 

Normal (e.g., Real Symmetric) Matrices: A special class of matrices called
normal matrices (which includes all real symmetric matrices) is guaranteed
to have a full set of eigenvectors that can be chosen to form an orthonormal
basis. For these matrices, eigenvectors corresponding to distinct eigenvalues
are automatically orthogonal.

In essence, while you can always normalize any given non-zero eigenvector to
unit length, the set of all eigenvectors for a general matrix may not be orthogonal
to each other, nor form a complete basis. 

"""