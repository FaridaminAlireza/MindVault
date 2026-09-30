"""
Distance Field

A distance field is a function that tells us 
the distance from every point in space to a 
geometric object, usually a surface.


For a 3D object, the distance field is written as:
d(x,y,z)
This means that for every point (x,y,z), 
the function gives the distance from that 
point to the surface.

For example, 

    imagine a sphere. 
    A point far away from the sphere 
    has a large distance value. 
    A point close to the sphere has a
    small distance value. 
    A point exactly on the surface 
    has distance zero.

    Therefore:
    d(p) = distance from point p to the surface.
    For a simple circle with center (0,0) and radius R,
    a point p = (x,y) has distance from the center:
    r = sqrt(x² + y²)

    The distance to the circle surface is:
    d(x,y) = |sqrt(x² + y²) - R|
    For example, if R = 5 and p = (8,0),
    the distance from the center is 8,
    so the distance to the surface is:
    d(8,0) = |8 - 5| = 3
    So that point is 3 units away 
    from the surface.

A distance field can be stored on a grid.
For example, in 2D, every grid point 
can store its distance to the object:

    3   2   1   2   3
    2   1   0   1   2
    1   0   X   0   1
    2   1   0   1   2
    3   2   1   2   3

Here X represents the object or surface,
 and the numbers represent distances from the surface.

In 3D, the same idea is used with voxels.
Each voxel can store a distance value:
voxel (i,j,k) → d(i,j,k)

Thus, a voxel grid can represent a discrete 3D 
distance field.

There is an important version called 
a signed distance field, or SDF. 
Instead of storing only the magnitude of the distance,
we also use the sign to indicate 
whether a point is inside or outside the object.

A common convention is:
d(p) > 0 → outside
d(p) = 0 → on the surface
d(p) < 0 → inside

The sign convention can also be reversed;
the important thing is to use one convention consistently.

The surface is therefore represented implicitly by:
d(x,y,z) = 0
This is called the zero level set of the distance field.

This gives an important connection 
between explicit and implicit geometry.

Mesh: vertices → edges → triangles → surface

Distance field: 3D space → distance values → d(x,y,z)

Surface: d(x,y,z) = 0
So a mesh explicitly describes the surface using triangles,
while a distance field describes the surface indirectly 
through a scalar function.

Distance fields are useful in mesh processing 
because they allow us to perform computations 
throughout the volume around an object. 
They can be used for collision detection, 
proximity queries, shape comparison, 
surface reconstruction, deformation, segmentation,
and path planning.

* Another important property is that 
the gradient of the distance field gives 
the direction of the surface normal.

(A distance field changes most rapidly in
the direction perpendicular to the surface.) 

The gradient is: ∇d = (∂d/∂x, ∂d/∂y, ∂d/∂z)
The normalized gradient gives the normal:
n = ∇d / |∇d|

So we can have:
distance field → gradient → surface normal

If the distance field is stored on a voxel grid,
the derivatives can be approximated using 
finite differences. For example:

∂d/∂x ≈ [d(i+1,j,k) - d(i-1,j,k)] / (2hx)

Similarly:
∂d/∂y ≈ [d(i,j+1,k) - d(i,j-1,k)] / (2hy)
and:
∂d/∂z ≈ [d(i,j,k+1) - d(i,j,k-1)] / (2hz)

Therefore, a voxel grid can store not only 
whether a region is inside or outside an object,
but also how far that region is from the surface.

The overall relationship is:

triangle mesh
↓
surface
↓
voxelization
↓
distance calculation
↓
distance field
↓
d(x,y,z)

And we can go in the other direction:

distance field
↓
zero level set
↓
surface extraction
↓
triangle mesh

This is why distance fields are important in
geometry processing: they provide a bridge between
a triangle-based surface representation and a 
volumetric representation of the surrounding 3D space.
"""