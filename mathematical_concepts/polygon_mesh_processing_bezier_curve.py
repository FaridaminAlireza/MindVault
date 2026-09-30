"""
CUBIC BÉZIER CURVE

1. Basic idea

A cubic Bézier curve is a parametric polynomial curve 
controlled by four control points: P₀, P₁, P₂, P₃.
The curve starts at P₀ and ends at P₃.

The middle points P₁ and P₂ 
generally do not lie on the curve. 
Instead, they control 
its shape and tangent directions.

The cubic Bézier curve is
B(t) = (1 − t)³P₀ + 3(1 − t)²tP₁ + 3(1 − t)t²P₂ + t³P₃,
where 0 ≤ t ≤ 1.
The curve is called cubic 
because the highest power of t is 3.

2. Why use a parameter t?
A Bézier curve is parametric.

Instead of describing the curve as y = f(x),
we describe both coordinates as functions of t:
B(t) = (x(t), y(t)).
As t moves from 0 to 1, we move along the curve.

t = 0 gives the beginning of the curve.
t = 1 gives the end of the curve.

Values between 0 and 1 
give points between the endpoints.

3. The Bernstein basis functions
The cubic Bézier equation can be written as
B(t) = b₀(t)P₀ + b₁(t)P₁ + b₂(t)P₂ + b₃(t)P₃,

where
b₀(t) = (1 − t)³,
b₁(t) = 3(1 − t)²t,
b₂(t) = 3(1 − t)t²,
b₃(t) = t³.

These are called the cubic Bernstein basis polynomials.
Each basis function determines 
how strongly its corresponding control point 
influences the curve at a particular value of t.

4. The basis functions add to 1
An important property is
b₀(t) + b₁(t) + b₂(t) + b₃(t) = 1.

To prove this, add the four functions:
(1 − t)³ + 3(1 − t)²t + 3(1 − t)t² + t³.

This is exactly the binomial expansion
[(1 − t) + t]³.

Since (1 − t) + t = 1,
we obtain [(1 − t) + t]³ = 1.
Therefore,
b₀(t) + b₁(t) + b₂(t) + b₃(t) = 1.

This property is called partition of unity.

5. Why partition of unity matters

The Bézier curve is

B(t) = b₀P₀ + b₁P₁ + b₂P₂ + b₃P₃.

The coefficients satisfy
b₀ + b₁ + b₂ + b₃ = 1.
Also, for 0 ≤ t ≤ 1,
b₀, b₁, b₂, b₃ ≥ 0.

Therefore, B(t) is a 
convex combination of the four control points.

This means that the entire Bézier curve 
lies inside the convex hull of the control points.

Geometrically, imagine stretching a rubber band around 
the four control points. The Bézier curve cannot leave
the region enclosed by that rubber band.

This property is very useful in geometric modeling and CAD.

6. Proof that the curve starts at P₀
Set t = 0:
B(0) = (1 − 0)³P₀ + 3(1 − 0)²(0)P₁ + 3(1 − 0)(0)²P₂ + (0)³P₃.
All terms except the first become zero:
B(0) = P₀. Therefore, B(0) = P₀.
So the curve starts exactly at P₀.

7. Proof that the curve ends at P₃

Set t = 1:
B(1) = (1 − 1)³P₀ + 3(1 − 1)²(1)P₁ + 3(1 − 1)(1)²P₂ + (1)³P₃.
All terms except the last become zero:
B(1) = P₃. Therefore, B(1) = P₃.
So the curve ends exactly at P₃.

8. The endpoint tangents
The control points P₁ and P₂ have an especially important role.

Differentiate the Bézier equation:
B′(t) = −3(1 − t)²P₀ + 3[(1 − t)² − 
2t(1 − t)]P₁ + 3[2t(1 − t) − t²]P₂ + 3t²P₃.

Now evaluate at t = 0.
B′(0) = −3P₀ + 3P₁.
Therefore, B′(0) = 3(P₁ − P₀).
Thus, the initial tangent direction is determined by the vector
P₁ − P₀.
In other words, the first segment of the control polygon
determines the tangent direction at the beginning of the curve.

9. The final tangent
Now evaluate the derivative at t = 1.
B′(1) = 3(P₃ − P₂).
Therefore, B′(1) = 3(P₃ − P₂).
The final tangent direction is therefore determined by
P₃ − P₂.

So we have:
P₀ → P₁ controls the initial tangent.
P₂ → P₃ controls the final tangent.

This is one of the most important 
geometric interpretations of a cubic Bézier curve.

10. Why the factor 3 appears
The factor 3 comes from the fact 
that the curve has degree 3.

For a Bézier curve of general degree n,
B′(0) = n(P₁ − P₀),
and
B′(1) = n(Pₙ − Pₙ₋₁).
The factor affects the speed at which 
the curve is traversed as t changes.

The direction of the tangent is 
determined by the corresponding 
control-point difference.

11. Deriving the Bézier curve 
using linear interpolation

The cubic Bézier curve has a particularly 
beautiful geometric construction.

Start with four control points: P₀, P₁, P₂, P₃.
First, linearly interpolate between neighboring points.

Define
Q₀ = (1 − t)P₀ + tP₁,
Q₁ = (1 − t)P₁ + tP₂,
Q₂ = (1 − t)P₂ + tP₃.

These three points lie on the three control-polygon edges.

As t changes, Q₀, Q₁, and Q₂ move along those edges.

12. Second interpolation level

Now interpolate between the Q points:

R₀ = (1 − t)Q₀ + tQ₁,

R₁ = (1 − t)Q₁ + tQ₂.

There are now only two points.

Again, these points move as t changes.

13. Third interpolation level

Finally, interpolate between R₀ and R₁:

B(t) = (1 − t)R₀ + tR₁.

There is now one point.

That point is the Bézier curve point 
corresponding to parameter t.

This construction is called de Casteljau's algorithm.

14. Deriving the cubic formula

Start with
Q₀ = (1 − t)P₀ + tP₁,
Q₁ = (1 − t)P₁ + tP₂,
Q₂ = (1 − t)P₂ + tP₃.

Now calculate R₀:
R₀ = (1 − t)Q₀ + tQ₁.

Substitute Q₀ and Q₁:
R₀ = (1 − t)[(1 − t)P₀ + tP₁] + t[(1 − t)P₁ + tP₂].
Expanding gives
R₀ = (1 − t)²P₀ + 2t(1 − t)P₁ + t²P₂.
Similarly,
R₁ = (1 − t)²P₁ + 2t(1 − t)P₂ + t²P₃.

Now perform the final interpolation:
B(t) = (1 − t)R₀ + tR₁.
Substituting R₀ and R₁ gives
B(t) = (1 − t)[(1 − t)²P₀ + 2t(1 − t)P₁ + t²P₂] +
 t[(1 − t)²P₁ + 2t(1 − t)P₂ + t²P₃].

Collecting the P₀ terms gives
(1 − t)³P₀.

Collecting the P₁ terms gives
2t(1 − t)²P₁ + t(1 − t)²P₁ = 3t(1 − t)²P₁.

Collecting the P₂ terms gives
t²(1 − t)P₂ + 2t²(1 − t)P₂ = 3t²(1 − t)P₂.

Collecting the P₃ terms gives
t³P₃.

Therefore,
B(t) = (1 − t)³P₀ + 3(1 − t)²tP₁ + 3(1 − t)t²P₂ + t³P₃.

This proves the cubic Bézier equation directly 
from repeated linear interpolation.

15. A concrete example

Suppose

P₀ = (0, 0),
P₁ = (1, 2),
P₂ = (3, 2),
P₃ = (4, 0).

The curve is
B(t) = (1 − t)³(0,0) + 3(1 − t)²t(1,2) + 3(1 − t)t²(3,2) + t³(4,0).

At t = 0,
B(0) = (0,0).

At t = 1,
B(1) = (4,0).

Now consider t = 0.5.
The four basis functions become

b₀ = 0.125,
b₁ = 0.375,
b₂ = 0.375,
b₃ = 0.125.

Therefore,
B(0.5) = 0.125P₀ + 0.375P₁ + 0.375P₂ + 0.125P₃.
Substituting the points gives B(0.5) = (2, 1.5).

Notice that the curve point is produced as 
a weighted combination of all four control points.

16. The geometric meaning of the control points

P₀ determines the starting position.
P₃ determines the ending position.
P₁ strongly controls the initial direction.
P₂ strongly controls the final direction.

The positions of P₁ and P₂ also influence 
the curvature and overall shape of the curve.

Importantly, P₁ and P₂ usually do not lie on the curve.
They are control points rather than interpolation points.

17. Why is the curve called "cubic"?

The equation contains powers up tot³.
Therefore, it is a polynomial of degree 3.
The general cubic polynomial has the form
a + bt + ct² + dt³.

The Bézier representation is another way of 
expressing a cubic polynomial, but instead of 
using coefficients a, b, c, d directly, 
it uses four geometric control points 
and Bernstein basis functions.

18. Bézier form versus ordinary polynomial form

An ordinary cubic polynomial can be written as
f(t) = a + bt + ct² + dt³.

A cubic Bézier curve is written as
B(t) = b₀(t)P₀ + b₁(t)P₁ + b₂(t)P₂ + b₃(t)P₃.

The important difference is that 
the Bézier representation has 
a direct geometric interpretation.

The four control points tell us 
how the curve should behave.

This makes Bézier curves particularly 
convenient for geometric design.

19. The convex-hull property

Because b₀ + b₁ + b₂ + b₃ = 1
and bᵢ ≥ 0,

the Bézier curve is a convex combination of its control points.

Therefore, B(t) must lie inside the convex hull of
P₀, P₁, P₂, P₃.
This gives us a powerful geometric guarantee:
the curve cannot suddenly move far outside 
the region determined by its control points.
This is one reason Bézier curves are convenient 
for interactive design.

20. The control polygon
The polygon formed by connecting
P₀ → P₁ → P₂ → P₃
is called the control polygon.

The Bézier curve is influenced by this polygon.
The first edge P₀ → P₁ controls the starting tangent.
The last edge P₂ → P₃ controls the ending tangent.
The middle portion P₁ → P₂ strongly affects the 
middle shape of the curve.

21. Bézier curves and smoothness

Suppose two Bézier curves are joined.
To obtain C⁰ continuity, they must meet at the same point.
For example, if the first curve ends at P₃ 
and the second begins at Q₀, then P₃ = Q₀.

For C¹ continuity, their tangent directions must also agree.
The first curve has final tangent 3(P₃ − P₂).
The second curve has initial tangent 3(Q₁ − Q₀).
Therefore, C¹ continuity requires these tangent vectors to be equal:
3(P₃ − P₂) = 3(Q₁ − Q₀).
Equivalently, P₃ − P₂ = Q₁ − Q₀.

Thus, Bézier control points provide 
a direct way of constructing smooth 
joins between curve segments.

22. Bézier curve versus cubic spline
A cubic Bézier curve uses four control points
to define one cubic segment.

A cubic spline consists of multiple polynomial pieces
joined together with continuity conditions.

A cubic spline is usually designed to 
interpolate specified data points.

A Bézier curve is usually designed using 
control points that influence the shape.

Therefore:
Cubic spline → interpolation-oriented.
Bézier curve → control-point-oriented.
Bézier curves are especially convenient 
for interactive geometric design.

23. The key conceptual difference

For interpolation, we might say:
"Pass through these points."

For Bézier control, we instead say:
"Shape the curve using these control points."

This distinction is fundamental.

24. The deeper mathematical idea

A cubic Bézier curve combines three important ideas:

1. Polynomial representation
The curve is a degree-3 polynomial.
2. Basis functions
The Bernstein polynomials determine 
the influence of each control point.
3. Geometric control
The control points determine position,
tangent directions, and overall shape.

Therefore, the Bézier representation connects 
algebra and geometry very naturally.

25. Connection to CAD and geometric modeling

Bézier curves are important in CAD, 
computer graphics, 
typography, 
and geometric modeling.

They are useful because they provide:
local geometric control,
smooth curves,
simple evaluation,
clear endpoint behavior,
convex-hull containment,
and intuitive control-point manipulation.

However, a single cubic Bézier segment 
can only represent a limited range of shapes.
More complicated curves are therefore often 
constructed from several Bézier segments 
or by using B-splines and NURBS.
"""