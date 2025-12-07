"""
ELLIPSES AND ELLIPSOIDS — DEFINITIONS, FORMULAS, AND PROOFS

1. WHAT IS AN ELLIPSOID?

 An ellipsoid is the 3-dimensional analogue of an ellipse.
It is a “stretched sphere” whose semi-axes lengths may 
differ in three perpendicular directions.

# Standard Equation (Axis-Aligned Ellipsoid)

(x² / a²) + (y² / b²) + (z² / c²) = 1

Where:

* a = semi-axis along the x-axis
* b = semi-axis along the y-axis
* c = semi-axis along the z-axis

If a = b = c, the ellipsoid becomes a sphere.

# Example (Ellipsoid)

(x² / 4) + (y² / 9) + (z² / 16) = 1
Here a = 2, b = 3, c = 4.

# General Quadratic Form (General Ellipsoid)

Ax² + By² + Cz² + Dxy + Eyz + Fzx + Gx + Hy + Iz + J = 0
When the quadratic part is positive definite,
this describes an ellipsoid.

# Proof: Ellipsoid = Linear Transformation of a Sphere

Start from the unit sphere:

x'² + y'² + z'² = 1
(The equation provided, x'² + y'² + z'² = 1, 
is indeed the standard formula for a unit sphere 
centered at the origin (0, 0, 0) in a 
three-dimensional Cartesian coordinate system. 
In general, the formula for any sphere with center 
(h,k,l) and radius r is: (x-h)^{2}+ (y-k)^{2}+ (z-l)^{2}= r^{2}
For a unit sphere, the center is the origin (h=0,k=0,l=0) and
the radius is one (r=1), which simplifies the general formula
to the equation you provided.)

Apply scaling:

x = a x'
y = b y'
z = c z'

Substitute:

(x² / a²) + (y² / b²) + (z² / c²) = 1

Thus: every axis-aligned ellipsoid
is a stretched sphere.

# Volume of an Ellipsoid (Proof)

Unit sphere volume: V = (4/3)π

    (The formula for the volume of a
    sphere is given by: V= (4/3)π r^3)

    Scaling factors: a, b, c
    Volume scales by determinant abc

    (When you scale 3D space by factors a, b, c 
    in the x-, y-, and z-directions, 
    the linear transformation is represented by
    the diagonal matrix:

    A = 
    [ a   0   0 ]
    [ 0   b   0 ]
    [ 0   0   c ]

    The determinant of this matrix is:
    det(A) = abc
    The determinant tells you exactly how much 
    all volumes scale under the transformation.

    Therefore:
    New Volume = (abc) × Original Volume

    WHY THIS IS TRUE (Explanation)
    --------------------------------
    Consider a unit cube: it has volume 1.
    
    After scaling by a, b, c:
    - the unit edge in the x-direction becomes length a
    - the unit edge in the y-direction becomes length b
    - the unit edge in the z-direction becomes length c

    So the new box’s volume is:

    Volume = a × b × c = abc

    The determinant measures how a linear transformation
    changes the volume of the unit cube. 
    Since the scaling matrix stretches dimensions independently,
    its determinant is simply the product of the stretch factors.

    EXAMPLE
    --------
    Original volume: 10  
    Scaling: a = 2, b = 3, c = 1/2

    det(A) = 2 × 3 × (1/2) = 3  
    New volume = 3 × 10 = 30

    - A diagonal scaling matrix diag(a, b, c)
    scales volume by abc.
    - determinant = product of scaling factors 
    = volume multiplier.
    )

Therefore:

V = (4/3)πabc

# Cross-Sections Are Ellipses (Proof)

At fixed z = z₀:

(x² / a²) + (y² / b²) = 1 − (z₀² / c²)

Right-hand side positive for |z₀| < c.
Thus each horizontal slice is an ellipse.


# 2. WHAT IS AN ELLIPSE?

An ellipse is the set of all points in the plane
whose sum of distances to two fixed points (the foci)
is constant.

# Standard Equation

(x² / a²) + (y² / b²) = 1
with a ≥ b > 0.

If a = b, we get a circle.

# Major and Minor Axes

* Major axis = 2a
* Minor axis = 2b

# Foci of an Ellipse

Located on the major axis at:

F₁ = (−c, 0)
F₂ = (c, 0)

where:

c = √(a² − b²)

Thus 0 ≤ c < a.

# 3. PROOF: WHY THE FOCI SATISFY THE CONSTANT-SUM PROPERTY

# Definition of an ellipse

For any point P = (x, y) on the ellipse:

distance(P, F₁) + distance(P, F₂) = 2a
= constant.


# 4. PROOF THAT THE CARTESIAN EQUATION 
IMPLIES THE FOCAL PROPERTY


# PARAMETRIC FORM (CLEAN PROOF)

Ellipse parametric equations:

x = a cos t
y = b sin t
with b² = a² − c².

Let P = (a cos t, b sin t).
Foci: (−c, 0) and (c, 0).

Distance to right focus:

d₂ = √[(a cos t − c)² + b² sin² t]
Simplify using b² = a² − c²:
d₂ = a − c cos t

Distance to left focus:

d₁ = √[(a cos t + c)² + b² sin² t]
d₁ = a + c cos t

Sum:

d₁ + d₂ = (a + c cos t) + (a − c cos t) = 2a
A constant.

Thus the ellipse satisfies the focal definition.


# 5. PROOF THAT THE FOCAL DEFINITION IMPLIES
THE CARTESIAN EQUATION

Start with foci ±c and the defining property:

√[(x − c)² + y²] + √[(x + c)² + y²] = 2a

Let these square roots be R₁ and R₂.

R₁ + R₂ = 2a
→ R₁ = 2a − R₂

Square both sides:

R₁² = 4a² − 4aR₂ + R₂²

Substitute 
R₁² = (x − c)² + y² and
R₂² = (x + c)² + y².
Simplify to get:

R₂ = a + (c/a)x

Square again.
Using R₂² = (x + c)² + y²:

(x + c)² + y² = a² + 2cx + (c²/a²)x²

Expand, simplify, use b² = a² − c².
After rearranging and dividing:

(x² / a²) + (y² / b²) = 1

This proves the equivalence.


# 6. PROOF OF THE RELATION c² = a² − b²

Use the top point of the ellipse 
Q = (0, b).
Distances to foci:

QF₁ = √(c² + b²)
QF₂ = √(c² + b²)

Sum = 2√(c² + b²)

Definition says the sum must equal 2a:

2√(c² + b²) = 2a
√(c² + b²) = a
c² + b² = a²
c² = a² − b²


# 7. CENTER AND FOCI — CLARIFICATION

# Center of the ellipse

Only one center: (0, 0) in standard position.
More generally: (h, k).

# The two “centers” some people refer to

These are the two foci:

(h − c, k) and (h + c, k)
or vertical equivalents.


# 8. PARAMETRIC FORM OF AN ELLIPSE

x = a cos t
y = b sin t
with 0 ≤ t < 2π.

Useful in geometry, physics, and computer graphics.


# 9. AREA OF AN ELLIPSE (PROOF)


Area of circle r = 1:

A = π

Ellipse is circle stretched by factors
 a horizontally, b vertically.

Area scaling = a × b.

Therefore:

A = πab


# 10. RELATION BETWEEN ELLIPSE AND ELLIPSOID

* Slice an ellipsoid by any plane parallel 
to coordinate axes → ellipse.
* Ellipsoid is the 3D extension of ellipse.
* Both arise from linear transformations 
of sphere / circle.

"""