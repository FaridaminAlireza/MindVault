"""
# 1. Quadratic Form

A quadratic form in variables x₁, x₂, ..., xₙ is:

Q(x) = Σᵢⱼ aᵢⱼ xᵢ xⱼ

This can be written in matrix form:
Q(x) = xᵀ A x

Where:

* x = [x₁, x₂, ..., xₙ]ᵀ
* A is an n×n symmetric matrix
  (Off-diagonal elements are half 
  the coefficients of cross-terms.)

---

# 2. Examples

Example 1: 2 variables

Q(x, y) = 3x² + 2xy + y²

Matrix form:

A = [[3, 1],
     [1, 1]]

Check:

xᵀ A x = 
[x y] [[3,1],[1,1]] [x y]ᵀ = 3x² + 2xy + y²

---

Example 2: 3 variables

Q(x, y, z) = x² + 2xy + 4xz + 3y² + 6yz + 5z²

Matrix form:

A = [[1, 1, 2],
     [1, 3, 3],
     [2, 3, 5]]

---

# 3. Hessian and Quadratic Forms

The Hessian of a scalar function f(x₁, ..., xₙ)
is the matrix of second derivatives:

H(f) = [[∂²f/∂xᵢ∂xⱼ]]

* For a quadratic form f(x) = xᵀ A x,
the Hessian is simply:

H(f) = 2A

* Example:

f(x, y, z) = x² + 2xy + 4xz + 3y² + 6yz + 5z²

Hessian H(f) = 2 * [[1,1,2],[1,3,3],[2,3,5]]
= [[2,2,4],
   [2,6,6],
   [4,6,10]]

---

# 4. Generalization to Higher-Order Forms

Cubic form (degree 3):

Q(x) = Σᵢⱼₖ aᵢⱼₖ xᵢ xⱼ xₖ

* Represented by a 3D tensor Aᵢⱼₖ
* Symmetric: aᵢⱼₖ = aⱼᵢₖ = ... (all permutations)
---
# Hessian Calculation Examples

Example: 3-variable function

Let:

f(x, y, z) = x² + 2xy + 4xz + 3y² + 6yz + 5z²

**Step 1: Variables**
x, y, z

**Step 2: First derivatives**

∂f/∂x = 2x + 2y + 4z
∂f/∂y = 2x + 6y + 6z
∂f/∂z = 4x + 6y + 10z

**Step 3: Second derivatives**

∂²f/∂x² = 2,  ∂²f/∂x∂y = 2,  ∂²f/∂x∂z = 4
∂²f/∂y∂x = 2,  ∂²f/∂y² = 6,  ∂²f/∂y∂z = 6
∂²f/∂z∂x = 4,  ∂²f/∂z∂y = 6,  ∂²f/∂z² = 10

**Step 4: Hessian matrix**

H(f) = [[2, 2, 4],
        [2, 6, 6],
        [4, 6, 10]]

"""