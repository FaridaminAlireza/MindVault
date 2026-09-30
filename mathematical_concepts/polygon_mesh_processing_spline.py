"""
TENSOR-PRODUCT SPLINE SURFACES

The main idea of a parametric spline surface is actually 
quite intuitive once we separate the terminology.

A spline surface is a way of describing a 3D surface 
using a collection of control points.

Imagine a grid of points:
  •--------•--------•
  |        |        |
  |        |        |
  •--------•--------•
  |        |        |
  |        |        |
  •--------•--------•

These points are called control points.
The surface is generated mathematically 
from these control points.

The important idea is: Instead of specifying every point of
the surface directly, we specify a relatively small number of
control points and use mathematical basis functions to generate the surface between them.

This is why spline surfaces are useful in CAD.

WHAT IS A SPLINE?
A spline is essentially a smooth function constructed 
from several simpler polynomial pieces.

For a curve, imagine:
   ______
 /        \__

Instead of using one enormous polynomial 
to describe the entire curve, 
we use several smaller polynomial pieces.

For example,

f(u) =
p₁(u),   u ∈ [u₀,u₁]
p₂(u),   u ∈ [u₁,u₂]
p₃(u),   u ∈ [u₂,u₃]

where each pᵢ(u) is a polynomial.

The pieces are joined smoothly.
This is the basic idea behind splines.

FROM SPLINE CURVES TO SPLINE SURFACES

A spline surface does essentially the same thing in two dimensions.
Instead of one parameter, u we have two parameters: (u,v).
So instead of f(u), we have f(u,v).

The surface is therefore represented as
f : Ω ⊂ R² → R³.
The parameter domain is typically rectangular:

v
↑
|
+----------------+
|                |
|                |
|                |
+----------------+ → u

The surface in 3D is generated from this rectangle.

WHAT DOES "TENSOR-PRODUCT SPLINE" MEAN?

"TENSOR product" sounds complicated, but the basic idea is simple.
A tensor-product spline surface is constructed by 
combining one spline basis in the u direction with 
another spline basis in the v direction.

Imagine a rectangular grid:

  u direction →
•-----•-----•-----•
|     |     |     |
•-----•-----•-----•
|     |     |     |
•-----•-----•-----•
|     |     |     |
•-----•-----•-----•
      ↑
    v direction

There are basis functions in the u direction 
and basis functions in the v direction.
Their product creates a 2D basis function.
This is the meaning of "tensor product" in this context.

B-SPLINE BASIS FUNCTIONS

The book writes Nᵢⁿ(u).
This is a B-spline basis function.
For now, think of it as a function that tells us:
How strongly does control point i influence 
the surface at parameter u?

A basis function has local support. Conceptually:
Nᵢ(u) Outside a certain parameter interval, Nᵢ(u) = 0.
Therefore, the corresponding control point has no influence there.

For a surface, we need basis functions in both directions:
Nᵢⁿ(u) and Nⱼⁿ(v).
We multiply them: Nᵢⁿ(u)Nⱼⁿ(v).

This gives a 2D basis function.

Conceptually:

influence in u
×
influence in v
==============
influence over a surface region.

THE CONTROL POINTS

The book writes

cᵢⱼ ∈ R³.

Each cᵢⱼ is a 3D control point.

For example, cᵢⱼ = (2,4,1).

The control points form the control mesh.

For example:

c₀₀ ---- c₁₀ ---- c₂₀ ---- c₃₀
|        |        |        |
|        |        |        |
c₀₁ ---- c₁₁ ---- c₂₁ ---- c₃₁
|        |        |        |
|        |        |        |
c₀₂ ---- c₁₂ ---- c₂₂ ---- c₃₂

This is called the control mesh.

Important:
The control mesh is generally NOT the actual surface.
Instead, it controls the surface.

EQUATION (1.2)
The book gives
# f(u,v) = Σᵢ Σⱼ cᵢⱼ Nᵢⁿ(u) Nⱼⁿ(v).

This looks complicated, but it can be read very simply.

cᵢⱼ is a control point.

Nᵢⁿ(u) is the influence in the u direction.

Nⱼⁿ(v) is the influence in the v direction.

Their product

Nᵢⁿ(u)Nⱼⁿ(v)

is the weight of control point cᵢⱼ.

Therefore:

# f(u,v) = weighted combination of control points.

This is the key idea behind the equation.

NUMERICAL EXAMPLE
Suppose at a particular location (u,v), 
only four control points matter.

Suppose their weights are
0.1, 0.2, 0.3, 0.4.

Then
f(u,v) = 0.1c₀₀ + 0.2c₁₀ + 0.3c₀₁ + 0.4c₁₁

Suppose
c₀₀ = (0,0,0)
c₁₀ = (1,0,0)
c₀₁ = (0,1,0)
c₁₁ = (1,1,0).

Then
f(u,v) =0.1(0,0,0) + 0.2(1,0,0) + 0.3(0,1,0) + 0.4(1,1,0).
Therefore,
f(u,v) = (0.6,0.7,0).

So the surface point is literally 
constructed from the control points.

---
WHY DOES THE BOOK SAY "CONVEX COMBINATION"?

The book states that Nᵢⁿ(u) ≥ 0
and Σᵢ Nᵢⁿ(u) = 1.
The same idea applies in the v direction.

Therefore the weights
wᵢⱼ = Nᵢⁿ(u)Nⱼⁿ(v)
are nonnegative and satisfy wᵢⱼ ≥ 0
and Σᵢ Σⱼ wᵢⱼ = 1.

Thus, f(u,v) = Σᵢ Σⱼ wᵢⱼ cᵢⱼ
is a convex combination of the control points.

WHAT IS A CONVEX COMBINATION?

Suppose we have three points:

   c₁
 /   \
c₂-----c₃

A point such as
p = 0.2c₁ + 0.3c₂ + 0.5c₃
is inside the triangle formed 
by the three points because
0.2 + 0.3 + 0.5 = 1
and all weights are nonnegative.

Therefore, the point is inside the 
convex hull of the control points.

For a spline surface, 
the same principle works in 3D.

Therefore:
f(u,v) lies inside
the convex hull of
the control mesh.

This explains the book's statement:
"the surface lies within the convex hull of the control mesh."

WHAT IS THE CONVEX HULL?
The convex hull is essentially the smallest 
convex "container" around the control points.

In 2D:

    •
  /   \
 /     \
•-------•

The triangle is the convex hull.

In 3D, the same idea gives a volume surrounding the control points.

The important consequence is:
The spline surface cannot suddenly jump outside
the convex hull of its control points.

This makes editing predictable.

LOCAL INFLUENCE

The book next says:
"Due to the minimal support of the basis functions, 
each control point has local influence only."

This means that a basis function is 
nonzero only over a limited parameter interval.

For example:
Outside that region,
Nᵢⁿ(u) = 0.
Therefore, the corresponding control point has no influence there.

For a surface, the same thing happens in both u and v.
Thus, a control point affects only a local region of the surface.

EXAMPLE OF LOCAL INFLUENCE

Imagine:

•---•---•---•
|   |   |   |
•---X---•---•
|   |   |   |
•---•---•---•

Suppose we move X.

Because its basis function has local support, 
only the nearby surface region changes significantly.

The far-away surface remains essentially unchanged.

This is very useful for CAD modeling.

You can move one control point without completely changing the entire surface.

WHY DOES THE SURFACE FOLLOW THE CONTROL MESH?

Two important properties work together:
1. The surface lies inside the convex hull of the control mesh.
2. Each control point has local influence.
Therefore, moving the control mesh causes 
predictable local changes in the surface.

This gives the designer an intuitive metaphor:

The control mesh acts like
a flexible framework
that controls the surface shape.

You don't directly manipulate every surface point.
Instead, you manipulate the control points.

BI-DEGREE n

The book says:
"A tensor-product spline surface f of bi-degree n..."
"Bi-degree" means that there is a polynomial degree 
associated with each parameter direction.

For example, (n,n).
If n = 3,
then the surface has degree 3 in u and degree 3 in v.
This is called a bicubic surface.

More generally, one could have different degrees: (nᵤ,nᵥ).
But the book uses the same n for both directions.

POLYNOMIAL PATCHES
The spline surface is divided into 
rectangular regions in parameter space.

For example:

+-------+-------+
|       |       |
|   P₁  |   P₂  |
|       |       |
+-------+-------+
|       |       |
|   P₃  |   P₄  |
|       |       |
+-------+-------+

Each rectangle corresponds to a polynomial patch.

Therefore:
# spline surface
many polynomial patches
joined together smoothly.

Cᶰ⁻¹ SMOOTHNESS

The book says the polynomial patches 
are connected in a smooth Cⁿ⁻¹ manner.
This is a smoothness condition.

Roughly: C⁰ means the surface is continuous.
There are no gaps.

C¹ means the first derivatives are continuous.

Therefore, tangent directions change continuously.

C² means the first and second derivatives are continuous.

And so on.

Therefore: 
Cⁿ⁻¹ means derivatives up to order n-1 are continuous
across the patch boundaries.

For example, if n = 3,
then Cⁿ⁻¹ = C².
So neighboring cubic patches can have 
continuous first and second derivatives.

This produces a very smooth surface.

---
KNOT VECTORS

The book introduces two knot vectors:
{u₀,...,uₘ₊ₙ} and {v₀,...,vₖ₊ₙ}.

These are called knot vectors.

A knot is simply a parameter value 
that helps determine where 
the polynomial pieces begin and end.

For example:

u₀   u₁   u₂   u₃   u₄
|----|----|----|----|

These values divide the u parameter axis into intervals.
Similarly:

v₀   v₁   v₂   v₃
|----|----|----|

divide the v parameter axis.

Together, the two knot vectors determine 
the rectangular patch structure in parameter space.

WHY ARE THERE TWO KNOT VECTORS?

Because the surface has two parameters:

u and v.
The u knot vector controls the subdivision in the u direction.
The v knot vector controls the subdivision in the v direction.

Together they define the rectangular regions of the parameter domain.

THE PARAMETER DOMAIN

The book writes

f : [uₙ,uₘ] × [vₙ,vₖ] → R³.
This simply means that the valid parameter domain is
Ω = [uₙ,uₘ] × [vₙ,vₖ].

So Ω is a rectangle in parameter space.

Don't let the notation make this look more complicated than it is.
It is simply saying:

(u,v) belongs to a rectangular domain,
and f maps that domain into 3D.

---
NURBS

The book says:

"Tensor-product spline surfaces—often called NURBS—
are the standard surface representation in today's CAD systems."

NURBS stands for Non-Uniform Rational B-Splines.
The important idea is that NURBS are a powerful 
spline-based representation for smooth 3D surfaces.

The three words mean:
B-spline: the surface is constructed from B-spline basis functions.

Non-uniform: the knot spacing does not have to be uniform.

Rational: weights can be incorporated into the representation.

For your current understanding, the most important point is:

NURBS are powerful spline-based surface 
representations used heavily in CAD.

WHY CAD USES SPLINE SURFACES

Imagine designing a car body.

You want a surface like:
   __________
__/          \__

rather than a rough surface such as:
//////////

Spline surfaces are designed to 
provide very smooth, controllable geometry.

This is what the book means by high-quality or "Class A" surfaces.

---
THE TOPOLOGY PROBLEM

Now connect this section to the previous section.

A tensor-product surface has a rectangular parameter domain:

Ω = [uₙ,uₘ] × [vₙ,vₖ].

Therefore, one tensor-product patch represents 
essentially one rectangular surface patch.

This is a limitation.
A complicated object may have a topology 
that cannot be represented conveniently 
by one rectangular patch.
Therefore, we divide the model into multiple patches.

---
MULTIPLE PATCHES

Instead of having one parameterization
f : Ω → S,
we may have
f₁ : Ω₁ → S₁
f₂ : Ω₂ → S₂
f₃ : Ω₃ → S₃
and so on.

Then S = S₁ ∪ S₂ ∪ S₃ ∪ ...
So a complicated CAD model can 
consist of many spline surface patches.

---
WHY MANY PATCHES ARE A PROBLEM

Suppose

S = S₁ ∪ S₂.

The two patches share a boundary.

We don't want:

patch 1        patch 2

      \ /
       X
      / \


We want them to meet smoothly.
Therefore, neighboring patches must satisfy 
continuity conditions along their shared boundaries.

For example, we might require
C⁰ continuity: the patches meet.
Or C¹ continuity: the tangent directions match.
Or higher-order continuity for even smoother behavior.

WHY THIS COMPLICATES CAD MODELS

Suppose a CAD model contains hundreds or thousands of patches.
Then many patch boundaries must satisfy geometric constraints.

We have to ensure:
* patches meet correctly,
* tangent directions match,
* curvature behaves properly,
* modifications do not destroy neighboring patches.

Therefore:

many patches
→ many constraints
→ more difficult surface construction
→ more difficult surface editing.

This is what the book means when it says that 
the large number of surface patches and 
their topological and geometric constraints 
complicate surface construction and modeling.

---
REFINEMENT

The final problem concerns refinement.

Suppose we have a control mesh:

•---•---•---•
|   |   |   |
•---•---•---•
|   |   |   |
•---•---•---•

We want more control points because
we want to modify a small region more precisely.

It might seem that we could simply add one control point:

•---•---•---•
|   | X |   |
•---•---•---•
|   |   |   |
•---•---•---•

But classical tensor-product splines 
do not allow arbitrary local refinement like this.

Why? Because the basis functions are organized according 
to the tensor-product structure in the u and v directions.

The book says refinement is possible by splitting parameter intervals

[uᵢ,uᵢ₊₁] or [vⱼ,vⱼ₊₁].

If we refine in the u direction, the refinement affects 
the corresponding row/column structure across the surface.

Similarly, refinement in the v direction affects 
the corresponding structure in the other direction.

So a local refinement request can produce a much larger refinement:

local refinement request → whole row or column affected.

WHY IS THIS A PROBLEM?

Suppose we only need extra detail here:

+-------------------+
|                   |
|          +---+    |
|          | X |    |
|          +---+    |
|                   |
+-------------------+

We want more control points only around X.

But classical tensor-product refinement may force us to 
introduce additional control structure across an entire row or column.

This creates unnecessary control points.

---
T-SPLINES

The book finally introduces T-splines.
The important advantage is: local refinement.
Classical tensor-product spline:
local refinement → potentially whole row/column.

T-spline:
local refinement → local region.

Therefore, T-splines can provide a more flexible control mesh 
when different regions require different levels of detail.

---
THE WHOLE SECTION AS ONE LOGICAL CHAIN

The entire section can be understood as:

control points
→ B-spline basis functions
→ weighted combination
→ smooth polynomial patches
→ tensor-product spline surface
→ useful CAD representation.

Mathematically:

# f(u,v) =  Σᵢ Σⱼ cᵢⱼ Nᵢⁿ(u)Nⱼⁿ(v).
Here:
# cᵢⱼ 3D control point.
# Nᵢⁿ(u) basis function in the u direction.
# Nⱼⁿ(v) basis function in the v direction.
# Nᵢⁿ(u)Nⱼⁿ(v) weight of control point cᵢⱼ.

Therefore:
# surface point
weighted combination
of control points.

Because the weights are nonnegative and sum to one:
S lies inside
the convex hull
of the control mesh.

Because the basis functions have local support:
moving one control point
→ mainly changes a local
surface region.

These two properties make spline surfaces intuitive to edit.


THE THREE MAIN LIMITATIONS

1. TOPOLOGICAL LIMITATION
One tensor-product patch comes from a
rectangular parameter domain.

Therefore: one patch ≈ rectangular surface region.

Complex topology requires multiple patches.

2. PATCH-CONTINUITY PROBLEM

Multiple patches must connect smoothly.

Therefore:

many patches
→ many continuity constraints
→ more complicated modeling.

3. REFINEMENT PROBLEM

Classical tensor-product splines 
do not provide completely local refinement.

Adding refinement in one parameter direction 
can affect an entire row or column.

T-splines improve this by 
allowing more local refinement.
"""