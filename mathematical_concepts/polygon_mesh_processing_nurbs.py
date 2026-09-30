"""
NURBS

NURBS stands for Non-Uniform Rational B-Spline.
It is one of the most important mathematical 
representations for curves and surfaces 
in computer-aided design (CAD), computer graphics,
animation, industrial design, automotive design,
and engineering.

A NURBS curve is defined using five ingredients:

* control points
* weights
* basis functions
* a knot vector
* a polynomial degree

The central equation is:

C(u) = [Σ N(i,p)(u) · w(i) · P(i)] / [Σ N(i,p)(u) · w(i)]

where:

P(i) = control points
w(i) = weights
N(i,p)(u) = basis functions
p = degree
u = parameter

Everything about NURBS follows from understanding this formula.
The most important new idea is the introduction of weights.

Suppose we have two points P₁ and P₂ and form the weighted average
C = [w₁P₁ + w₂P₂] / [w₁ + w₂].

If w₁ = w₂, the point lies halfway between them.
If w₁ becomes larger, the result moves closer to P₁.
If w₂ becomes larger, the result moves closer to P₂.

The same idea extends to a NURBS curve.
A control point with a larger weight pulls
the curve more strongly toward itself. 
A control point with a smaller weight has
less influence.

You can think of the weights as controlling 
the "strength" of each control point.

The word "rational" means
that the formula contains a ratio.

For example,

f(x) = (x² + 1)/(x + 3)

is a rational function because one expression
is divided by another.

Since the NURBS equation contains both
a numerator and denominator, it is called a
rational representation rather than a purely
polynomial one.

To understand where this formula comes from, 
it helps to introduce homogeneous coordinates.

Normally a two-dimensional point is written as
P = (x, y).

In homogeneous coordinates we instead write
P̃ = (w·x, w·y, w).

Similarly, a three-dimensional point
P = (x, y, z)

becomes
P̃ = (w·x, w·y, w·z, w).

The curve is first constructed in this
higher-dimensional space using ordinary
spline basis functions.

At the end, we divide by the last coordinate
to return to ordinary Euclidean space.

This division naturally produces
the rational NURBS formula.

The basis functions used in NURBS 
are called rational basis functions.

They are defined as
R(i,p)(u) = [N(i,p)(u) · w(i)] / [Σ N(j,p)(u) · w(j)].
Using these rational basis functions, 
the NURBS curve can be written as
C(u) = Σ R(i,p)(u) · P(i).

This form resembles many other spline representations,
but now the basis functions themselves depend on the weights.

An important property is Σ R(i,p)(u) = 1.
This is called the partition of unity property.

It guarantees that the curve is a
weighted combination of control points.

If all weights are positive,

w(i) > 0, then
R(i,p)(u) ≥ 0.

Together with Σ R(i,p)(u) = 1,
this implies that the curve is
a convex combination of control points.

Consequently, the curve lies inside
the convex hull of the relevant control points.

This gives NURBS good geometric stability.

One of the most important reasons NURBS 
became dominant in CAD is that they can
represent circles exactly.

By choosing suitable control points and 
carefully selected weights, a NURBS curve
can reproduce an exact circular arc rather 
than merely approximating one.

This is significant because circles, 
ellipses, parabolas, and hyperbolas 
are extremely common in engineering.

Collectively these shapes are called conic sections.

NURBS can represent all of them exactly.

The ability to represent conic sections
comes from the rational denominator.

Ordinary polynomial curves generally cannot 
represent these shapes exactly.

The denominator introduces additional 
flexibility that makes exact representation possible.

The weights have a clear geometric interpretation.

Imagine three control points P₀, P₁, and P₂.

If the weight associated with P₁ increases,
the curve moves closer to P₁.

If the weight decreases, the curve moves farther away.

Therefore the shape of the curve can be modified in two ways:

1. Move the control points.
2. Change the weights.

The basis functions still possess local support.

If a basis function N(i,p)(u) is zero 
outside a certain interval, then the
corresponding rational basis function R(i,p)(u)
is also zero there.

Therefore each control point influences only a
limited portion of the curve.

This local influence is one of the reasons NURBS 
are practical for modeling complex shapes.

The continuity of a NURBS curve depends on
the degree and the knot vector.

For degree p, a knot with multiplicity
r generally produces continuity C^(p-r) at that knot.

For example, for a cubic NURBS curve, p = 3.
A simple knot (r = 1) gives C² continuity.
A double knot (r = 2) gives C¹ continuity.
A triple knot (r = 3) gives C⁰ continuity.

Increasing knot multiplicity therefore 
reduces smoothness and allows sharper features.

The same ideas extend naturally from curves to surfaces.

Instead of a one-dimensional sequence of control points,
we use a two-dimensional grid of control points.

The surface is defined by
S(u,v) = ΣΣ R(i,j)(u,v) · P(i,j).

The control points form a control net, 
and the two parameters u and v determine 
movement across the surface.

By varying u and v, every point on
the surface can be evaluated.

NURBS surfaces are widely used because
they can represent both free-form shapes
and exact engineering geometry.

A useful mental picture is that 
every control point has two properties:
* a position
* a weight

The position tells the curve 
where the control point is located.

The weight tells the curve how strongly 
that control point attracts it.

The basis functions determine where 
that influence is active.

The knot vector determines how these influences
are distributed across the parameter domain.

The deepest idea behind NURBS is therefore:

A NURBS curve is a weighted combination of 
control points in which the weights are 
rational basis functions. By combining 
control points, basis functions, knot vectors, 
and adjustable weights, NURBS can represent 
both free-form shapes and exact conic sections
while maintaining smoothness and local control.

A concise definition is:
A NURBS curve is a rational spline curve defined 
by control points, weights, basis functions, 
and a knot vector, where the weights allow 
exact representation of conic sections and
provide additional geometric control over the shape.
"""
