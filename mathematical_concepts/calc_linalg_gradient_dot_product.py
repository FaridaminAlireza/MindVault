"""
**Gradient Dot Product**

---
1. **Definition**

The **gradient** of a scalar function f(x, y, z, ...)
is the vector of its partial derivatives:

∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z, ...)

The **dot product** of the gradient ∇f with another vector **v** 
gives the **directional derivative** of f along the direction of v:

D_v f = ∇f · v

* ∇f · v = (∂f/∂x) v_x + (∂f/∂y) v_y + (∂f/∂z) v_z + ...
* This measures the rate of change of f in the direction of vector v.
* If v is a unit vector, it gives the rate of change per unit distance along v.

---

2. **Example 1 (2D function)**

Let f(x, y) = x^2 + y^2, and let v = (1, 2)

Step 1: Compute the gradient

∇f = (∂f/∂x, ∂f/∂y) = (2x, 2y)

Step 2: Compute the dot product with v

∇f · v = (2x, 2y) · (1, 2) = (2x)(1) + (2y)(2) = 2x + 4y

Step 3: Example at point (x, y) = (1, 3)

∇f · v = 2(1) + 4(3) = 2 + 12 = 14

So the rate of change of f in the direction of v at (1, 3) is 14.

---

3. **Example 2 (3D function)**

Let f(x, y, z) = xyz, and v = (1, -1, 2)

Step 1: Compute the gradient

∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z) = (yz, xz, xy)

Step 2: Dot product with v

∇f · v = (yz, xz, xy) · (1, -1, 2) = 
yz*1 + xz*(-1) + xy*2 = yz - xz + 2xy

Step 3: Example at point (x, y, z) = (1, 2, 3)

∇f · v = (2*3) - (1*3) + 2*(1*2) = 6 - 3 + 4 = 7

So the rate of change of f along v at (1, 2, 3) is 7.

---

4. **Key Points**

* The gradient points in the **direction of maximum increase** of the function.
* The dot product with a vector v measures how much the function increases in 
that specific direction.
* If ∇f · v = 0, the function does **not change** in the direction of v 
(v is tangent to a level surface).


"""