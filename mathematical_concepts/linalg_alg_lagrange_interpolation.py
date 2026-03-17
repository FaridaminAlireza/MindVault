"""
Here is the full explanation in **plain raw text**, with no Markdown formatting.
Everything is copy-pastable.

---

## LAGRANGE INTERPOLATION — RAW TEXT VERSION

1. GENERAL LAGRANGE FORMULA

Given points (x0, y0), (x1, y1), ..., (xn, yn), the Lagrange interpolation polynomial is:

L(x) = sum_{i=0 to n} [ y_i * l_i(x) ]

where the Lagrange basis polynomials are:

l_i(x) = product over j ≠ i of (x - x_j) / (x_i - x_j)

This general formula is used to construct the interpolating polynomial of degree n.

---

2. LINEAR CASE (DEGREE 1)
   f(x) = ax + b

Only two points are needed:
(x0, y0)
(x1, y1)

Step 1: Lagrange basis polynomials

l0(x) = (x - x1) / (x0 - x1)
l1(x) = (x - x0) / (x1 - x0)

Step 2: Lagrange interpolation polynomial

L(x) = y0 * l0(x) + y1 * l1(x)

Explicitly:

L(x) = y0 * (x - x1)/(x0 - x1) + y1 * (x - x0)/(x1 - x0)

This is the Lagrange form of any linear polynomial.

---

3. QUADRATIC CASE (DEGREE 2)
   f(x) = ax^2 + bx + c

Three points are needed:
(x0, y0)
(x1, y1)
(x2, y2)

Step 1: Lagrange basis polynomials

l0(x) = (x - x1)(x - x2) / ((x0 - x1)(x0 - x2))
l1(x) = (x - x0)(x - x2) / ((x1 - x0)(x1 - x2))
l2(x) = (x - x0)(x - x1) / ((x2 - x0)(x2 - x1))

Step 2: Lagrange interpolation polynomial

L(x) =
y0 * l0(x)

* y1 * l1(x)
* y2 * l2(x)

Explicitly:

L(x) =
y0 * (x - x1)(x - x2) / ((x0 - x1)(x0 - x2))

* y1 * (x - x0)(x - x2) / ((x1 - x0)(x1 - x2))
* y2 * (x - x0)(x - x1) / ((x2 - x0)(x2 - x1))

This is the Lagrange form of any quadratic polynomial.

---

If you want, I can also give:
– a raw-text derivation for cubic case,
– examples with actual numbers,
– or a raw-text template you can fill in on your own.

"""

"""
Below is a clear, step-by-step proof of the Lagrange interpolation formula in plain raw text (copy-pasteable). It shows existence (the formula produces an interpolating polynomial of degree ≤ n) and uniqueness (there is only one such polynomial).

---

## PROOF OF THE LAGRANGE INTERPOLATION FORMULA — RAW TEXT

Setup:
Let (x0, y0), (x1, y1), ..., (xn, yn) be n+1 distinct points (all xi are distinct).
We want a polynomial L(x) of degree at most n such that L(xi) = yi for each i = 0,...,n.

1. Define the Lagrange basis polynomials:
   For each i = 0,...,n define
   li(x) = product_{j = 0, j ≠ i}^{n} (x - xj) / (xi - xj).

   Notes:

   * The denominator (xi - xj) is nonzero because the xi are distinct.
   * Each li(x) is a polynomial of degree n (product of n linear factors).
   * li(x) is well-defined for all x (it is a genuine polynomial).

2. Key property of li(x) (Kronecker-delta property):
   For any indices i and k in {0,...,n}:

   * If k = i, then evaluate li at xk = xi:
     li(xi) = product_{j ≠ i} (xi - xj) / (xi - xj) = 1.
   * If k ≠ i, then evaluate li at xk:
     In the numerator product there is a factor (xk - xk) = 0,
     while the denominator has no zero factor, so li(xk) = 0.
     Therefore li(xk) = 1 when k = i, and li(xk) = 0 when k ≠ i.
     In short, li(xk) = δ_{ik} (the Kronecker delta).

3. Construct L(x) as the linear combination:
   Define
   L(x) = sum_{i = 0}^{n} yi * li(x).

4. Show L(x) interpolates the data (existence):
   For any k in {0,...,n},
   L(xk) = sum_{i = 0}^{n} yi * li(xk).
   But li(xk) = δ_{ik}, so the sum reduces to only the i = k term:
   L(xk) = yk * 1 + sum_{i ≠ k} yi * 0 = yk.
   Hence L(xk) = yk for every k. Thus L interpolates the given points.

5. Show degree bound (L has degree ≤ n):
   Each li(x) is a polynomial of degree n.
   L(x) is a linear combination of the li(x) with constant coefficients yi.
   Potential cancellation could lower degree, but in any case L(x) is a polynomial of degree at most n.
   Therefore the construction gives a polynomial of degree ≤ n that interpolates the points.

6. Show uniqueness of the interpolating polynomial (uniqueness):
   Suppose there are two polynomials P(x) and Q(x) of degree at most n such that
   P(xi) = yi and Q(xi) = yi for all i = 0,...,n.
   Consider the difference R(x) = P(x) - Q(x).
   Then R(x) is a polynomial of degree at most n and satisfies R(xi) = 0 for each i = 0,...,n.
   So R(x) has n+1 distinct roots x0,...,xn.
   But a nonzero polynomial of degree ≤ n can have at most n roots.
   Therefore R(x) must be the zero polynomial; hence P(x) = Q(x) identically.
   So the interpolating polynomial of degree ≤ n is unique.

7. Conclusion:

   * Existence: The Lagrange polynomial L(x) defined in step 3 exists and satisfies L(xi) = yi.
   * Degree: L(x) has degree ≤ n.
   * Uniqueness: Any polynomial of degree ≤ n that interpolates the points must equal L(x).
     Thus L(x) is the unique interpolating polynomial of degree at most n, and the Lagrange formula yields it.

---

## ADDITIONAL REMARKS (optional, quick intuition)

* Intuition for li(x): li(x) is built to be 1 at xi and 0 at the other interpolation nodes; multiplying li(x) by yi places the correct value at xi and contributes nothing at other nodes. Summing over i stitches all values together.
* Degree comment: although each li has degree n, clever cancellations in the sum can produce a polynomial of degree less than n when the underlying data come from a lower-degree polynomial; the formula still works and yields the same lower-degree polynomial.
* Practical note: the Lagrange form is explicit and conceptually simple, but for numerical work with many nodes it can be inefficient; alternatives include Newton form (divided differences) or barycentric Lagrange for stable evaluation.

---

If you’d like, I can also produce:

* A short raw-text worked numerical example (showing step-by-step simplification), or
* A visual sketch / ASCII plot for the basis polynomials li(x) to build intuition. Which would you prefer?

"""