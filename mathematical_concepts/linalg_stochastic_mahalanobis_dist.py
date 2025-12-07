"""
INTRODUCTION
The Mahalanobis distance between two vectors x and y 
(with respect to a covariance matrix Σ) is defined by

d_M(x,y) = sqrt( (x - y)^T Σ^{-1} (x - y) ).

When the context uses a mean vector μ 
(for distance from a distribution center),
we write

d_M(x; μ, Σ) = sqrt( (x - μ)^T Σ^{-1} (x - μ) ).

Intuition: it measures distance 
after accounting for 
the scale and correlation of the data: 

directions of high variance count less,
directions of low variance count more.

Level sets { x : d_M(x; μ, Σ) = c } are 
ellipsoids aligned with covariance eigenvectors.

REQUISITES (what you need / assumptions)

1. A mean vector μ ∈ R^n 
(if measuring from a distribution center)
or two points x,y ∈ R^n 
(if measuring pairwise).
2. A covariance matrix Σ ∈ R^{n×n} 
that is symmetric and positive semidefinite.
3. For the standard formula to produce
a bona fide distance
 ('bona fida' term is used to
 emphasize that a proposed function or 
 measure rigorously satisfies all the formal axioms
 required to be a mathematical metric 
 (or a distance metric).
with all metric properties,
Σ must be positive definite (invertible).
If Σ is singular, 
use a Moore–Penrose pseudo-inverse Σ^+ 
(then some metric properties can fail; 
interpret distances carefully) or 
regularize Σ (e.g., Σ_reg = Σ + εI).
4. Data should be numeric and
on a continuous scale;
Mahalanobis is meaningful only when 
Σ captures variability structure.

APPLICATIONS

1. Outlier detection: compute d_M(x; μ, Σ); 
large values indicate multivariate outliers.
2. Multivariate hypothesis testing and
 confidence regions (ellipsoids).
3. Classification (e.g., discriminant analysis
 uses Mahalanobis distances).
4. Clustering and anomaly detection 
(distance that accounts for feature correlations).
5. Data whitening/preprocessing: 
equivalently used to transform data
to unit covariance.
6. Multivariate regression diagnostics 
and robust statistics.
7. Feature matching and similarity when 
features have different scales and correlation.

DERIVATIONS, EXAMPLES, AND PROOFS (step-by-step)

Notation:
x, y in R^n; μ in R^n;
Σ is symmetric positive definite (SPD)
unless otherwise noted.
For simplicity denote 
δ = x - y or δ = x - μ.

1. FORMULA (definition / motivation)
   Start from intuition: 
   standardize each component and
   sum squares. 
   
   If Σ were diagonal with entries σ_i^2,
   then a sensible distance is
   sum_i ( (x_i - μ_i)^2 / σ_i^2 ).
   This is exactly the quadratic form
   (x - μ)^T Σ^{-1} (x - μ)
   when Σ = diag(σ_1^2,...,σ_n^2). 
   
   For the correlated case,
   the natural generalization 
   is the same quadratic form
   with Σ the full covariance matrix:
   d_M(x; μ, Σ) = sqrt( (x - μ)^T Σ^{-1} (x - μ) ).

2. RELATION TO WHITENING 
(equivalence to Euclidean distance 
after linear transform)
   Step 1: Since Σ is SPD, 
   there exists an invertible matrix L 
   (for instance from Cholesky) such that
   Σ = L L^T.
   Step 2: Let z = L^{-1} (x - μ). Then
   ||z||_2^2 = z^T z =
   (x - μ)^T (L^{-T} L^{-1}) (x - μ) =
   (x - μ)^T Σ^{-1} (x - μ).
   So
   d_M(x; μ, Σ) = || L^{-1} (x - μ) ||_2.
   Thus Mahalanobis distance is 
   Euclidean distance 
   after applying the linear transform L^{-1} 
   that whitens (decorrelates and rescales) Σ.
   This explains scale/correlation invariance.

3. PROPERTY PROOFS

    3A) Nonnegativity and definiteness
    For SPD Σ, the quadratic form
    q(δ)=δ^T Σ^{-1} δ ≥ 0 and
    equals 0 iff δ = 0. 
    Hence d_M ≥ 0 and
    d_M = 0 ⇔ x = y (or x = μ). 
    (If Σ is only positive semidefinite,
    q(δ) ≥ 0 but q(δ)=0 can occur for δ ≠ 0
    lying in the nullspace.)

    3B) Symmetry
    d_M(x,y) = 
    sqrt( (x-y)^T Σ^{-1} (x-y) ) = 
    d_M(y,x) 
    because expression depends only
    on x-y squared.

    3C) Triangle inequality
    Using whitening: 
    define T(z) = L^{-1} z. 
    Then d_M(x,y) = || T(x) - T(y) ||_2.
    Euclidean norm satisfies triangle inequality, so
    ||T(x)-T(z)||_2 ≤ ||T(x)-T(y)||_2 + ||T(y)-T(z)||_2,
    i.e. d_M(x,z) ≤ d_M(x,y) + d_M(y,z).
    Thus triangle inequality holds 
    when Σ is SPD (so L invertible).
    Therefore d_M is a metric in that case.

    3D) Invariance to linear re-scalings matched by Σ
    If you apply an invertible linear transform B 
    to the raw variables and adjust Σ accordingly 
    (Σ' = B Σ B^T), Mahalanobis distances are preserved:
    d_{M,Σ'}(Bx, By) 
    = sqrt( (Bx-By)^T (B Σ B^T)^{-1} (Bx-By) )
    = sqrt( (x-y)^T B^T (B Σ B^T)^{-1} B (x-y) )
    = sqrt( (x-y)^T Σ^{-1} (x-y) )
    (the algebra uses 
    (B Σ B^T)^{-1} = B^{-T} Σ^{-1} B^{-1}).
    So Mahalanobis distance is consistent 
    with the covariance-adjusted geometry.

4. RELATION TO MULTIVARIATE NORMAL PDF
   If X ∼ N(μ, Σ), its density is
   f_X(x) = 
   (2π)^{-n/2} |Σ|^{-1/2} exp( -1/2 (x-μ)^T Σ^{-1} (x-μ) ).
   So the squared Mahalanobis distance appears exactly
   in the exponent: high Mahalanobis distance → low density.

5. EXAMPLE 1 — DIAGONAL COVARIANCE 
   (standardized Euclidean)
   Let Σ = diag(σ_1^2, σ_2^2, ..., σ_n^2). Then
   d_M(x; μ, Σ)^2 = sum_{i=1}^n (x_i - μ_i)^2 / σ_i^2.
   Example: n=2, μ=[0,0], σ_1=2, σ_2=1, x=[2,1]:
   d_M^2 = (2^2)/(2^2) + (1^2)/(1^2) = 4/4 + 1 = 2.
   d_M = sqrt(2) ≈ 1.41421356.

6. EXAMPLE 2 — FULL 2×2 COVARIANCE (numerical)
   Given
   μ = [0,0],
   x = [2,1].
    Σ = [[4, 1.2],
         [1.2, 1]],
   Step A: compute Σ^{-1}.

   For a 2×2 matrix [[a,b],[b,c]],
   inverse is (1/(ac-b^2)) * [[c,-b],[-b,a]].

   Here a=4, b=1.2, c=1 so 
   det = 4*1 - 1.2^2 = 4 - 1.44 = 2.56.
   Σ^{-1} = 
   (1/2.56) * [[1, -1.2], [-1.2, 4]] = 
   [[0.390625, -0.46875],
    [-0.46875, 1.5625]].

   Step B: compute δ = x - μ = [2,1].
 
   Step C: compute squared Mahalanobis:
   d_M^2 = δ^T Σ^{-1} δ = 
   [2,1] * 
   [[0.390625, -0.46875], 
    [-0.46875, 1.5625]] *
   [2,1]^T.

   First compute Σ^{-1} δ = 
   [0.390625*2 + (-0.46875)*1,
    -0.46875*2 + 1.5625*1]
   = [0.78125 - 0.46875, -0.9375 + 1.5625]
   = [0.3125, 0.625].
   Then δ^T (Σ^{-1} δ) = 
   2*0.3125 + 1*0.625 = 
   0.625 + 0.625 = 1.25.
   So d_M^2 = 1.25 and 
   d_M = sqrt(1.25) ≈ 1.118033988749895.

   Interpretation: although Euclidean norm of x is
   sqrt(2^2+1^2)=sqrt(5)≈2.236, 
   after accounting for covariance Σ 
   the Mahalanobis distance is ≈1.118 
   — the covariance structure downweights
   the effective distance in some directions.

7. LEVEL SETS ARE ELLIPSOIDS (geometric proof)
   Consider set { x : (x-μ)^T Σ^{-1} (x-μ) = c^2 }.
   Use eigen-decomposition Σ = Q Λ Q^T 
   (Λ diagonal of positive eigenvalues λ_i,
    Q orthogonal).
   Let y = Q^T (x-μ). Then condition becomes
   y^T Λ^{-1} y = c^2  =>  sum_i y_i^2 / λ_i = c^2.
   This is an ellipsoid in y-space;
   mapping back by Q gives ellipsoid in x-space
   with principal axes Q and 
   squared axis lengths proportional to λ_i.

8. HANDLING SINGULAR OR ILL-CONDITIONED COVARIANCES
    * If Σ is singular (rank < n), 
    Σ^{-1} does not exist. 
    Option: use Moore–Penrose pseudo-inverse Σ^+ 
    and compute δ^T Σ^+ δ. 
    Interpretation: distance is defined only 
    in the subspace spanned by Σ.
    * Regularization: Σ_reg = Σ + ε I with small ε > 0 
    makes Σ_reg SPD and invertible; 
    compute Mahalanobis with Σ_reg.
    * For small sample sizes relative to dimension,
    prefer shrinkage estimators of covariance 
    before using Mahalanobis distance.

9. NUMERICAL/IMPLEMENTATION NOTES

    * Compute Mahalanobis robustly by
    using a Cholesky solve or
    an LDL^T decomposition
    instead of explicitly forming Σ^{-1}. 
    For example compute z = solve(L, x-μ) 
    where L is Cholesky factor, then d_M = ||z||_2.
    * For many queries against same Σ,
    precompute factorization (Cholesky or eigen)
    to speed repeated distance computations.
    * When Σ is ill-conditioned,
    use regularization or 
    pseudo-inverse; 
    avoid direct inversion.

CONCLUDING REMARKS:
    Mahalanobis distance generalizes
    standardized Euclidean distance to
    the correlated multivariate case 
    by measuring distance in
    units of the covariance geometry.
    It is central to multivariate statistics,
    detection of outliers, and algorithms 
    that need a scale- and correlation-aware
    similarity measure.
"""

"""
Explanation of the expression (x - y)^T Σ^{-1} (x - y)

1. WHAT THE SYMBOLS MEAN
   1.1) x, y ∈ ℝⁿ are column vectors.
   Often y is a mean vector μ, 
   so δ = x − y 
   is the displacement from the center.
   1.2) Σ ∈ ℝⁿˣⁿ is a covariance matrix 
   (symmetric, usually positive semidefinite;
   assume positive definite for now).
   1.3) Σ^{-1} is the matrix inverse of Σ 
   (exists when Σ is positive definite).
   1.4) The whole expression is a scalar:
   q = (x - y)^T Σ^{-1} (x - y).
   People call q the *squared Mahalanobis distance*
   between x and y (or between x and the distribution
   centered at y with covariance Σ).

2. DIMENSIONAL CHECK (why this is scalar)
   2.1) δ = x − y is n×1.
   2.2) Σ^{-1} is n×n; Σ^{-1} δ is n×1.
   2.3) δ^T (Σ^{-1} δ) is 
   (1×n) · (n×1) = 1×1, i.e. a scalar. 
   So the expression makes algebraic sense.

3. WHY Σ^{-1} (AND NOT JUST Σ)
   3.1) If Σ were diagonal with variances σ_i^2 on the diagonal,
   then “divide by variance” for each coordinate is natural:
   sum_i (δ_i^2 / σ_i^2).
   Writing that in matrix form gives δ^T Σ^{-1} δ when Σ = diag(σ_i^2).
   3.2) For non-diagonal Σ (correlations between features),
   Σ^{-1} generalizes the “divide by variance” idea 
   while also accounting for correlations (cross terms).
   Intuitively, directions of high variance get downweighted 
   (large σ → small 1/σ → smaller contribution), 
   and correlated coordinates are adjusted 
   so we measure independent effective displacement.

4. GEOMETRIC INTERPRETATION (whitening → Euclidean length)
   4.1) Since Σ is symmetric positive definite,
   there exists an invertible square root 
   or Cholesky factor L with Σ = L L^T 
   (L can be lower triangular).

   4.2) Let z = L^{-1} δ. Then
   q = δ^T Σ^{-1} δ = δ^T (L^{-T} L^{-1}) δ =
   (L^{-1} δ)^T (L^{-1} δ) = z^T z = ||z||_2^2.
   
   4.3) So q is the squared Euclidean norm of δ 
   after applying the linear transform L^{-1}.
   That transform “whitens” the data: 
   it rescales and rotates so the covariance
   becomes identity.
   Thus q measures the
   Euclidean squared length in whitened space.
   This is the core reason Σ^{-1} appears.

5. SPECTRAL VIEW 
   (eigen-decomposition, component contributions)
   5.1) Eigen-decompose Σ = Q Λ Q^T 
   with orthogonal Q and 
   diagonal Λ = diag(λ₁,...,λ_n) (λ_i > 0).
   5.2) Put δ in that basis: u = Q^T δ 
   (components along eigenvectors).
   5.3) Then q = u^T Λ^{-1} u = Σ_i (u_i^2 / λ_i).
   5.4) Interpretation: 
   each component u_i (projection of δ onto eigenvector i)
   contributes u_i^2/λ_i. Large λ_i (direction of large variance)
   reduces that component’s contribution; small λ_i amplifies it.

6. ILLUSTRATIVE 2×2 NUMERICAL EXAMPLE (detailed arithmetic)
   6.1) Let x = [2, 1]^T, y = [0, 0]^T 
   (so δ = x − y = [2,1]^T).
   6.2) Let Σ = [[4, 1.2], [1.2, 1]].
   6.3) Compute det(Σ) = 
   4·1 − 1.2² = 4 − 1.44 
   = 2.56 (nonzero → invertible).
   6.4) Inverse formula for 2×2:
   Σ^{-1} = (1/det) * [[c, -b], [-b, a]]
   where Σ = [[a,b],[b,c]].
   Here a=4, b=1.2, c=1 → Σ^{-1} =
     (1/2.56) * [[1, -1.2], 
                 [-1.2, 4]].
   Numerically Σ^{-1} = 
   [[0.390625, -0.46875], [-0.46875, 1.5625]].
   6.5) Multiply Σ^{-1} δ:
   Σ^{-1} δ = [0.390625*2 + (-0.46875)*1,
   -0.46875*2 + 1.5625*1]
   = [0.78125 - 0.46875, -0.9375 + 1.5625]
   = [0.3125, 0.625].
   6.6) Compute q = δ^T (Σ^{-1} δ) =
   2*0.3125 + 1*0.625 = 0.625 + 0.625 = 1.25.
   6.7) So the squared Mahalanobis distance 
   q = 1.25; the Mahalanobis distance is
   sqrt(1.25) ≈ 1.1180.
   6.8) Compare Euclidean: ||δ||₂² = 2² + 1² = 5;
   ||δ||₂ ≈ 2.236. The Mahalanobis distance is 
   smaller because the covariance structure 
   reduces the effective distance along directions
   of larger variance.

7. PRACTICAL COMPUTATION (do NOT invert Σ explicitly)
   7.1) Numerically, directly computing Σ^{-1} and
   then multiplying is less stable and slower. 
   Better methods:
   a) Cholesky: compute L such that Σ = L L^T 
   (L lower triangular). 
   Solve L z = δ for z (forward substitution), 
   then solve L^T w = z for w (back substitution);
   q = δ^T w = z^T z. 
   Simpler: solve L u = δ and
   q = ||u||₂² where u = L^{-1} δ.
   b) Use linear solver: compute v by solving Σ v = δ 
   (e.g., using a stable solver), then q = δ^T v.
   7.2) In code (NumPy style, without forming inverse):
   import numpy as np
   delta = x - y

   # Option A: using solve

   v = np.linalg.solve(Sigma, delta)     
   # solves Sigma v = delta
   q = float(delta.dot(v))

   # Option B: using Cholesky

   L = np.linalg.cholesky(Sigma)         
   # Sigma = L @ L.T
   u = np.linalg.solve(L, delta)         
   # u = L^{-1} delta
   q = float(u.dot(u))                   
   # squared Mahalanobis

8. EFFECTS OF COVARIANCE STRUCTURE (intuition)
   8.1) If features are highly correlated, 
   Σ has off-diagonal terms; Σ^{-1} introduces 
   cross terms that subtract correlated deviations 
   so that moving along a correlated direction
   doesn’t increase distance as much.
   8.2) If one direction has tiny variance (λ small),
   even a small projection u_i produces a big u_i^2/λ_i contribution —
   that direction is “important” and deviations there are rare/meaningful.
   8.3) If Σ has very large eigenvalues 
   (directions with huge variance), 
   differences in those directions contribute little to q.

9. CONNECTIONS & USES (brief)
   9.1) q appears in the exponent of 
   multivariate Gaussian density: 
   p(x) ∝ exp(−½ q). 
   So q quantifies how unlikely x is under N(y, Σ).
   9.2) In statistics, q is used to detect outliers: 
   large q → point far from the distribution center
   relative to covariance.
   9.3) In optimization, the gradient wrt x is 
   ∇_x q = 2 Σ^{-1} (x − y). 
   That can be used in learning algorithms.

10. HANDLING SINGULAR OR NEAR-SINGULAR Σ
    10.1) If Σ is singular (some eigenvalues 0), 
    Σ^{-1} does not exist. Then:
    a) Work in the subspace where Σ is positive 
    (use pseudo-inverse Σ^+ and 
    interpret distances only in that subspace).
    b) Regularize: Σ_reg = Σ + ε I (ε > 0 small);
    then use Σ_reg^{-1}.
    10.2) When sample size < dimension, 
    empirical Σ is often singular—use shrinkage estimators 
    (Ledoit–Wolf, etc.) 
    before computing Mahalanobis distances.

11. SUMMARY
    11.1) (x − y)^T Σ^{-1} (x − y) = 
    squared length of x − y after whitening by Σ^{-1/2} 
    (or equivalently L^{-1} where Σ = L L^T).
    11.2) Σ^{-1} rescales and removes correlation,
    turning covariance geometry into Euclidean geometry.
    11.3) Compute q robustly via solving linear systems 
    (Cholesky or solver) rather than explicit inversion.
    11.4) Interpret component contribution via eigenvalues:
    contribution = sum (projection² / eigenvalue).
"""

"""
# ✔ FACT: An SPD matrix transforms *any* vector 
# only through its eigenvector directions
==================

For any SPD matrix ( Σ ) and any vector ( v ):

Σ v = Σ_i λ_i ⟨v, e_i⟩ e_i

This states:
⟨v, e_i⟩ = projection of v onto eigenvector e_i
λ_i = eigenvalue
each component is scaled and recombined 
along the same eigenvector directions

This means:

* ( v ) is decomposed using only 
the eigenvectors (e_1,...,e_n)
* Each part is scaled by 
the corresponding eigenvalue (  λ_i )
* The output ( Σ v ) is a mixture of those same 
eigenvectors and no others
* No new directions appear

So > An SPD matrix cannot create components 
outside its eigenvector directions.

This is true not because SPD matrices are special,
but because all real symmetric matrices admit
a basis of orthogonal eigenvectors.

SPD matrices are a *subset* of symmetric matrices
with the additional property λᵢ > 0.

==================
# ✔ WHY no other directions appear?

Because symmetric matrices 
have orthogonal diagonalization:

Σ = Q  λ Q^T

Where:

* Q is an orthonormal basis (eigenvectors)
* Λ is diagonal (eigenvalues)

So:
Σ v = Q  λ Q^T v

Meaning:

1. Qᵀ v → expresses v entirely in the eigenvector basis
2. Λ (Qᵀ v) → scales each eigen-basis component
3. Q (…) → recombines those eigenvectors,
 still only using eigenvectors

At no point does the matrix introduce a direction outside
the span of the eigenvectors 
— because the eigenvectors *already* form 
the entire basis of ℝⁿ.

==================
# ✔ Very simple analogy

Think of eigenvectors as “the native axes” of the matrix.
Any vector you feed the matrix gets translated into that
coordinate system, stretched along those axes,
and then translated back.

So the transformation always stays inside
that eigenvector system.

==================
# ✔ Important subtlety (but essential)

The output does not necessarily point 
purely in one eigenvector direction, unless:

* v is itself an eigenvector, OR
* it has nonzero component only along
one eigenvector
Usually v has parts along 
multiple eigenvectors, so the result is 
a *combination* of eigen-directions:
[
Σ v =  λ_1 c_1 e_1 +  λ_2 c_2 e_2 + ....
]

But the space of directions is limited 
to those eigenvectors 
— the matrix cannot “invent” new ones.


==================
# ✔ Tiny numeric illustration

Given:

e1 = [ 1,  1 ] / √2
e2 = [ 1, -1 ] / √2

Any vector v = [a, b] 
can be written uniquely as:

v = c1 * e1 + c2 * e2

Then:

Σ v = λ1*c1 * e1  +  λ2*c2 * e2

No third direction. 
No arbitrary mixing.
Only scaled eigenvectors.

==================

# ✔ Final statement
> A0ny general vector multiplied by 
an SPD matrix is transformed ONLY 
by scaling its components along 
the eigenvectors of the SPD matrix.
> No other directions are introduced.
> This is a fundamental consequence of
the fact that SPD (and all symmetric)
matrices possess an orthonormal eigenbasis.
"""


"""
What happens when a symmetric matrix Σ 
acts on a general vector v by decomposing v 
into eigenvector components, 
scaling each component, and recombining.

CHOSEN MATRICES AND VECTOR

Σ = [ 2  1 ]
    [ 1  2 ]

v = [ 3 ]
    [ 1 ]


Σ is symmetric. We will:

1. find eigenvectors and eigenvalues of Σ
2. express v in the eigenvector basis 
(find coefficients)
3. scale each coefficient by its eigenvalue
4. recombine to get Σ v
5. verify by direct multiplication


1. EIGEN-DECOMPOSITION (analytical)

Solve det(Σ − λI) = 0:

| 2−λ   1   |
|  1   2−λ  | = (2−λ)^2 − 1 = λ^2 − 4λ + 3 = 0
Roots: λ = 3, 1

Eigenvalue λ1 = 3  → eigenvector e1 proportional to [1, 1]
Eigenvalue λ2 = 1  → eigenvector e2 proportional to [1, −1]

Normalize to unit length:

e1 = (1/√2) [ 1,  1 ]^T
e2 = (1/√2) [ 1, −1 ]^T

So Q = [ e1 | e2 ] = (1/√2) [ [1, 1], [1, −1] ]
Λ = diag(3, 1)

2. PROJECT v ONTO EIGENVECTORS (compute coefficients)

c = Q^T v   (coordinates of v in eigenbasis)

Compute c1 = e1^T v = (1/√2) * (3 + 1) = 4 / √2 = 2√2
Compute c2 = e2^T v = (1/√2) * (3 − 1) = 2 / √2 = √2

So v = c1 * e1 + c2 * e2
   = (2√2)*e1 + (√2)*e2

(You can verify by recombining:
(2√2)*(1/√2)[1,1] + (√2)*(1/√2)[1,−1] 
= 2[1,1] + 1[1,−1] 
= [3,1] = v.)


3. APPLY Σ TO v VIA EIGENCOMPONENTS 
(scale each component)

Σ v = c1 * λ1 * e1 + c2 * λ2 * e2

Compute scalar multiples:

c1 * λ1 = (2√2) * 3 = 6√2
c2 * λ2 = (√2) * 1 = √2

Now multiply by e1, e2:

c1*λ1*e1 = 6√2 * (1/√2) [1, 1] = 6 [1, 1]
c2*λ2*e2 =  √2 * (1/√2) [1, −1] = 1 [1, −1]

Sum:
Σ v = [6, 6] + [1, −1] = [7, 5]

4. DIRECT MATRIX MULTIPLICATION 
(verification)

Σ v = [ 2 1 ] [3] = [ 2*3 + 1*1 ] = [7]
      [ 1 2 ] [1]   [ 1*3 + 2*1 ]   [5]
Matches the result from 
eigen-decomposition: [7, 5].


5. INTERPRETATION / TAKEAWAYS

• Decomposition view: 
  Σ acts by (i) projecting v onto 
  principal directions (eigenvectors),
  (ii) scaling each projection by 
  the corresponding eigenvalue (amount of stretch),
  (iii) recombining.

• Numerically: 
  v had large component along 
  e1 (c1 = 2√2) and 
  smaller along e2 (c2 = √2).
  Since λ1 = 3 (larger),
  the e1-component got amplified more 
  (6√2 before re-normalizing),
  producing the final Σv = [7,5].

• Geometric intuition: Σ stretches the space 
  most along e1 (direction [1,1]),
  so a vector with large projection on [1,1]
  gets stretched a lot in that direction.

• This example shows explicitly 
  "what happens when Σ acts on a general vector":
  it doesn't simply scale the vector uniformly —
  it scales different directional components differently.

"""

"""
# 1. What eigen-decomposition *means*

==================
For a symmetric matrix like a covariance matrix Σ,
eigen-decomposition says:

Σ = Q  λ Q^T

Where:

* Q = matrix whose columns are eigenvectors
* Λ = diagonal matrix of eigenvalues
* Qᵀ = inverse of Q (because Q is orthogonal)

This decomposition says:

> The matrix Σ acts on space by stretching along
 special directions (eigenvectors), 
 with stretch amounts (eigenvalues).

==================
# 2. What happens when Σ acts on a *unit vector*?

Take a unit vector (u).
Applying Σ gives: Σ u

If u happens to be an eigenvector, then:

Σ u =  λ u

Meaning:

* Σ does not rotate u
* It only stretches it by λ
* That direction is special 
because it remains on the same line

That’s what eigenvectors *are*:

> Directions that Σ scales but does not rotate.

==================
# 3. What happens when Σ acts on a *general vector*?

A general vector v is *not* an eigenvector.
But v can be expressed as a combination of eigenvectors:

v = c_1 e_1 + c_2 e_2 + ... + c_n e_n
Then:
Σ v = c_1  λ_1 e_1 + c_2  λ_2 e_2 + ...

Meaning:

* Σ decomposes v into its eigenvector components
* Then scales each component separately
* And adds them back

So Σ acting on a vector = 
stretch along eigen-directions + recombination.


==================
# 4. What does eigen-decomposition mean
when applied to a *matrix*?

When we say: 
Σ = Q  λ Q^T

we are saying:

> Σ can be viewed as:
> 1. Rotate space so axes line up with eigenvectors 
 (apply (Q^T))
> 2. Scale each axis independently 
(apply diagonal Λ)
> 3. Rotate back to original coordinate system
 (apply Q)

This is the geometric meaning when applied to the whole matrix.

# In steps:
1. (Q^T) rotates your coordinate system to
eigenvector coordinates
2. ( λ) stretches space along each axis by λ₁, λ₂, …
3. (Q) rotates back to original space

So Σ is a combination of rotation → scaling → rotation back.

==================
# 5. Why this matters (especially for Mahalanobis distance)

Mahalanobis distance uses Σ⁻¹:

[
Σ^{-1} = Q  λ^{-1} Q^T
]

This means:

1. Rotate δ (x−μ) into eigenvector space
2. Scale each component by 
1 / eigenvalue (inverse variance)
3. Rotate back
4. Compute Euclidean length

So eigen-decomposition explains:

* Why Mahalanobis distance 
weights directions differently
* Why correlated directions contribute less
* Why low-variance directions contribute more

Because it’s computing distance
after whitening the space.

==================
# 6. Shorter intuition

Eigenvectors ≈ 
directions where Σ acts “cleanly” 
(just scaling, no rotation)
Eigenvalues ≈ amount of stretching
Eigen-decomposition of Σ = a recipe for 
understanding its entire geometric effect

The decomposition isn’t only about unit vectors —
it describes how Σ transforms all vectors by breaking
the transformation into simpler parts.
"""


"""
Σ⁻¹ is directly related to 
the eigenvalues and eigenvectors of Σ, 
and this connection is very important to
understand how Mahalanobis distance 
measures distance in multivariate space. 
Let me break it down step by step in a simple, intuitive way.

 1) Eigen-decomposition of Σ

Any symmetric positive definite
covariance matrix Σ can be decomposed as:

Σ = Q  λ Q^T

where:

* (Q) is an orthogonal matrix whose 
columns are the eigenvectors of Σ
* ( λ = diag( λ_1,  λ_2, ...,  λ_n)) is
 a diagonal matrix of eigenvalues (( λ_i > 0))
* Geometrically: eigenvectors show the
 principal directions of variance, e
 igenvalues show the amount of variance 
 along each direction

 2) Expressing Σ⁻¹ using 
# eigenvectors and eigenvalues

Since Σ is SPD, 
its inverse can be written as:

Σ^{-1} = Q  λ^{-1} Q^T

where ( λ^{-1} =
 diag(1/ λ_1, 1/ λ_2, ..., 1/ λ_n)).

Implications:

* The eigenvectors of Σ⁻¹ are the same as Σ
* The eigenvalues of Σ⁻¹ are 
the reciprocals of the eigenvalues of Σ

3) Why this matters for Mahalanobis distance

Mahalanobis distance:

d^2 = (x - μ)^T Σ^{-1} (x - μ)

Using eigen-decomposition:

1. Let δ = x − μ
2. Transform into eigenvector coordinates:
(y = Q^T δ)
3. Then
d^2 = δ^T Q  λ^{-1} Q^T δ = 
y^T  λ^{-1} y = 
sum_{i=1}^n  y_i^2 / λ_i


Interpretation:

* Project δ along principal axes 
(eigenvectors)
* Scale by 1/λ_i 
(inverse variance along that axis)
* Directions with high variance
 (large λ_i) → contribute less
* Directions with low variance
 (small λ_i) → contribute more

This is exactly why Mahalanobis distance is
scale- and correlation-aware.

4) Geometric intuition

1. Σ defines a multivariate ellipse 
(or ellipsoid in higher dimensions) 
of constant density around μ
2. Eigenvectors: directions of the ellipsoid’s axes
3. Eigenvalues: lengths of the axes (√λ_i)
4. Σ⁻¹ “inverts” the ellipse: 
long axes contribute less, short axes contribute more
5. Mahalanobis distance measures distance 
in this transformed space, effectively “whitening” the data

5) Quick numeric example

Let Σ = [[4,0],[0,1]]

* Eigenvectors: standard axes
* Eigenvalues: λ1=4, λ2=1
* Σ⁻¹ = [[1/4,0],[0,1/1]] =
[[0.25,0],[0,1]]

Point δ = [2,1]:

d^2 = δ^T Σ^{-1} δ = 
2^2*0.25 + 1^2*1 = 1 + 1 = 2

* Along axis 1 (variance=4),
deviation 2 contributes only 1 (downweighted)
* Along axis 2 (variance=1),
deviation 1 contributes 1 (full)

# Summary

1. Σ⁻¹ shares eigenvectors with Σ; 
eigenvalues are reciprocals
2. Mahalanobis distance projects δ 
along principal axes and scales 
by 1/variance along each axis
3. This is why the distance accounts 
for variance and correlation naturally
4. Intuitively: Σ⁻¹ “reshapes” space 
so that Euclidean distance in 
whitened coordinates = Mahalanobis distance
"""


"""
1. Covariance (2D), parameters:
   Σ = [[σ1^2,   ρ*σ1*σ2],
            [ρ*σ1*σ2,   σ2^2]]
   with -1 < ρ < 1

det(Σ) = σ1^2 σ2^2 (1 - ρ^2)

Σ^{-1} = (1 / (σ1^2 σ2^2 (1 - ρ^2))) *
[[σ2^2,   -ρ*σ1*σ2],
 [-ρ*σ1*σ2,   σ1^2]]

2. Mahalanobis squared for x = (x1, x2) and mean 0:
   dM^2(x) = x^T Σ^{-1} x

Compute numerator N = x^T (unscaled matrix) x:
N = x1*(σ2^2 x1 - ρ*σ1*σ2 x2)
    +
    x2*(-ρ*σ1*σ2 x1 + σ1^2 x2)
  = 
  σ2^2 x1^2 - 
  2 ρ σ1 σ2 x1 x2 +
  σ1^2 x2^2

Therefore
dM^2(x) = N / (σ1^2 σ2^2 (1 - ρ^2))

Divide numerator and denominator by 
σ1^2 σ2^2 to expose scaled terms:

dM^2(x) = 
(1 / (1 - ρ^2)) 
( x1^2 / σ1^2 
- 2 ρ x1 x2 / (σ1 σ2) 
+ x2^2 / σ2^2 
)

3. The correlation term (exact place ρ appears):
   The only ρ-dependent pieces are:
   a) the global scale factor 1 / (1 - ρ^2)
   b) the cross term - 2 ρ x1 x2 / (σ1 σ2)

Isolated middle term (inside parentheses):

* 2 ρ x1 x2 / (σ1 σ2)

Interpretation:

* If ρ > 0 and x1, x2 have same sign, 
the middle term is negative and reduces dM^2.
* If ρ > 0 and x1, x2 have opposite signs, 
the middle term is positive and increases dM^2.
* The factor 1/(1-ρ^2) slightly amplifies 
the whole expression (important for large |ρ|).

4. Numeric check (matches earlier example):
   Let σ1 = σ2 = 2  (so variances = 4)
   Let ρ = 3/4 = 0.75
   Let x1 = x2 = 3

Compute inside parentheses:
x1^2 / σ1^2 = 9 / 4
x2^2 / σ2^2 = 9 / 4
-2 ρ x1 x2 / (σ1 σ2) 
= -2 * 0.75 * 9 / 4 = -13.5 / 4

Sum = 9/4 + 9/4 - 13.5/4 =
18/4 - 13.5/4 = 4.5/4 = 18/16 = 9/8  
(keep fractional steps below)

Now 1 / (1 - ρ^2) =
1 / (1 - 0.75^2) = 
1 / (1 - 0.5625) = 
1 / 0.4375 = 16/7

Thus dM^2 =
(16/7) * (18/16) = 18/7

So dM = sqrt(18/7) ≈ 1.603
(Which equals the manual result 18/7
under the square root.)

final scalar formula:
dM^2 = 
(1/(1-ρ^2)) 
(x1^2/σ1^2 - 2ρ x1 x2/(σ1σ2) + x2^2/σ2^2)

---




"""