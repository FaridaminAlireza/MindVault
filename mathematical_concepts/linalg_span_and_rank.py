"""
SPAN, RANK, AND LINEAR INDEPENDENCE


LINEAR INDEPENDENCE

Vectors are said to be LINEARLY INDEPENDENT if 
none of them can be written as a linear combination of the others.

Formally, a set of vectors {v1, v2, ..., vk} is linearly independent
 if the only solution to:
c1*v1 + c2*v2 + ... + ck*vk = 0
is
c1 = c2 = ... = ck = 0

If there exists a non-zero combination (some ci ≠ 0) that
makes the sum zero, then the vectors are LINEARLY DEPENDENT.

Example:

v1 = (1, 0)
v2 = (0, 1)
These are independent because no scalar multiple of v1 can produce v2.

v1 = (1, 2)
v2 = (2, 4)
These are dependent because v2 = 2*v1.

Linear independence is important because it tells us whether 
vectors add “new directions” to the space.

---
SPAN

The SPAN of a set of vectors is the set of all possible
linear combinations of those vectors.

Mathematically:
    Span{v1, v2, ..., vk} = { c1*v1 + c2*v2 + ... + ck*vk | c1, c2, ..., ck ∈ ℝ }

Geometric meaning:
- In R^2: the span of one nonzero vector is a line through the origin.
- In R^2: the span of two independent vectors is the whole plane.
- In R^3: the span of three independent vectors is the whole 3D space.

Examples:

Example 1:
v1 = (1, 0)
v2 = (0, 1)
→ Span{v1, v2} = all of ℝ^2 (the entire 2D plane)

Example 2:
v1 = (1, 2)
→ Span{v1} = all multiples of (1, 2), i.e., a line through the origin.

Example 3:
v1 = (1, 2)
v2 = (2, 4)
Since v2 = 2*v1, they are dependent.
→ Span{v1, v2} = Span{v1} = a line.

---
RANK

The RANK of a matrix is the number of linearly independent rows or columns.
It tells you the dimension of the space spanned by the rows (row rank)
or columns (column rank).
Row rank = Column rank = Rank(A)

So:
  Rank(A) = dimension of Span(columns of A) = number of independent columns.

How to find rank:

Method 1: Gaussian Elimination
- Reduce the matrix to row echelon form.
- Count the number of non-zero rows. That count = rank.

Method 2: Check independence manually for small matrices.

Examples:

Example 1:
A = [ [1, 2],
      [2, 4] ]

Row2 = 2 * Row1 → dependent
=> Only one independent row
=> Rank(A) = 1
=> Column span is a line in ℝ^2

Example 2:
B = [ [1, 2],
      [3, 4] ]

No row or column is a multiple of another.
=> Both are independent
=> Rank(B) = 2
=> Column span = ℝ^2 (the whole 2D plane)

Example 3:
C = [ [1, 2, 3],
      [2, 4, 6],
      [1, 1, 1] ]

Perform row operations:
R2 = R2 - 2*R1 → [0, 0, 0]
R3 = R3 - R1   → [0, -1, -2]
Now we have two non-zero rows → rank = 2

So, Rank(C) = 2, meaning the columns (or rows) span a 2D subspace of ℝ^3.

---
RELATION BETWEEN SPAN, INDEPENDENCE, AND RANK

- The span of a set of vectors tells you the "space covered".
- The rank tells you the DIMENSION of that span 
(how many independent directions it has).
- Linear independence determines whether adding a vector 
increases the span.

If you keep adding vectors:
- Each new independent vector increases the dimension of the span by 1.
- Once a vector is dependent, the span does NOT grow anymore.

Example:

v1 = (1, 0)
v2 = (0, 1)
v3 = (1, 1)

Span{v1, v2} = ℝ^2
Adding v3 does NOT expand it because v3 = v1 + v2 → dependent
So Rank = 2 (two independent vectors)

"""

"""
ORTHONORMAL SETS, SUBSPACES, AND BASIS

SUBSPACES
A subspace is a subset of a vector space 
that is also a vector space by itself.

To be a subspace, a set of vectors must satisfy three conditions:
1. It contains the zero vector.
2. It is closed under vector addition (u + v is in the set).
3. It is closed under scalar multiplication (c * u is in the set).

Examples:

- In ℝ³, the set of all vectors lying on a plane through the origin is a subspace.
- The set of all scalar multiples of (1, 2, 3) forms a line through the origin → a 1D subspace.
- The span of any set of vectors is always a subspace.

Intuitively:
A subspace represents a "flat" region 
(line, plane, or higher-dimensional analog) that passes through the origin.

---
BASIS

A basis of a vector space (or subspace) is a set of vectors that:
1. Are linearly independent, and
2. Span the space.

The number of vectors in the basis is called the dimension of the space.

Formally:

Let V be a vector space. A set of vectors 
{v1, v2, ..., vk} is a BASIS of V if:
- Span{v1, v2, ..., vk} = V
- The vectors are linearly independent.

Examples:

Example 1:
The standard basis for ℝ² is:
   e1 = (1, 0)
   e2 = (0, 1)
→ These are independent and span ℝ².
→ Basis = {e1, e2}, Dimension = 2

Example 2:
In ℝ³, the standard basis is:
   e1 = (1, 0, 0)
   e2 = (0, 1, 0)
   e3 = (0, 0, 1)
→ Basis = {e1, e2, e3}, Dimension = 3

Example 3:
Let v1 = (1, 2, 3), v2 = (2, 4, 6)
→ v2 = 2*v1 → dependent → cannot be a basis
→ The span is just a line (dimension = 1)
→ Basis could be just {v1}.


---
ORTHONORMAL SETS
 
A set of vectors is orthonormal if:
1. Each pair of different vectors is orthogonal (their dot product is 0).
2. Each vector has unit length (its magnitude is 1).

Mathematically:
   For vectors u_i and u_j in the set:
       u_i ⋅ u_j = 0 if i ≠ j
       u_i ⋅ u_i = 1

Examples:

Example 1:
In ℝ²:
   u1 = (1, 0)
   u2 = (0, 1)
→ u1 ⋅ u2 = 0 and both have length 1 → orthonormal set

Example 2:
In ℝ³:
   u1 = (1, 0, 0)
   u2 = (0, 1, 0)
   u3 = (0, 0, 1)
→ Orthonormal set (standard basis of ℝ³)

Example 3:
   u1 = (1/√2, 1/√2)
   u2 = (−1/√2, 1/√2)
→ Also orthonormal, rotated 45° from the standard basis.


---
RELATIONSHIPS BETWEEN ORTHONORMAL SETS, SUBSPACES, AND BASIS
- The span of a set of vectors forms a subspace.
- A basis is a minimal set of independent vectors that span a subspace.
- If the basis vectors are orthonormal, then they form an orthonormal basis.

An orthonormal basis has nice properties:
- Coordinates of any vector can be found easily using dot products.
- Transformations and projections are simpler.
- The Gram-Schmidt process can convert any independent set
into an orthonormal one.

Example:

Let’s say we have:
   u1 = (1/√2, 1/√2)
   u2 = (−1/√2, 1/√2)

They are orthonormal. So, any vector v = (x, y) can be written as:
   v = (v ⋅ u1)u1 + (v ⋅ u2)u2

The coefficients (v ⋅ u1) and (v ⋅ u2) are 
the vector’s coordinates in this orthonormal basis.

In summary:
- Subspace = region (like line/plane) that’s closed under linear operations.  
- Basis = smallest independent set that defines that subspace.  
- Orthonormal set = “nice” basis with perpendicular unit-length vectors.
"""

"""
ZERO VECTOR

A zero vector is the vector whose all components are zero.

In ℝ² → (0, 0)  
In ℝ³ → (0, 0, 0)  
In general, in ℝⁿ → (0, 0, 0, ..., 0)

It is usually denoted as 0 or →0.

Mathematically:
If v = (v₁, v₂, ..., vₙ), then
    v = 0  ⇔  v₁ = v₂ = ... = vₙ = 0

Properties:
1. Additive Identity:
   For any vector v,
       v + 0 = v
   The zero vector acts like “0” does for real numbers.

2. Scalar Multiplication:
   For any scalar c,
       c * 0 = 0

3. Zero Magnitude:
   The zero vector has length (or magnitude) 0:
       ||0|| = 0

4. Not Directional:
   Unlike other vectors, the zero vector has 
   no direction, only a magnitude of zero.

5. Belongs to Every Subspace:
   The zero vector is always part of every subspace,
   because it satisfies closure under addition 
   and scalar multiplication.


Examples:

- In 2D:  (0, 0)
- In 3D:  (0, 0, 0)
- In 4D:  (0, 0, 0, 0)
In each case, it’s the “neutral” element for vector addition.

Geometric Meaning:
It’s the point at the origin of the coordinate system
 — where all components are zero.

In diagrams, it’s represented by a dot at the origin 
(not an arrow), since it has no direction and zero length.

Summary: The zero vector is the additive identity in vector spaces,
has zero magnitude, and is contained in every subspace.
"""