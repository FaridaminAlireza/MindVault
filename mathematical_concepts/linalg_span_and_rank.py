"""
SPAN, RANK, AND LINEAR INDEPENDENCE
----------------------------------

1. LINEAR INDEPENDENCE
----------------------
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
---------
v1 = (1, 0)
v2 = (0, 1)
These are independent because no scalar multiple of v1 can produce v2.

v1 = (1, 2)
v2 = (2, 4)
These are dependent because v2 = 2*v1.

Linear independence is important because it tells us whether 
vectors add “new directions” to the space.


2. SPAN
-------
The SPAN of a set of vectors is the set of all possible
linear combinations of those vectors.

Mathematically:
    Span{v1, v2, ..., vk} = { c1*v1 + c2*v2 + ... + ck*vk | c1, c2, ..., ck ∈ ℝ }

Geometric meaning:
- In R^2: the span of one nonzero vector is a line through the origin.
- In R^2: the span of two independent vectors is the whole plane.
- In R^3: the span of three independent vectors is the whole 3D space.

Examples:
----------
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


3. RANK
-------
The RANK of a matrix is the number of linearly independent rows or columns.
It tells you the dimension of the space spanned by the rows (row rank)
or columns (column rank).
Row rank = Column rank = Rank(A)

So:
  Rank(A) = dimension of Span(columns of A) = number of independent columns.

How to find rank:
-----------------
Method 1: Gaussian Elimination
- Reduce the matrix to row echelon form.
- Count the number of non-zero rows. That count = rank.

Method 2: Check independence manually for small matrices.

Examples:
----------
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


4. RELATION BETWEEN SPAN, INDEPENDENCE, AND RANK
------------------------------------------------
- The span of a set of vectors tells you the "space covered".
- The rank tells you the DIMENSION of that span 
(how many independent directions it has).
- Linear independence determines whether adding a vector 
increases the span.

If you keep adding vectors:
- Each new independent vector increases the dimension of the span by 1.
- Once a vector is dependent, the span does NOT grow anymore.

Example:
---------
v1 = (1, 0)
v2 = (0, 1)
v3 = (1, 1)

Span{v1, v2} = ℝ^2
Adding v3 does NOT expand it because v3 = v1 + v2 → dependent
So Rank = 2 (two independent vectors)

"""