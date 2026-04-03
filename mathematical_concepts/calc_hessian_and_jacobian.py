"""
Hessian matrix and a Jacobian matrix:

# Jacobian Matrix

* The Jacobian is the matrix of first-order partial derivatives.
* It describes how a vector-valued function changes
with respect to its inputs.

* If you have a function
  f(x) = [f₁(x), f₂(x), ..., f_m(x)]
  where x = (x₁, x₂, ..., x_n),
  then the Jacobian J is an m×n matrix:

  Jᵢⱼ = ∂fᵢ / ∂xⱼ

* The Jacobian captures rates of change (slopes)
in multiple dimensions.
* Used in: optimization, differential equations,
neural networks, transformations, change of variables.

---
# Hessian Matrix

* The Hessian is the matrix of second-order partial derivatives.
* It describes how the gradient itself changes.

* It applies to scalar-valued functions 
(functions that output one number).
  For a function
  g(x) : ℝⁿ → ℝ
  the Hessian H is an n×n matrix:

  Hᵢⱼ = ∂²g / (∂xᵢ ∂xⱼ)

* The Hessian captures curvature:

  * Positive definite → local minimum
  * Negative definite → local maximum
  * Indefinite → saddle point

* Used in: second-order optimization (Newton’s method),
 convexity analysis, machine learning, physics.


# “MIXED PARTIALS” in Hessian

A mixed partial derivative ∂²f / (∂x ∂y) means:

1. first see how f changes with y (take ∂f/∂y), 
i.e. take the slope in the y-direction;
2. then see how that slope (the function ∂f/∂y) changes
 when you vary x (take ∂/∂x of that slope).

Another viewpoint: mixed partials measure interaction or
coupling between variables.
If ∂²f/∂x∂y ≠ 0, then changing x changes how f will
respond to changes in y (and vice versa).
---

# EXAMPLE A — mixed partials = 0 (independent variables)

Let f(x,y) = g(x) + h(y). Example: f(x,y) = x^2 + 3y.

Step 1: compute first partials
∂f/∂x = 2x
∂f/∂y = 3

Step 2: compute mixed partials
∂²f/∂x∂y = ∂/∂x (∂f/∂y) = ∂/∂x (3) = 0
∂²f/∂y∂x = ∂/∂y (∂f/∂x) = ∂/∂y (2x) = 0

Interpretation:

* The slope in y (which is constant 3) does not depend on x,
so changing x does not change the y-slope.
* There is no coupling — x and y affect f independently.

---
# EXAMPLE B — mixed partials ≠ 0 (variables interact)

Let f(x,y) = x*y (simple product). 
Another, slightly richer example: f(x,y) = x^2 y + 3xy.

Step 1: compute first partials for f(x,y) = x^2 y + 3xy
∂f/∂x = 2xy + 3y = y(2x + 3)
∂f/∂y = x^2 + 3x = x(x + 3)

Step 2: compute mixed partials
∂²f/∂x∂y = ∂/∂x (∂f/∂y) = ∂/∂x [ x(x + 3) ] =
 ∂/∂x ( x^2 + 3x ) = 2x + 3
∂²f/∂y∂x = ∂/∂y (∂f/∂x) = ∂/∂y [ y(2x + 3) ] = 2x + 3

Both mixed partials are the same (2x + 3) 
— they depend on x and are not zero unless x = -3/2.

Interpretation:

* The slope in y (∂f/∂y = x^2 + 3x) depends on x.
 If you change x, the y-slope changes by 2x + 3.
* So x affects how f responds to changes in y 
— coupling between x and y.

---
# STEP-BY-STEP GEOMETRIC INTUITION (2D surface)

Imagine the surface z = f(x,y) above the (x,y) plane.

1. Fix y and move in the x-direction. You see a curve x ↦ f(x,y_fixed).
The slope of that curve is ∂f/∂x (for that fixed y).

2. Now change y a little. Does that x-slope change? 
The rate at which the x-slope changes with y is ∂²f/∂y∂x.

   * If ∂²f/∂y∂x > 0: increasing y makes the slope in x more positive 
   (surface tilts so the x-direction rises faster).
   * If ∂²f/∂y∂x < 0: increasing y makes the slope in x more negative 
   (surface tilts to reduce rise in x-direction).
---
# MIXED PARTIALS IN THE 2nd-ORDER TAYLOR EXPANSION
# (why cross-terms appear)

Tylor of expansion of two variables:
f(x,y) = sum_{n=0 to ∞} (1/n!) *
         [ (x-a)∂/∂x + (y-b)∂/∂y ]^n f(a,b)

Second-order Taylor expansion of f near (x0, y0)
(using dx = x - x0, dy = y - y0):

f(x0+dx, y0+dy) ≈ f(x0,y0)
+ f_x dx + f_y dy   (first-order terms)
+ 1/2 [ f_xx dx^2 + 2 f_xy dx dy + f_yy dy^2 ] (second-order terms)

Note the cross-term: 2 f_xy dx dy.

* That term comes directly from mixed partials.
* It contributes when both dx and dy are nonzero:
 it shows that the combined change in x and y produces
 an effect that is not explained by separate 
 x^2 and y^2 curvature alone.
* The coefficient 2 appears because when you expand the quadratic form
 (dx, dy) H (dx, dy)^T you get two identical off-diagonal contributions.

---
# SYMMETRY (Clairaut / Young)
Under mild conditions 
(continuous second partials in a neighborhood),
mixed partials are equal: ∂²f/∂x∂y = ∂²f/∂y∂x

This is useful because:

* It means the Hessian matrix is symmetric.
* The quadratic form v^T H v is well-defined and
 obeys usual rules for curvature.

If equality fails, the function's second derivatives
are not "nice" (discontinuous or singular behavior).

---
# NUMERIC ILLUSTRATION (small numbers)

Take f(x,y) = x^2 y. Evaluate near (x0,y0) = (1,2).
Let dx = 0.1, dy = -0.05.

Compute second derivatives at the point:
f_xx = ∂²/∂x² (x^2 y) = 2y    → at (1,2): 2*2 = 4
f_yy = ∂²/∂y² (x^2 y) = 0     → at (1,2): 0
f_xy = ∂²/∂x∂y (x^2 y) = 2x   → at (1,2): 2*1 = 2

Second-order Taylor correction ≈ 
1/2 [ f_xx dx^2 + 2 f_xy dx dy + f_yy dy^2 ]
= 1/2 [ 4*(0.1)^2 + 2*2*(0.1)*(-0.05) + 0*(...)]
= 1/2 [ 4*0.01 + 4*( -0.005 ) ]
= 1/2 [ 0.04 - 0.02 ]
= 1/2 * 0.02
= 0.01

Notice how the mixed term 2 f_xy dx dy = 4*( -0.005 ) = -0.02
reduces the pure dx^2 contribution 0.04. So the interaction 
of dx and dy changed the overall second-order change.

Interpretation:

* Even though dy is small and f_yy = 0, the product dx*dy and
nonzero f_xy significantly affected the second-order correction.
* This is exactly why mixed partials matter
in approximations and optimization.

---
#  SUMMARY

* Mixed partials ∂²f/∂x∂y measure how the slope in one variable
changes when you vary the other variable.
* They appear as cross-terms (dx dy) in the second-order Taylor expansion
and are essential for understanding curvature in mixed directions.
* Mixed terms capture coupling: they tell you how joint small changes
(dx and dy together) influence the function differently than separate changes.
* If second partials are continuous,
 ∂²f/∂x∂y = ∂²f/∂y∂x and the Hessian is symmetric.

"""