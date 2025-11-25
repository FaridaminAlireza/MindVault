"""
Curvature is a measure of how sharply a curve bends 
or changes direction at a specific point. A line has zero
curvature because it does not bend, while a small circle has
a large curvature because it changes direction quickly, and 
a large circle has a small curvature because it changes direction
slowly. Mathematically, curvature can be defined as the magnitude
of the rate of change of the unit tangent vector with respect to arc length. 

"""

"""
What curvature measures (intuitively)
Curvature tells you how sharply a curve bends at a point.
Equivalently: how fast the unit tangent direction rotates
per unit arc length. 
Large curvature = tight bending;
small curvature = gentle bending.
Curvature κ is nonnegative when given as a magnitude;
a signed curvature records the bend direction (left vs right).

Basic definitions (plain formulas)

1. Intrinsic definition (vector form):
   κ = ||dT/ds||
   where T is the unit tangent vector and s is arc length.

2. Parametric plane curve r(t) = (x(t), y(t)):
   κ(t) = | x'(t) y''(t) − y'(t) x''(t) | / ( (x'(t)^2 + y'(t)^2)^(3/2) )

3. Function y = f(x) (viewed as parametric with x = t):
   κ(x) = | f''(x) | / ( 1 + (f'(x))^2 )^(3/2)

4. Space curve in R^3, r(t):
   κ(t) = || r'(t) × r''(t) || / || r'(t) ||^3

How the y = f(x) formula comes from the parametric formula (step by step)

1. Represent the graph as r(x) = (x, f(x)). Treat x as parameter t.
2. Compute derivatives: r'(x) = (1, f'(x)), r''(x) = (0, f''(x)).
3. Plug into parametric numerator: | x' y'' − y' x'' | =
 | 1 * f''(x) − f'(x) * 0 | = | f''(x) |.
4. Denominator: (x'^2 + y'^2)^(3/2) = (1 + (f'(x))^2)^(3/2).
5. Therefore κ(x) = | f''(x) | / (1 + (f'(x))^2)^(3/2).

Geometric interpretation and osculating circle
At a point the curve can be locally approximated by
a circle (the osculating circle). 
Its radius ρ (radius of curvature) is  ρ = 1 / κ.
So large curvature → small osculating circle (tight bend);
zero curvature → infinite radius → straight line.

Signed curvature (optional)
If you want to keep orientation (which side the curve bends toward),
use the signed version for y = f(x):
κ_signed = f''(x) / (1 + (f'(x))^2)^(3/2)
Positive/negative indicates bend direction relative to chosen orientation.

Insightful examples (step-by-step with arithmetic)

A — parabola y = x^2

1. Compute derivatives:
   f'(x) = 2x
   f''(x) = 2

2. Plug into curvature formula:
   κ(x) = | 2 | / ( 1 + (2x)^2 )^(3/2)
   = 2 / ( 1 + 4x^2 )^(3/2)

3. Evaluate at x = 0:
   4x^2 = 4 * 0^2 = 4 * 0 = 0
   1 + 4x^2 = 1 + 0 = 1
   (1)^(3/2) = 1
   κ(0) = 2 / 1 = 2
   Radius of curvature ρ(0) = 1 / κ(0) = 1 / 2 = 0.5

4. Evaluate at x = 1:
   4x^2 = 4 * 1^2 = 4 * 1 = 4
   1 + 4x^2 = 1 + 4 = 5
   (1 + 4x^2)^(3/2) = 5^(3/2)
   compute 5^(3/2) as 5 * sqrt(5).
   sqrt(5) ≈ 2.23606797749979  (standard numerical value)
   5 * sqrt(5) ≈ 5 * 2.23606797749979
   = 11.18033988749895
   κ(1) = 2 / 11.18033988749895
   ≈ 0.17888543819998318
   (rounded: κ(1) ≈ 0.178885)
   Radius ρ(1) = 1 / κ(1) ≈ 5.585... 
   (more precisely 11.18033988749895 / 2 =
   5.590169943749475 → note 1/0.178885... = same)

Interpretation for the parabola:

* At the vertex (x=0) curvature is highest (κ=2),
so the parabola is bending most there.
* As x increases, curvature decreases; far out 
the parabola becomes gentler (κ → 0), 
which matches the graph flattening out.

B — circle of radius R (parametric example)

1. Parametrize: x(t) = R cos t, y(t) = R sin t.
2. Compute derivatives:
   x'(t) = −R sin t,  x''(t) = −R cos t
   y'(t) =  R cos t,  y''(t) = −R sin t
3. Plug into parametric formula numerator:
   x' y'' − y' x'' 
   = (−R sin t)(−R sin t) − (R cos t)(−R cos t)
   = R^2 sin^2 t + R^2 cos^2 t
   = R^2 (sin^2 t + cos^2 t) = R^2
   Absolute value: |R^2| = R^2 (R > 0)
4. Denominator:
   x'^2 + y'^2 = R^2 sin^2 t + R^2 cos^2 t = R^2
   (R^2)^(3/2) = R^3
5. κ = R^2 / R^3 = 1 / R
   So curvature is constant and equals reciprocal of radius.
   Radius of curvature ρ = R.

Practical notes and uses

* Curvature is used in geometry, computer graphics, path planning 
(robots/vehicles), interpolation (creating smooth splines), 
differential geometry, and physics (motion on curved paths).
* In design and manufacturing, curvature continuity (C2 continuity) 
is important for visually smooth transitions.
* When computing numerically from sampled data, noise can badly affect
estimates of derivatives; smoothing or fitting a local polynomial
before differentiating is common.

Summary

* Definition: κ = ||dT/ds|| (change of unit tangent per unit arc length).
* For y = f(x): κ(x) = | f''(x) | / (1 + (f'(x))^2)^(3/2).
* For parametric plane curve r(t): κ = | x' y'' − y' x'' | / (x'^2 + y'^2)^(3/2).
* Radius of curvature ρ = 1/κ.
* Example: y = x^2 → κ(x) = 2 / (1 + 4x^2)^(3/2); κ(0)=2, κ(1)≈0.178885.

"""