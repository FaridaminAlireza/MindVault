"""
In matrix transformations, 
rows and columns play very different roles,
 and understanding that difference is key.

Core idea:
When you apply a matrix to a vector:

y = A x

* Columns of A tell you where the basis vectors go
* Rows of A tell you how to compute each output coordinate

Columns = transformed basis vectors:
Each column shows how the matrix transforms the standard basis vectors.

For a 2D example:

A = [ 2  1
      0  3 ]

* First column [2, 0]^T: where (1, 0) goes
* Second column [1, 3]^T: where (0, 1) goes

So the columns define the geometry of the transformation 
(stretching, rotating, shearing).

Rows = how outputs are computed:
Each row tells you how to compute one coordinate of the result.

If:

x = [ x1
      x2 ]

then:

A x = [ 2x1 + 1x2
        0x1 + 3x2 ]

* First row computes the first output coordinate
* Second row computes the second output coordinate

Rows act like dot products with the input vector.

Intuition summary:

* Columns: where basis vectors end up (geometric view)
* Rows: how each output coordinate is calculated (algebraic view)

Another way to see it:

A x = x1 * (column 1) + x2 * (column 2)

So the result is a linear combination of the columns.

"""

"""
A square matrix A can be thought of as 
a linear transformation of space. 
It does not just move individual vectors—it reshapes
the entire coordinate system in a consistent way.

1. Matrix as a transformation of space
When you apply:
y = A x
you are mapping every point x in space to a new point y.
So instead of thinking “this matrix changes one vector,” think:
“This matrix changes the whole space.”


2. What happens in 2D

Start with the unit square defined 
by the basis vectors:

e1 = (1, 0)
e2 = (0, 1)

When you apply A:

* e1 becomes column 1 of A
* e2 becomes column 2 of A

So the square transforms into a shape 
defined by these two new vectors.

This shape is always a parallelogram 
because linear transformations:

* preserve straight lines
* preserve parallel lines
* keep the origin fixed

3. What happens in 3D

Start with the unit cube:

(1,0,0), (0,1,0), (0,0,1)

Applying a 3x3 matrix A:
* each basis vector becomes a column of A
The cube transforms into a parallelepiped (a skewed box).


4. Columns define the new space

Any vector:

x = x1 e1 + x2 e2

becomes:

A x = x1 * column1 + x2 * column2

So every point is a linear combination of the columns.

The columns act as new building blocks of space.


5. Geometric effects of a matrix

A matrix can:

* scale (stretch/shrink)
* rotate
* shear (skew shapes)
* reflect

But it always maps:
* squares → parallelograms
* cubes → parallelepipeds

6. Determinant = area/volume scaling

* In 2D: determinant = area scaling
* In 3D: determinant = volume scaling

Examples:

* det(A) = 2 → doubles size
* det(A) = 0 → collapses dimension
* negative → includes a flip


7. Mental model

Instead of thinking:
The vector moves in fixed axes
Think:
The axes themselves move, and everything follows


8. There are two equivalent ways to 
understand matrix transformations:

A. Standard view (most common)

y = A x

* axes stay fixed
* vector moves

So (x1, x2) becomes a different point
in the same coordinate system.


B. Change of basis view (your intuition)

* axes move
* coordinates stay the same
So (x1, x2) represents a different point
because the axes changed.


Key insight:
- Moving the vector by 𝐴 is equivalent 
to moving the axes by 𝐴^-1
- These are two perspectives of the same transformation.
- Coordinates do not have meaning by themselves.
They only have meaning relative to a choice of axes.
- Interpretation:
After transforamtion, 
the coordinates (x1, x2) stay the same, 
but their meaning changes because 
the axes (basis vectors) have changed.


"""

"""
An example for the point:
Moving the vector by 𝐴 is equivalent 
to moving the axes by 𝐴^-1

Example: 
understanding A and A⁻¹ using a simple scaling matrix

Let:

A = [ 2  0
      0  1 ]

This matrix stretches space in 
the x-direction by a factor of 2.


1. Vector transformation (standard view)

Take a point:

x = (1, 1)

Apply A:

y = A x

y = (2*1, 1*1) = (2, 1)

So the point moves from:
(1,1) → (2,1)


2. What is A⁻¹?
A⁻¹ is the inverse transformation that undoes A.

So:

A⁻¹ = [ 1/2  0
        0    1 ]

This shrinks the x-direction by a factor of 2.

3. Using A⁻¹
Now apply A⁻¹ to y:

x = A⁻¹ y

x = (1/2 * 2, 1 * 1) = (1, 1)

So:

(2,1) → (1,1)


4. Key interpretation

* A stretches space (or vectors)
* A⁻¹ restores the original space

They exactly cancel each other:

A⁻¹ (A x) = x


5. Geometric intuition (axes view)

If instead of moving the vector you think of changing axes:
* A = stretching the space (vector view)
* A⁻¹ = shrinking the coordinate system so that 
the same point is re-measured correctly
So:
* stretching vectors is equivalent to shrinking axes
* shrinking vectors is equivalent to stretching axes

"""