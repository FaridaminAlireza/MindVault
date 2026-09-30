"""
B-SPLINES

1. Why do we need B-splines?

A Bézier curve is defined using control points 
and basis functions. For a cubic Bézier curve, 
we have exactly four control points, 
P₀, P₁, P₂, and P₃, and the curve is 
B(t) = (1−t)³P₀ + 3(1−t)²tP₁ + 3(1−t)t²P₂ + t³P₃. 
The basis functions determine how strongly 
each control point influences the curve.

This works very well for a single curve segment.
However, suppose we want to model a complicated curve 
using ten or twenty control points. 
A single cubic Bézier curve cannot use all of them.
We could construct several Bézier segments, 
but then we have to decide how the segments should
meet and how to enforce C⁰, C¹, or C² continuity between them.

B-splines provide a more systematic solution.
Instead of treating the curve as a collection of 
separately defined Bézier curves, we define 
one curve using many control points and
a collection of basis functions with local support.

The basic idea is therefore: C(u) = Σ Nᵢ,ₚ(u) Pᵢ
where Pᵢ are the control points, 
Nᵢ,ₚ(u) are the B-spline basis functions,
p is the polynomial degree,
and u is the curve parameter.

The most important idea to remember is:
A B-spline is a curve obtained by 
blending control points 
with B-spline basis functions.

2. Connection with Bézier curves

You can understand a B-spline 
as a generalization of the Bézier idea.

For Bézier, we have
B(t) = Σ bᵢ(t)Pᵢ
where bᵢ(t) are Bernstein basis functions.

For a B-spline, we have
C(u) = Σ Nᵢ,ₚ(u)Pᵢ
where Nᵢ,ₚ(u) are B-spline basis functions.

So the basic structure has not changed. 
In both cases, the curve is 
a weighted combination of control points.

The important difference is that Bézier basis functions
are defined directly from the parameter t, 
while B-spline basis functions are defined using 
a knot vector. This allows B-splines to use many control points 
while maintaining local control over the curve.

3. The problem with Bézier curves

Consider a cubic Bézier curve with four control points:
P₀, P₁, P₂, P₃.
Every Bernstein basis function is nonzero 
over essentially the whole parameter interval 0 ≤ t ≤ 1. 
Therefore, moving one control point can influence the entire curve.

For example, if we move P₁, the whole Bézier curve changes.
This is called global control.

Now imagine a curve with 20 control points. 
If moving one control point changes the entire curve,
editing a small region becomes inconvenient.

B-splines solve this using local support.
A particular B-spline control point affects 
only part of the curve. Therefore, if you move 
one control point, the modification is localized
to a region around that control point.

4. The B-spline curve equation
The general B-spline curve is C(u) = Σᵢ Nᵢ,ₚ(u)Pᵢ.
This equation has three important components.

- Pᵢ is a control point. It determines the 
geometric information used to shape the curve.
- Nᵢ,ₚ(u) is a basis function. It determines how strongly 
Pᵢ contributes to the curve at parameter u.
- p is the degree of the polynomial used by the basis functions.

Therefore, if we evaluate the curve at a particular value of u,
we calculate the basis-function values and use them as weights 
for the control points.

For example, suppose at some parameter value u  we obtain 
N₂,₃(u) = 0.1, N₃,₃(u) = 0.3, N₄,₃(u) = 0.5, and N₅,₃(u) = 0.1. 
Then the curve point is C(u) = 0.1P₂ + 0.3P₃ + 0.5P₄ + 0.1P₅. 
Notice that only four control points participate in this 
particular calculation.

5. What does the degree mean?
The degree p determines the degree of the polynomial
pieces used by the B-spline.
If p = 0, the basis functions are piecewise constant. 
If p = 1, they are piecewise linear. 
If p = 2, they are piecewise quadratic. 
If p = 3, they are piecewise cubic.

Cubic B-splines are particularly important 
because they provide smooth curves 
while remaining relatively simple mathematically.
When we say "cubic B-spline", we therefore mean that 
p = 3 and that the curve is constructed 
from cubic polynomial pieces.

6. What is a knot vector?

The next important concept is the knot vector.
A knot vector is a nondecreasing sequence of parameter values:

U = {u₀, u₁, ..., uₘ}.
For example, we might have
U = {0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4}.
The values in this sequence are called knots.
The knots divide the parameter domain into intervals 
called knot spans. For example, the interior knots 
1, 2, 3, and 4 divide the parameter domain into
intervals [1,2], [2,3], and [3,4].

The knot vector is one of the major differences 
between Bézier curves and B-splines. In a Bézier curve,
the basis functions are fixed Bernstein polynomials.
In a B-spline, the knot vector helps determine where 
each basis function is active and how its influence 
is distributed along the parameter domain.

7. Why do knots matter?
Imagine moving along 
the parameter axis u from left to right.
At one location, one group of control points 
influences the curve. As u moves further, 
some of those control points gradually lose influence 
while neighboring control points gain influence.
The knots determine where these changes occur.
This means that the curve is not represented 
by one single cubic polynomial over its entire length.
Instead, it consists of polynomial pieces 
that are smoothly connected.

For a cubic B-spline, each knot span corresponds 
to a cubic polynomial piece, although the basis-function
representation is usually much more convenient 
than explicitly writing each polynomial piece.

8. Constructing the basis functions
The B-spline basis functions are constructed recursively.
The starting point is the degree-zero basis function.

For degree zero, we define
Nᵢ,₀(u) = 1 if uᵢ ≤ u < uᵢ₊₁, and Nᵢ,₀(u) = 0 otherwise.
This means that a degree-zero basis function is simply 
active over one knot interval and zero everywhere else.
For example, if the knots contain 0, 1, 2, and 3, 
then one degree-zero basis function may be active 
between 0 and 1, another between 1 and 2, and another 
between 2 and 3.

So degree-zero B-spline basis functions look 
conceptually like rectangular blocks.

9. From degree zero to degree one
The next step is to construct 
degree-one basis functions.

The Cox–de Boor recursion formula is
Nᵢ,ₚ(u) = 
[(u − uᵢ)/(uᵢ₊ₚ − uᵢ)]         Nᵢ,ₚ₋₁(u) + 
[(uᵢ₊ₚ₊₁ − u)/(uᵢ₊ₚ₊₁ − uᵢ₊₁)] Nᵢ₊₁,ₚ₋₁(u).

This formula may initially look complicated, 
but its basic meaning is simple.

To construct a degree-p basis function, 
we combine two neighboring degree-(p−1) basis functions.
Therefore the construction works like this:
degree 0 → degree 1 → degree 2 → degree 3 → ...
Each step blends neighboring
lower-degree basis functions together.

10. Understanding the recursion conceptually

Consider the first coefficient in the recursion:
(u−uᵢ)/(uᵢ₊ₚ−uᵢ).
As u moves through the relevant interval, 
this coefficient changes gradually.

The second coefficient, (uᵢ₊ₚ₊₁−u)/(uᵢ₊ₚ₊₁−uᵢ₊₁),
changes in the opposite direction.

Therefore, the two lower-degree basis 
functions are smoothly blended.

This is the important conceptual point: 
B-spline basis functions are not chosen arbitrarily.
They are built recursively by blending neighboring 
lower-degree basis functions.

11. A simple analogy with Bézier

For a cubic Bézier curve, the Bernstein basis functions are
b₀(t) = (1−t)³, 
b₁(t) = 3(1−t)²t, 
b₂(t) = 3(1−t)t², 
and b₃(t) = t³.
These four functions determine the weights 
of the four control points.

For a B-spline, we also have basis functions 
that determine the weights, but they are constructed 
recursively from the knot vector.

So you should not think:
"B-splines are a completely different idea from Bézier."
Instead think: "B-splines use the same control-point and
basis-function idea, but make the basis functions local 
and flexible."

12. Local support
The most important property of 
B-spline basis functions is local support.

For a degree-p B-spline basis function Nᵢ,ₚ(u),
the function is nonzero only over a limited region.
Its support is [uᵢ, uᵢ₊ₚ₊₁).
Outside this interval, Nᵢ,ₚ(u) = 0.

For a cubic B-spline, p = 3, so the support covers 
four consecutive knot spans. This means that at any 
particular value of u, only a small number of 
basis functions are active.

That is why a B-spline can have many control points
without every control point influencing the entire curve.

13. Why local support gives local control

Suppose we have ten control points:
P₀, P₁, ..., P₉.

The curve is C(u) = Σᵢ Nᵢ,₃(u)Pᵢ.
Suppose at some particular u, 
only N₂,₃, N₃,₃, N₄,₃, and N₅,₃ are nonzero.

Then the curve point is simply
C(u) = N₂,₃(u)P₂ + N₃,₃(u)P₃ + N₄,₃(u)P₄ + N₅,₃(u)P₅.
The other control points do not contribute at all.

If we move P₈, this particular curve point does not change.
As we move further along the curve, 
P₈ eventually becomes active and starts affecting the curve.

This is the mathematical reason for local control.

14. Partition of unity
B-spline basis functions satisfy an important property:
Σᵢ Nᵢ,ₚ(u) = 1. This is called partition of unity.
It is exactly analogous to the property you saw 
for Bézier basis functions.

For cubic Bézier curves,
b₀(t) + b₁(t) + b₂(t) + b₃(t) = 1.
For B-splines, the sum of all active basis functions 
is also 1. This means that the curve point is 
a weighted combination of control points 
whose weights add to one.

15. Nonnegativity and the convex hull

B-spline basis functions are also nonnegative: Nᵢ,ₚ(u) ≥ 0.
Together with partition of unity, Σᵢ Nᵢ,ₚ(u) = 1,
this means that the curve is a convex combination of 
the relevant control points.
Consequently, the curve lies inside the convex hull of 
the relevant control points.
This is another property that B-splines share with Bézier curves.
The difference is that for a B-spline, 
the relevant convex hull is local because 
only nearby control points participate.

16. A cubic B-spline with ten control points

Suppose we have ten control points:
P₀, P₁, P₂, P₃, P₄, P₅, P₆, P₇, P₈, P₉.

We choose degree p = 3.
Then the curve is
C(u) = N₀,₃(u)P₀ + N₁,₃(u)P₁ + ... + N₉,₃(u)P₉.
Although ten control points are available, 
only a small number are active 
at any particular location.

As u moves from left to right, 
the active group changes.

Conceptually, the influence moves like this:

P₀ P₁ P₂ P₃ → first region
P₁ P₂ P₃ P₄ → next region
P₂ P₃ P₄ P₅ → next region
P₃ P₄ P₅ P₆ → next region
and so on.
This overlapping structure is 
what allows the entire curve 
to remain smooth while each control 
point has only local influence.

17. B-splines are piecewise polynomials

A B-spline is not one giant polynomial.
Instead, it is piecewise polynomial.
Suppose the knots are u₀ < u₁ < u₂ < u₃ < ...
Then between two consecutive knots, 
for example between u₂ and u₃, 
the curve can be represented by a polynomial.

For a cubic B-spline, that polynomial is cubic.

When we cross a knot, 
we move to another cubic polynomial piece.
The important point is 
that the pieces are not independent.
The B-spline basis functions make them 
overlap and connect smoothly.

18. Continuity

Because neighboring polynomial pieces overlap,
B-splines can provide smooth transitions between them.

For a cubic B-spline with ordinary simple interior knots,
the curve is generally C² continuous.
C² continuity means that the following
are continuous across the knot:
- the position C(u),
- the first derivative C'(u),
- and the second derivative C''(u).
Therefore there is no jump in 
position, tangent, or curvature-related second-derivative 
information at a simple interior knot.

This is one reason cubic B-splines are 
useful for smooth geometric modeling.

19. Knot multiplicity

Knots can be repeated.
For example, instead of
{0, 1, 2, 3}, we might have {0, 1, 2, 2, 3}.
The number of times a knot appears is called
its multiplicity.

Knot multiplicity affects continuity.
For a degree-p B-spline, a knot of multiplicity r 
generally gives continuity C^(p−r) at that knot.

For a cubic B-spline, p = 3.
A simple knot, with r = 1, gives C² continuity.
A double knot, with r = 2, gives C¹ continuity.
A triple knot, with r = 3, gives C⁰ continuity.

Increasing the knot multiplicity therefore
reduces continuity and allows the curve to
become sharper at that location.

20. Open knot vectors
A particularly important type of knot vector
is the open knot vector.

For a cubic B-spline, an example is
U = {0,0,0,0,1,2,3,4,4,4,4}.
Notice that the first knot is repeated four times 
and the last knot is also repeated four times.

Why four? Because the degree is three, so p + 1 = 4.
This repeated-endpoint construction gives 
useful endpoint behavior. In particular, with 
the standard open knot-vector construction,
the curve starts at the first control point 
and ends at the last control point.

21. Uniform and nonuniform B-splines

A uniform B-spline uses 
equally spaced interior knots.
For example, {0,0,0,0,1,2,3,4,5,5,5,5}.

A nonuniform B-spline may instead use
{0,0,0,0,1,1.5,3,4.7,5,5,5,5}.
The spacing of the knots affects how 
the basis functions are distributed and 
therefore gives additional control over the curve.

This is why the knot vector is not just 
a technical detail. It is one of the mechanisms 
that determines the geometry of the B-spline.

22. Number of control points and knots

Suppose we have n+1 control points and degree p.
The standard relationship is m = n + p + 1,
where the knot vector contains m+1 knots.
Therefore, the number of knots is n + p + 2.

For example, 
suppose we have six control points 
and a cubic B-spline. Then
n + 1 = 6 and p = 3.
Therefore the number of knots is
6 + 3 + 1 = 10.
So we need ten knots in the knot vector.

23. B-spline versus Bézier

The most useful comparison is this.
A cubic Bézier curve uses four control points 
and four Bernstein basis functions. 
All four basis functions are associated with 
the entire Bézier segment, so changing 
one control point can affect the whole segment.

A cubic B-spline can use many control points.
Its basis functions have local support,
so only a few nearby control points affect
the curve at a particular parameter value.
Therefore, Bézier curves are especially convenient 
for individual curve segments, while B-splines provide 
a more flexible framework for constructing long,
 complex curves.

24. B-spline versus interpolating cubic spline

Do not confuse B-splines with the cubic interpolation 
splines you studied earlier. In cubic spline interpolation,
we start with data points such as (x₀,y₀), (x₁,y₁), ..., (xₙ,yₙ)
and construct polynomial pieces that pass through the data points.
We impose conditions such as C⁰, C¹, and C² continuity 
to determine the unknown coefficients.
The result is an interpolating curve.

In a B-spline representation, 
the Pᵢ are normally control points rather 
than points that the curve must pass through.
Therefore, a standard B-spline is generally 
an approximation or control-point representation,
not an interpolation method.

This distinction is very important.

25. The control polygon

Just as with Bézier curves, 
we can connect the control points 
with straight line segments.

This produces the control polygon. For example:
P₀ — P₁ — P₂ — P₃ — P₄ — P₅.
The B-spline curve is influenced by this polygon, 
but it normally does not pass through every control
point. Instead, the control polygon provides a 
geometric framework that guides the curve.
Because the influence is local, moving one vertex 
of the control polygon generally changes only a 
nearby portion of the curve.

26. A useful geometric interpretation
Imagine that every control point has an 
influence function attached to it.
For example, P₃ has an influence function N₃,ₚ(u).
Where N₃,ₚ(u) is large, P₃ strongly influences the curve.
Where N₃,ₚ(u) is small, P₃ has little influence.
Where N₃,ₚ(u) is zero, P₃ has no influence.
The curve is produced by combining 
all these local influences: C(u) = Σ Nᵢ,ₚ(u)Pᵢ.
As u moves along the curve, 
the influence functions change continuously,
causing the curve to move smoothly from 
one group of control points to the next.

27. Why B-splines are useful in CAD
B-splines are important in computer-aided 
geometric design because they provide a 
combination of flexibility and mathematical structure.

We can use many control points, obtain local control,
choose the degree, manipulate knot placement, 
and control continuity through knot multiplicity.

This makes B-splines useful for designing 
complicated curves without having to construct 
and manually join many independent polynomial segments.

The same idea can also be extended from curves to surfaces.

28. From B-spline curves to B-spline surfaces

For a B-spline curve we have one parameter: C(u) = Σᵢ Nᵢ,ₚ(u)Pᵢ.
For a B-spline surface we introduce a second parameter v.
The surface can be written as S(u,v) = Σᵢ Σⱼ Nᵢ,ₚ(u) Mⱼ,ᑫ(v) Pᵢⱼ.

Now the control points form a two-dimensional control 
net instead of a one-dimensional control polygon.

The same basic idea remains: basis functions 
determine how strongly each control point contributes 
to a particular location on the surface.

29. The relationship between Bézier,
B-splines, and NURBS

The progression is useful to remember:

Bézier → B-spline → NURBS.

- Bézier curves introduce 
the idea of control points and basis functions.
- B-splines extend that idea to many control points,
local support, knot vectors, and multiple polynomial pieces.
- NURBS extend B-splines further by introducing weights 
and rational basis functions.

This progression is important in CAD 
because many sophisticated curve and surface 
representations are based on these ideas.
"""