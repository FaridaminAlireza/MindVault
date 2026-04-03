"""
NUMERICAL INTEGRATION AND SIMPSON’S RULE
---
1. WHAT IS NUMERICAL INTEGRATION

Numerical integration is used to approximate the definite integral
Integral from a to b of f(x) dx
when:
* the function is complicated
* the function is only known at discrete points
* an exact analytical integral is difficult or impossible

The idea is to approximate the area under the curve using
simple geometric shapes.

---
2. TRAPEZOIDAL
The trapezoidal rule approximates 
the curve by straight-line segments.

For a single interval [a, b]:
T = (b - a) / 2 * [ f(a) + f(b) ]

For multiple equal subintervals:
Let h = (b - a) / n
Composite trapezoidal rule:
T_n = (h / 2) * [ f(x0) + 2f(x1) + 2f(x2) + ... + 2f(xn-1) + f(xn) ]

Error behavior:
Trapezoidal rule error is proportional to h^2

---
3. LIMITATION OF TRAPEZOIDAL RULE

The trapezoidal rule uses straight lines.
Straight lines do not capture curvature well.
This limits accuracy, especially when the function bends.

---
4. IDEA OF SIMPSON’S RULE

Simpson’s rule improves accuracy by:

* using parabolas instead of straight lines
* fitting a quadratic polynomial through three points

A quadratic needs exactly three points.

---
5. GRID AND STEP SIZE IN SIMPSON’S RULE

Points are equally spaced:
x0, x1 = x0 + h, x2 = x0 + 2h

* h is the smallest spacing between points
* Simpson’s rule does NOT increase step size
* It groups two adjacent h-intervals together

So the integration region is:
[x0, x2] = two intervals of size h

---
6. WHY SIMPSON’S RULE USES f0, f1, f2
Simpson’s rule fits a quadratic polynomial through:

(x0, f0)
(x1, f1)
(x2, f2)

This parabola approximates the function 
over two intervals at once.
That is why integration is performed from x0 to x2.

---
7. Derivation of the integral

Step 1:
Approximate f(x) by a quadratic polynomial p(x) 
that passes through the three points.

Step 2:
Use Lagrange interpolation to 
construct the quadratic polynomial.

Step 3:
Integrate the quadratic exactly from x0 to x2.


After simplification, the integral becomes:

Integral from x0 to x2 of f(x) dx
≈ (h / 3) [ f0 + 4f1 + f2 ]

This formula is exact for all quadratic functions.

---

8. DOES USING TWO INTERVALS REDUCE PRECISION?

No. It increases precision.

Reason:
* Trapezoidal rule uses linear approximation
* Simpson’s rule uses quadratic approximation

Error comparison:
Trapezoidal rule error is proportional to h^2
Simpson’s rule error is proportional to h^4

Simpson’s rule converges much faster.

---

10. COMPOSITE SIMPSON’S RULE

For a larger interval [a, b]:

* The interval is divided into 
an even number of subintervals
* Each Simpson panel uses two subintervals

---
11. WHY NUMBER OF INTERVALS MUST BE EVEN

Each Simpson segment uses two intervals.
Therefore, the total number of intervals 
must be divisible by 2.

---
EXAMPLE

Integrate f(x) = x^2 from 0 to 1.

Exact integral:

I = ∫0^1 x^2 dx = 1/3 ≈ 0.333333

Step size h = 1 (one strip):

T1 = (1 / 2) * [ f(0) + f(1) ] = (1/2) * (0 + 1) = 0.5

Error = T1 − I = 0.5 − 0.333333 = 0.166667

Step size h = 0.5 (two strips):

x0 = 0, x1 = 0.5, x2 = 1

T2 = (0.5/2) * [ f0 + 2 f1 + f2 ] = 
0.25 * [0 + 2*0.25 + 1] = 0.25 * 1.5 = 0.375

Error = T2 − I = 0.375 − 0.333333 = 0.041667

Compare:

* h = 1 → error ≈ 0.1667
* h = 0.5 → error ≈ 0.0417 ≈ 1/4 of previous error

This confirms error ∝ h^2.

"""

"""
Deriving the Simpson’s rule formula
using Lagrange interpolation

# 1. Set up the interval and points

Simpson’s rule is based on approximating f(x)
by a quadratic polynomial passing through three points.
Let’s take three points in the interval [a, b]:

* x0 = a
* x1 = (a + b)/2 (the midpoint)
* x2 = b

We want a quadratic polynomial P2(x)
that passes through these points:

P2(x) = f(x0) * L0(x) + f(x1) * L1(x) + f(x2) * L2(x)

Where L0, L1, L2 are Lagrange basis polynomials:

* L0(x) = (x - x1)*(x - x2) / ((x0 - x1)*(x0 - x2))
* L1(x) = (x - x0)*(x - x2) / ((x1 - x0)*(x1 - x2))
* L2(x) = (x - x0)*(x - x1) / ((x2 - x0)*(x2 - x1))

---
# 2. Approximate the integral

The integral of f(x) from a to b is
approximated by the integral of P2(x):

Integral from a to b of f(x) dx 
≈ Integral from a to b of P2(x) dx

Substitute P2(x):
Integral ≈ Integral from a to b of 
[f(x0)*L0(x) + f(x1)*L1(x) + f(x2)*L2(x)] dx

= f(x0) * Integral[L0(x) dx] + f(x1) * Integral[L1(x) dx] +
f(x2) * Integral[L2(x) dx]

---
# 3. Compute the integrals of Lagrange polynomials

Let h = (b - a)/2. Then the points are:

* x0 = a
* x1 = a + h
* x2 = a + 2h = b

It is known (from integrating quadratics) that:

* Integral from a to b of L0(x) dx = h / 3
* Integral from a to b of L1(x) dx = 4h / 3
* Integral from a to b of L2(x) dx = h / 3

---

# 4. Write Simpson’s rule formula

Now plug the integrals back:

Integral from a to b of f(x) dx 
≈ (h / 3) * [f(x0) + 4*f(x1) + f(x2)]

This is exactly the basic Simpson’s rule
for a single interval.

---
# 5. Composite Simpson’s rule

If the interval [a, b] is divided into 
n subintervals (n even), you apply 
this formula over each pair of 
subintervals and sum the results:

Integral from a to b of f(x) dx 
≈ (h / 3) * 
[f(x0) + 4*f(x1) + 2*f(x2) + 4*f(x3) 
+ 2*f(x4) + ... + 4*f(x_{n-1}) + f(xn)]

* h = (b - a)/n
* Coefficients alternate: 1, 4, 2, 4, ..., 4, 1
"""