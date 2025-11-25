"""
GENERAL INTEGRATION RULES AND PROOFS

**1. Constant Rule**
∫ c dx = c x + C

**Proof:**

* The derivative of c x is c, 
because d/dx (c x) = c.
* Integration is the reverse of differentiation.
* Therefore ∫ c dx = c x + C, where C is 
the constant of integration.

**Example:**
∫ 7 dx = 7x + C

---

**2. Power Rule**
∫ x^n dx = x^(n+1)/(n+1) + C, for n ≠ −1

**Proof:**

* Let F(x) = x^(n+1)/(n+1).
* Then F'(x) = (n+1)/(n+1) * x^n = x^n.
* Integration is the reverse of
 differentiation, so ∫ x^n dx = F(x) + C.

**Example:**
∫ x^3 dx = x^4/4 + C

---

**3. Integral of 1/x**
∫ 1/x dx = ln|x| + C

**Proof:**

* d/dx [ln|x|] = 1/x for x ≠ 0.
* By definition of antiderivative,
 ∫ 1/x dx = ln|x| + C.

**Example:**
∫ 1/x dx = ln|x| + C

---

**4. Sum Rule**
∫ [f(x) + g(x)] dx = ∫ f(x) dx + ∫ g(x) dx

**Proof:**

* Differentiation is linear: 
d/dx [F(x) + G(x)] = F'(x) + G'(x).
* Integration is the reverse of
 differentiation, so linearity holds.

**Example:**
∫ (x^2 + 3x) dx = 
∫ x^2 dx + ∫ 3x dx = x^3/3 + 3x^2/2 + C

---
**5. Difference Rule**
∫ [f(x) − g(x)] dx = ∫ f(x) dx − ∫ g(x) dx

**Proof:**

* Follows from linearity of integration:
subtraction is addition of the negative function.

**Example:**
∫ (5x^4 − x) dx =
 ∫ 5x^4 dx − ∫ x dx = x^5 − x^2/2 + C

---

**6. Constant Multiple Rule**
∫ k f(x) dx = k ∫ f(x) dx

**Proof:**

* d/dx [k F(x)] = k F'(x).
* So if F'(x) = f(x), then d/dx [k F(x)] = k f(x).
* Therefore ∫ k f(x) dx = k ∫ f(x) dx.

**Example:**
∫ 4x^3 dx = 4 ∫ x^3 dx = x^4 + C

---

**7. Product of Separate Integrals 
(Separable Integration Rule)**
(∫ f(x) dx)(∫ g(y) dy) = ∫∫ f(x) g(y) dx dy

**Proof:**

* By Fubini’s theorem: if f(x) and g(y) are
 integrable over their domains,
  ∫∫ f(x) g(y) dx dy = (∫ f(x) dx)(∫ g(y) dy).
* This works because x and y are independent variables.

**Example:**
∫*{−∞}^{∞} e^(−B x^2) dx * ∫*{−∞}^{∞} e^(−B y^2) dy
= ∫∫_{−∞}^{∞} e^(−B(x^2 + y^2)) dx dy = π/B

---

**8. Integration by Substitution 
(Reverse Chain Rule)**
∫ f(g(x)) g'(x) dx = ∫ f(u) du, where u = g(x)

**Proof:**

* Let u = g(x) ⇒ du = g'(x) dx
* Then dx = du / g'(x)
* Substitute into the integral: 
∫ f(g(x)) g'(x) dx = ∫ f(u) du

**Example:**
∫ 2x (x^2 + 1)^5 dx
Let u = x^2 + 1 ⇒ du = 2x dx
∫ 2x (x^2 + 1)^5 dx =
 ∫ u^5 du = u^6/6 + C = (x^2 + 1)^6 / 6 + C

---
**9. Integration of Exponential Functions**
∫ e^x dx = e^x + C
∫ a^x dx = a^x / ln(a) + C, a > 0

**Proof:**

* d/dx e^x = e^x
* d/dx a^x = a^x ln(a)
* Reverse gives the formulas above.

**Example:**
∫ 2^x dx = 2^x / ln(2) + C
---

**10. Integration of Trigonometric Functions**

∫ sin(x) dx = −cos(x) + C
∫ cos(x) dx = sin(x) + C
∫ sec^2(x) dx = tan(x) + C
∫ csc(x) cot(x) dx = −csc(x) + C

**Proof:**

* Directly from derivatives: 
 d/dx [−cos(x)] = sin(x), etc.

**Example:**
∫ cos(x) dx = sin(x) + C

---

**11. Integration of Rational Functions
 (Special Cases)**

∫ 1/(x^2 + 1) dx = arctan(x) + C
∫ 1/√(1 − x^2) dx = arcsin(x) + C

**Proof:**

* Based on derivative identities: 
d/dx arctan(x) = 1/(1 + x^2),
 d/dx arcsin(x) = 1/√(1 − x^2)

**Example:**
∫ 1/(1 + x^2) dx = arctan(x) + C

---

**12. Definite Integral Rule 
(Fundamental Theorem of Calculus)**

If F'(x) = f(x), then
∫[a to b] f(x) dx = F(b) − F(a)

**Proof:**

* The derivative of F is f, so the 
accumulated area from a to b is F(b) − F(a)

**Example:**
∫[0 to 2] x^2 dx = (2^3 / 3) − (0^3 / 3) = 8/3

---

**SUMMARY**

* Integration is linear: 
sum, difference, constant multiple.
* Power, exponential, logarithmic,
trigonometric, and rational functions
have standard formulas.
* Substitution handles chain-rule type integrals.
* Multiplying separate integrals over independent
variables gives a double integral.
* Definite integrals give accumulated area/volume
using the antiderivative.

"""


"""
Proof of
(∫ f(x) dx)(∫ g(y) dy) = ∫∫ f(x) g(y) dx dy

using **Fubini’s theorem**

---
## PROOF OF THE PRODUCT-TO-DOUBLE-INTEGRAL RULE

Let

A = ∫_a^b f(x) dx
B = ∫_c^d g(y) dy

We want to prove:
A · B = ∫_a^b ∫_c^d f(x) g(y) dy dx

---

## STEP 1 — START FROM THE PRODUCT

A · B
= ( ∫_a^b f(x) dx ) ( ∫_c^d g(y) dy )

Write out the product using the definition of
definite integrals as limits of Riemann sums:

A = lim_{n→∞} Σ f(x_i*) Δx
B = lim_{m→∞} Σ g(y_j*) Δy

Thus:

A·B = 
lim_{n→∞} Σ f(x_i*) Δx  ·  lim_{m→∞} Σ g(y_j*) Δy

Combine the limits:

A·B = 
lim_{n→∞} lim_{m→∞} Σ Σ f(x_i*) g(y_j*) Δx Δy

This is now a **double Riemann sum** over 
the rectangle [a,b] × [c,d].

---

## STEP 2 — RECOGNIZE THIS AS A DOUBLE INTEGRAL

The expression

Σ Σ f(x_i*) g(y_j*) Δx Δy

is exactly the Riemann sum for the function

h(x, y) = f(x) g(y)

over the rectangular domain in the xy-plane.

Therefore:

A · B
= ∫_a^b ∫_c^d f(x) g(y) dy dx

This step is justified by **Fubini’s theorem**,
which states:
If a function defined on a rectangle is integrable
and can be written as h(x,y) = f(x)g(y), then the
double integral exists and equals the iterated 
integral.

---
## STEP 3 — FINAL FORM

Thus, we conclude:

( ∫_a^b f(x) dx )( ∫_c^d g(y) dy )
= ∫_a^b ∫_c^d f(x) g(y) dy dx

Similarly:

= ∫_c^d ∫_a^b f(x) g(y) dx dy

So the product of two 1D integrals of
independent variables equals a 2D 
integral of their product.

---
## WHY THE PROOF WORKS

1. f(x) and g(y) depend on **different variables**.
   So f(x)g(y) is defined on a 2D rectangle.

2. The product of Riemann sums becomes 
a **double sum**, which is a double integral.

3. Fubini’s theorem allows converting between
the double integral and iterated integrals.

4. No special property of Gaussian functions 
is needed — the rule works for all integrable
functions.

---
## SAME FUNCTION OR DIFFERENT?
The proof NEVER used that f = g.

Thus the rule works whether:

* f = g
* f ≠ g
* f and g are unrelated

As long as the integrals converge.

"""