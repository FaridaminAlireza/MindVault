"""
1.3 PARAMETRIC SURFACE REPRESENTATIONS

The main idea of a parametric surface is 
to represent a 3D surface using a 2D parameter domain.

We define a function f : Ω ⊂ R² → R³
where (u,v) ∈ Ω are the parameters.

The function gives us a 3D point:
f(u,v) = (x(u,v), y(u,v), z(u,v))

Therefore: (u,v) → (x,y,z)

The parameter domain Ω is 2D, 
while the resulting surface S lives in 3D.

The surface is defined as S = f(Ω)

This means: take every point (u,v) in Ω,
evaluate f(u,v), and the collection of 
all resulting 3D points forms the surface S.

Example 1: Plane
Consider f(u,v) = (u,v,0)
with Ω = [0,1] × [0,1].
The parameter domain is a square in 2D.

For example, (u,v) = (0.3,0.7)
gives f(0.3,0.7) = (0.3,0.7,0).

Thus, a point in the 2D parameter domain 
corresponds to a point on the 3D surface.

Example 2: Sphere
A sphere can be parameterized using
longitude and latitude:

f(u,v) = (cos(u)cos(v), sin(u)cos(v), sin(v))

where, for example,
u ∈ [0,2π] and v ∈ [-π/2,π/2].

Here u controls the longitude and 
v controls the latitude.

For example,
f(0,0) = (1,0,0) and
f(π/2,0) = (0,1,0).
By changing u and v, we generate points over the entire surface.

WHY PARAMETRIC SURFACES ARE USEFUL

The main advantage is that many problems involving 
a complicated 3D surface can be converted into problems
involving the simpler 2D parameter domain Ω.

1. Sampling the surface

Suppose we want points on S.
Instead of directly searching 
through 3D space, we can sample points

(u₁,v₁), (u₂,v₂), ..., (uₙ,vₙ)
inside Ω.

Then evaluate pᵢ = f(uᵢ,vᵢ).

Therefore:

2D sampling → evaluate f → 3D surface points.

For example, suppose

Ω = [0,1]²
and
f(u,v) = (u,v,0).

We can create a regular grid in Ω:
(0,0), (0.25,0), (0.5,0), ...
and map every point through f.
For a curved surface, the same 2D grid is mapped onto the curved 3D surface.

2. Surface neighborhoods

Suppose p = f(u₀,v₀).
To investigate the neighborhood of p,
we can look at points close to (u₀,v₀)
in the parameter domain.

For example:
(u₀ + Δu, v₀ + Δv)
maps to
f(u₀ + Δu, v₀ + Δv).

Therefore, instead of searching over the whole 3D surface,
we can investigate a local region of the 2D parameter domain.
This is what the book means when it says that geodesic neighborhoods 
can be found by considering neighboring points in the parameter domain.

However, there is an important subtlety:
being close in parameter space does not necessarily mean 
being equally close on the surface.

For example, consider f(u,v) = (10u,v,0).

Take two parameter points:
p₁ = (0,0)
p₂ = (0.1,0).
Their distance in parameter space is dΩ = 0.1.

But f(0,0) = (0,0,0)
and f(0.1,0) = (1,0,0).
Their distance on the surface is dS = 1.
Therefore, dS = 10 dΩ.
The parameterization has stretched distances 
by a factor of 10 in this direction.

This is called distortion.

3. Deforming a surface

Suppose f : Ω → R³
defines a surface.
Now suppose we have a deformation function 
d : R³ → R³.

The function d takes a 3D point and moves it somewhere else.

Instead of creating a completely new surface,
we can simply compose the two functions:

f_new = d ∘ f.
This means
f_new(u,v) = d(f(u,v)).

Example:

Suppose
f(u,v) = (u,v,0).
This is a flat plane.

Now define d(x,y,z) = (x,y,z+x²).

Then

f_new(u,v) = d(f(u,v))
= d((u,v,0)) = (u,v,u²).

So the original flat plane 
z = 0
has become the curved surface
z = u².

This is why the book says that composition 
with a deformation function provides 
an efficient way to modify surface geometry.

THE MAIN DIFFICULTY: CONSTRUCTING f

So far, parametric surfaces sound very convenient.
However, there is a major problem:

constructing a good parameterization f can be difficult.

We need to construct both Ω and f : Ω → S
so that the 2D domain correctly represents the 3D surface.

A useful way to think about this is flattening a 3D surface into 2D.

Imagine a globe.
We want to make a 2D map of the globe.
The 3D globe must somehow be represented by a 2D domain.
But flattening a curved surface generally introduces distortion.

This is similar to the distortion that occurs when making a map of the Earth.

METRIC STRUCTURE

The word "metric" essentially refers to geometric measurements
such as distances and angles.

Suppose two points in the parameter domain are q₁ = (u₁,v₁) and q₂ = (u₂,v₂).

Their parameter-space distance is dΩ(q₁,q₂).

Their corresponding surface points are
p₁ = f(u₁,v₁) and p₂ = f(u₂,v₂).
Their surface distance is dS(p₁,p₂).

A good parameterization tries to make 
these two geometric structures correspond reasonably well: dΩ ≈ dS.

If they are very different, 
the parameterization has significant distortion.

For example, if dS = 10dΩ,
the surface is stretched by a factor of 10 relative to the parameter domain.

This explains the statement:
"a low-distortion parameterization requires the metrics in S and Ω to be similar."

In simple terms:
the geometry of Ω should resemble
the geometry of S as much as possible.

WHY DISTORTION MATTERS

Suppose we create a regular grid in Ω:

+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+

If the parameterization has low distortion, 
the corresponding surface regions have 
reasonably similar sizes and shapes.

But if the parameterization stretches some regions heavily,
one small parameter-domain cell could correspond
to a very large surface region.

Therefore:
regular spacing in Ω
does not necessarily mean
regular spacing on S.

This is one of the central problems in parameterization.

CHANGING THE SHAPE OF S

The book says that when the shape of S changes, 
the parameterization may need to be updated.

Suppose we have f : Ω → S.
If we deform S strongly, the old parameterization may become highly distorted.
For example, imagine a regular parameter grid before deformation:

+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+

After a strong deformation, the corresponding regions might become highly stretched:

+--+--------+
|  |        |
+--+--------+

The original parameterization may no longer represent the surface well.

Therefore, we may need to construct a new parameterization.

---
TOPOLOGY

The next important concept is topology.

The book says:
"Since the manifold surface S is defined as the range of the parameterization f,
its topology is equivalent to that of Ω if f is continuous and injective."

This sounds complicated, but it can be understood step by step.

First: S = f(Ω). So the surface is produced by mapping Ω through f.

Now suppose f is continuous.
Roughly, continuity means that small changes in the parameter coordinates 
produce small changes in the resulting surface point.
There are no sudden jumps.

Next, suppose f is injective.

Injective means that two different parameter points 
cannot map to the same surface point.
Mathematically:
f(p₁) = f(p₂) implies p₁ = p₂.
Equivalently, if p₁ ≠ p₂, then f(p₁) ≠ f(p₂).

So there is no overlap caused by two different parameter locations 
representing the same surface point.

For example, f(u,v) = (u,v,0) is injective.
If f(u₁,v₁) = f(u₂,v₂), then necessarily u₁ = u₂ and v₁ = v₂.

NON-INJECTIVE PARAMETERIZATION
Suppose instead that two different parameter points satisfy
(u₁,v₁) ≠ (u₂,v₂) but f(u₁,v₁) = f(u₂,v₂).
Then two different locations in the parameter domain
correspond to the same 3D point.
This creates an overlap.

Mathematically: p₁ ≠ p₂ but f(p₁) = f(p₂).
This is a failure of injectivity.

---
TOPOLOGY AND THE PARAMETER DOMAIN

The important consequence is that 
the topology of Ω constrains the topology of S.

Think of Ω as a 2D sheet.
If f is continuous and injective, 
the sheet is mapped into 3D without tearing or overlapping.

Therefore, the surface cannot arbitrarily change 
its topology while keeping the same parameter-domain structure.

For example, suppose Ω is disk-like
A surface obtained from this domain through 
a continuous injective mapping has compatible topology.

If we want a surface with a completely different topology, such as a torus. 
we generally need to change the parameterization structure and/or the parameter domain.
This is what the book means by:
"not only the parameterization but also the domain Ω has to be adjusted accordingly."

Therefore:
changing geometry is not necessarily
the same as changing topology.

Geometry can often be deformed continuously.
Topology involves more fundamental changes in connectivity.

INSIDE/OUTSIDE QUERIES
The next weakness of parametric surfaces concerns spatial queries.

Suppose we have a point q ∈ R³
and a surface S.

We may want to ask: "Is q inside or outside the surface?"
For a complicated parametric surface, answering such questions 
may require finding where q is closest to S.

This is called finding the closest point or foot point.

Mathematically, we want

p* = arg min_{p∈S} ||q-p||.

Since every surface point has the form p = f(u,v),
we can rewrite this as

# (u*,v*)
arg min_{(u,v)∈Ω}
||q - f(u,v)||.

Then the closest surface point is p* = f(u*,v*).

So a 3D spatial query becomes an optimization 
problem over the 2D parameter domain.

For a simple plane this is easy.

Example: f(u,v) = (u,v,0)
and q = (2,3,5).

The closest surface point is
p* = (2,3,0).
The distance is ||q-p*|| = 5.

For a complicated curved surface, however, solving
min ||q-f(u,v)||
can be much more difficult and 
may require numerical optimization.

---
SELF-COLLISION / SELF-INTERSECTION

The same issue occurs when checking 
whether a parametric surface intersects itself.

We need to determine whether there exist 
two different parameter points such that

(u₁,v₁) ≠ (u₂,v₂) but f(u₁,v₁) = f(u₂,v₂).
If this happens, two different parts of the parameter domain 
map to the same 3D location.

Therefore, the mapping is not injective.
Finding all such pairs can be computationally expensive.

---
Summary 

Think of f as a mapping from a 2D sheet into 3D.

Start with:
2D parameter domain Ω
Then apply f: Ω --f--> S.

The function f tells us where every point 
on the 2D sheet goes in 3D.

A good parameterization 
should avoid excessive:

stretching,
compression,
shearing,
and overlap.

It should also have a parameter-domain topology 
compatible with the surface topology.

Therefore, the entire section can be summarized by:

Parametric surface: f : Ω ⊂ R² → R³
with S = f(Ω).

Strength:
A complicated 3D surface can often be manipulated 
through a simpler 2D domain.

Weakness:
The 2D domain must faithfully represent 
the geometry and topology of the 3D surface.

The four major issues to remember are:

1. Distortion
Distances in Ω should correspond reasonably to distances on S.

2. Topology
The topology of Ω constrains the topology of S.

3. Injectivity
Different parameter points should not map to the same surface point.

4. Spatial queries
Finding closest points, inside/outside relationships,
and self-intersections can be expensive.

So the central idea of Section 1.3 is:

A parametric surface gives us a convenient
2D coordinate system for a 3D surface.

But constructing and maintaining that coordinate system
is itself a difficult geometry-processing problem.

"""