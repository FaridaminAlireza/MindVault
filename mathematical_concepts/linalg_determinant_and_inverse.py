"""
# Why a Matrix with Determinant 0 Has No Inverse

1. Intuition: Determinant as Volume Scaling

A square matrix A can be thought of as a linear transformation of space:

* In 2D, it transforms a square into a parallelogram.
* In 3D, it transforms a cube into a parallelepiped.

The determinant det(A) tells us how the matrix scales volume:

* det(A) ≠ 0 → space is scaled but not collapsed → matrix is invertible.
* det(A) = 0 → space is flattened to a lower dimension → matrix is non-invertible.

Intuition: If space collapses, multiple points map to the same output.
Therefore, the transformation cannot be reversed uniquely.

---
2. Definition of Inverse
A square matrix A is invertible if there exists a matrix A⁻¹ such that:

A * A⁻¹ = A⁻¹ * A = I

(where I is the identity matrix).

If det(A) = 0, no such A⁻¹ exists because A is singular.

---
3. Example in 2D

Let A = [[2, 4], 
         [1, 2]]

* Determinant: det(A) = 2*2 - 4*1 = 0
* Formula for 2x2 inverse: A⁻¹ = (1/det(A)) * [[d, -b], 
                                               [-c, a]] 
→ division by 0, impossible.

Geometric intuition: The second row is half of the first row.
Outputs lie along a line in 2D, so there is no unique inverse.

---
4. Proof via Linear Dependence

* det(A) = 0 ⇔ rows or columns are linearly dependent
* Then the system A * x = b cannot have a unique solution
* Proof using determinant property:
  det(A * A⁻¹) = det(A) * det(A⁻¹) = det(I) = 1
  If det(A) = 0, left-hand side = 0, which is a contradiction.
   
  Hence, no inverse exists.

---
5. Determinant in 3D

a) Definition for 3x3 matrix

Let A = [v1 v2 v3] with columns v1, v2, v3.
det(A) = v1 · (v2 × v3)

* This is the signed volume of the parallelepiped formed by the three vectors.
* det(A) = 0 → vectors are coplanar → volume = 0 → no inverse.

b) Transformation viewpoint

* Apply A to a unit cube: edges e1, e2, e3 transform to A*e1, A*e2, A*e3
* Volume of transformed parallelepiped = |det(A)|
* If det(A) = 0 → cube collapses → transformation flattens space → no inverse.

# Example 3x3

A = [[1, 2, 3], [2, 4, 6], [0, 1, 1]]

* det(A) = 0
* Columns are linearly dependent → vectors lie in a plane → no inverse.

---

 6. Non-Unit Cube Case

* Determinant measures volume scaling.
* For any parallelepiped (not necessarily a unit cube):
  Volume_new = |det(A)| * Volume_original
* If det(A) = 0 → Volume_new = 0 → space collapses → no inverse

Example: same matrix A as above, original parallelepiped edges = [1,0,0], [0,2,0], [0,0,3] → transformed volume = 0 → no inverse

---

 7. Summary Table

| det(A)     | Meaning                                                                                 |
| ---------- | --------------------------------------------------------------------------------------- |
| det(A) ≠ 0 | Matrix is invertible, transformation preserves volume                                   |
| det(A) = 0 | Matrix is singular, columns/rows dependent, transformation collapses space → no inverse |

---

Key Takeaways

* Determinant measures linear independence and volume scaling.
* det(A) = 0 → space flattened, information lost → no unique inverse.
* Works for unit cubes or any shape.

"""