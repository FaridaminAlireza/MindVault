"""
POLYGON MESH PROCESSING
CHAPTER 1: SURFACE CONCEPTS
PAGES 2-10


1. SURFACE DEFINITION

A surface is a continuous
2D manifold embedded in R³.

Intuitively:

    a 2D object
    embedded in 3D space.

Examples:

    sphere
    cylinder
    cube surface

Although the surface exists
in 3D, locally it behaves
like a 2D object.


2. MANIFOLD

The key idea is LOCAL behavior.

Around a normal point on
a surface, a small neighborhood
looks like a flat 2D disk.

For example:

    small part of sphere
            ↓
       approximately
       like a flat disk

This local property is what
makes it a 2D manifold.


3. ORIENTABILITY

A surface is orientable if
we can consistently choose
one normal direction over
the entire surface.

For example, on a sphere:

    outside
       ↑
       | normal
    surface
       |
    inside

The normal direction can be
defined consistently.


4. SURFACE PATCH

A surface patch is a local
piece of a larger surface.

Instead of describing an
entire complicated surface
at once:

    entire surface
          |
    +-----+-----+
    |     |     |
    | P1  | P2  |
    +-----+-----+
    |     |     |
    | P3  | P4  |
    +-----+-----+

Each Pi is a surface patch.


5. PIECEWISE SURFACE

A complex surface can be
represented by multiple
surface patches.

Conceptually:

    S = S1 ∪ S2 ∪ S3 ∪ ...

Each patch describes only
a local part of the surface.

This makes complex surfaces
easier to represent and
process.


6. PATCH CONNECTIONS

When patches are combined,
their boundaries must connect
properly.

Otherwise we can get:

    gaps
    overlaps
    discontinuities

Therefore, neighboring
patches must satisfy suitable
continuity conditions.


7. LOCAL VS GLOBAL

A surface representation can
be considered locally or
globally.

Local:

    describe one small
    region of the surface.

Global:

    describe the complete
    surface.

Complex geometry is often
easier to handle locally.


8. APPROXIMATION

In geometry processing,
the original surface is often
approximated.

For example:

    real object
        ↓
    mathematical surface
        ↓
    approximation
        ↓
    polygon mesh

The approximation should
capture the important
geometric properties.


9. APPROXIMATION POWER

A representation should be
able to approximate surfaces
with sufficient accuracy.

More local pieces generally
give more flexibility.

For example:

    few large patches
        ↓
    less local flexibility

    many small patches
        ↓
    more local flexibility


10. THREE CATEGORIES OF
    SURFACE OPERATIONS

The book discusses three
important categories:

    1. Evaluation
    2. Query
    3. Modification


11. EVALUATION

Evaluation means computing
geometric information from
a surface.

Examples:

    surface position
    surface normal
    tangent
    curvature
    other geometric values

Typical question:

    "What is the geometric
     information at this
     location?"


12. QUERY

A query asks a question
about the geometry.

Examples:

    Is this point inside
    or outside?

    How far is this point
    from the surface?

    Does a ray intersect
    the surface?

    What is the closest
    point on the surface?

Queries retrieve information
without necessarily changing
the surface.


13. MODIFICATION

Modification changes the
surface or its representation.

Examples:

    deformation
    smoothing
    refinement
    simplification
    editing

Modification can affect:

    geometry

or:

    topology


14. GEOMETRIC MODIFICATION

Geometric modification changes
the shape while preserving
the basic connectivity.

Examples:

    move vertices
    smooth a surface
    deform a shape

The connectivity can remain
the same while positions
change.


15. TOPOLOGICAL MODIFICATION

Topological modification
changes the connectivity
or structure of the surface.

Examples:

    add connections
    remove connections
    split a surface
    merge regions
    change mesh connectivity

So:

    geometry = shape

    topology = connectivity


16. WHY LOCAL PATCHES ARE USEFUL

Complex surfaces can contain
many different geometric
features.

Using patches allows us to
handle different regions
independently.

For example:

    smooth region
        ↓
    one simple patch

    highly curved region
        ↓
    more/smaller patches


17. SURFACE TO MESH

A polygon mesh can be viewed
as a discrete approximation
of a continuous surface.

Conceptually:

    continuous surface
            ↓
        discretize
            ↓
       sample points
            ↓
       connect points
            ↓
       polygons/triangles
            ↓
       polygon mesh


18. IMPORTANT DISTINCTION

Geometry:

    Where are the points?

Topology:

    Which points are connected?


For a triangle mesh:

    vertices
       = geometric positions

    edges/faces
       = connectivity


19. CORE IDEAS TO REMEMBER

Surface:
    continuous 2D object
    embedded in 3D.

Manifold:
    locally behaves like
    a 2D disk.

Orientable:
    consistent normal
    direction can be chosen.

Surface patch:
    local piece of a surface.

Piecewise surface:
    complete surface made
    from multiple patches.

Approximation:
    representing a complex
    surface approximately.

Evaluation:
    calculate geometric
    information.

Query:
    ask a geometric question.

Modification:
    change the geometry
    or topology.

Polygon mesh:
    discrete approximation
    of a surface.
"""