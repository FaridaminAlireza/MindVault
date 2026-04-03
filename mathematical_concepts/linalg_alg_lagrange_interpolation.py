"""
 LAGRANGE INTERPOLATION

---
GENERAL LAGRANGE FORMULA

Given points (x0, y0), (x1, y1), ..., (xn, yn),
the Lagrange interpolation polynomial is:
L(x) = sum_{i=0 to n} [ y_i * l_i(x) ]
where the Lagrange basis polynomials are:
l_i(x) = product over j ≠ i of (x - x_j) / (x_i - x_j)

This general formula is used to construct the 
interpolating polynomial of degree n.

---
LINEAR CASE (DEGREE 1)
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
QUADRATIC CASE (DEGREE 2)
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
y0 * l0(x) + y1 * l1(x) + y2 * l2(x)

Explicitly:

L(x) =
y0 * (x - x1)(x - x2) / ((x0 - x1)(x0 - x2))
+ y1 * (x - x0)(x - x2) / ((x1 - x0)(x1 - x2))
+ y2 * (x - x0)(x - x1) / ((x2 - x0)(x2 - x1))

This is the Lagrange form of any quadratic polynomial.

---
PROOF OF THE LAGRANGE INTERPOLATION FORMULA

Setup:
Let (x0, y0), (x1, y1), ..., (xn, yn) 
be n+1 distinct points (all xi are distinct).
We want a polynomial L(x) of degree at most n
such that L(xi) = yi for each i = 0,...,n.

1. Define the Lagrange basis polynomials:
   For each i = 0,...,n define
   li(x) = product_{j = 0, j ≠ i}^{n} (x - xj) / (xi - xj).

   Notes:
   * The denominator (xi - xj) is nonzero because the xi are distinct.
   * Each li(x) is a polynomial of degree n (product of n linear factors).
   * li(x) is well-defined for all x (it is a genuine polynomial).

2. Key property of li(x) (Kronecker-delta property):
   For any indices i and k in {0,...,n}:
     
     li(xk) = 1 when k = i, and li(xk) = 0 when k ≠ i.
     In short, li(xk) = δ_{ik} (the Kronecker delta).

3. Show L(x) interpolates the data (existence)

   We evaluate L(x) at a data point xk:

   L(xk) = sum over i=0 to n of [ yi * li(xk) ]

   Now use the key property:

   * li(xk) = 0 for all i ≠ k
   * lk(xk) = 1

   So all terms vanish except one:
   L(xk) = yk * 1 + all other terms * 0
   L(xk) = yk

   Conclusion:
   For every k, L(xk) = yk
   So L(x) passes through all given points 
   → it interpolates the data

4. Show degree of L(x) is at most n

   * Each li(x) is a polynomial of degree n
   * L(x) is a sum of these polynomials 
   multiplied by constants yi

   So:
   L(x) = y0*l0(x) + y1*l1(x) + ... + yn*ln(x)
   Since each term has degree n, the total also
   has degree at most n

   Important note:
   * Some terms might cancel out and
   reduce the degree
   * But it can never exceed n
   Conclusion:
   L(x) is a polynomial with degree ≤ n

5. Show uniqueness of the interpolating polynomial

   Assume there are two polynomials:

   * P(x) and Q(x)
   * Both have degree ≤ n
   * Both satisfy: P(xi) = yi and Q(xi) = yi for all i

   Now define:
   R(x) = P(x) - Q(x)

   Step-by-step reasoning:

      1. R(x) is still a polynomial of degree ≤ n

      2. At each data point xi:

         R(xi) = P(xi) - Q(xi)
         = yi - yi
         = 0

      So R(x) has zeros at x0, x1, ..., xn

      That is n+1 distinct roots

      Key fact: A nonzero polynomial of degree ≤ n
      can have at most n roots

      Conclusion:
      * R(x) has n+1 roots → 
      impossible unless it is zero everywhere
      * So R(x) = 0 for all x
      * Therefore P(x) = Q(x)

---
Conclusion:
   * L(x) matches all data points → existence
   * L(x) has degree ≤ n → valid construction
   * No other polynomial can do this → uniqueness

REMARKS:
* Intuition for li(x): li(x) is built to be 1 at xi and 0
at the other interpolation nodes; multiplying li(x) by yi
places the correct value at xi and contributes nothing 
at other nodes. Summing over i stitches all values together.

* Practical note: the Lagrange form is explicit and conceptually simple,
but for numerical work with many nodes it can be inefficient;
alternatives include Newton form (divided differences) 
or barycentric Lagrange for stable evaluation.

* The Lagrange formula gives a polynomial of 
degree ≤ n that matches all values. Because 
the matching polynomial is unique,
the Lagrange one must be the polynomial.
Therefore the Lagrange polynomial is guaranteed to 
represent the original polynomial exactly.
"""