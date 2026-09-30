"""
TWO VIEWS OF A SURFACE
Based on Polygon Mesh Processing, Chapter 1

1. PARAMETRIC VIEW
A surface is described by parameters
that generate points on the surface.

For a circle of radius R:
    x = R cos(t)
    y = R sin(t)
where:
    0 <= t < 2π
So:
    t -> (x,y)

Example:

    t = 0     -> (R, 0)
    t = π/2   -> (0, R)
    t = π     -> (-R, 0)

As t changes, the point moves
along the circle.

For a 3D surface, usually two
parameters are needed:
S(u,v) = (x(u,v), y(u,v), z(u,v))

2. ZERO-SET / IMPLICIT VIEW

A surface is defined as all points
where a function equals zero.

For a circle:

    x² + y² = R²

Rewrite as:

    F(x,y) = x² + y² - R²

The circle is:

    F(x,y) = 0

Example for R = 1:

    (1,0):   F = 0  -> on circle
    (0,0):   F = -1 -> inside
    (2,0):   F = 3  -> outside

Thus:

    F < 0  -> inside
    F = 0  -> surface
    F > 0  -> outside


KEY DIFFERENCE

Parametric:

    parameter -> point on surface

    t -> (x,y)

Zero-set:

    point -> function value

    (x,y) -> F(x,y)

    F(x,y) = 0 means
    the point is on the surface.


SAME CIRCLE, TWO DESCRIPTIONS

Parametric:

    (x,y) = (R cos(t), R sin(t))

Zero-set:

    x² + y² - R² = 0


INTUITION

Parametric:
"How do I generate points
on the surface?"

Zero-set:
"Which points belong
to the surface?"

----
For curves
For spheres


"""