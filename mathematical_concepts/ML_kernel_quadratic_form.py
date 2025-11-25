"""
DOT PRODUCT KERNELS,
KERNEL MATRIX COEFFICIENTS,
QUADRATIC FORMS, AND PSD

This document covers:

1. Dot product kernels
2. Kernel (Gram) matrix example and coefficients
3. Why coefficient groupings arise
4. Why αᵀKα is introduced
5. Why cross-term expressions (α₁α₂K₁₂) are still quadratic
6. Geometry of quadratic forms, PSD, eigenvalues, and ellipses

--
## 1. What is a dot-product kernel?

A **dot-product kernel** is any kernel of the form:
K(x, y) = f(x⋅y)

Examples:
* Linear kernel: K(x, y) = x⋅y
* Polynomial kernel: K(x, y) = (x⋅y + c)ᵈ
* Quadratic special case: K(x, y) = (x⋅y)²

Such kernels implicitly map data into (possibly higher)
feature spaces in which inner products can be computed
through the kernel function.

---

## 2. Example: Kernel (Gram) matrix for a tiny dataset

Take a 2-point dataset:

x₁ = [1, 2]
x₂ = [3, 4]

And use the **quadratic dot-product kernel**:

K(x, y) = (x⋅y)²

Compute dot products:
x₁⋅x₁ = 1·1 + 2·2 = 5
x₁⋅x₂ = 1·3 + 2·4 = 11
x₂⋅x₂ = 3·3 + 4·4 = 25

Square them:
5²  = 25
11² = 121
25² = 625

Thus the Gram matrix is:

K = [  25    121
       121   625 ]

---

### What are “the coefficients” inside the kernel matrix?

Just the **inner-product results** after applying the kernel function.

For quadratic kernel, the entries look like:

Kᵢⱼ = (xᵢ⋅xⱼ)²

The cross term K₁₂ = 121, for instance, comes from:

(1·3 + 2·4)² = 11² = 121.

These numbers are **not** arbitrary; 
they are enforced by the kernel function 
and must yield a **positive semidefinite** matrix.
This automatically guarantees the kernel is valid.

---
## 3. How the coefficients “group” into terms

When you expand (x⋅y)²:

(x₁y₁ + x₂y₂)²
= x₁²y₁² + 2x₁x₂y₁y₂ + x₂²y₂²

The grouping follows **algebraic rules of multiplying sums**.

The kernel matrix entry Kᵢⱼ contains the sum of all such grouped terms.

More generally, the grouping follows the **product rule for polynomials**:

(a + b + c + …)²
→ pairwise products: a² + b² + 2ab + …

This grouping structure is why dot-product kernels 
correspond to polynomial feature mappings.

---

## 4. Why αᵀKα appears and why it matters

αᵀKα appears in SVMs, Gaussian processes,
kernel ridge regression, and all dual formulations.

It comes from rewriting an optimization objective in dual form.

Example: SVM dual objective contains the term:

½ αᵀKα

because:

αᵀKα = (∑ᵢ αᵢ φ(xᵢ)) ⋅ (∑ⱼ αⱼ φ(xⱼ))

This equals the **squared norm of a weighted
combination of mapped data points**:

‖∑ᵢ αᵢ φ(xᵢ)‖² ≥ 0

This explains why kernels must be PSD:

* αᵀKα must always be nonnegative (it is a squared norm)
* Negative value would break convexity,
optimization stability, and violate geometry.

Thus αᵀKα is not optional — 
it is the core of the dual formulation 
and what ensures optimization remains convex.

---

## 5. Why α₁α₂K₁₂ is still quadratic,
# even without squares

Quadratic form:

Q(α) = αᵀKα
= K₁₁ α₁² + 2K₁₂ α₁α₂ + K₂₂ α₂²

A term like α₁α₂ is still **quadratic**,
because:
* “Quadratic” means 
“degree 2 polynomial in the variables”.
* α₁α₂ has total degree 2: 1+1 = 2.

You do **not** need a square like
α₁² to be quadratic.
Mixed terms are still degree-2 monomials.

Thus α₁α₂K₁₂ is part of a quadratic expression.

---
## 6. Why quadratic forms relate to geometry

A symmetric matrix A defines a quadratic form:

Q(α) = αᵀAα

In 2-D:

Q(x,y) = ax² + 2bxy + cy²

This describes conic sections 
(ellipse, hyperbola, parabola).

If A is PSD (all eigenvalues ≥ 0),
then:

{ α | αᵀAα = 1 } is an **ellipse**

If A is indefinite, 
the curve becomes a hyperbola.

The cross term (2bxy):

* causes tilting of the ellipse
* couples x and y
* indicates basis is not aligned
with eigenvectors

---
## 7. Diagonalization removes cross terms

Any symmetric PSD matrix A can be diagonalized:

A = PΛPᵀ

If we rotate coordinates by β = Pᵀα, then:

Q(β) = λ₁ β₁² + λ₂ β₂²

All the cross-terms vanish.

The ellipse becomes axis-aligned
in the eigenvector basis.

Eigenvalues control stretching:

* Large λ = short axis
* Small λ = long axis

---
## 8. PSD condition in terms of eigenvalues

A matrix A is PSD exactly when its eigenvalues satisfy:

λᵢ ≥ 0

This ensures the quadratic form is always non-negative:

αᵀAα = Σ λᵢ βᵢ² ≥ 0.

For kernels:

* Gram matrix K must be PSD
* This ensures it truly represents 
inner products in some feature space
* If K were not PSD, such a feature space
could not exist

Thus PSD = valid kernel.

---

## 9. summary
* Dot-product kernels generate Gram matrices via K(xᵢ, xⱼ).
* These matrices must be PSD to represent legitimate inner products.
* The dual formulation of many learning algorithms introduces αᵀKα.
* This is a quadratic form whose geometry depends on eigenvalues of K.
* Cross terms (e.g., 2K₁₂α₁α₂) are quadratic even though not squared.
* Diagonalizing K removes cross terms and reveals eigenvalue structure.
* PSD kernels correspond to inner-product geometries that form ellipses.
* Non-PSD matrices correspond to impossible geometries and invalid kernels.

In short:
K valid ⇔ K PSD ⇔ αᵀKα ≥ 0 for all α ⇔ 
Realizable feature space ⇔ Sound geometry.

---
2D illustration** showing the Gaussian PDF and RBF kernel intuitively.

### **1D Gaussian PDF (centered at 0)**

```
f(x)
^
|        *
|       * *
|      *   *
|     *     *
|    *       *
|   *         *
|  *           *
+-----------------> x
 -3 -2 -1  0  1  2  3
```

* Peak at 0 (mean μ = 0)
* Decays smoothly as x moves away
* Represents **probability density** of a random variable

---

### **RBF Kernel (similarity to a point at 0)**

```
K(x, 0)
^
|        *
|       * *
|      *   *
|     *     *
|    *       *
|   *         *
|  *           *
+-----------------> x
 -3 -2 -1  0  1  2  3
```

* Peak at x = 0 (point of reference)
* Decays with distance ||x - 0||
* Represents **similarity**: closer points → higher value

---

### **Observation**

* Shape is **identical**: bell curve
* Difference is **meaning**:
  * Gaussian PDF → probability density
  * RBF kernel → similarity measure
* Both use `exp(-distance^2 / scaling)` form

"""