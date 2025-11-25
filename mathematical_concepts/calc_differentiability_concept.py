"""
Function Linearity 

A function or map L from a vector space to another vector space
is called linear if it satisfies two properties 
for all vectors u, v and all scalars c:

Additivity (or superposition):
L(u + v) = L(u) + L(v)

Homogeneity (or scalar multiplication):
L(c * u) = c * L(u)

In one dimension, any linear map L(h) can be written as:
L(h) = c * h, where c is a constant.

In multiple dimensions, a linear map can be represented
as a matrix acting on a vector:
L(h) = A * h, where A is a matrix.
"""


"""
Differentiability

The expression
f(x+h) = f(x) + L(h) + r(h)
is one of the *cleanest and most powerful* ways to define 
**differentiability** in higher dimensions (and it also 
works in one dimension). Here's the idea step-by-step.

---
# The Concept

A function f is **differentiable at (x) 
if, when you zoom in very closely around (x),
the function begins to look like a **linear map**.

To formalize that, we write:

f(x+h) = f(x) + L(h) + r(h)

where:

### 1. **(L(h))** is a linear function of (h)

This is the **best linear approximation** of (f) near (x).
In multiple dimensions, (L(h)) is:

L(h) = Df(x)  h
i.e., matrix multiplication by the Jacobian.

In 1D, this is simply:

L(h) = f'(x) h

---

### 2. **(r(h))** is the *error term*

For differentiability, this error must become
*negligible* compared to (h) as (h -> 0).

Formally, the condition is:

lim_{h->0} r(h)/h = 0

This means:

> The error is much smaller than (|h|);
> the linear part dominates for very small steps.

This is written as:

r(h) = o(|h|)

---

# Why this matters

This definition captures the idea that:

> **Differentiable functions are locally linear.**

It also ensures:

* The derivative is unique.
* Continuity of the derivative implies nice behaviors.
* Works naturally in (R^n -> R^m).
* Avoids limits that are direction-dependent.

---

# In One Dimension (Simple Case)
For ( f: R -> R ):


f(x+h) = f(x) + f'(x)h + r(h),
lim_{h->0} r(h)/h = 0

This is just the familiar fact that the
tangent line approximates the function.
---

# In Higher Dimensions

For ( f:R^n -> R^m):

L(h) = Df(x)  h

is a linear map represented by the Jacobian matrix at (x).

Differentiability means the nonlinear part is negligible.

---

# Intuition Summary

Imagine taking a small step (h) from point (x).

* The *main* change in (f) comes from the linear part (L(h)).
* The remainder (r(h)) becomes insignificant relative to (|h|).

Thus:
**Differentiability = linear approximation + vanishing error**
"""


"""
Differentiability via the formula f(x+h) = f(x) + L(h) + r(h)

1. The concept
   A function f is differentiable at a point x 
-   if, when you zoom in close enough around x, 
   the function behaves like a linear map. Formally,
   f is differentiable at x if there exists a linear
   map L such that:
   
   f(x+h) = f(x) + L(h) + r(h),
   with r(h) satisfying
   r(h) / ||h|| -> 0 as h -> 0.
   This means the error term is much smaller than h,
   so the linear part gives the best local approximation.

In one dimension, L(h) = f′(x) h.
In higher dimensions, L(h) = Df(x) h,
 where Df(x) is the Jacobian matrix.

2. One-dimensional examples

Example A: f(x) = x^2 at x = a
Compute:
f(a+h) = (a+h)^2 = a^2 + 2ah + h^2.
Compare with f(a+h) = f(a) + L(h) + r(h):
f(a) = a^2,
L(h) = 2ah,
r(h) = h^2.
Check differentiability:
r(h)/|h| = |h| -> 0.
Thus f is differentiable 
at a with derivative f′(a) = 2a.

Example B: f(x) = |x| at x = 0
Assume differentiability at 0. Then L(h) = c h for some c.
We would have:
|h| = ch + r(h).
Then r(h)/|h| = 1 - c for h>0, and r(h)/|h| = 1 + c for h<0.
These both cannot go to 0 unless c = 1 and c = -1 simultaneously — impossible.
Hence |x| is not differentiable at 0.


Graph has a corner, not smooth like in x^2
Exxample A vs B:
x²: slopes from left and right 
→ same value (0) → derivative exists

|x|: slopes from left and right 
→ different values (-1 and +1) 
→ derivative does not exist

Both have a minimum, but differentiability
is about the slope approaching the same value
from all directions, not just about having a minimum.


x²: smooth “U”, tangent at 0 is horizontal,
slopes from left/right → 0

|x|: sharp “V”, no horizontal tangent line 
can touch both sides, slopes from left/right
→ -1 and +1


3. Multivariable examples

Example C: f(x,y) = x^2 + y^2 at (a,b)
Compute:
f(a+h1, b+h2) = (a+h1)^2 + (b+h2)^2
= a^2 + b^2 + 2a h1 + 2b h2 + h1^2 + h2^2.
So:
L(h) = 2a h1 + 2b h2 = gradient dot h,
r(h) = h1^2 + h2^2.
Check:
r(h)/||h|| = sqrt(h1^2 + h2^2) = ||h|| -> 0.
Thus differentiable.

Example D: f(x,y) = x y at (0,0)
f(h1, h2) = h1 h2.
Candidate linear part L(h) = 0.
r(h) = h1 h2.
Check:
|h1 h2| <= ||h||^2, hence r(h)/||h|| <= ||h|| -> 0.
So differentiable at (0,0).

4. Subtle counterexample: 
partial derivatives exist but function isn’t differentiable
   Define:
   f(x,y) = (x^2 y)/(x^4 + y^2) except f(0,0) = 0.

Partial derivatives along axes are 0.
But along the curve y = x^2:
f(x, x^2) = (x^4)/(2x^4) = 1/2.
This does not go to 0 as (x,y)->(0,0). 
Therefore f is not differentiable at (0,0).
This shows partial derivatives existing 
does not imply differentiability.

5. Uniqueness of the linear map
   If two linear maps L1 and L2 satisfy the 
   differentiability condition, subtract the
   two approximations and divide by ||h||.
   The difference tends to 0, and because a
   linear map that shrinks faster than ||h|| must 
   be identically zero, we conclude L1 = L2. 
   Thus the derivative is unique.

6. Differentiability implies continuity
   If f(x+h) = f(x) + L(h) + r(h), 
   then as h->0, both L(h)->0 and r(h)->0.
   Hence f(x+h)->f(x). So differentiability
   implies continuity.

7. How to check differentiability (practical recipe)

8. Compute candidate L (gradient or Jacobian).

9. Form r(h) = f(x+h) - f(x) - L(h).

10. Show r(h)/||h|| -> 0.
    A common method is to show r(h) = O(||h||^2).

11. Two fully worked multivariable examples

Example 1: F(x,y) = (x^2, xy) at (1,2)
Compute:
(1+h1)^2 = 1 + 2h1 + h1^2,
(1+h1)(2+h2) = 2 + 2h1 + h2 + h1 h2.
Jacobian:
[[2, 0], [2, 1]].
Linear part:
L(h) = (2h1, 2h1 + h2).
Remainder:
r(h) = (h1^2, h1 h2).
Since each term is O(||h||^2), r(h)/||h|| -> 0.
Hence differentiable.

Example 2: g(x,y) = x^3/(x^2 + y^2), g(0,0) = 0
Need only note that along y=0, g(x,0) = x, 
so the ratio g(x,0)/||(x,0)|| does not approach 0 uniformly.
Therefore g is not differentiable at (0,0).

9. Why f′(a) = 2a for f(x)=x^2 (clarification)
   Start from f(a+h) = f(a) + L(h) + r(h).
   We computed:
   f(a+h) = a^2 + 2ah + h^2.
   Thus:
   L(h) = 2ah,
   r(h) = h^2.
   Check:
   r(h)/|h| = |h| -> 0.
   So differentiability is confirmed.

Now, because in one dimension, the linear map L 
must be of the form L(h) = c h for a unique constant c,
we identify c = 2a. Therefore the derivative is f′(a) = 2a.

Connection to the classical limit:
(f(a+h) - f(a))/h = (2ah + h^2)/h = 2a + h -> 2a.
Both definitions give the same answer.

10. Summary of differentiability theory
* Differentiability means the function admits 
a linear approximation whose error is o(||h||).
* In 1D, the derivative is the coefficient multiplying h in the expansion.
* In multiple dimensions, the derivative is the Jacobian 
(or gradient for scalar outputs).
* Partial derivatives alone do not guarantee differentiability.
* Differentiability implies continuity.
* The derivative (or linear approximation L) is unique.

"""

"""
Here is the **full explanation in clean raw text format** — with no LaTeX, no symbols, no formatting other than plain text.

---
Jacobian Matrix

1. What a Jacobian is
   A Jacobian is the multivariable generalization of the derivative.
   If a function maps R^n to R^m, meaning it takes an n-dimensional input vector
   and produces an m-dimensional output vector, then the derivative is no longer
   a single number. Instead, the derivative must describe how every output component
   changes with respect to every input component.
   The Jacobian is an m-by-n matrix whose (i,j)-entry is the partial derivative of 
   output i with respect to input j.
   The Jacobian gives the best linear approximation of the function around a point:
   f(a + h) ≈ f(a) + J(a) * h
   where J(a) * h is the linear map that approximates how the output changes for 
   a small input change h.

2. 1D case
   When a function goes from R^1 to R^1, there is only one input and one output.
   The derivative f'(a) is a single number.
   The linear approximation is:
   f(a + h) ≈ f(a) + f'(a) * h
   In this case, the Jacobian is simply the 1-by-1 
   matrix [ f'(a) ], which is just the number f'(a).
   So in 1D, derivative = Jacobian.

3. Multivariable input, single output (R^n → R)
   If the function takes multiple inputs but produces
   one output, the derivative becomes a gradient vector:
   df/dx1, df/dx2, ..., df/dxn
   This gradient can also be seen as a 1-by-n Jacobian matrix.
   The linear approximation is:
   f(a + h) ≈ f(a) + gradient(a) dot h

4. Multivariable input and multivariable output (R^n → R^m)
   Here the derivative becomes a full matrix. Each output has its
   own gradient with respect to the inputs.
   Stacking these gradients produces the m-by-n Jacobian matrix.
   The linear approximation is:
   f(a + h) ≈ f(a) + J(a) * h

5. Why we need a Jacobian instead of just a derivative vector
   If the output has more than one component, a single derivative
   vector cannot describe how all outputs change.
   Example: if f maps R^2 to R^2, each output depends on two inputs.
   We need to know:
   how output 1 changes with input 1
   how output 1 changes with input 2
   how output 2 changes with input 1
   how output 2 changes with input 2
   All of these relationships form a 2-by-2 Jacobian matrix.
   This matrix is the unique linear map that
   best approximates the function near the point.

6. Practical example: 2-joint robotic arm
   A simple robot arm has two joint angles, theta1 and theta2.
   The position of the robot hand in 2D space is:
   x = cos(theta1) + cos(theta1 + theta2)
   y = sin(theta1) + sin(theta1 + theta2)
   So the function goes from R^2 to R^2:
   input = (theta1, theta2)
   output = (x, y)

Compute the partial derivatives:
partial x / partial theta1 = -sin(theta1) - sin(theta1 + theta2)
partial x / partial theta2 = -sin(theta1 + theta2)
partial y / partial theta1 =  cos(theta1) + cos(theta1 + theta2)
partial y / partial theta2 =  cos(theta1 + theta2)

So the Jacobian matrix J(theta1, theta2) is:
[ -sin(theta1) - sin(theta1 + theta2),   -sin(theta1 + theta2) ]
[  cos(theta1) + cos(theta1 + theta2),    cos(theta1 + theta2) ]

This matrix converts small joint changes (dtheta1, dtheta2)
into small hand movements (dx, dy) through the linear approximation:
[dx, dy]^T = J * [dtheta1, dtheta2]^T

Example numeric calculation:
Choose theta1 = 30 degrees and theta2 = 45 degrees.
Suppose the joint changes are dtheta1 = 0.01 and dtheta2 = -0.02 radians.
Multiply J by this vector to get approximately:
dx ≈ 0.0047
dy ≈ 0.0061
This tells us that small joint movements cause a predictable small hand movement.
This use of the Jacobian is essential in robotics, because it acts as
a conversion between joint-space motion and end-effector motion.

"""