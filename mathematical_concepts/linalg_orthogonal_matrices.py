"""
Orthogonal Matrices — Definition, Derivation, and Properties

1. Definition

Orthogonal vectors:
Two vectors are orthogonal if their dot product is zero.
In mathematical terms, for vectors u and v,
u · v = 0 ⟺ u and v are orthogonal.

Orthonormal vectors:
Two vectors are orthonormal if they are both orthogonal and each has a magnitude (length) of 1.
That is, for vectors u and v,
u · v = 0 and ||u|| = ||v|| = 1 ⟺ u and v are orthonormal.

A square matrix Q in R^{n x n} is orthogonal if:
    Q^T Q = Q Q^T = I
Equivalently, Q^{-1} = Q^T.

2. Geometric meaning
Orthogonal matrices preserve the Euclidean inner product, lengths, and angles.
For any x, y in R^n:
    (Qx) · (Qy) = x · y
Hence norms are preserved: ||Qx|| = ||x||.

3. Deriving the orthogonality condition
Start from the requirement that a linear map Q preserves inner products:
    (Qx) · (Qy) = x · y    for all x, y in R^n.
Write using transpose:
    (Qx)^T (Qy) = x^T Q^T Q y.
This must equal x^T y for all x, y, therefore:
    Q^T Q = I.
Thus Q is orthogonal.

4. Column-orthonormality
Let Q = [q_1, q_2, ..., q_n] with columns q_i in R^n.
Then
    Q^T Q = [ q_i^T q_j ]_{i,j=1..n}.
For Q^T Q = I we require:
    q_i^T q_j = 0 if i != j, and q_i^T q_i = 1.
So columns are an orthonormal set.

5. Row-orthonormality
Because QQ^T = I also holds for orthogonal Q, the rows of Q are orthonormal as well.

6. Example — 2×2 rotation
Let
    Q = [ [cos θ, -sin θ],
          [sin θ,  cos θ] ].

Compute Q^T Q; using cos^2 θ + sin^2 θ = 1 we get I, so Q is orthogonal.
This matrix represents a rotation by angle θ (determinant +1).

7. Proof that orthogonal Q preserves lengths and inner products
For any x in R^n:
    ||Qx||^2 = (Qx)^T (Qx) = x^T Q^T Q x = x^T x = ||x||^2.
For any x, y:
    (Qx)·(Qy) = x^T Q^T Q y = x^T y.

8. Properties
- Inverse: Q^{-1} = Q^T.
- Determinant: det(Q) = ±1. 
  Matrices with det = +1 form the special orthogonal group SO(n) (rotations).
- Eigenvalues: all eigenvalues λ satisfy |λ| = 1 
  (for real orthogonal matrices, eigenvalues are ±1 
  or complex conjugate pairs on the unit circle).
- Composition: product of orthogonal matrices is orthogonal;
  the set of orthogonal matrices O(n) forms a group under multiplication.
- Orthogonal diagonalization: symmetric matrices with an orthonormal set
  of eigenvectors can be diagonalized as A = Q Λ Q^T with Q orthogonal.

9. Constructing orthogonal matrices
- Gram-Schmidt Orthogonalization

10. Remarks and summary
- Orthogonal matrices represent rigid motions that preserve 
distances and angles: rotations, reflections, and combinations.
- To verify orthogonality numerically, check that 
Q^T Q ≈ I within numerical tolerance.
- Orthogonalization algorithms (Gram–Schmidt, modified Gram–Schmidt,
QR factorization) are practical ways to derive orthogonal matrices
from arbitrary matrices.

"""


"""
Gram-Schmidt Orthogonalization

Prerequisites:
Before understanding Gram-Schmidt, you should be familiar with:
1. Vectors: Concept of a vector in R^n (e.g., [1, 2, 3]).
2. Vector operations: Vector addition, scalar multiplication.
3. Dot product: For vectors u and v in R^n: u · v = sum(u_i * v_i)
4. Norm (length) of a vector: ||v|| = sqrt(v · v)
5. Linear independence:
A set of vectors {v1, v2, ..., vn} is linearly independent 
if no vector can be written as a linear combination of the others.

---
Purpose of Gram-Schmidt

Given a set of linearly independent vectors {v1, v2, ..., vn},
Gram-Schmidt produces an orthogonal (or orthonormal) set 
{u1, u2, ..., un} that spans the same space:

* Orthogonal: u_i · u_j = 0 for i ≠ j
* Orthonormal: u_i · u_j = 0 for i ≠ j and ||u_i|| = 1

---
Gram-Schmidt Procedure

Step 1: Start with the first vector
Set u1 = v1

Step 2: Orthogonalize the next vector
For v2:
u2 = v2 - proj_u1(v2)
where proj_u1(v2) = (v2 · u1) / (u1 · u1) * u1

Step 3: Repeat for subsequent vectors
For v3:
u3 = v3 - proj_u1(v3) - proj_u2(v3)
where proj_ui(v3) = (v3 · ui) / (ui · ui) * ui

Step 4: (Optional) Normalize to get orthonormal vectors
e_i = u_i / ||u_i||

---
Example

Let's orthonormalize the following set of 2D vectors:

v1 = [1, 1]
v2 = [1, 0]

Step 1: Start with u1
u1 = v1 = [1, 1]

Step 2: Orthogonalize v2
proj_u1(v2) = (v2 · u1) / (u1 · u1) * u1

* v2 · u1 = (1*1 + 0*1) = 1
* u1 · u1 = (1*1 + 1*1) = 2
* proj_u1(v2) = (1/2) * [1, 1] = [0.5, 0.5]

u2 = v2 - proj_u1(v2) = [1, 0] - [0.5, 0.5] = [0.5, -0.5]

Step 3: Normalize to get orthonormal vectors

* e1 = u1 / ||u1|| = [1, 1] / sqrt(1^2 + 1^2) = 
[1, 1] / sqrt(2) = [0.707, 0.707]
* e2 = u2 / ||u2|| = [0.5, -0.5] / sqrt(0.5^2 + (-0.5)^2) =
 [0.5, -0.5] / sqrt(0.5) = [0.707, -0.707]

Result:

Orthogonal vectors: u1 = [1, 1], u2 = [0.5, -0.5]
Orthonormal vectors: e1 = [0.707, 0.707], e2 = [0.707, -0.707]

---

 Example in 3D

v1 = [1, 1, 0]
v2 = [1, 0, 1]
v3 = [0, 1, 1]

Step 1: u1 = v1 = [1, 1, 0]

Step 2: u2 = v2 - proj_u1(v2)

* v2 · u1 = 1*1 + 0*1 + 1*0 = 1
* u1 · u1 = 1^2 + 1^2 + 0^2 = 2
* proj_u1(v2) = (1/2) * [1, 1, 0] = [0.5, 0.5, 0]
* u2 = [1, 0, 1] - [0.5, 0.5, 0] = [0.5, -0.5, 1]

Step 3: u3 = v3 - proj_u1(v3) - proj_u2(v3)

* proj_u1(v3) = (v3 · u1) / (u1 · u1) * u1
  v3 · u1 = 0*1 + 1*1 + 1*0 = 1
  proj_u1(v3) = (1/2) * [1, 1, 0] = [0.5, 0.5, 0]

* proj_u2(v3) = (v3 · u2) / (u2 · u2) * u2
  v3 · u2 = 0*0.5 + 1*(-0.5) + 1*1 = -0.5 + 1 = 0.5
  u2 · u2 = 0.5^2 + (-0.5)^2 + 1^2 = 0.25 + 0.25 + 1 = 1.5
  proj_u2(v3) = (0.5 / 1.5) * [0.5, -0.5, 1] = 
  (1/3) * [0.5, -0.5, 1] = [0.1667, -0.1667, 0.3333]

* u3 = v3 - proj_u1(v3) - proj_u2(v3) = 
[0, 1, 1] - [0.5, 0.5, 0] - [0.1667, -0.1667, 0.3333]

* u3 = [-0.6667, 0.6667, 0.6667]

Step 4: Normalize to get orthonormal vectors e1, e2, e3.

---
In Summary
* Gram-Schmidt takes linearly independent vectors and
makes them orthogonal/orthonormal.
* It uses projection subtraction repeatedly.
* Orthonormal sets are extremely useful in QR decomposition,
eigenvector computations, and numerical linear algebra.

"""