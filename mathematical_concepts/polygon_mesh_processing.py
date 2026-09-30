"""
 Grid and Voxels in Mesh Processing

1. What is a grid?

A grid is a regular arrangement of points in space.
In 2D, we usually have a rectangular grid:

(0,2) ---- (1,2) ---- (2,2)
  |          |          |
  |          |          |
(0,1) ---- (1,1) ---- (2,1)
  |          |          |
  |          |          |
(0,0) ---- (1,0) ---- (2,0)

The grid divides space into regular cells.

In 2D, these cells are usually squares or rectangles.

In 3D, the equivalent structure is a 3D grid.

Its cells are usually cubes.

The important idea is:
Grid = regular discretization of space
Instead of representing every possible
point in continuous space, we divide
space into discrete locations or cells.

2. Grid coordinates
Suppose a 3D grid has spacing hx, hy, hz
along the x, y, and z directions.

A grid point can be written as P(i,j,k)
with physical coordinates
x = x0 + i hx
y = y0 + j hy
z = z0 + k hz
where:
i = grid index in x
j = grid index in y
k = grid index in z

For a uniform grid,
hx = hy = hz = h


and therefore
x = x0 + ih
y = y0 + jh
z = z0 + kh


3. What is a voxel?

A voxel is the 3D equivalent of a pixel.

Pixel: 2D image element
Voxel: 3D volume element

For example:
pixel -> square region
voxel -> cubic region

A voxel represents a small volume
of 3D space.

Imagine dividing a 3D object into
many tiny cubes.

Each cube is a voxel.

4. Voxel coordinates
Suppose the voxel grid has spacing
hx, hy, hz

A voxel indexed by (i,j,k)
occupies approximately

 [x0 + i hx, x0 + (i+1)hx]
× [y0 + j hy, y0 + (j+1)hy]
× [z0 + k hz, z0 + (k+1)hz]

So the voxel has dimensions hx × hy × hz
and its volume is V = hx hy hz
For a cubic voxel, hx = hy = hz = h
so V = h³

---
5. Grid points vs grid cells

This distinction is important.
A grid point is a location: (xi, yj, zk)

A voxel is the region between
neighboring grid points.

For example, in 1D:
x0 ---- x1 ---- x2 ---- x3
The intervals are:
[x0,x1]
[x1,x2]
[x2,x3]

The same idea extends to 3D.
Eight neighboring grid points
define one voxel.

Therefore:
grid points -> locations
voxels -> spatial regions

---
6. Why are voxels useful in mesh processing?

A mesh represents geometry using
vertices, edges, and faces.

For example:
vertices
   ↓
 edges
   ↓
triangles
   ↓
surface

A voxel grid provides another way
to represent the geometry.

Instead of explicitly storing the
surface everywhere, we ask:

Which voxels contain the object?

For example:

empty  empty  empty
empty  filled filled
empty  filled filled

In 3D, this becomes a collection
of occupied and empty cubes.

---
7. Voxelization

Converting a mesh into a voxel representation
is called voxelization.

Suppose we have a triangle mesh.

We construct a 3D grid around it.

Then, for every voxel, we determine
whether the voxel is:

empty
or
occupied
or 
sometimes
intersected by the surface

The result is a voxelized representation
of the mesh.

8. Inside, outside, and surface voxels

A useful classification is:

inside voxel
outside voxel
surface voxel

For example:

outside outside outside
outside surface surface
outside inside  inside

The exact classification depends
on the voxelization method.

For closed meshes, we can also determine
whether a point is inside or outside
using a point-in-mesh test.

9. Voxel center
The center of voxel (i,j,k) is

xc = x0 + (i + 1/2)hx
yc = y0 + (j + 1/2)hy
zc = z0 + (k + 1/2)hz

For cubic voxels:
xc = x0 + (i + 1/2)h
yc = y0 + (j + 1/2)h
zc = z0 + (k + 1/2)h

The center is often used to test
whether the voxel represents
inside or outside space.

10. Mapping a point to a voxel

Suppose we have a 3D point p = (x,y,z)
We want to find which voxel contains it.

For a uniform grid:
i = floor((x - x0) / hx)
j = floor((y - y0) / hy)
k = floor((z - z0) / hz)

These three integers give the voxel index:
voxel = (i,j,k)

This formula is extremely important.
It converts continuous coordinates (x,y,z)
into discrete grid coordinates (i,j,k).

11. Example of point-to-voxel mapping
Suppose:
x0 = 0
y0 = 0
z0 = 0

and
h = 1

Consider the point
p = (2.3, 1.7, 4.2)

Then:
i = floor(2.3) = 2
j = floor(1.7) = 1
k = floor(4.2) = 4

Therefore the point belongs to
voxel (2,1,4)

The voxel occupies
x: [2,3]
y: [1,2]
z: [4,5]


12. Mapping a voxel back to space
Given voxel indices (i,j,k)
we can recover its spatial bounds.

The lower corner is
pmin =
(x0 + i hx,
 y0 + j hy,
 z0 + k hz)

The upper corner is

pmax =
(x0 + (i+1)hx,
 y0 + (j+1)hy,
 z0 + (k+1)hz)

Therefore a voxel is essentially
an axis-aligned box.

13. Grid resolution

The resolution determines how small
the voxels are.

Suppose an object occupies a region
Lx × Ly × Lz

and the voxel size is h

Then approximately
Nx = Lx / h
Ny = Ly / h
Nz = Lz / h

voxels are required in each direction.

The total number is approximately
N = Nx Ny Nz

or N ≈ Lx Ly Lz / h³

This has an important consequence.

If we make h smaller,
the number of voxels increases rapidly.

For example, reducing h by 2 gives: h -> h/2

Then the number of voxels becomes
2³ = 8 times larger in 3D.

---
14. Why resolution matters

Large voxels:
low memory
fast processing
low geometric detail


Small voxels:
high memory
slower processing
high geometric detail

Therefore voxel resolution is
a trade-off between:
accuracy
and
computational cost.

---
15. Mesh vertices and voxel grids

Suppose a mesh contains vertices
v1, v2, ..., vn

Each vertex can be mapped
to a voxel.

For vertex
v = (x,y,z)

we calculate

i = floor((x-x0)/hx)
j = floor((y-y0)/hy)
k = floor((z-z0)/hz)

Now we know which voxel contains
the vertex.

This is useful for spatial organization.

16. Spatial hashing / voxel indexing

Suppose a mesh has thousands
or millions of triangles.

Testing every triangle against
every other triangle is expensive.

A grid can divide space into regions.

Each triangle is assigned to the
voxels it overlaps.

Then when processing one triangle,
we only examine nearby voxels.

Conceptually:


entire mesh
     ↓
divide space
     ↓
grid / voxels
     ↓
find nearby geometry
     ↓
perform local operations

This is called spatial partitioning.

---
17. Why this helps mesh processing

Without a spatial structure:

triangle A
   ↓
check against
every triangle

This can become very expensive.

With a voxel grid:

triangle A
   ↓
find its voxels
   ↓
find geometry
in nearby voxels
   ↓
test only candidates

The grid therefore helps with
spatial queries.

---
18. Distance from a point to a grid

A voxel grid can also be used to
approximate distance fields.

Suppose we define a function d(x,y,z)

representing distance to a surface.

For each voxel center, we can store
the distance to the mesh.

For example:


voxel center
     ↓
closest point on surface
     ↓
distance


The result is a discrete
distance field.

 19. Signed distance field

A particularly useful representation
is the signed distance field.

Define:


d(p) > 0


outside the object,


d(p) < 0


inside the object,

and


d(p) = 0


on the surface.

Therefore the zero level set


d(p) = 0


represents the surface.

This connects voxel grids with
implicit surface representations.

 20. Surface reconstruction

Voxel grids can also be used
to reconstruct surfaces.

A common idea is:


mesh
  ↓
voxel grid
  ↓
scalar values
  ↓
extract surface
  ↓
mesh


One well-known algorithm is
Marching Cubes.

It examines each voxel and determines
how the surface passes through it.

The resulting triangles approximate
the original surface.

 21. Scalar fields on a grid

A voxel does not necessarily
only contain "inside" or "outside".

We can store a numerical value:


f(i,j,k)


For example:


density
temperature
distance
probability
material value
signed distance


Then the grid represents a
discrete 3D scalar field.

For example:


f(i,j,k) = distance
           from voxel center
           to the surface


 22. Interpolation inside a voxel

Sometimes we know values only at
grid points but want the value at
an arbitrary point.

Then interpolation is used.

In 3D, the standard method is
trilinear interpolation.

A voxel has eight corners.

We know:


f000
f100
f010
f110
f001
f101
f011
f111


We want:


f(x,y,z)


inside the voxel.

First normalize the coordinates:


u = (x-x0)/hx

v = (y-y0)/hy

w = (z-z0)/hz


where


0 <= u,v,w <= 1


 23. Trilinear interpolation formula

The interpolated value is


f(u,v,w) =

(1-u)(1-v)(1-w) f000
+
u(1-v)(1-w) f100
+
(1-u)v(1-w) f010
+
uv(1-w) f110
+
(1-u)(1-v)w f001
+
u(1-v)w f101
+
(1-u)vw f011
+
uvw f111


The eight terms correspond
to the eight voxel corners.

This is very important in geometry
processing because scalar values stored
on a grid can be evaluated continuously
inside the voxel.

 24. Gradient on a voxel grid

If a scalar field is stored
on a grid, we can approximate
its gradient.

The gradient is


∇f =
(∂f/∂x,
 ∂f/∂y,
 ∂f/∂z)


Using central differences:


∂f/∂x ≈
[f(i+1,j,k) - f(i-1,j,k)]
/ (2hx)


Similarly,


∂f/∂y ≈
[f(i,j+1,k) - f(i,j-1,k)]
/ (2hy)


and


∂f/∂z ≈
[f(i,j,k+1) - f(i,j,k-1)]
/ (2hz)


Therefore:


∇f ≈
(df/dx, df/dy, df/dz)


This is useful for finding
surface normals from scalar fields.

 25. Normal from a signed distance field

For a signed distance field,


d(x,y,z)


the surface is


d = 0


The gradient points approximately
in the surface-normal direction.

Therefore:


n = ∇d / |∇d|


where


|∇d| =
sqrt(dx² + dy² + dz²)


This gives a normalized surface normal.

 26. Grid-based mesh processing

A voxel/grid representation can therefore
support many operations:


spatial search
collision detection
voxelization
inside/outside tests
distance computation
surface reconstruction
segmentation
volumetric processing
scalar-field processing
normal estimation
interpolation


The important conceptual transition is:


continuous geometry
       ↓
discrete spatial grid
       ↓
numerical processing
       ↓
reconstructed / processed geometry


 27. Grid vs voxel

It is useful to distinguish
the terminology.

Grid:


the regular spatial structure


Grid point:


a discrete location


Cell:


region between neighboring
grid points


Voxel:


a 3D grid cell


Pixel:


a 2D grid cell


Therefore:


2D:
grid → pixels

3D:
grid → voxels


 28. Relation to mesh processing

A triangle mesh is a
surface representation.

A voxel grid is a
volume-based representation.

Mesh:


vertices
edges
faces


Voxel grid:


regular 3D cells
containing values


So they represent geometry
in fundamentally different ways.

Mesh representation:


explicit surface


Voxel representation:


discretized volume


 29. Main advantage of a mesh

Meshes are efficient for representing
surfaces.

If the surface is thin compared
with the surrounding empty space,
a mesh does not need to store
the empty region.

For example:


triangle
triangle
triangle
triangle


Only the surface is represented.

 30. Main advantage of voxels

Voxels make spatial operations
very regular.

Every cell has a predictable
location and size.

This makes them convenient for:


volumetric data
medical imaging
simulations
distance fields
collision detection
geometric queries
segmentation
reconstruction


For example, CT and MRI data are
naturally represented as 3D voxel data.

31. Important formulas to remember

Grid point:


x = x0 + i hx
y = y0 + j hy
z = z0 + k hz


Voxel bounds:


x ∈ [x0+i hx, x0+(i+1)hx]

y ∈ [y0+j hy, y0+(j+1)hy]

z ∈ [z0+k hz, z0+(k+1)hz]


Voxel volume:


V = hx hy hz


Cubic voxel:


V = h³


Point → voxel:


i = floor((x-x0)/hx)

j = floor((y-y0)/hy)

k = floor((z-z0)/hz)


Voxel center:


xc = x0 + (i+1/2)hx

yc = y0 + (j+1/2)hy

zc = z0 + (k+1/2)hz


Approximate number of voxels:


N ≈ Lx Ly Lz / (hx hy hz)


Gradient:


∇f =
(∂f/∂x,
 ∂f/∂y,
 ∂f/∂z)


Central difference:


∂f/∂x ≈
[f(i+1,j,k)-f(i-1,j,k)]
/ (2hx)


Normalized gradient:


n = ∇f / |∇f|


 32. Big picture

The most important concept is this:


Mesh:
"Where is the surface?"

Voxel grid:
"What is happening
 throughout 3D space?"


A mesh explicitly describes
the boundary using triangles.

A voxel grid divides space into
regular small volumes and stores
information in those volumes.

This makes voxel grids particularly
useful when geometry processing
needs spatial information, volume
information, distance fields,
interpolation, or numerical
computation.

In geometry processing, you will
often see the two representations
used together:


triangle mesh
      ↓
  voxelization
      ↓
  voxel grid
      ↓
computation
      ↓
scalar field /
distance field
      ↓
surface extraction
      ↓
  triangle mesh


So a voxel grid is not necessarily
a replacement for a mesh.

It is often an intermediate
computational representation.

"""