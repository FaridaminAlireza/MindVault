"""
Arc Length (Perimeter) of an Ellipse Using Parametric Equations

INTRODUCTION

The problem of finding the perimeter (arc length) of an ellipse is a
classical problem in calculus and geometry. While the circle admits a
simple closed-form expression for its perimeter, the ellipse does not.
This difficulty led historically to the development of elliptic
integrals.

In this document, we give a complete and well-organized derivation of
the arc length of an ellipse using parametric equations. All geometric
and analytic steps are justified carefully, including: - why the chosen
parametric equations describe an ellipse, - why the differential arc
length satisfies ds = sqrt((dx)^2 + (dy)^2), - how the arc length
integral arises, - and why no elementary closed-form solution exists.

1. GEOMETRY OF THE ELLIPSE

An ellipse centered at the origin with semi-major axis a (horizontal)
and semi-minor axis b (vertical) is defined by:

    x^2 / a^2 + y^2 / b^2 = 1

This equation represents all points whose scaled squared distances from
the origin sum to one. When a = b, the ellipse reduces to a circle of
radius a.

2. JUSTIFICATION OF THE PARAMETRIC EQUATIONS

We begin with the fundamental trigonometric identity:

    cos^2 t + sin^2 t = 1

Multiply the cosine term by a^2 and the sine term by b^2:

    (a cos t)^2 / a^2 + (b sin t)^2 / b^2 = 1

This expression has exactly the same form as the equation of the
ellipse. Therefore, defining:

    x = a cos t
    y = b sin t

guarantees that every point (x, y) satisfies the ellipse equation.

As t varies continuously from 0 to 2π, the point (x, y) moves smoothly
along the ellipse and returns to its starting position, tracing the
entire curve exactly once. This parametrization is natural, smooth, and
exploits the symmetry of the ellipse.

3. INTERPRETATION OF THE PARAMETER t

The parameter t does not represent the angle measured from the center of
the ellipse. Instead, it should be viewed as the angle of a
corresponding point on the unit circle.

The ellipse can be understood as a stretched unit circle: - the
x-coordinate is stretched by a factor of a, - the y-coordinate is
stretched by a factor of b.

This geometric interpretation explains why trigonometric functions
appear in the parametrization.

4. DIFFERENTIAL ARC LENGTH IN THE PLANE

Consider two very close points on a smooth curve:

    (x, y) and (x + dx, y + dy)

In Euclidean geometry, the distance between these points is given by the
Pythagorean theorem:

    distance = sqrt((dx)^2 + (dy)^2)

When the separation becomes infinitesimally small, this distance is
defined as the differential arc length ds:

    ds = sqrt((dx)^2 + (dy)^2)

This is not an approximation but a definition arising from the Euclidean
metric.

5. ARC LENGTH FOR A PARAMETRIC CURVE

If the curve is described parametrically by x(t) and y(t), then:

    dx = (dx/dt) dt
    dy = (dy/dt) dt

Substituting into the arc length formula gives:

    ds = sqrt((dx/dt)^2 + (dy/dt)^2) dt

The total arc length between t = t1 and t = t2 is therefore:

    s = ∫[t1 to t2] sqrt((dx/dt)^2 + (dy/dt)^2) dt

This formula follows rigorously from limits of polygonal approximations.

6. APPLYING THE FORMULA TO THE ELLIPSE

Using the parametric equations:

    x = a cos t
    y = b sin t

compute derivatives:

    dx/dt = -a sin t
    dy/dt =  b cos t

Substitute into the arc length formula:

    ds = sqrt(a^2 sin^2 t + b^2 cos^2 t) dt

7. TOTAL PERIMETER OF THE ELLIPSE

The full perimeter L is obtained by integrating over one full
revolution:

    L = ∫[0 to 2π] sqrt(a^2 sin^2 t + b^2 cos^2 t) dt

Because the ellipse is symmetric in all four quadrants, this simplifies
to:

    L = 4 ∫[0 to π/2] sqrt(a^2 sin^2 t + b^2 cos^2 t) dt

8. CONNECTION TO ELLIPTIC INTEGRALS

The integral appearing in the ellipse perimeter formula cannot be
expressed using elementary functions (algebraic, trigonometric,
exponential, or logarithmic functions).

It defines a special function known as the complete elliptic integral of
the second kind. This explains why the ellipse perimeter has no simple
closed-form expression.

9. APPROXIMATION FORMULAS (RAMANUJAN)

Because exact evaluation is difficult, accurate approximations are
commonly used. One famous approximation due to Ramanujan is:

    L ≈ π [ 3(a + b) - sqrt((3a + b)(a + 3b)) ]

This approximation is remarkably accurate for most ellipses encountered
in practice.

10. CONCLUSION

The perimeter of an ellipse provides a fundamental example where
geometry, calculus, and special functions intersect. Using parametric
equations and the Euclidean notion of distance, we obtain an exact
integral formula for the arc length. Although the integral cannot be
evaluated in elementary terms, it is well understood and widely used in
both theoretical and applied mathematics.

"""