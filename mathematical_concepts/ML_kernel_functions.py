"""
Short SVM note (one line)
A support-vector machine (SVM) in its dual form uses 
only inner products between data points; a kernel is a 
function that computes an inner product in some feature space 
so the SVM can operate as if it worked in that space 
without explicitly mapping data there.

1. What a kernel is — precise definition
   A kernel K is a function K: X × X → R  (X is the input space, e.g. R^d)
   with the property that there exists a (possibly infinite-dimensional)
   Hilbert space H and a mapping φ: X → H such that
   K(x,z) = ⟨φ(x), φ(z)⟩_H for every x,z in X. When such φ exists 
   we call K a positive-definite kernel or reproducing kernel.
   The mapping φ is called a feature map and
   H is the associated feature space or RKHS.

2. Two basic, necessary properties you must check
   (a) Symmetry:
    K(x,z) = K(z,x) for all x,z.
   (b) Positive semidefiniteness (PSD) on every finite set:
    For any finite set {x1,...,xn} and any vector c in R^n,
    c^T K c = sum_{i,j=1}^n c_i c_j K(x_i,x_j)  >=  0.
    Here K denotes the n×n Gram matrix with entries 
    K(x_i,x_j). PSD is the key property that characterizes
    kernels that come from inner products.

Proof that an inner-product kernel is PSD (short, exact)
Assume K(x,z)=⟨φ(x),φ(z)⟩*H.
Let c = (c1,...,cn) in R^n. Then
c^T K c = sum*{i,j} c_i c_j ⟨φ(x_i), φ(x_j)⟩
= ⟨ sum_i c_i φ(x_i) , sum_j c_j φ(x_j) ⟩
= || sum_i c_i φ(x_i) ||_H^2  >= 0.
Thus any valid kernel generates PSD Gram matrices.

3. Closure properties — how to build new kernels from old
(useful, proven facts)
   If K1 and K2 are kernels on X, then:

* For any α >= 0, α K1 is a kernel.
* K1 + K2 is a kernel (sum preserves PSD).
* K1 * K2 (pointwise product) is a kernel 
(Schur product theorem + feature map argument).
* If f: X → R and h(x) = f(x) is any function,
then K(x,z) = h(x) h(z) is a kernel (rank-1 kernel).
* If {Km} is a sequence of kernels and
 Km → K pointwise with nonnegative coef. limits in
 an appropriate series expansion, K can be a kernel 
 (pointwise limit under conditions).
 These follow from the fact that PSD matrices are closed
 under positive scaling, addition, and the Schur (elementwise) product,
 and multiplication by h(x)h(z) corresponds to similarity transform 
 by diagonal matrix.

4. Practical ways to test whether a function K is a kernel
   Method A (finite test): For any finite sample {x1,...,xn},
   compute Gram matrix K_ij = K(x_i,x_j). Check K is symmetric
   and all eigenvalues ≥ 0 (or attempt Cholesky decomposition).
   If this holds for arbitrary finite sets, K is PSD.
   Method B (construct φ): Exhibit an explicit φ mapping and
   show K(x,z)=⟨φ(x),φ(z)⟩. This proves K is a kernel.
   Method C (closure rules): Express K as sums/products/positive scalings
   of known kernels. If you can write K as compositions
   from known kernels (linear, polynomial, Gaussian, etc.) 
   using closure operations, K is valid.
   Method D (series expansion): Express K as ∑_{k} α_k K_k 
   where α_k ≥ 0 and each K_k is a PSD kernel; then K is PSD.

5. Concrete kernels and why they are kernels

5.1 Linear kernel
K(x,z) = x^T z.
Feature map: φ(x)=x (H = R^d). Gram = X X^T. PSD obvious.

5.2 Polynomial kernel (homogeneous)
K(x,z) = (x^T z)^d   (d positive integer)
Feature map: all monomials of degree d.
Example d = 2 with x in R^2:
K(x,z) = (x1 z1 + x2 z2)^2
= x1^2 z1^2 + 2 x1 x2 z1 z2 + x2^2 z2^2.
So φ(x) = (x1^2, sqrt(2) x1 x2, x2^2).
Check ⟨φ(x),φ(z)⟩ equals K(x,z).
General d: φ(x) contains all degree-d monomials 
(with appropriate combinatorial √coefficients).
Finite-dimensional, PSD.

5.3 Polynomial kernel with bias and scale
K(x,z) = (γ x^T z + c)^d, with γ>0, c≥0.
This expands via binomial theorem into 
nonnegative-weighted sums of (x^T z)^k terms,
each PSD; therefore the whole kernel is PSD.

5.4 Gaussian RBF kernel (very common)
K(x,z) = exp(-||x - z||^2 / (2 σ^2))
or  K(x,z) = exp(-γ ||x - z||^2), γ>0.
Two short proofs that it is PSD:

Proof via product and power series decomposition
(elementary, constructive):
Start from the identity
||x - z||^2 = ||x||^2 + ||z||^2 - 2 x^T z.
Then
K(x,z) = exp(-γ ||x - z||^2)
= exp(-γ ||x||^2) * exp(-γ ||z||^2) * exp(2γ x^T z).
(Here exp(-γ||x||^2) is a scalar function of x only.)
Now expand the last factor using the exponential series:
exp(2γ x^T z) = sum_{k=0}^∞ (2γ)^k / k! * (x^T z)^k.
Each kernel (x^T z)^k is PSD (polynomial kernel of degree k).
A nonnegative weighted sum (coefficients (2γ)^k / k! > 0) of
PSD kernels is PSD. Finally, multiplying a PSD kernel by 
h(x) h(z) with h(x)=exp(-γ||x||^2) preserves PSD because Gram
is D K0 D where D is diagonal with entries h(x_i). Thus K is PSD.
Therefore Gaussian RBF is a valid kernel. (This is a constructive
proof showing an explicit expansion; it avoids advanced Fourier/Bochner
machinery but is equivalent in spirit.)

Alternative standard proof uses Bochner’s theorem: a continuous,
shift-invariant kernel K(x,z)=ψ(x−z) is positive definite iff ψ is
the Fourier transform of a nonnegative measure. The Gaussian’s Fourier 
transform is Gaussian (positive), so the kernel is PSD. This uses Fourier
analysis and is standard in theory references.

5.5 Sigmoid kernel (tanh)
K(x,z) = tanh(α x^T z + c).
This resembles one layer of a neural net. It is not universally PSD for 
all α,c; for some parameter ranges it is PSD but for others it is not.
You cannot assume it is a kernel unless you verify PSD for your parameter
choice or your solver supports indefinite kernels.

6. Worked example: polynomial kernel degree 2 in general d, explicit φ and dimension
   Let x ∈ R^d. Consider K(x,z) = (x^T z)^2.
   Expand: (x^T z)^2 = sum_{i=1}^d sum_{j=1}^d x_i x_j z_i z_j.
   The feature map φ(x) can be taken as all pairwise products x_i x_j, but to get 
   an orthonormal-like scaling you usually take:

* For i = j: component sqrt(1) * x_i^2.
* For i < j: component sqrt(2) * x_i x_j.
  Then φ(x) has dimension m = d(d+1)/2. Check ⟨φ(x),φ(z)⟩ reproduces (x^T z)^2.

Worked numeric demonstration (small d=2)
x = (x1,x2), z=(z1,z2).
K(x,z) = (x1 z1 + x2 z2)^2
= x1^2 z1^2 + 2 x1 x2 z1 z2 + x2^2 z2^2.
Take φ(x) = (x1^2, sqrt(2) x1 x2, x2^2).
Compute inner product:
⟨φ(x),φ(z)⟩ = x1^2 z1^2 + 2 x1 x2 z1 z2 + x2^2 z2^2 = K(x,z).
This is exact and finite-dimensional.

7. Concrete toy example: XOR and degree-2 polynomial kernel (worked)
   Data: four points in R^2:
   A = (1,1) label +1
   B = (-1,-1) label +1
   C = (1,-1) label -1
   D = (-1,1) label -1
   These are not linearly separable in R^2. Map by φ(x) = (x1^2, √2 x1 x2, x2^2).
   Compute mapped points:
   φ(A) = (1, √2, 1)      label +1
   φ(B) = (1, √2, 1)      label +1  (same as A)
   φ(C) = (1, -√2, 1)     label -1
   φ(D) = (1, -√2, 1)     label -1
   Now classes are separated by the sign of the second coordinate of φ: 
   if second coordinate > 0 then +1, else -1. So a linear separator exists
   in φ-space. The polynomial kernel (x^T z)^2 computes inner products in 
   that space without explicitly forming the 3-dimensional vectors.

8. Gram matrix example and PSD check (explicit small Gram)
   Take three points in R^2: x1=(1,0), x2=(0,1), x3=(1,1).
   Use polynomial degree 2 kernel K(x,z)=(x^T z)^2.

   Compute K:
   K11 = (1*1 + 0*0)^2 = 1
   K22 = (0*0 + 1*1)^2 = 1
   K33 = (1*1 + 1*1)^2 = 4
   K12 = (1*0 + 0*1)^2 = 0
   K13 = (1*1 + 0*1)^2 = 1
   K23 = (0*1 + 1*1)^2 = 1
   Gram matrix K =
   [1 0 1
   0 1 1
   1 1 4]
   Check PSD: compute eigenvalues or check quadratic form.
   One quick check: for any vector c=(c1,c2,c3),
   c^T K c = || sum_i c_i φ(x_i) ||^2 >= 0 by feature-map proof.
   Numerically the eigenvalues are positive (approx values: one
   small positive, others larger), so PSD holds.

9. Representer-type consequence (short)
   For many regularized learning problems in RKHS with kernel K,
   the optimal solution can be written as a finite linear combination
   of kernel evaluations at training points:
   f*(·) = sum_{i=1}^n α_i K(x_i, ·).
   This explains why kernel methods produce decision functions built
   from kernels centered at data points (support vectors in SVMs).

10. More on intuition: what kernels "do"

* A kernel defines similarity. K(x,z) large → x and z are similar
in the feature space induced by K.
* Different kernels encode different notions of similarity:

  * Linear: similarity by dot product (angle and magnitude).
  * Polynomial: similarity by matching low- or 
  higher-order interactions (products of features).
  * RBF: similarity by proximity; decays with Euclidean distance.
* The effective capacity (complexity) of the model depends on the
kernel choice and its hyperparameters (degree d, γ for RBF, etc.).
RBF corresponds to an infinite-dimensional feature space and
can represent very complex boundaries; polynomial kernels of
low degree produce simpler decision surfaces.

11. When a kernel might be invalid or problematic

* If K is not symmetric or Gram matrices are not PSD,
optimization problems that assume convexity (like SVM dual)
can fail or become non-convex.
* Numerical issues: even valid kernels can produce Gram matrices
 that are ill-conditioned (very small eigenvalues),
 causing numerical instability. 
 Regularization (adding small λ to diagonal) is common: replace K by K + λ I.

12. How to choose and tune kernels (practical rules)

* Start with linear kernel for high-dimensional,
 linearly separable or roughly linear problems.
* Use RBF as a default when you expect locality/smoothness;
 tune γ (or σ) and regularization C.
* Use polynomial if you suspect explicit polynomial interactions
 matter; low degree (2 or 3) often suffices.
* Cross-validate kernel hyperparameters on held-out data.
* Scale/standardize features before using RBF or polynomial
kernels: feature scales affect distances and inner-products.

13. Summary checklist for verifying or building a kernel

* Symmetry: check K(x,z) = K(z,x).
* PSD on samples: compute Gram matrix on varied finite samples,
 check eigenvalues ≥ 0 (or attempt Cholesky).
* If you can express K as combinations (sum, product, positive scale)
 of known kernels, it is valid.
* If you can exhibit φ such that K(x,z)=⟨φ(x),φ(z)⟩, you are done.
* Remember special-case kernels like tanh may fail PSD — verify before using.

14. Final concise proofs offered in this text

* Proof that inner-product kernels yield PSD Gram matrices (given in section 2).
* Elementary constructive proof that Gaussian RBF is PSD using series expansion
 and the product decomposition (section 5.4).
* Explicit derivation of φ for polynomial kernel degree 2 and the XOR separability
 example (sections 6 and 7).

If you want, next I can:
• give more worked-out numerical examples (explicit α solving or small QP)
 using a chosen kernel;
• produce plain ASCII code (Python/numpy) that computes Gram matrices and
 tests PSD for arbitrary K;
• or provide a short list of exercises with answers to test your understanding.

Tell me which of those (if any) you want, and I’ll include it as raw text as well.


"""