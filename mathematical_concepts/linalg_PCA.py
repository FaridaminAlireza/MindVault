"""
It chooses them because eigenvectors are the
directions where the covariance matrix acts as a pure scaling,
and the extreme values of the variance occur exactly in those directions.

INTRODUCTION

The goal of PCA (Principal Component Analysis), also called 
the Hotelling Transform in many image processing books, is 
to find a new coordinate system that describes 
the variation in data more naturally.

The key idea is:

* Original variables may be correlated.
* PCA finds new axes where the variables become uncorrelated.
* The first new axis captures the largest variation.
* The second new axis captures the next largest variation.
* And so on.

Geometrically, PCA rotates the coordinate system so 
that it aligns with the natural shape of the data cloud.

---
1. DATA AS OBSERVATIONS AND VARIABLES

Suppose we have 6 observations of 3 variables:

Observation 1: (x1, x2, x3)
Observation 2: (x1, x2, x3)
...
Observation 6: (x1, x2, x3)

Think of each observation as a point in 3D space.

If we plot all observations, they form a cloud of points.

PCA tries to answer:
"What directions best describe the spread of this cloud?"


CENTER THE DATA:

First compute the mean:

m_x = average of all observations
Then subtract the mean from every observation:
x_centered = (x - m_x)
This moves the cloud so that its center is located at the origin.

Without centering:
* The covariance matrix contains information about location and spread.
* PCA can become influenced by where the cloud sits relative to the origin.

With centering:
* The covariance matrix only measures variation around the center.
* PCA focuses on the shape of the cloud.

A useful interpretation:
Centering moves the coordinate system so that 
the origin sits at the center of mass of the data.

---
2. BUILDING THE COVARIANCE MATRIX

Covariance matrix:

C_x = E[(x - m_x)(x - m_x)^T]

For 3 variables:

C_x =
[var(x1)      cov(x1,x2)   cov(x1,x3)]
[cov(x2,x1)   var(x2)      cov(x2,x3)]
[cov(x3,x1)   cov(x3,x2)   var(x3)]

Interpretation:

Diagonal entries:
var(x1)
var(x2)
var(x3)
These measure how much each variable varies.

Off-diagonal entries:
cov(x1,x2)
cov(x1,x3)
cov(x2,x3)
These measure how two variables vary together.

For example, 
To get  cov(x1,x2):
    look at the six pairs:
    (x1 observation 1, x2 observation 1)
    (x1 observation 2, x2 observation 2)
    ...
    (x1 observation 6, x2 observation 6)

    So the six observations provide 
    the data used to calculate the covariance.

Dimensions after the matrix multiplication:
X_c = 6 x 3
X_c^T     = 3 x 6
X_c^T X_c = (3 x 6) (6 x 3)
C_x = (1/N) X_c^T X_c
C_x = 3 x 3    
  
WHY COVARIANCE LOOKS LIKE DOT PRODUCTS:
The covariance matrix is built from: (x - m_x)(x - m_x)^T
It can be viewed as a type of 
averaged dot-product relationship between variables.

---
3. EIGENVECTORS AND EIGENVALUES

Next solve:

C_x e_i = lambda_i e_i

where:
e_i = eigenvector
lambda_i = eigenvalue

Interpretation:
An eigenvector is a direction.
An eigenvalue tells how much variance exists along that direction.

For an eigenvector, the covariance matrix does not change its direction.
It only scales it:
e_i --> lambda_i * e_i


 WHY EIGENVECTORS ARE ORTHOGONAL

The covariance matrix is symmetric: C_x = C_x^T

A fundamental theorem says: A real symmetric matrix has:
* Real eigenvalues
* Orthogonal eigenvectors

Therefore: e_i^T e_j = 0 when i != j
and e_i^T e_i = 1 after normalization.

So PCA axes are perpendicular to one another.

---
4. BUILDING THE MATRIX E
Place eigenvectors as columns:

E = [e1 e2 e3]
ordered from largest eigenvalue to smallest:
lambda1 >= lambda2 >= lambda3

The first column corresponds to 
the direction with the largest variance.

---
5. BUILDING THE HOTELLING TRANSFORM

The book defines: A = E^T
which means the eigenvectors are placed as rows:
A =
[e1^T]
[e2^T]
[e3^T]

The PCA transformation is:

y = A(x - m_x)

or y = E^T(x - m_x)

WHAT DOES y REPRESENT?

The transformed vector:
y =
[y1]
[y2]
[y3]

Each component is:

y1 = e1^T(x - m_x)

y2 = e2^T(x - m_x)

y3 = e3^T(x - m_x)

Interpretation:

Each y-value is a projection onto an eigenvector direction.

Geometrically:

y1 = distance from the mean along principal axis 1
y2 = distance from the mean along principal axis 2
y3 = distance from the mean along principal axis 3


GEOMETRIC INTERPRETATION

Before PCA:
* The cloud may be tilted.
* The coordinate axes do not match the cloud.

After PCA:
* The coordinate system rotates.
* The new axes align with the cloud.

The cloud itself does not move.
Only the coordinate system changes.

PC1 points along the direction of largest spread.
PC2 points along the second-largest spread.
PC3 points along the third-largest spread.

---
6. COVARIANCE OF THE TRANSFORMED DATA

The covariance of y is:

C_y = E[(y - m_y)(y - m_y)^T]

Since y is centered: m_y = 0

Therefore: C_y = E[yy^T]

Substituting: y = A(x - m_x)

gives: C_y = A C_x A^T

This is the general covariance transformation formula.

---
7. THE KEY PCA DERIVATION

WHY MATRIX MULTIPLICATION ACTS ON EACH COLUMN

Suppose:

E = [e1 e2 e3]

Then: C_x E

means: C_x E = [C_x e1   C_x e2   C_x e3]

This follows directly from the definition of matrix multiplication.

The matrix acts separately on each column.

---
Because each column is an eigenvector:

C_x e1 = lambda1 e1
C_x e2 = lambda2 e2
C_x e3 = lambda3 e3

Therefore:

C_x E = E Lambda

where

Lambda =

[lambda1 0       0]
[0       lambda2 0]
[0       0       lambda3]

Now: C_y = E^T C_x E

Substitute: C_x E = E Lambda

giving: C_y = E^T E Lambda

Since eigenvectors are orthonormal:

E^T E = I

Therefore: C_y = Lambda

This is the central result of PCA.

WHY THE OFF-DIAGONALS BECOME ZERO

After PCA:
C_y =
[lambda1 0       0]
[0       lambda2 0]
[0       0       lambda3]

The off-diagonal entries are covariances.

Therefore:
cov(y1,y2) = 0
cov(y1,y3) = 0
cov(y2,y3) = 0

The transformed variables are uncorrelated.

This does NOT happen merely because the axes are orthogonal.
It happens because:
1. The axes are eigenvectors of the covariance matrix.
2. The eigenvectors are orthogonal.
Both facts are required.

---
8. WHAT THE EIGENVALUES MEAN IN PCA

After transformation:

var(y1) = lambda1
var(y2) = lambda2
var(y3) = lambda3

sweet :-) -> 
Thus: Each eigenvalue equals the variance 
along its corresponding principal axis.

This is one of the most important interpretations in PCA.

---
9. DIMENSIONALITY REDUCTION

Suppose:

lambda1 = 100
lambda2 = 20
lambda3 = 1

Almost all variation exists in the first two directions.
The third direction contributes very little.

We may keep:
y1
y2
and discard: y3

This reduces dimensionality 
while preserving most information.

---
10. RECONSTRUCTION

The forward transform is:

y = E^T(x - m_x)

The inverse transform is:

x = m_x + E y

If only the first k components are kept:
x_approx = m_x + sum(y_i * e_i)
for i = 1 to k

Thus the original data can be approximated
using only the most important principal directions.

---
11. PCA FOR IMAGES

Suppose we have 6 registered images.

For each pixel location:

x =
[I1(r,c)
I2(r,c)
...
I6(r,c)]

Apply PCA:

y = A(x - m_x)

which gives:

[y1
y2
...
y6]

for that pixel.

Now repeat for every pixel location.

PRINCIPAL COMPONENT IMAGES:

The first component image is formed by 
collecting all y1 values.

For every pixel:
store y1(r,c)
and reshape into image form.

Similarly:
Component Image 2 uses all y2 values.
Component Image 3 uses all y3 values.
etc.

Thus:
6 original images
become
6 principal component images.

Typically:

* Component 1 contains most information.
* Later components contain progressively less variance.
* The last components often contain mostly noise.

---
12. THE MOST IMPORTANT POINT

PCA finds a new orthogonal coordinate system, 
centered at the data mean, in which:

* The covariance matrix becomes diagonal.
* The transformed variables become uncorrelated.
* Each eigenvalue equals the variance along its eigenvector.
* The first few principal directions contain most of
 the information in the data.

#
"""
