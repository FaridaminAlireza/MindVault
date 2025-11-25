"""
Overview
Kernels and regularization are two central ideas in modern probability,
statistics and machine learning. They often appear separately 
(kernel density estimation, ridge regression) and together 
(kernel ridge regression, smoothing splines, Gaussian processes).

Part A — Kernels

1. What is a kernel?

* Informal: A kernel is a function K(x, y) that measures
similarity between points x and y. Larger values mean more similar.
* Formal (positive-definite kernel): K : X × X → R is positive definite
if for any finite set {x1,...,xn} and any real coefficients c1,...,cn we have
 sum_{i=1}^n sum_{j=1}^n c_i c_j K(x_i, x_j) ≥ 0.
This property ensures many useful mathematical consequences 
(existence of an associated reproducing kernel Hilbert space, or RKHS).

2. Common kernel examples (1D / Euclidean inputs)

* Gaussian (RBF) kernel: K(x,y) = exp(-||x-y||^2 / (2σ^2)).
 Smooth, infinitely differentiable; controlled by length-scale σ.
* Laplace kernel: K(x,y) = exp(-||x-y|| / σ).
* Polynomial kernel: K(x,y) = (x·y + c)^d.
* Linear kernel: K(x,y) = x·y (a special polynomial kernel).
These kernels are widely used in practice;
each induces different notions of similarity and function smoothness.

3. Kernel trick (why kernels are powerful)

* Many algorithms depend only on dot products between features: x·y.
If we map x to a (possibly infinite-dimensional) feature map φ(x),
dot products become φ(x)·φ(y).
* A positive-definite kernel K(x,y) 
equals such a dot product: K(x,y)=φ(x)·φ(y) in some feature space.

We can compute similarities via K without ever computing φ explicitly.
This enables algorithms like kernel SVM, kernel PCA, etc.

4. Reproducing Kernel Hilbert Space (RKHS)

* For a PD kernel K there exists an RKHS H of functions
f: X→R with inner product ⟨·,·⟩_H such that:
  (a) For each x, K(·,x) ∈ H.
  (b) Reproducing property: f(x) = ⟨f, K(·,x)⟩_H for all f∈H.
* Intuition: H is the space of functions that can be “built”
from the kernel; the RKHS norm ‖f‖_H measures function complexity
(roughly how wiggly/large it is in the kernel-induced geometry).

5. Kernel Density Estimation (KDE) — kernels used as weights
   Step-by-step KDE (1D):

1) Suppose we have iid samples x1,...,xn from an unknown density p.
2) Choose a kernel function k(u) (commonly symmetric, integrates to 1,
 e.g., the standard normal density) and a bandwidth h>0.
3) KDE estimator at point x:
   p̂_h(x) = (1/n) ∑_{i=1}^n (1/h) k((x - x_i)/h).
   Equivalently, p̂_h is a sum of bumps centered at each sample;
   h controls bump width.
4) Bandwidth tradeoff:
   * Small h → low bias, high variance; p̂_h follows points closely, may overfit (spikes).
   * Large h → high bias, low variance; p̂_h oversmooths, can miss structure.
5) Asymptotic bias/variance (informal):
   * Bias roughly ∝ h^2 (for smooth densities and symmetric kernels).
   * Variance roughly ∝ 1/(n h).
   * Optimal tradeoff (minimizing mean integrated squared error)
   scales like h ∝ n^{-1/5} in 1D for smooth densities.

Insightful example (KDE with Gaussian kernel):

* Let k(u) = (2π)^{-1/2} exp(-u^2/2). Then
  p̂_h(x) = (1/n) ∑ (1/h) φ((x-x_i)/h)
  where φ is Gaussian pdf. If n=100 and h=0.2,
  each sample contributes a narrow Gaussian; with h=1.5 
  you get much smoother estimate.
* Practical point: bandwidth selection methods include cross-validation
 (likelihood or L2), plug-in rules, and heuristic rules (Silverman’s rule of thumb).

Part B — Regularization

1. Motivation

* In statistical estimation we face the bias–variance tradeoff:
complex models can overfit (low bias, high variance); 
simple models can underfit (high bias, low variance).
* Regularization introduces a penalty on model complexity 
to stabilize estimation and reduce variance, 
often at the cost of a little bias, improving generalization.

2. Classical regularizers

* Ridge (Tikhonov) regression (L2 penalty):
  Given data (X, y), solve min_w ||y - X w||^2 + λ ||w||^2.
  Closed-form solution: ŵ = (X^T X + λ I)^{-1} X^T y.
  Interpretation: shrink coefficients toward zero;
  λ controls shrinkage (λ→0 => OLS; λ→∞ => coefficients→0).
* Lasso (L1 penalty): min_w ||y - X w||^2 + λ ||w||_1.
  L1 produces sparsity (some coefficients exactly zero),
  but no closed-form; use convex optimization.
* Elastic net: combination of L1 and L2 to blend shrinkage + sparsity.

3. Why ridge works (intuition)

* Small eigenvalues of X^T X cause instability in OLS 
(huge variance in directions with little data).
Adding λ shifts eigenvalues up by λ, stabilizing inversion.
* Ridge is equivalent to MAP estimation with Gaussian prior w∼N(0, τ^2 I),
where τ^2 = 1/λ (up to noise variance scaling).

4. Regularization as constrained optimization

* Alternate view: ridge solution solves 
min ||y - X w||^2 subject to ||w||^2 ≤ c. 
This geometric view clarifies how regularization
restricts the feasible set.

5. Smoothing splines and penalized function estimation

* We can estimate a function f by minimizing
  ∑_{i=1}^n (y_i - f(x_i))^2 + λ ∫ (f''(t))^2 dt.
  The penalty ∫(f'')^2 measures curvature; minimizing yields 
  a smooth function that interpolates the data in a balanced way.
  The solution is a natural cubic spline with knots at the x_i’s.
* This is a special case of RKHS regularization:
 the penalty is the RKHS norm for a particular kernel,
 so the representer theorem applies (see next part).

Part C — Where kernels and regularization meet (deep connection)

1. Representer theorem (key step)

* Problem: minimize over f in an RKHS H
  J(f) = L( f(x1),..., f(xn) ) + λ ‖f‖_H^2,
  where L depends only on values f(x_i).
* Representer theorem: any minimizer f* has the form
  f*(·) = ∑_{i=1}^n α_i K(·, x_i).
  So the infinite-dimensional problem reduces to an 
  n-dimensional one in coefficients α = (α1,...,αn).
* This is why kernel methods are practical: 
you only need kernel evaluations K(x_i, x_j).

2. Kernel ridge regression (KRR)
   Step-by-step derivation:

1) Start from RKHS H with kernel K. Minimize
   ∑_{i=1}^n (y_i - f(x_i))^2 + λ ‖f‖_H^2.
2) By representer theorem, f(·)=∑ α_j K(·, x_j).
 Let K be the n×n Gram matrix with K_{ij}=K(x_i,x_j).
3) Define vector f_vals = K α (length n).
 The objective becomes
   ||y - K α||^2 + λ α^T K α.
4) Differentiate w.r.t. α and set to zero:
   -2 K (y - K α) + 2 λ K α = 0  =>  K (K α - y + λ α) = 0.
   If K is positive definite, cancel K:
   (K + λ I) α = y.
5) So α = (K + λ I)^{-1} y, and prediction at new x_* is
   f̂(x_*) = k_*^T α = k_*^T (K + λ I)^{-1} y,
   where k_* = [K(x_*, x_1), ..., K(x_*, x_n)]^T.

Interpretation:

* KRR is ridge regression in feature space φ where K = Φ Φ^T.
* λ controls smoothness/complexity in the RKHS induced by K.
* Computationally, you invert an n×n matrix (K + λ I).

3. Connection to Gaussian processes (GP)

* A Gaussian process with zero mean and covariance function K implies
 that for noise model y_i = f(x_i) + ε_i with ε_i∼N(0, σ^2),
the posterior mean of f at x_* is f_post(x_*) = k_*^T (K + σ^2 I)^{-1} y.
* Compare with KRR: set λ = σ^2 and the KRR predictor equals the GP posterior mean. 
So kernel-based regularization has a probabilistic interpretation: the RKHS penalty
corresponds to a Gaussian prior on functions when careful with scaling.
This explains why kernels encode prior beliefs about smoothness.

4. Example — small KRR numerical illustration (conceptual)

* Data: n=3 points x=[0,1,2] with y=[1,2,1.5].
* Kernel: Gaussian with σ=1. Compute Gram matrix K (3×3), add λ, invert,
 compute α=(K+λ I)^{-1} y, then predict f̂ at new x_* using k_*^T α.
 (This is straightforward linear algebra; numbers omitted here but
 can be computed with any numerical tool.)

5. Smoothing splines as kernel regularization

* The cubic spline penalty ∫(f'')^2 dt corresponds to an RKHS whose kernel
is a particular function (the Green’s function for a differential operator).
Solving the penalized least squares yields the spline, which by representer
theorem is a finite combination of kernel sections K(·, x_i).

Part D — Bias–variance, regularization parameter selection,
and kernel hyperparameters

1. Bias–variance tradeoff in kernel/regression contexts

* Bandwidth h in KDE or length-scale σ in RBF kernel and
penalty λ all control bias-variance.
* Small λ (or small smoothing/big model capacity) → 
low bias, high variance.
Large λ → smoother function, higher bias, lower variance.

2. Tuning methods

* Cross-validation (CV): choose λ and kernel hyperparameters by
minimizing predictive error in held-out folds.
* Generalized Cross-Validation (GCV): 
an efficient, leave-one-out type measure for smoothing problems.
* Marginal likelihood / evidence optimization: 
for Gaussian process models, tune kernel hyperparameters by
 maximizing the marginal likelihood p(y | hyperparameters).
* Information criteria: AIC, BIC for model comparison
(less common than CV for kernel methods).

Part E — More examples and intuitions

1. Kernel PCA

* PCA in feature space using kernel trick: center Gram matrix,
solve eigenvalue problem K v = n λ v; principal components in
feature space are linear combos of K(·, x_i).
Useful for nonlinear dimensionality reduction.

2. Example contrasting KDE and KRR

* KDE estimates density (nonparametric) by averaging
local contributions (no training step besides choosing h).
* KRR estimates regression function from inputs to outputs
by solving regularized least squares in RKHS. Both use kernels
but for different tasks: KDE uses kernel as a local smoother for
densities; KRR uses kernel as basis functions plus regularization.

3. Gaussian process regression example (interpretative)

* If you believe the function is smooth on length-scale ℓ 
(i.e., distant points are weakly correlated), choose RBF with σ=ℓ.
The GP posterior mean gives both a point estimate and a posterior
variance at each x_* (uncertainty estimate); KRR gives the mean but
not the probabilistic variance unless you view it as a GP.

Part F — Practical tips and pitfalls

1. Scaling of inputs matters: For RBF kernels,
features should be on similar scales. Otherwise, 
one dimension dominates the distance.
2. Kernel selection: RBF is a safe default for smooth functions;
polynomial kernels can be useful if you suspect polynomial relationships;
choose based on prior knowledge and validate via cross-validation.
3. Numerical stability: 
Inverting K+λ I can be expensive or ill-conditioned for large n. Remedies:
   * Use Cholesky decomposition.
   * Use low-rank approximations (Nyström, random Fourier features).
   * Use iterative solvers with preconditioning if n is large.
4. Interpretability: Kernel methods (especially with complex kernels) can
be less interpretable than sparse linear models; choose methods aligning with goals.

Appendix — Some derivations and formulae (concise)

1. KDE: p̂_h(x) = (1/n) ∑_{i} (1/h) k((x-x_i)/h).
   Asymptotic MSE tradeoff: Bias ∝ h^2, Var ∝ 1/(n h) => optimal h ∝ n^{-1/5} (1D).
2. Ridge closed form: ŵ = (X^T X + λ I)^{-1} X^T y.
   Equivalent to α solution in KRR: α = (K + λ I)^{-1} y.
3. GP predictive mean: f_post(x_*) = k_*^T (K + σ^2 I)^{-1} y,
predictive variance: var = K(x_*,x_*) - k_*^T (K + σ^2 I)^{-1} k_*.

Concluding intuition

* Kernels define similarity and a geometry on functions (the RKHS);
regularization imposes a penalty that prefers simpler/smoother functions
according to that geometry. Together they let you do flexible nonparametric
estimation while controlling overfitting. Many familiar tools 
(ridge, splines, Gaussian processes, kernel machines) are different faces of 
the same underlying idea: choose a prior or penalty (via a kernel)
and balance data fit against complexity (via λ).

"""