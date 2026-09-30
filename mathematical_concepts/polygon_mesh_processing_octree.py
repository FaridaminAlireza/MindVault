"""
OCTREE, OCTREE CELLS, AND THREE-COLOR OCTREES

1. What is an octree?

An octree is a hierarchical data structure for dividing
a 3D space into smaller and smaller cubic regions.

The word "octree" comes from:
oct = eight
tree = hierarchical tree structure

The key idea is very simple:

Start with one large cube.
Divide it into 8 smaller cubes.
Any smaller cube can again be divided into 8.
Continue recursively where more detail is needed.

So an octree is essentially the 3D equivalent of a
quadtree.

In 2D:
    one square
        |
        +-- 4 smaller squares
In 3D:
    one cube
        |
        +-- 8 smaller cubes

2. Why divide space into cubes?

Suppose we have a 3D object such as a sphere.

A very fine regular grid could divide the entire space
into millions of tiny cubes.

Most of these cubes might contain only empty space.

For example:

        +-----------------------+
        |                       |
        |        sphere         |
        |       ******          |
        |     **********        |
        |     **********        |
        |       ******          |
        |                       |
        +-----------------------+

There is no reason to use extremely small cells in the
empty regions.

An octree solves this problem.

We keep large cells where nothing interesting happens,
and subdivide cells only where more detail is required.

Therefore:

    large uniform region
        -> large octree cell

    complicated region
        -> smaller octree cells


3. What is an octree cell?

An octree cell is one of the cubic spatial regions
represented by a node of the octree.

For example, suppose the original domain is

    [0,8] x [0,8] x [0,8]

This is one cube with side length 8.

Its center is (4,4,4)

We divide it at
    x = 4
    y = 4
    z = 4

These three planes divide the cube into 8 cubes.

Each child therefore has side length 8 / 2 = 4

So the root cell has: side length = 8
and each child cell has: side length = 4.

4. Why exactly 8 children?
A cube has three spatial dimensions:
x
y
z

When we divide each dimension into two parts:
x -> 2 intervals
y -> 2 intervals
z -> 2 intervals

The total number of regions is
2 x 2 x 2 = 8

Therefore:
one cell -> eight child cells

This is the fundamental reason an octree has
eight children per subdivision.

5. Coordinates of the eight child cells
Consider a cube: [0,8] x [0,8] x [0,8]
with center (4,4,4)
For each dimension we have two choices:
x: [0,4] or [4,8]
y: [0,4] or [4,8]
z: [0,4] or [4,8]

Therefore there are: 2 x 2 x 2 = 8 combinations.

For example:

    Cell 1:
    [0,4] x [0,4] x [0,4]

    Cell 2:
    [4,8] x [0,4] x [0,4]

    Cell 3:
    [0,4] x [4,8] x [0,4]

    Cell 4:
    [4,8] x [4,8] x [0,4]

and similarly for z in [4,8].

These eight regions exactly fill the original cube.

6. The octree hierarchy

The first cube is called the root cell.

After subdivision:

    Level 0:
        1 cell

    Level 1:
        8 cells

If every cell is subdivided again:

    Level 2:
        8 x 8 = 64 cells

At level 3:

    8 x 8 x 8 = 512 cells

In general, at depth d:

    number of cells = 8^d

provided that every cell is subdivided.

The side length also decreases by a factor of 2
at every level.

If the original side length is L:

    level 0:
        L

    level 1:
        L/2

    level 2:
        L/4

    level 3:
        L/8

Therefore, at depth d:
    cell size = L / 2^d

    
7. But real octrees are usually adaptive

The important point is that we do NOT necessarily
subdivide every cell. Suppose a large cell contains
only empty space. There is no reason to subdivide it.

Instead:
    empty region
        -> keep one large cell
while:
    region near surface
        -> subdivide

For example, imagine a sphere.

        root
       / | \
      /  |  \
   empty surface empty

- The empty cells can remain large.
- Cells intersecting the sphere can be subdivided.
- Then some of those cells can be subdivided again.
- This creates an adaptive spatial representation.

8. Leaf cells
A cell that is not subdivided is called a leaf cell.
For example:
                root
              /  ...  \
             /         \
          cell          cell
         / | ... \       |
        ...       ...   leaf

The leaves represent the final spatial regions.

Depending on the application, a leaf may store:
    empty
    occupied
    surface
    density
    color
    material
    distance
    geometry information

Therefore an octree is not just a geometric object.
It is a way of organizing spatial information.

9. Example: representing a sphere
Suppose our domain is: [-1,1] x [-1,1] x [-1,1]

and the object is a sphere: x^2 + y^2 + z^2 <= 1

At the root level, the entire cube contains both
inside and outside regions.

So we subdivide it.
Each child is then classified.

For example:
    completely outside sphere
        -> outside

    completely inside sphere
        -> inside

    intersects sphere boundary
        -> subdivide further

The important cells are therefore the ones near
the sphere surface.

This produces something conceptually like:

    large cells
    +-------------------------+
    |       large empty       |
    |                         |
    |       +---------+       |
    |       | smaller |       |
    |       | cells   |       |
    |       | sphere  |       |
    |       +---------+       |
    |                         |
    +-------------------------+

The octree spends more memory where the geometry
is complicated and less memory where it is simple.

10. Why is this useful in mesh processing?

Octrees are useful because they provide spatial
localization.

Suppose we have 10 million triangles.

Without a spatial structure, finding which triangles
are near a point could require checking many triangles.

An octree divides space.

A query can then say:

    "Which cells contain this point?"

or:

    "Which cells intersect this ray?"

or:

    "Which cells are near this surface?"

Instead of searching the entire mesh, we follow
the relevant branches of the tree.

This is why octrees are used for:

    collision detection
    ray tracing
    nearest-neighbor search
    surface reconstruction
    voxelization
    mesh processing
    spatial queries
    distance fields

11. What is a three-color octree?

A three-color octree is an octree in which each cell
is classified into one of three categories.

The usual classification is:
    BLACK
    WHITE
    GRAY

The exact terminology can vary between applications,
but the basic idea is:

    WHITE:
        cell is completely outside the object

    BLACK:
        cell is completely inside the object

    GRAY:
        cell contains part of the boundary

Therefore:

    white = outside
    black = inside
    gray  = boundary/intersection


12. Why do we need three colors?

Consider a cube and a surface passing through it.

There are three fundamentally different situations.

Situation 1:

    The entire cell is outside.

        +-------+
        |       |
        |       |
        +-------+

        -> WHITE

Situation 2:

    The entire cell is inside.

        +-------+
        |███████|
        |███████|
        +-------+

        -> BLACK

Situation 3:

    The surface passes through the cell.

        +-------+
        |       /
        |     /
        |   /
        +-------+

        -> GRAY

The gray cells are therefore the interesting cells.

They contain the boundary between inside and outside.


13. Why does gray mean "subdivide"?

Suppose we want an accurate representation of a surface.

If a cell is entirely inside:

    no boundary exists inside the cell

so there is no need to subdivide it.

If a cell is entirely outside:

    no boundary exists inside the cell

again, no need to subdivide.

But if the cell is gray:

    the boundary passes through the cell

so we need more information.

Therefore:

    WHITE -> stop
    BLACK -> stop
    GRAY  -> subdivide

This is one of the main ideas behind a
three-color octree.


14. Example with a sphere

Suppose we have a sphere inside a cube.

At the root:
    the cube contains both
    inside and outside space

Therefore:
    root = GRAY

We subdivide it into 8 cells.

Some cells might be:

    completely outside
        -> WHITE

Some might be:

    completely inside
        -> BLACK

Some might intersect the sphere boundary:

    -> GRAY

Then we subdivide only the gray cells.

For example:

                GRAY
                  |
       +----------+----------+
       |          |          |
     WHITE      GRAY       WHITE
                  |
            +-----+-----+
            |     |     |
          BLACK GRAY  BLACK
                  |
                ...

The subdivision continues around the surface.


15. Why is this efficient?

Imagine the sphere has a large empty region around it.

A uniform grid might use: 1024 x 1024 x 1024 cells.

That is:

    1,073,741,824 cells

which is enormous.

But an octree does not need to represent
every empty region at maximum resolution.

Large empty regions can be represented by
a single white cell.

Large interior regions can be represented by
a single black cell.

Only cells near the surface become very small.

Therefore the number of cells can be dramatically
smaller than a uniform grid.

16. The mathematical idea behind the classification

Let the object be represented by a set O.

A cell C can be classified using set relationships.

WHITE means: C ∩ O = empty
The cell does not contain any part of the object.

BLACK means: C is completely contained in O
In set notation: C ⊆ O

GRAY means neither condition holds.
The cell contains both object and non-object space:
C ∩ O is not empty
but
C is not completely contained in O

Therefore:

    WHITE:
        C ∩ O = empty
    BLACK:
        C ⊆ O
    GRAY:
        otherwise


17. More precise boundary interpretation

For a solid object O, let its boundary be:

boundary(O)

A useful interpretation is:

    WHITE:
        C does not intersect O

    BLACK:
        C lies completely inside O

    GRAY:
        C intersects the boundary

The gray cell is therefore an uncertainty region
with respect to the boundary.

As we subdivide gray cells, the uncertainty region
gets smaller.

This gives the octree a progressively finer
approximation of the surface.


18. Why does subdivision improve accuracy?

Suppose the original cell has side length: L
After one subdivision: L/2
After two: L/4
After three: L/8
In general: size = L / 2^d
where d is the depth.
Therefore, as depth increases: cell size -> 0

- The spatial region in which the surface can lie
becomes progressively smaller.

- This is the mathematical reason that increasing
octree depth gives a finer spatial approximation.


19. A simple 1D analogy

It is easier to understand the idea first in 1D.

Suppose we have:

    [0,8]

and an object occupies:

    [3,5]

Start with:

    [0,8]

This interval contains both object and empty space.

So it is:

    GRAY

Split it:

    [0,4] [4,8]

The first interval contains both:

    [0,4]

because [3,4] is inside and [0,3] is outside.

Therefore:

    [0,4] -> GRAY

The second interval contains both:

    [4,8]

because [4,5] is inside and [5,8] is outside.

Therefore:

    [4,8] -> GRAY

Continue subdividing.

Eventually we get intervals that are:

    completely outside -> WHITE

    completely inside  -> BLACK

    near boundary      -> GRAY

The 3D octree does exactly the same thing,
but with cubes instead of intervals.


20. Three-color octree as a recursive algorithm

The algorithm can be written conceptually as:

    classify(cell)

        if cell is completely outside:
            color = WHITE
            stop

        else if cell is completely inside:
            color = BLACK
            stop

        else:
            color = GRAY

            if maximum depth not reached:
                subdivide cell
                classify each child


This is a recursive algorithm.

The important point is that only gray cells
normally need further subdivision.

--
21. Example with a cube and a plane

Consider the plane: x + y + z = 0
inside a larger cube.

The plane divides the cube into two regions.

One side is:

    outside

The other side is:

    inside

The root cube is intersected by the plane.

Therefore:

    root = GRAY

After subdivision:

    some child cubes
        -> entirely on one side
        -> WHITE

    some child cubes
        -> entirely on the other side
        -> BLACK

    some child cubes
        -> intersect plane
        -> GRAY

Only the gray cubes need further subdivision.

Because a plane is geometrically simple, the number
of gray cells remains concentrated around a thin region.


22. Octree versus voxel grid

A voxel grid usually has a fixed resolution.

For example:

    100 x 100 x 100 voxels

Every location gets a voxel.

An octree is adaptive.

It can represent the same region using:

    large cells in simple areas
and
    small cells in complicated areas.

So:
    regular voxel grid
        = uniform resolution

    octree
        = hierarchical adaptive resolution

23. Octree cell versus voxel

A voxel is essentially a volume element.

For example:

    one small cube representing
    a small volume of space

An octree cell can also be a volume element,
but the important difference is its hierarchy.

A voxel grid might have:

    every cell same size

An octree has:

    different cells at different sizes

Therefore, an octree can be thought of as a
hierarchical organization of volumetric cells.


24. Important property: cells do not overlap

At each level, the eight children partition
the parent cell.

That means:

    child 1 ∪ child 2 ∪ ... ∪ child 8
        = parent

and the interiors of different children do not overlap.

Therefore every point inside the parent belongs
to exactly one child, except for points lying
exactly on shared boundaries.

This property is important because it gives a
well-defined spatial decomposition.


25. Proof of the eight-child partition

Let the parent cube be:

    [xmin,xmax]
    x [ymin,ymax]
    x [zmin,zmax]

Define the midpoint:

    xm = (xmin + xmax)/2
    ym = (ymin + ymax)/2
    zm = (zmin + zmax)/2

Each coordinate has two possibilities:

    x <= xm or x >= xm
    y <= ym or y >= ym
    z <= zm or z >= zm

Therefore:

    2 choices for x
    2 choices for y
    2 choices for z

giving:

    2^3 = 8

regions.

Every point in the parent has one combination
of these three binary choices.

Therefore the eight child cells cover the parent
without missing any interior region.


26. Depth and resolution

Suppose the original cube has side length:

    L = 1 meter

At depth 0:

    size = 1 m

At depth 1:

    size = 1/2 m

At depth 2:

    size = 1/4 m

At depth 3:

    size = 1/8 m

At depth 10:

    size = 1/1024 m

approximately:

    0.000977 m

or about:

    0.977 mm

So the depth directly controls the spatial resolution.


27. Number of possible cells

If every cell is subdivided to depth d,
the number of cells at exactly that depth is:

    8^d

For example:

    d = 0:
        1

    d = 1:
        8

    d = 2:
        64

    d = 3:
        512

    d = 4:
        4096

But the total number of cells in a completely
full tree up to depth d is:

    1 + 8 + 8^2 + ... + 8^d

This is a geometric series.

Its sum is:

    (8^(d+1) - 1) / 7

An adaptive octree usually contains far fewer
cells because not every branch reaches the
maximum depth.


28. The central idea of a three-color octree

The whole concept can be summarized as:

    BLACK
        completely inside

    WHITE
        completely outside

    GRAY
        boundary/intersection

Then:

    BLACK -> stop
    WHITE -> stop
    GRAY  -> subdivide

So the tree concentrates its resolution
around the object's boundary.


29. Why this matters for surface reconstruction

Suppose we want to reconstruct a surface from
samples or geometric information.

We may not know the exact surface everywhere.

An octree lets us progressively narrow down
where the surface can exist.

At a coarse level:

    surface is somewhere
    inside this large cell

After subdivision:

    surface is somewhere
    inside these smaller cells

After more subdivision:

    surface is restricted
    to even smaller regions

Thus the octree provides a hierarchical
approximation of the geometry.

This is especially useful for:

    implicit surfaces
    signed distance fields
    voxelization
    Marching Cubes
    collision detection
    adaptive meshing


30. Relationship with distance fields

Suppose we have a signed distance field.

For every point x, we have:

    d(x) = signed distance
           to the surface

A common convention is:

    d(x) < 0
        inside

    d(x) = 0
        surface

    d(x) > 0
        outside

Then an octree cell can use this information
to determine its classification.

If the entire cell has:

    d(x) > 0

then it is outside:

    WHITE

If the entire cell has:

    d(x) < 0

then it is inside:

    BLACK

If the cell contains points where the sign changes:

    GRAY

because the surface may pass through it.

This connects octrees directly to implicit
surface representations.


31. Important subtlety

Simply evaluating the distance at one point,
such as the cell center, is not always enough.

For example, imagine a very thin surface passes
through the cell but does not pass through its center.

The center might be outside.

If we only examine the center, we could incorrectly
classify the entire cell as WHITE.

Therefore a robust classification needs information
about the whole cell.

For example, we might use:

    geometric intersection tests

or

    bounds on the signed distance

or

    corner samples

or

    interval arithmetic

depending on the application.

---
The key formulas to remember are:

    number of children = 2^3 = 8

    cell size at depth d:
        L / 2^d

    cells at depth d:
        8^d

    total cells through depth d:
        (8^(d+1) - 1) / 7

And the key three-color rule is:

    WHITE = outside
    BLACK = inside
    GRAY  = boundary

    WHITE -> stop
    BLACK -> stop
    GRAY  -> subdivide
"""