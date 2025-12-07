"""
Lower Triangular Matrix Determinant

Definition:
A square matrix 
A = [a_ij] of size n x n 
is lower triangular 
if all entries above the main diagonal are zero:
a_ij = 0 for all i < j

Example (3x3 lower triangular matrix):
A = | a_11   0     0   |
    | a_21  a_22   0   |
    | a_31  a_32  a_33 |

Claim:
For a lower triangular matrix, 
the determinant is the product of the diagonal elements:
det(A) = a_11 * a_22 * ... * a_nn 
= product_{i=1}^{n} a_ii

Proof by Induction:

Step 1: Base case (n=1)
A = [a_11] → det(A) = a_11  True

Step 2: Inductive hypothesis
Assume true for 
(n-1)x(n-1) lower triangular matrix B:
det(B) = product_{i=1}^{n-1} b_ii

Step 3: Inductive step
Consider n x n lower triangular matrix:
A = | a_11   0     0   ...   0   |
    | a_21  a_22   0   ...   0   |
    | a_31  a_32  a_33 ...   0   |
    | ...   ...   ... ...  ...   |
    | a_n1  a_n2  a_n3 ...  a_nn |

Use cofactor expansion along the first row:
det(A) = sum_{j=1}^{n} (-1)^{1+j} a_1j * det(M_1j)

Step 4: Simplify using triangular structure

* For j>1, a_1j = 0
* Only j=1 survives:
  det(A) = a_11 * det(M_11)

M_11 is (n-1)x(n-1) lower triangular 
with diagonal elements a_22, a_33, ..., a_nn
By inductive hypothesis:
det(M_11) = product_{i=2}^{n} a_ii

Step 5: Combine
det(A) = a_11 * product_{i=2}^{n} a_ii =
product_{i=1}^{n} a_ii  Proven

---
Quick Algebraic Proof Using Row Operations:

1. Determinant is unchanged if 
we add a multiple of one row to another row below it.
2. In a lower triangular matrix, 
all entries above the diagonal are already zero.
3. No row operations are needed 
to create zeros above the diagonal.
4. Determinant of a triangular matrix = 
product of diagonal entries 
(because determinant is the product of
 pivots in Gaussian elimination).

Thus, det(A) = a_11 * a_22 * ... * a_nn.

"""

"""
Example for the second proof:

Pivot in Gaussian Elimination:

* A pivot is the first nonzero element in
a row (from left to right) used to 
eliminate entries below it in that column.
* During Gaussian elimination, we transform 
a matrix into row echelon form 
(upper triangular form).
* The determinant of a matrix equals 
the product of its pivots, 
up to sign changes if rows are swapped.
* For triangular matrices, 
no row swaps are needed, so 
the determinant = product of diagonal elements.

---

Example: Triangular Matrix

Consider a 3x3 lower triangular matrix:

A = | 2   0   0 |
    | 3   4   0 |
    | 1  -2   5 |

We want to compute det(A) 
and show the determinant rule holds.

---

Step 1: Identify pivots

Since A is lower triangular,
the pivots are the diagonal elements:
Pivot 1 = a_11 = 2
Pivot 2 = a_22 = 4
Pivot 3 = a_33 = 5

---
Step 2: Gaussian elimination (for demonstration)

We perform elimination to make entries below 
the diagonal zero, but they are already zero 
above the diagonal.

* Row 1 pivot = 2 → no elimination needed 
(row 2 and 3 already have zeros above column 1 in
 upper triangular form, but let's simulate):

  Eliminate below pivot:
  row2 = row2 - (3/2)*row1 → new row2 = [0, 4, 0]
  row3 = row3 - (1/2)*row1 → new row3 = [0, -2, 5]

* Row 2 pivot = 4 → eliminate below:
  row3 = row3 - (-2/4)*row2 
  = row3 + 0.5*row2 → new row3 = [0, 0, 5]

Now matrix is upper triangular:

U = | 2   0   0 |
    | 0   4   0 |
    | 0   0   5 |

    
Step 3: Determinant from pivots

* Determinant = product of pivots = 2 * 4 * 5 = 40

Step 4: Verify determinant using original formula

* For a lower triangular matrix, 
determinant = product of diagonal elements:
  det(A) = a_11 * a_22 * a_33 = 2 * 4 * 5 = 40  True

  
Step 5: Conclusion

* The pivots in Gaussian elimination are 
the diagonal elements for triangular matrices.
* Gaussian elimination provides an algebraic 
confirmation of the rule ( the determinant for
triangular matrices (product of diagonal elements))
* This method works for upper or lower triangular 
matrices and scales to any n x n matrix.

"""

"""
Determinant = Product of Pivots in Row Echelon Form

Step 1: Gaussian Elimination and Row Echelon Form

Gaussian elimination transforms matrix A 
into row echelon form U.

Row echelon form properties:

1. All zero rows are at the bottom.
2. Pivot is first nonzero element of each row.
3. Entries below each pivot are zero.
   Let p_1, p_2, ..., p_n be the pivots.

---

Step 2: Effect of Row Operations

Three types of row operations:

1. Swap two rows: determinant changes sign.
2. Multiply a row by k: multiplies determinant by k.
3. Add multiple of one row to another: determinant unchanged.
   Gaussian elimination uses type 3 only, except swaps.

---
Step 3: Determinant of Triangular Matrix

Upper triangular matrix U has zeros below pivots.
Determinant = product of diagonal elements.
Recursive expansion along first row gives product of pivots.

---
Step 4: Combining Steps

Let A be any square matrix.
Apply Gaussian elimination to get U.
Number of row swaps = s.
Then det(A) = (-1)^s * det(U).
det(U) = product of pivots = p_1 * ... * p_n.
If no swaps, det(A) = product of pivots.

---

Step 5: Important Notes

Triangular matrices: no swaps needed.
Adding multiples of rows does not change determinant.
General matrices may require swaps; include (-1)^s sign.

---

Step 6: Summary

Gaussian elimination transforms A → U (upper triangular).
Determinant changes only by row swaps or scaling.
det(U) = product of pivots.
det(A) = (sign from swaps) * (product of pivots).

---

Numerical 3x3 Example

A = | 2  1  3 |
    | 4  2  6 |
    | 1  1  1 |

Step 1: Pivot 1 = 2
Eliminate below pivot:
Row2 = Row2 - 2*Row1 → [0 0 0]
Row3 = Row3 - 0.5*Row1 → [0 0 -0.5]

Step 2: Pivot 2 = 0 (skip or swap row2/row3)
Swap row2 and row3: determinant sign changes
New row2 = [0 0 -0.5], row3 = [0 0 0]

Step 3: Pivot 3 = -0.5
Matrix is now upper triangular:
U = 
| 2  1   3  |
| 0  0 -0.5 |
| 0  0   0  |

Step 4: Determinant = product of pivots * swap sign
det(A) = (-1)^1 * 2 * 0 * -0.5 = 0 

"""

"""
Why Adding a Linear Combination of One Row to Another Row
Does Not Change the Determinant?


Step 1: Definition

Let A be an n x n matrix.
Suppose we form matrix B by:
Row_i(B) = Row_i(A) + k * Row_j(A), i ≠ j
All other rows are unchanged.

We want to prove det(B) = det(A).

---

Step 2: Determinant is Linear in Each Row

* Determinant is a multilinear function of rows.
* If we fix all rows except row_i:
  det(row_1, ..., row_i + k*row_j, ..., row_n) = 
  det(row_1, ..., row_i, ..., row_n)

  * k * det(row_1, ..., row_j, ..., row_n with row_i replaced by row_j)

---

Step 3: Determinant is Zero if Two Rows Are Equal

* If two rows are identical, determinant = 0.
* In our formula, the second term becomes:
  det(row_1, ..., row_j, ..., row_n with row_i replaced by row_j) = 0
  because row_i and row_j are now identical.

---

Step 4: Combine Results

* So det(B) = det(row_1, ..., row_i, ..., row_n) + 0
* det(B) = det(A) 

---

Step 5: Example (3x3)

A = | 1  2  3 |
| 4  5  6 |
| 7  8  9 |

Add 2 * Row1 to Row2 → new Row2 = [6 9 12]

B = | 1  2   3 |
| 6  9  12 |
| 7  8   9 |

Check determinant:

det(B) = det(A) = 0 

---

Step 6: Conclusion

* Adding multiples of one row to another
preserves determinant.
* This is because determinant is linear in rows
and vanishes when two rows are equal.
* This property is fundamental in Gaussian elimination,
allowing elimination without changing determinant.

"""

"""
Multilinearity of Determinant Explained

Step 1: Multilinearity Definition

* Determinant is linear in each row separately.
* If we change one row as a sum of two vectors:
  Row_i → Row_i + k * Row_j
* Determinant splits into sum of two determinants:

det(row_1, ..., row_i + k*row_j, ..., row_n)
= 
    det(row_1, ..., row_i, ..., row_n)
+
k * det(row_1, ..., row_j, ..., row_n with row_i replaced by row_j)

First term: original row_i
Second term: linear part k*row_j
---

Step 2: Why the second term is zero

* In the second determinant, 
row_i and row_j are identical.
* Determinant = 0 if two rows are equal.
* So only the first term remains:
  det(row_1, ..., row_i + k*row_j, ..., row_n) =
  det(row_1, ..., row_i, ..., row_n)

This shows determinant does not change.

---

Step 3: Concrete 3x3 Example

A = | 1  2  3 |
    | 4  5  6 |
    | 7  8  9 |

* Let’s add 2*Row1 to Row2 → new Row2 = [6 9 12]

B = | 1  2   3  |
    | 6  9  12  |
    | 7  8   9  |

* Apply multilinearity:

det(B) = det(Row1, Row2 + 2*Row1, Row3)
= det(Row1, Row2, Row3) + 2 * det(Row1, Row1, Row3)

* Second term = 0 because Row1 is repeated

det(B) = det(Row1, Row2, Row3)

---
Step 4: Explanation

* The determinant “splits” across sums in one row.
* Any term with two identical rows = 0.
* So adding multiples of one row to another 
does not change the determinant.



A visual diagram showing why 
adding a multiple of one row to 
another does not change the determinant.

---
Visual Diagram: Adding Multiple of One Row
Note that rows and columns are interchangeable 
in this geometric interpretation

Original Matrix A:

Row1 → [1 2 3]
Row2 → [4 5 6]
Row3 → [7 8 9]


Add 2 * Row1 to Row2 → Row2' = Row2 + 2*Row1

Row1 → [1 2 3]
Row2' → [6 9 12]
Row3 → [7 8 9]

---
Determinant Splitting (Multilinearity):

det(Row1, Row2', Row3)
= det(Row1, Row2, Row3)

* 2 * det(Row1, Row1, Row3)

---
Check second term:
det(Row1, Row1, Row3) = 0 (two identical rows)

Result:
det(Row1, Row2', Row3) = det(Row1, Row2, Row3)

Geometric Intuition:

* Row2 slides along direction of Row1
* Shape (parallelogram or parallelepiped)
volume unchanged
* Determinant = signed volume → remains same

---
Step 5: Conclusion
* Adding a multiple of one row to another
* Does not change the determinant
* Explained algebraically and geometrically

"""