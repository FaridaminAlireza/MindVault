"""
 Marching Cubes

Goal

Marching Cubes is an algorithm for extracting 
a triangle mesh from an implicit surface.

Given a scalar field:

f(x,y,z)

and an isovalue:

c

the desired surface is:

f(x,y,z) = c

The scalar field is sampled on a regular 3D grid.
The algorithm examines one grid cube at a time 
and determines how the isosurface passes through
that cube.

---

Step 1: Classify Cube Vertices

Each cube has 8 vertices.

For every vertex, 
compare its scalar value with the isovalue c.

* If f > c, mark the vertex as inside.
* If f < c, mark the vertex as outside.

Each vertex therefore has two possible states.

Since there are 8 vertices:

2⁸ = 256

possible configurations exist.

Each configuration describes a different way 
the surface can pass through the cube.

---

 Step 2: Detect Edge Intersections

A cube contains 12 edges.

The surface intersects an edge only if the two edge
endpoints lie on opposite sides of the isovalue.

For an edge with endpoints:

p₁ , p₂

and scalar values:

f₁ , f₂

an intersection exists if:

(f₁ − c)(f₂ − c) < 0

This means one endpoint is inside and the other is outside.

---

 Step 3: Compute the Intersection Point

Assume the scalar field varies linearly along the edge.

A point on the edge is:

p(t) = (1 − t)p₁ + tp₂

where:

0 ≤ t ≤ 1

The scalar value along the edge is approximated by:

f(t) = (1 − t)f₁ + tf₂

The isosurface occurs where:

f(t) = c

Substituting:

(1 − t)f₁ + tf₂ = c

Solving for t:

t = (c − f₁)/(f₂ − f₁)

The intersection point becomes:

p = p₁ + ((c − f₁)/(f₂ − f₁))(p₂ − p₁)

This is the interpolation formula used by Marching Cubes.

---

 Proof of the Interpolation Formula

Define:

g(t) = (1 − t)f₁ + tf₂

Since g(t) is linear and continuous:

g(0) = f₁

g(1) = f₂

If f₁ and f₂ are on opposite sides of c, then:

(g(0) − c)(g(1) − c) < 0

By continuity, a solution exists in [0,1].

Because g(t) is linear, only one solution exists.

Solving:

g(t) = c

gives:

t = (c − f₁)/(f₂ − f₁)

Therefore each crossed edge contains exactly one isosurface point.

---

 Step 4: Encode the Cube Configuration

Each vertex contributes one bit:

* 1 = inside
* 0 = outside

The eight bits form a binary number.

Example:

11110000

This binary pattern is converted into an integer index between:

0 and 255

The index uniquely identifies the cube configuration.

---

 Step 5: Lookup Table

A precomputed lookup table stores the triangle pattern 
associated with each cube configuration.

The table specifies:

* which edges are intersected,
* which intersection points should be connected,
* how many triangles must be generated.

Instead of computing topology from scratch,
the algorithm simply reads the corresponding entry.

This is the reason Marching Cubes is efficient.

---

 Example

Suppose the four bottom cube vertices satisfy:

f < c

and the four top cube vertices satisfy:

f > c

The isosurface must separate the top half from the bottom half.

The four vertical edges connect vertices with opposite signs.

Therefore the surface intersects all four vertical edges.

Linear interpolation computes four intersection points.

The lookup table connects these points into two triangles.

Together these triangles form a square-like patch through
the center of the cube.

---

 Why It Is Called "Marching Cubes"

The algorithm processes cubes one after another across the grid.

For each cube it:

1. Classifies vertices.
2. Detects crossed edges.
3. Interpolates intersection points.
4. Generates triangles.

The algorithm effectively "marches" through all cubes in the volume.

---

 Final Result

After every cube has been processed:

* all generated triangles are collected,
* neighboring cubes share edge intersections,
* the triangles form a connected mesh approximating the isosurface.

The resulting mesh is a piecewise-linear approximation of:

f(x,y,z) = c

and is widely used in medical imaging, volume visualization,
signed-distance fields, geometry processing, and scientific computing.

"""