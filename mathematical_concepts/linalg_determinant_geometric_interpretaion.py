"""
A determinant is only defined for square matrices (n × n).
Why?
The determinant has a geometric meaning:

For a square matrix: it measures volume scaling in n dimensions
But a non-square matrix does not map: ℝⁿ → ℝⁿ
instead it maps ℝⁿ → ℝᵐ (different dimension)

So: You cannot define a “volume scaling factor” in the same way
→ hence no determinant

Example:
A =
[ 1  2  3
4  5  6 ]   (2 × 3 matrix)
det(A) does not exist.

What you can do instead:

1. Rank → number of independent rows/columns
2. Minors → determinants of square submatrices (e.g., 2×2 parts)
3. Form square matrices:
   * AᵀA or AAᵀ (these are square, so determinants exist)

"""

"""
The determinant is a number associated with a square matrix.
Although it can be calculated algebraically, its most useful 
interpretation is geometric.

A matrix represents a transformation of space.
The determinant tells us what happens to the overall size of objects
under that transformation.

In 2D: absolute(det(A)) = area scaling factor

In 3D: absolute(det(A)) = volume scaling factor

More generally: 
absolute(det(A)) = n-dimensional volume scaling factor

The determinant also tells us 
whether a transformation has collapsed a dimension 
and whether the matrix has an inverse.

---
2. DETERMINANT AS A GEOMETRIC SCALING FACTOR

Imagine starting with a square having area 1.
If a transformation changes it into a shape with area 6:
absolute(det(A)) = 6
The transformation has multiplied the area by 6.

If: absolute(det(A)) = 0.5
the area has been reduced by half.

If: absolute(det(A)) = 1
the area has remained unchanged.

Therefore:
determinant = overall area/volume scaling

IMPORTANT:
The determinant does NOT tell us the exact new shape.
A transformation can rotate, stretch, compress, or shear 
an object while the determinant only describes 
the overall area or volume scaling.

---
3. EXAMPLE: SCALING IN 3D

Consider the transformation:

A = [ 2  0  0
      0  1  0
      0  0  2 ]

This transformation does:

x direction: multiplied by 2
y direction: unchanged
z direction: multiplied by 2

Its determinant is:

det(A) = 2 * 1 * 2 = 4

Therefore: new volume = 4 * original volume


Example: 
Suppose an object initially has dimensions:
3 x 5 x 2

Its volume is: 3 * 5 * 2 = 30

After the transformation:
3 -> 6
5 -> 5
2 -> 4


The new volume is: 6 * 5 * 4 = 120


Therefore: 120 / 30 = 4

which agrees with: det(A) = 4

---
4. WHY CAN THE DETERMINANT BE NEGATIVE?

The determinant is actually a signed scaling factor.
The absolute value tells us how much area or volume changes:

absolute(det(A)) = amount of scaling

The sign tells us whether the orientation has been reversed.

For example: det(A) = 2
means:
volume is multiplied by 2
orientation is preserved


while:
det(A) = -2
means:
volume is multiplied by 2
orientation is reversed

Therefore:
sign of det(A)
    =
orientation information

---
5. THE MOST IMPORTANT CASE: det(A) = 0

Now consider:
A = [ 1  0
      0  0 ]


Apply this matrix to:

x = [ x
      y ]

We get:

Ax = [ x
       0 ]


Therefore:

(x, y) -> (x, 0)

The entire 2D plane is being mapped onto the x-axis.

Before:

          y
          ^
          |
    .-----------.
    |            |
    |   2D       |
    |   region   |
    |            |
    '------------' ---> x


After:


          y
          ^
          |
          |
    ==================> x


Everything has been compressed onto one line.

WHY IS THIS CALLED "FLATTENING"?
Originally the object occupied 2 dimensions.
After the transformation, it occupies only 1 dimension.

Therefore: 2D -> 1D

The area has become: area = 0
because a line has no 2D area.
This is what "flattening" means in this context.

A dimension has completely disappeared.

In 3D, the same idea can happen: 3D -> 2D


For example:
a solid object -> flat plane
Then: volume = 0
It could also collapse further:
3D -> 1D or: 3D -> 0D

-> The important idea is: det(A) = 0
means that the transformation has collapsed
at least one dimension.

---
WHY DOES FLATTENING MEAN INFORMATION LOSS?

Consider two different points:

x1 = [ 2
       3 ]

x2 = [ 2
       7 ]


Using:

A = [ 1  0
      0  0 ]


we obtain:

Ax1 = [ 2
        0 ]

Ax2 = [ 2
        0 ]

Two different inputs produce exactly the same output.
This means that after the transformation, 
we cannot determine which original point we had.

For example, if we only see:
[ 2
  0 ]

the original point could have been:
[ 2
  3 ]

or any point of the form:

[ 2
  y ]

The y information has disappeared.

Therefore:
dimension collapse -> information loss

---
6. DETERMINANT AND INVERTIBILITY

An inverse transformation is supposed
to undo the original transformation.

For matrix A:
A_inverse * A = I
where I is the identity matrix.

But if different inputs produce the same output,
there is no unique way to reverse the transformation.

Therefore:
det(A) = 0 -> A is not invertible

The fundamental relationship is:
det(A) = 0 -> information is lost ->
transformation cannot be uniquely reversed ->
A has no inverse

Conversely:
det(A) != 0 -> no complete dimension collapse ->
A is invertible -> 
the original point can be uniquely recovered


---
7. DETERMINANT AND EIGENVALUES

There is an important connection between
the determinant and eigenvalues.

For an n by n matrix:

det(A) = lambda1 * lambda2 * ... * lambdan

where the lambda values are the eigenvalues.

Recall the eigenvector equation:
A qi = lambda_i qi
This means: qi = special direction
and: lambda_i = scaling along that direction


Therefore, the eigenvalues can be thought of 
as directional scaling factors 
along the eigenvector directions.

The determinant combines all of these scaling factors:

determinant = product of directional scaling factors

---
EXAMPLE: EIGENVALUES AND VOLUME
Suppose a 3D transformation has eigenvalues:
lambda1 = 2
lambda2 = 1
lambda3 = 2
The transformation therefore scales 
its three eigenvector directions by:
2
1
2
The total volume scaling is: 2 * 1 * 2 = 4
Therefore: det(A) = 4
This gives a useful geometric interpretation:
eigenvalues -> scaling in individual directions
product of eigenvalues -> overall volume scaling
determinant -> overall volume scaling

---
8. ZERO EIGENVALUE AND FLATTENING
Suppose instead:
lambda1 = 2
lambda2 = 1
lambda3 = 0
For the third eigenvector: A q3 = 0 q3
Therefore: A q3 = 0
The entire third direction has been collapsed.
There is no remaining length in that direction.
Consequently: det(A) = 2 * 1 * 0 = 0

So: 
zero eigenvalue ->
one direction completely disappears ->
dimension is lost ->
volume becomes zero ->
determinant is zero ->
matrix is not invertible

This is one of the clearest connections between
eigenvalues and determinants.
---
9. HOW DIFFERENT TRANSFORMATIONS AFFECT THE DETERMINANT

SCALING

Example:
A = [ 2  0
      0  3 ]
Then: det(A) = 6
Area is multiplied by 6.

ROTATION

A pure rotation has:
absolute(det(A)) = 1
It changes orientation in space 
but does not change area or volume.
Therefore:
determinant magnitude = 1


SHEARING

A shear can dramatically change the shape
of an object while preserving its area or volume.

For a typical 2D shear: det(A) = 1
So: shape changes, area stays the same


REFLECTION

A reflection has:
det(A) = -1
The size of the object stays the same,
but its orientation is reversed.

FLATTENING

If: det(A) = 0
then at least one dimension is completely collapsed.


---
10. MAIN APPLICATIONS OF THE DETERMINANT

The determinant is useful for several reasons.

- CHECKING INVERTIBILITY

If: det(A) != 0 then A has an inverse.

If: det(A) = 0 then A has no inverse.

- MEASURING AREA OR VOLUME SCALING

In 2D: absolute(det(A)) = area scaling
In 3D: absolute(det(A)) = volume scaling

- DETECTING DIMENSIONAL COLLAPSE
If: det(A) = 0
then the transformation has lost 
at least one dimension.
This means information has been lost.

- UNDERSTANDING EIGENVALUES

Because: det(A) = lambda1 * lambda2 * ... * lambdan
the determinant gives the 
combined effect of all eigen-direction scalings.

- LINEAR SYSTEMS

For a system: Ax = b
a nonzero determinant means A is invertible,
so there is a unique solution.

A zero determinant means A is not invertible,
so the system does not have a unique solution.

---
11. CONNECTION TO PCA

The determinant is not the main operation used to perform PCA,
but it helps connect several important ideas.

PCA starts with a covariance matrix: C

The covariance matrix describes how the data spreads.
Its eigenvectors give the principal directions.
Its eigenvalues give the variance along those directions.

The determinant of the covariance matrix is:
det(C) = lambda1 * lambda2 * ... * lambdan

Therefore, the determinant is the product of 
the variances along the principal directions.

Geometrically, the covariance matrix can be associated
with an ellipsoid describing the spread of the data.
The eigenvectors give the principal axes of that ellipsoid.
The eigenvalues describe the amount of variance along those axes.

The determinant combines all of them into 
an overall volume-related quantity.

---
12. THE KEY CONCEPTUAL CHAIN

MATRIX
   |
   v
TRANSFORMATION
   |
   v
CHANGES VECTORS AND SHAPES
   |
   v
EIGENVECTORS
   |
   v
SPECIAL DIRECTIONS
   |
   v
EIGENVALUES
   |
   v
SCALING IN THOSE DIRECTIONS
   |
   v
PRODUCT OF EIGENVALUES
   |
   v
DETERMINANT
   |
   v
OVERALL AREA / VOLUME SCALING


For the special case of flattening:


DET(A) = 0
     |
     v
VOLUME = 0
     |
     v
AT LEAST ONE DIMENSION COLLAPSES
     |
     v
INFORMATION IS LOST
     |
     v
MATRIX IS NOT INVERTIBLE

-
"""