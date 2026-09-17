"""
Understanding Linear Transformations Through Basis Vectors

Introduction

A useful way to understand linear transformations is
to start with the idea of a basis.

In 2D, the standard basis consists of two vectors:
e1 = [1, 0]
e2 = [0, 1]

Any vector can be written as 
a combination of these basis vectors.
For example:
x = [3, 1]
means: x = 3*e1 + 1*e2

Geometrically, the vector points to the position (3, 1).

The important idea is that a matrix transformation
can be understood by asking:

"What does the transformation do to the basis vectors?"
Once we know what happens to the basis vectors, we know 
what happens to every other vector.

1. Matrix Transformation and Basis Vectors

Suppose we have a matrix A:

A = [a11 a12
     a21 a22]

and a vector:

x = [x1
     x2]

Then: y = A*x

Expanding the multiplication:

y = [a11*x1 + a12*x2
     a21*x1 + a22*x2]

There is another, more geometric way to understand this.

The columns of A are:

A*e1 = [a11
        a21]

A*e2 = [a12
        a22]

Therefore:

A*x = x1*(A*e1) + x2*(A*e2)

This means that A transforms 
the original basis vectors into new vectors.

The original vector was:

x = x1*e1 + x2*e2

After transformation:

A*x = x1*(A*e1) + x2*(A*e2)

So the same coefficients x1 and x2 are used,
but the basis vectors have been transformed.

This is one of the most important geometric 
interpretations of matrix multiplication.

---
Two Ways to Interpret a Transformation
There are two closely related ways to think about a matrix.

- First interpretation: transform the vector:
The coordinate system stays fixed, while the vector moves.

For example: x -> A*x
The arrow representing x changes its position, direction, or length.
This is called an active transformation.

- Second interpretation: transform the basis.
Instead of imagining that the vector moves, 
we can imagine that the coordinate axes or basis vectors have changed.
* The vector can be viewed relative to these new basis vectors.
* This is closely related to a change of coordinates or a change of basis.

The two interpretations use the same mathematical machinery,
but they answer different geometric questions.

--
2. Rotation

A rotation changes the direction of a vector while preserving its length.

The 2D rotation matrix for an angle theta is:

R = [cos(theta)  -sin(theta)
     sin(theta)   cos(theta)]

Applying it to a vector gives:

x_new = R*x

Geometrically, the coordinate system can be thought of
as staying fixed while the vector rotates.

But we can also look at the columns of R.

The first column is:

R*e1 = [cos(theta)
        sin(theta)]

The second column is:

R*e2 = [-sin(theta)
        cos(theta)]

These are the original basis vectors
after they have been rotated.

Therefore, a rotation matrix can be understood as:
"Rotate the basis vectors."

Then every other vector is constructed 
from these rotated basis vectors.

---
3. Scaling

Scaling changes the length of vectors.

A simple 2D scaling matrix is:

S = [sx  0
     0   sy]

Applying it:

[x_new]   [sx  0] [x]
[y_new] = [0   sy] [y]

Therefore:

x_new = sx*x
y_new = sy*y

For example:
S = [2  0
     0  1]

means:
x_new = 2*x
y_new = y

So the horizontal direction is stretched by a factor of 2,
while the vertical direction is unchanged.

Looking at the basis vectors:

S*e1 = [2
        0]

S*e2 = [0
        1]

Therefore, the first basis vector becomes 
twice as long, while the second basis vector 
stays the same.

This explains the geometric effect of scaling.

---
4. Shear Transformation
A shear transformation tilts an object 
by moving points in one direction according 
to their position in another direction.

A horizontal shear is:

H = [1  k
     0  1]

Applying it to:

x = [x
     y]

gives:

H*x = [x + k*y
       y]

Therefore:

x_new = x + k*y
y_new = y

The vertical coordinate does not change.
The horizontal coordinate changes according to the height y.
This means that points higher up move farther horizontally.

- Shear and the Basis Vectors:

The easiest way to understand the shear matrix is again
to look at what it does to the basis vectors.

The standard basis is:

e1 = [1
      0]

e2 = [0
      1]

For:

H = [1  k
     0  1]

we get:

H*e1 = [1
        0]

and:

H*e2 = [k
        1]

So:

* e1 stays unchanged.
* e2 tilts.

For example, when k = 1:

H*e1 = [1
        0]

H*e2 = [1
        1]

The horizontal axis stays where it was,
while the vertical basis vector becomes tilted.

Consequently, a square becomes a parallelogram.

- What Happens to a Square Under Shear?

Start with the unit square:

(0,0), (1,0), (0,1), (1,1)

Using:

H = [1  1
     0  1]

we transform each corner.

(0,0) -> (0,0)

(1,0) -> (1,0)

(0,1) -> (1,1)

(1,1) -> (2,1)

The square therefore becomes a parallelogram.

The important point is that the object has been tilted,
rather than simply rotated or uniformly stretched.

- Shear Does Not Change Area

The determinant of the horizontal shear matrix is:
det(H) = 1*1 - 0*k

Therefore: det(H) = 1
The absolute value of the determinant tells us
the area-scaling factor.

Since: |det(H)| = 1
a pure shear preserves area.

It changes the shape but not the area.

For example, a unit square has area 1.
After the shear, the resulting parallelogram still has area 1.

- Vertical Shear

There is also a vertical shear:

V = [1  0
     k  1]

Applying it:

V*[x
   y]

gives:

[x
k*x + y]

Therefore:

x_new = x

y_new = k*x + y

This time, the horizontal position determines
how much a point moves vertically.

So:

Horizontal shear:
x_new = x + k*y
y_new = y

Vertical shear:
x_new = x
y_new = y + k*x

---
5. Comparing the Main Transformations

Rotation:
The direction of vectors changes.
Length is preserved.
Angles are preserved.

Example:
R = [cos(theta)  -sin(theta)
sin(theta)   cos(theta)]

Scaling:
The lengths of vectors change.
Angles can remain unchanged for uniform scaling,
but non-uniform scaling can change angles.

Example:
S = [sx  0
     0   sy]

Horizontal shear:
The shape is tilted horizontally.
x_new = x + k*y
y_new = y
Vertical shear:
The shape is tilted vertically.
x_new = x
y_new = y + k*x

-> The Unifying Idea
Rotation, scaling, and shear may look like
very different operations,
but they can all be understood through the same idea:
Look at what happens to the basis vectors.

For a matrix A:
A = [column1  column2]

the first column tells us:
"What happens to e1?"

The second column tells us:
"What happens to e2?"

Then any vector:
x = x1*e1 + x2*e2

becomes:
A*x = x1*(A*e1) + x2*(A*e2)

So a matrix transformation can be thought of as changing the basis
vectors and then reconstructing every vector using the same coefficients.

---
Geometric Summary:

The most useful mental picture is:

Original basis:
e1 = horizontal axis
e2 = vertical axis

A transformation changes these basis vectors.

Rotation: Both basis vectors rotate while remaining perpendicular 
and keeping their lengths.

Scaling: The basis vectors become longer or shorter.

Shear: One basis vector becomes tilted relative to the other.

More generally, a matrix can simultaneously 
rotate, stretch, shrink, reflect, and shear a shape.

The columns of the matrix tell you exactly what happens 
to the original basis vectors.

This is why examining the columns of a transformation matrix
is such a powerful way to understand its geometry.

---
Important Distinction: Transformation vs Change of Basis

There is one subtle point to keep separate.

When we calculate: y = A*x
we normally interpret this as transforming the vector x
into a new vector y while keeping the coordinate axes fixed.

But when we talk about a change of basis, 
we are asking a different question:
"The geometric vector stays the same, but 
what are its coordinates when I describe it 
using a different set of basis vectors?"

The same kinds of matrices appear in both contexts,
but the interpretation is different.

The safest way to avoid confusion is to always ask:
"Am I moving the vector, or am I changing 
the coordinate system used to describe the vector?"

#
"""