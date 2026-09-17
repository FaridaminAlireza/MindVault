"""
Support Vector Machines can use different kernels depending on the
dataset and the problem: 
- Linear kernel 
- Polynomial kernel 
- Radial Basis Function (RBF) or Gaussian kernel 
- Sigmoid kernel

The RBF kernel is the most commonly used because it handles nonlinear
boundaries well without requiring manual feature engineering.

Understanding the Gaussian (RBF) Kernel
and Its Feature Space:
---

1. The Gaussian Kernel

We start with the Gaussian (RBF) kernel:

K(x, x') = exp(-gamma * ||x - x'||^2)

This kernel measures similarity between two
vectors based on their distance.

---

2. Expanding the Squared Distance

We use a basic identity from vector algebra:

(Based on the defintion of second norm of a vector v,
where v = x - x’)

||x - x'||^2 = (x - x') · (x - x')

Expanding this using distributivity:

= x·x - x·x' - x'·x + x'·x'

Since dot product is symmetric (x·x' = x'·x), we get:

= ||x||^2 + ||x'||^2 - 2 x·x'

This is just the vector version of (a - b)^2 = a^2 + b^2 - 2ab.

---

3. Decomposing the Kernel

Substitute the expansion into the kernel:

K(x, x') = exp(-gamma (||x||^2 + ||x'||^2 - 2 x·x'))

Split the exponential:

= exp(-gamma ||x||^2) * exp(-gamma ||x'||^2) * exp(2 gamma x·x')

This separates the kernel into:

* a term depending only on x
* a term depending only on x'
* a term depending on their dot product

---

4. Expanding the Exponential

Use the Taylor series:

exp(2 gamma x·x') = sum over k=0 to infinity of:
(2 gamma)^k / k! * (x·x')^k

So the kernel becomes an infinite sum of 
terms involving powers of (x·x').

---
5. Why (x·x')^k is a Kernel

A function is a valid kernel if it can be written as:

K(x, x') = <phi(x), phi(x')>

So we must show that (x·x')^k has this form.

---
6. Concrete Examples (d = 2)

Let x = (x1, x2), x' = (x1', x2').

Then: x·x' = x1 x1' + x2 x2'

---
Case k = 1:

(x·x') = x1 x1' + x2 x2'

Feature map:
phi(x) = (x1, x2)

---
Case k = 2:

(x·x')^2 = (x1 x1' + x2 x2')^2

Expand:

= x1^2 x1'^2 + 2 x1 x2 x1' x2' + x2^2 x2'^2

Rewrite the middle term:

2 x1 x2 x1' x2' = (sqrt(2) x1 x2)(sqrt(2) x1' x2')

So:
(x·x')^2 = (x1 x1' + x2 x2')^2 = 
(x1^2)(x1'^2)
* (sqrt(2) x1 x2)(sqrt(2) x1' x2')
* (x2^2)(x2'^2)

Feature map:

phi(x) = (x1^2, sqrt(2) x1 x2, x2^2)

---
Case k = 3:

(x·x')^3 expands to:

= x1^3 x1'^3
* 3 x1^2 x2 x1'^2 x2'
* 3 x1 x2^2 x1' x2'^2
* x2^3 x2'^3

Feature map:

phi(x) = (x1^3, sqrt(3) x1^2 x2, sqrt(3) x1 x2^2, x2^3)

---
7. What Are Monomials?

A monomial is a product of variables raised to powers.

Examples:

* x1
* x1 x2
* x1^2
* x1^2 x2

For degree k, monomials look like:

x1^a x2^b where a + b = k

Examples:
k = 2 → x1^2, x1 x2, x2^2
k = 3 → x1^3, x1^2 x2, x1 x2^2, x2^3

These form the coordinates of the feature map.

---
8. Why the Square Roots Appear

When expanding (x·x')^k, some terms appear
multiple times (due to combinatorics).

We rewrite coefficients like:

c * f(x) * f(x') = (sqrt(c) f(x)) * (sqrt(c) f(x'))

This ensures the expression matches an inner product exactly.

---

9. General Pattern

(x·x')^k = sum over all monomials of degree k:

c_alpha * m_alpha(x) * m_alpha(x')

Define:

phi(x)_alpha = sqrt(c_alpha) * m_alpha(x)

Then:

(x·x')^k = <phi(x), phi(x')>

So it is a valid kernel.

---
10. Why the Gaussian Kernel is Infinite-Dimensional

Recall:

exp(2 gamma x·x') = sum over k=0 to infinity of:
(2 gamma)^k / k! * (x·x')^k

Each k introduces:

* all monomials of degree k

So the feature map includes:

* degree 0: 1
* degree 1: x1, x2, ...
* degree 2: x1^2, x1 x2, ...
* degree 3: x1^3, x1^2 x2, ...
* and so on forever

This never stops → infinitely many features.

---

11. Final Intuition

The Gaussian kernel is equivalent to:

* mapping input data into a space with 
all polynomial features of all degrees
* computing a linear dot product in that space

But:

* we never explicitly compute the feature map
* the kernel trick lets us compute everything efficiently

---
Summary

* The distance identity comes from expanding dot products
* (x·x')^k is a kernel because it equals an inner product over monomials
* Monomials are products of variables like x1^a x2^b
* The Gaussian kernel is an infinite weighted sum of polynomial kernels
* Therefore, it corresponds to an infinite-dimensional feature space


"""

"""
Expanding powers of a dot product

Using the multinomial theorem:

(x·x’)ⁿ = Σ_{|α| = n} (n! / (α₁! α₂! … α_d!)) x^α x’^α

where:

-   x^α = x₁^{α₁} x₂^{α₂} … x_d^{α_d}
-   |α| = α₁ + α₂ + … + α_d

Example in 2D, n = 3:

(x₁x₁’ + x₂x₂’)³ = 1 · x₁³ x₁’³ + 3 · x₁² x₂ · x₁’² x₂’ + 3 · x₁ x₂² ·
x₁’ x₂’² + 1 · x₂³ x₂’³

This produces all monomials of total degree 3.
"""