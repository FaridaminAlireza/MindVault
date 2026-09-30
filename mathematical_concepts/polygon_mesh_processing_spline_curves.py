"""
SPLINE CURVES

1. What is a spline?

A spline is a smooth curve constructed 
from several polynomial pieces.

Suppose we have data points
(x₀, y₀), (x₁, y₁), ..., (xₙ, yₙ)
with x₀ < x₁ < ... < xₙ.

Instead of fitting one large polynomial 
through all points, we construct a 
separate polynomial on each interval:

[x₀, x₁], [x₁, x₂], ... [xₙ₋₁, xₙ].

For a cubic spline, 
each piece is a cubic polynomial:
Sᵢ(x) = aᵢ + bᵢ(x - xᵢ) + cᵢ(x - xᵢ)² + dᵢ(x - xᵢ)³
for xᵢ ≤ x ≤ xᵢ₊₁.

The important idea is: 
A spline is not one polynomial.
It is a collection of polynomial pieces
that are connected smoothly.

2. Why use several polynomial pieces?
Suppose we have many points.
We could use one polynomial passing
through every point.
For n + 1 points, this polynomial
has degree n.
For example:
2 points → degree 1
3 points → degree 2
4 points → degree 3
10 points → degree 9

- High-degree polynomials can behave badly.
- They may oscillate strongly between points.
- They are also difficult to control locally.

A spline solves this problem.
Each interval gets a low-degree polynomial.

For a cubic spline: 
every interval uses degree 3.

Changing one point generally affects
only nearby pieces much more directly
than changing one point in a single
high-degree polynomial.

3. What does "smooth" mean?

Simply passing through the points is not enough.
Suppose two polynomial pieces meet at xᵢ.
We want them to connect smoothly.
For a cubic spline, we normally require:

1. Function continuity: 
(C^0: position matches, Visually: no gap.)
Sᵢ(xᵢ₊₁) = Sᵢ₊₁(xᵢ₊₁)

2. First-derivative continuity: 
(C^1: slope matches, The two pieces have the
same tangent direction. Visually: no sharp corner.)
Sᵢ'(xᵢ₊₁) = Sᵢ₊₁'(xᵢ₊₁)

3. Second-derivative continuity: 
(C^2: curvature behavior matches.
Visually: no sudden change in bending)
Sᵢ''(xᵢ₊₁) = Sᵢ₊₁''(xᵢ₊₁)

Therefore the complete cubic spline is
usually a C²-continuous curve.
C² means:
the function is continuous,
the first derivative is continuous,
and the second derivative is continuous.

4. Physical intuition
- Imagine bending a thin flexible ruler
through the data points.
- The ruler does not suddenly change
its direction at each point.
- It also does not suddenly change
its curvature.
- A cubic spline mathematically models
this type of smooth bending.

This is one reason splines are useful
in CAD, computer graphics,
geometry processing, interpolation,
and numerical computation.

- 5. Cubic spline on one interval

Consider the interval [xᵢ, xᵢ₊₁].

Define hᵢ = xᵢ₊₁ - xᵢ.

We write the cubic polynomial as

Sᵢ(x) = aᵢ+ + bᵢ(x - xᵢ) + cᵢ(x - xᵢ)² + (x - xᵢ)³

This form is convenient because
x - xᵢ = 0 at the left endpoint.
Therefore: Sᵢ(xᵢ) = aᵢ.

Since the spline must pass through
the data point, Sᵢ(xᵢ) = yᵢ.
Therefore: aᵢ = yᵢ.

So we can write Sᵢ(x) = 
yᵢ + bᵢ(x - xᵢ) + cᵢ(x - xᵢ)² + dᵢ(x - xᵢ)³.

6. Derivatives
Differentiate once:
Sᵢ'(x) = bᵢ + 2cᵢ(x - xᵢ) + 3dᵢ(x - xᵢ)².
Differentiate again:
Sᵢ''(x) = 2cᵢ + 6dᵢ(x - xᵢ).
Differentiate a third time:
Sᵢ'''(x) = 6dᵢ.

The second derivative is especially useful
because cubic splines are constructed by
controlling the curvature.

Define Mᵢ = Sᵢ''(xᵢ).
Then: Mᵢ = 2cᵢ.
Therefore: cᵢ = Mᵢ / 2.

7. Deriving the cubic spline formula

We now derive a particularly useful
representation of the cubic spline.

On interval [xᵢ, xᵢ₊₁], define

hᵢ = xᵢ₊₁ - xᵢ.
We know Sᵢ''(xᵢ) = Mᵢ
and Sᵢ''(xᵢ₊₁) = Mᵢ₊₁.

Because Sᵢ''(x) is linear,
it must interpolate between Mᵢ and Mᵢ₊₁.

Let t = (x - xᵢ) / hᵢ.
Then t = 0 at x = xᵢ,
and t = 1 at x = xᵢ₊₁.

Therefore:
Sᵢ''(x) = (1 - t)Mᵢ + tMᵢ₊₁.
Substituting t:
Sᵢ''(x) = Mᵢ + (Mᵢ₊₁ - Mᵢ) (x - xᵢ)/hᵢ.
This is already an important result.

The second derivative of a cubic is linear.

8. Integrating to obtain the spline

We now integrate twice.
Start with
Sᵢ''(x) = Mᵢ + (Mᵢ₊₁ - Mᵢ) (x - xᵢ)/hᵢ.
Integrating once gives
Sᵢ'(x) = Mᵢ(x - xᵢ) + (Mᵢ₊₁ - Mᵢ) (x - xᵢ)²/(2hᵢ) +  C.
Integrating again gives
Sᵢ(x) = Mᵢ(x - xᵢ)²/2 + (Mᵢ₊₁ - Mᵢ) (x - xᵢ)³/(6hᵢ) + C(x - xᵢ)+ D.

The constants C and D are determined by requiring
Sᵢ(xᵢ) = yᵢ and Sᵢ(xᵢ₊₁) = yᵢ₊₁.

A more convenient final expression is
Sᵢ(x) = Mᵢ (xᵢ₊₁ - x)³ / (6hᵢ) +
        Mᵢ₊₁ (x - xᵢ)³ / (6hᵢ)+ 
        [yᵢ - Mᵢhᵢ²/6] (xᵢ₊₁ - x)/hᵢ + 
        [yᵢ₊₁ - Mᵢ₊₁hᵢ²/6] (x - xᵢ)/hᵢ.

This is the standard cubic spline
interpolation formula in terms of
the second derivatives Mᵢ.

9. Why does this formula pass
   through the two endpoints?

Check x = xᵢ.
Then x - xᵢ = 0
and xᵢ₊₁ - x = hᵢ.

The formula becomes

# Sᵢ(xᵢ) = Mᵢhᵢ³/(6hᵢ) + [yᵢ - Mᵢhᵢ²/6](hᵢ/hᵢ).

Therefore:
# Sᵢ(xᵢ) = Mᵢhᵢ²/6 + yᵢ -Mᵢhᵢ²/6
so Sᵢ(xᵢ) = yᵢ.

Similarly, at x = xᵢ₊₁:
Sᵢ(xᵢ₊₁) = yᵢ₊₁.

Thus every spline piece passes
through its two data points.

10. How do we determine Mᵢ?

The data points give us
y₀, y₁, ..., yₙ.
But the spline formula also contains
M₀, M₁, ..., Mₙ.
These are unknown.

We need equations that determine them.
The key requirement is:
# Sᵢ'(xᵢ₊₁) = Sᵢ₊₁'(xᵢ₊₁).

This means the first derivative must
be continuous at every interior point.

11. Deriving the equation for Mᵢ

For interval i, the derivative at
the right endpoint is

Sᵢ'(xᵢ₊₁) = 
(yᵢ₊₁ - yᵢ)/hᵢ + hᵢ(2Mᵢ + Mᵢ₊₁)/6.

For the next interval, the derivative
at its left endpoint is

Sᵢ₊₁'(xᵢ₊₁) =

(yᵢ₊₂ - yᵢ₊₁)/hᵢ₊₁
+
hᵢ₊₁(Mᵢ₊₁ + 2Mᵢ₊₂)/6.

Set them equal:

(yᵢ₊₁ - yᵢ)/hᵢ + hᵢ(2Mᵢ + Mᵢ₊₁)/6
=
(yᵢ₊₂ - yᵢ₊₁)/hᵢ₊₁ + hᵢ₊₁(Mᵢ₊₁ + 2Mᵢ₊₂)/6.

Rearranging gives

hᵢMᵢ + 2(hᵢ + hᵢ₊₁)Mᵢ₊₁ + hᵢ₊₁Mᵢ₊₂
= 6[(yᵢ₊₂ - yᵢ₊₁)/hᵢ₊₁ - (yᵢ₊₁ - yᵢ)/hᵢ]

This is the central equation
of the cubic-spline system.

It relates three consecutive
second derivatives:

Mᵢ, Mᵢ₊₁, and Mᵢ₊₂.

Repeating this equation for every
interior knot produces a
tridiagonal linear system for
the unknown values Mᵢ.

It is obtained from first-derivative
continuity.

12. Why is the system tridiagonal?

For each interior point, the equation
contains only three neighboring
second derivatives:
Mᵢ,
Mᵢ₊₁,
Mᵢ₊₂.

Therefore the system has the form
[diagonal structure]
```
  M₀
  M₁
  M₂
  M₃
  ...
```

with each equation involving only
neighboring unknowns.

The resulting matrix is tridiagonal.

This is computationally important because
a tridiagonal system can be solved very
efficiently.

13. Boundary conditions

The interior equations are not enough.
There are n + 1 unknowns:
M₀, M₁, ..., Mₙ.

The continuity equations give only
n - 1 equations.

We therefore need two additional
boundary conditions.

---
A common choice is the natural spline.

14. Natural cubic spline

For a natural spline we impose
M₀ = 0 and Mₙ = 0.

Since Mᵢ = Sᵢ''(xᵢ),
this means S''(x₀) = 0
and S''(xₙ) = 0.

In other words, 
the curvature is zero
at the two endpoints.

---
15. Example: three points
Suppose we have
(x₀, y₀),
(x₁, y₁),
(x₂, y₂).

There are two intervals: [x₀, x₁] and [x₁, x₂].

There are therefore two cubic pieces:
S₀(x) and S₁(x).
We have four unknown second derivatives:
M₀, M₁, M₂.

For a natural spline:
M₀ = 0 and M₂ = 0.

Only M₁ remains unknown.

The continuity equation becomes
h₀M₀ + 2(h₀ + h₁)M₁ + h₁M₂ =
6[(y₂ - y₁)/h₁ -(y₁ - y₀)/h₀].

Since M₀ = M₂ = 0,
we get
2(h₀ + h₁)M₁ = 6[ (y₂ - y₁)/h₁ - (y₁ - y₀)/h₀].

Therefore
M₁ = 3/(h₀ + h₁)[(y₂ - y₁)/h₁ - (y₁ - y₀)/h₀]

---
16. Special case: equally spaced points
Suppose
x₀ = 0,
x₁ = 1,
x₂ = 2.

Then h₀ = h₁ = 1.

The formula becomes

4M₁ = 6[(y₂ - y₁) - (y₁ - y₀)].

Therefore
M₁ = 3/2 (y₂ - 2y₁ + y₀).

Notice that y₂ - 2y₁ + y₀
is a second finite difference.
This is not accidental.
The spline's second derivative is
closely related to the discrete curvature
of the data.

17. Cubic spline in coefficient form

Another common representation is
Sᵢ(x) = aᵢ + bᵢ(x − xᵢ) + cᵢ(x − xᵢ)² + dᵢ(x − xᵢ)³.

Here, aᵢ = yᵢ
and cᵢ = Mᵢ/2.
From the second-derivative conditions, we obtain
dᵢ = (Mᵢ₊₁ − Mᵢ)/(6hᵢ).

The coefficient bᵢ is
bᵢ = (yᵢ₊₁ − yᵢ)/hᵢ − hᵢ(2Mᵢ + Mᵢ₊₁)/6.

Therefore, the complete cubic polynomial on interval i is

Sᵢ(x) = yᵢ + 
[(yᵢ₊₁ − yᵢ)/hᵢ − hᵢ(2Mᵢ + Mᵢ₊₁)/6](x − xᵢ) +
(Mᵢ/2)(x − xᵢ)² + [(Mᵢ₊₁ − Mᵢ)/(6hᵢ)](x − xᵢ)³.

18. What the coefficients mean

In Sᵢ(x) = aᵢ + bᵢ(x − xᵢ) + cᵢ(x − xᵢ)² + dᵢ(x − xᵢ)³,

the coefficients control different properties of the curve.
aᵢ controls the value at xᵢ.
bᵢ controls the slope at xᵢ.
cᵢ controls the second derivative, 
and therefore the local curvature.
dᵢ controls how the curvature changes across the interval.

This is one reason cubic polynomials are
particularly useful for splines.


19. Why cubic?

A polynomial of degree 3 has four coefficients:
a, b, c, d.
At each interval, we need enough freedom to 
satisfy smoothness conditions.

For two neighboring cubic pieces, 
we want to control the value, 
first derivative, 
and second derivative at their common endpoint.

A cubic provides sufficient flexibility while
remaining computationally simple.

A linear spline provides only C⁰ continuity.
A quadratic spline can provide higher smoothness,
but cubic splines are the standard choice when we want
C² continuity while keeping the polynomial degree 
relatively low.Thus, cubic splines provide C² 
continuity with a relatively low polynomial degree.

20. Spline versus polynomial interpolation

Polynomial interpolation uses one polynomial 
that passes through all data points.
Cubic spline interpolation uses many cubic polynomials 
that are connected smoothly.

For example, with five data points:

Polynomial interpolation: one degree-4 polynomial.
Cubic spline interpolation: four cubic polynomials.
The spline is more local because changing one part
of the data generally affects nearby spline pieces 
rather than requiring one high-degree polynomial 
to change everywhere.

21. Spline versus piecewise linear interpolation
Piecewise linear interpolation consists of
straight line + straight line + straight line + ...
It is continuous, so it has C⁰ continuity.
However, the derivative normally jumps at the data points.

A cubic spline consists of
curved piece + curved piece + curved piece + ...
with C² continuity.
Therefore, the spline has continuous slope 
and continuous second derivative across the interior knots.

23. The geometric interpretation
Think of each interval as a small flexible 
cubic segment. At every interior data point,
two segments meet.

The condition Sᵢ(xᵢ₊₁) = Sᵢ₊₁(xᵢ₊₁)
makes the two pieces meet at the same position.

The condition Sᵢ′(xᵢ₊₁) = Sᵢ₊₁′(xᵢ₊₁)
makes their tangent directions agree.

The condition Sᵢ″(xᵢ₊₁) = Sᵢ₊₁″(xᵢ₊₁)
makes their second derivatives agree.

Therefore:
C⁰ → no gap
C¹ → no sharp corner
C² → no sudden change in second derivative

24. The complete construction process

Given the points
(x₀, y₀), ..., (xₙ, yₙ),

Step 1: Compute the interval widths hᵢ = xᵢ₊₁ − xᵢ.

Step 2: Introduce the unknown second derivatives
M₀, ..., Mₙ, where Mᵢ = S″(xᵢ).

Step 3: Use first-derivative continuity 
at every interior point. This gives

hᵢMᵢ + 2(hᵢ + hᵢ₊₁)Mᵢ₊₁ + hᵢ₊₁Mᵢ₊₂ = 
6[(yᵢ₊₂ − yᵢ₊₁)/hᵢ₊₁ − (yᵢ₊₁ − yᵢ)/hᵢ].

Step 4: Add two boundary conditions.

For a natural spline:
M₀ = 0,
Mₙ = 0.

Step 5: Solve the resulting tr
"""