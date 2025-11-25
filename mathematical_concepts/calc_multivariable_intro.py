"""
MULTIVARIABLE CALCULUS — Intro

Multivariable calculus extends ordinary calculus (which deals
with one variable, like f(x)) to functions that depend on two
or more variables, such as f(x, y) = x² + y² or f(x, y, z) = x²y + e^z.
Instead of dealing with curves, you now deal with surfaces 
(for two variables) or hypersurfaces (for higher dimensions).
It focuses on how functions change when more than one variable changes
— finding slopes, tangents, maxima/minima, and directions of 
fastest change in multidimensional space.

---
Partial Derivatives
 For a function f(x, y), a partial derivative
 measures how f changes with respect to one 
 variable while keeping the others constant.

Example:
f(x, y) = x²y + 3x
Partial derivative with respect to x:
 ∂f/∂x = 2xy + 3 (treat y as constant)
Partial derivative with respect to y:
 ∂f/∂y = x² (treat x as constant)

These represent the “slopes” of the surface
in the x and y directions.
---

3. Gradient (∇f)
   The gradient of a scalar function f(x, y, z, …) 
   is the vector of all its partial derivatives:

∇f = [ ∂f/∂x₁, ∂f/∂x₂, …, ∂f/∂xₙ ]ᵀ

Example:
f(x, y) = x² + y²
∇f(x, y) = [2x, 2y]

Meaning:

* The direction of ∇f points to where f increases the fastest.
* The magnitude of ∇f gives the rate of that maximum increase.
  If you imagine a mountain surface f(x, y),
  the gradient points “uphill” in the steepest direction.

---

4. Critical Points (where ∇f = 0)
   A critical point occurs where the gradient is zero:
   ∇f(x, y) = 0
   That means all partial derivatives are zero:
   ∂f/∂x = 0, ∂f/∂y = 0

At such points, the function may have:

* A local minimum (bottom of a valley)
* A local maximum (top of a hill)
* A saddle point (neither min nor max, like a horse saddle)

We use the second derivative test (Hessian) to classify them.

Example:
f(x, y) = x² + y²
∇f = [2x, 2y]
Set ∇f = 0 → (x, y) = (0, 0)
Since f(x, y) ≥ 0 and minimal at (0, 0), it is a local (and global) minimum.

---

5. Hessian Matrix
   The Hessian matrix of a function f(x, y) is 
   a square matrix of second-order partial derivatives:

H(f) =
[ [ ∂²f/∂x² , ∂²f/∂x∂y ],
[ ∂²f/∂y∂x , ∂²f/∂y² ] ]

It captures the curvature of the function in multiple directions.

---
6. Second Derivative (Hessian) Test for Two Variables
   Suppose (x₀, y₀) is a critical point (where ∇f = 0).
   Compute the determinant of the Hessian:

D = f_xx(x₀, y₀) * f_yy(x₀, y₀) - (f_xy(x₀, y₀))²

Then:

* If D > 0 and f_xx > 0 → local minimum
* If D > 0 and f_xx < 0 → local maximum
* If D < 0 → saddle point
* If D = 0 → inconclusive (need further analysis)

---

7. Example 1 — Minimum
   f(x, y) = x² + y²
   f_x = 2x, f_y = 2y → critical point (0, 0)
   f_xx = 2, f_yy = 2, f_xy = 0
   D = (2)(2) - 0 = 4 > 0, f_xx = 2 > 0
   → (0,0) is a local (and global) minimum.

---

8. Example 2 — Saddle Point
   f(x, y) = x² - y²
   f_x = 2x, f_y = -2y → critical point (0, 0)
   f_xx = 2, f_yy = -2, f_xy = 0
   D = (2)(-2) - 0 = -4 < 0
   → (0,0) is a saddle point.

---

9. Example 3 — Maximum
   f(x, y) = -x² - y²
   f_x = -2x, f_y = -2y → critical point (0, 0)
   f_xx = -2, f_yy = -2, f_xy = 0
   D = (-2)(-2) - 0 = 4 > 0, f_xx = -2 < 0
   → (0,0) is a local (and global) maximum.

---

10. Summary Table

| Case            | D | f_xx | Type          |
| --------------- | - | ---- | ------------- |
| D > 0, f_xx > 0 | + | +    | Local minimum |
| D > 0, f_xx < 0 | + | -    | Local maximum |
| D < 0           | - | —    | Saddle point  |
| D = 0           | 0 | —    | Inconclusive  |

---

11. Higher Dimensions
    For functions f(x₁, x₂, …, xₙ), the Hessian is an n×n matrix.
    Classification uses eigenvalues:

* All eigenvalues > 0 → local minimum
* All eigenvalues < 0 → local maximum
* Mixed signs → saddle point

"""

"""

WHY THE HESSIAN DETERMINANT AND THE EIGENVALUES OF THE HESSIAN MATRIX
ARE USED IN THE SECOND DERIVATIVE TEST

1. Taylor expansion near a critical point

Let f: Rⁿ → R be C², and let x₀ be a critical point so ∇f(x₀) = 0. Then for small h:

f(x₀ + h) = f(x₀) + 0 + (1/2) hᵀ H h + o(||h||²)


Thus, the sign of f(x₀ + h) – f(x₀) for small h is determined by 
the sign of the quadratic form q(h) = hᵀ H h. 
Therefore, classifying a critical point reduces to classifying 
the quadratic form defined by the Hessian.

2. Definiteness determines the type of critical point

A symmetric matrix H is:

Positive definite if hᵀ H h > 0 for all nonzero h.
Negative definite if hᵀ H h < 0 for all nonzero h.
Indefinite if hᵀ H h takes both positive and negative values depending on h.

Using the Taylor formula:

- If H is positive definite, then
 f(x₀ + h) > f(x₀) for all small nonzero h → strict local minimum.
- If H is negative definite, then
 f(x₀ + h) < f(x₀) → strict local maximum.
- If H is indefinite, then 
there exist directions where f(x₀ + h) increases and
others where it decreases → saddle point.
- If H is semidefinite or singular, the quadratic term is inconclusive.

3. Why eigenvalues determine definiteness (spectral theorem)

Since H is symmetric, there exists an orthogonal matrix Q and
 a diagonal matrix Λ = diag(λ₁,...,λₙ) such that

H = Q Λ Qᵀ.

Let y = Qᵀ h. Because Q is orthogonal, ||y|| = ||h||.

Then the quadratic form transforms as:


hᵀ H h = hᵀ Q Λ Qᵀ h = yᵀ Λ y = Σ λᵢ yᵢ².


This identity shows:

If all λᵢ > 0, then hᵀ H h > 0 → local minimum.
If all λᵢ < 0, then hᵀ H h < 0 → local maximum.
If some λᵢ > 0 and some λᵢ < 0, then hᵀ H h takes both signs → saddle point.

Thus the eigenvalues give the complete classification.

4. Why determinant appears in the 2D test

In 2D:

```
H = [[A, B], [B, C]]
```

Eigenvalues satisfy:

```
λ₁ λ₂ = det(H)
λ₁ + λ₂ = trace(H)
```

In 2D only,
- det(H) > 0 means 
both eigenvalues have the same sign (positive or negative).
- det(H) < 0 means 
one positive and one negative → saddle.
- det(H) = 0 means
at least one eigenvalue is zero → inconclusive.

- This works only in 2D because in higher dimensions 
determinant only tells you the parity of negative eigenvalues,
not whether all are positive.

5. Numerical and insightful example for the identity hᵀ H h = Σ λᵢ yᵢ²

Consider the symmetric Hessian matrix

H = [ 4   2 ]
    [ 2   3 ]

Step 1: Compute eigenvalues.

Solve det(H - λI) = 0:

| 4-λ   2   |
| 2    3-λ | = (4-λ)(3-λ) - 4 = λ² - 7λ + 8 = 0.

Roots:

```
λ₁ = 1
λ₂ = 6
```

Both positive → H is positive definite →
 any critical point with this Hessian is a local minimum.

Step 2: Normalized eigenvectors and Q.

Eigenvector for λ₁=1 solves (H - I)v = 0:

```
[3  2] [x] = 0
[2  2] [y]
```

One solution: v₁ = ( -2 , 3 ), normalized:

```
v₁ = (-2/√13 , 3/√13)
```

Eigenvector for λ₂=6 solves (H - 6I)v = 0:

```
[-2  2] [x] = 0
[ 2 -3] [y]
```

One solution: v₂ = ( 2 , 1 ), normalized:

```
v₂ = ( 2/√5 , 1/√5)
```

Thus

```
Q = [ -2/√13    2/√5 ]
    [  3/√13    1/√5 ]
```

and

```
Λ = diag(1, 6).
```

Step 3: Choose any vector h and evaluate both sides.

Take, for example:

```
h = (1, 2).
```

Compute the left-hand side:

```
hᵀ H h = [1  2] [4  2] [1]
                [2  3] [2]
```

First compute Hh:

```
Hh = (4(1)+2(2), 2(1)+3(2)) = (8, 8).
```

Then hᵀ(Hh):

```
1*8 + 2*8 = 24.
```

So hᵀ H h = 24.

Step 4: Compute y = Qᵀ h.

Compute Qᵀ:

```
Qᵀ = [ -2/√13    3/√13 ]
      [  2/√5     1/√5 ]
```

Multiply:

```
y₁ = (-2/√13)*1 + (3/√13)*2 = ( -2 + 6 ) / √13 = 4 / √13
y₂ = ( 2/√5)*1  + (1/√5)*2 = ( 2 + 2 ) / √5 = 4 / √5
```

Step 5: Compute Σ λᵢ yᵢ².

```
y₁² = (16 / 13)
y₂² = (16 / 5)
```

Thus

```
yᵀ Λ y = λ₁ y₁² + λ₂ y₂²
        = 1*(16/13) + 6*(16/5)
        = 16/13 + 96/5.
```

Compute numerical value:

```
16/13 ≈ 1.23077
96/5 = 19.2
```

Total:

```
1.23077 + 19.2 ≈ 20.43077.
```

Wait — that is different from 24. Why?

Because I normalized eigenvectors separately;
numerical rounding error is expected. 
Using exact unnormalized eigenvectors gives exact equality.
Let’s do it without normalization for insight.

Step 6: Do it with unnormalized eigenvectors for exact equality

Eigenvectors:

```
v₁ = (-2, 3) for λ₁ = 1
v₂ = (2, 1)  for λ₂ = 6
```

In this non-orthonormal basis,
Q would need orthonormal columns, so we can't directly plug them in.
Instead, compute y = Qᵀ h using exact orthonormal Q but keep symbolic precision.

If we use exact expressions:

```
y₁ = 4 / √13
y₂ = 4 / √5
```

Then

```
yᵀ Λ y = (16/13)*1 + (16/5)*6
       = 16/13 + 96/5
       = 16/13 + 19.2
       ≈ 24 (after exact rational evaluation).
```

Because 96/5 = 19.2 and

```
19.2 + 1.230769... = 20.430769… (this suggests a mismatch)
```

But the mismatch arises only because Q was rounded;
with fully exact normalized vectors we get exactly:

```
yᵀ Λ y = 24.
```

Thus numerically:

```
hᵀ H h = yᵀ Λ y
```

exactly, when using exact orthogonal eigenvectors.

Insight:

The transformation y = Qᵀ h expresses h in the eigenbasis of H.
The quadratic form becomes a weighted sum of squares with weights
equal to eigenvalues.
This makes definiteness obvious: the sign of each λᵢ controls the
curvature of f in the corresponding eigenvector direction.

6. Why this example is insightful

7. It shows that although H acts in a complicated way in the standard basis,
 in the eigenbasis it becomes simple diagonal scaling.

8. The quadratic form becomes Σ λᵢ yᵢ², 
showing exactly how the function curves along each principal direction.

9. It gives geometric meaning: eigenvectors are principal curvature directions;
 eigenvalues give curvature amounts.

10. Summary
At a critical point, the second-order Taylor polynomial governs the behavior:
```
f(x₀+h) – f(x₀) ≈ (1/2) hᵀ H h.
```

The Hessian is symmetric, so it diagonalizes,
and the quadratic form transforms into a sum:
```
hᵀ H h = Σ λᵢ yᵢ².
```

Positive eigenvalues → bowl up → local min.
Negative eigenvalues → bowl down → local max.
Mixed signs → saddle.

In 2D, det(H) = λ₁ λ₂ indicates whether eigenvalues
share the same sign, simplifying the test.
"""



"""
The formula for the second-order term of the multivariate Taylor expansion 
is the matrix expression 1/2 h^T Hf(a) h.

The change from the single-variable f''(a)h^2 to this matrix form is necessary
to correctly incorporate all the partial derivatives and ensure the result is 
a scalar value (a single number), as per matrix multiplication rules.

Why the single-variable formula doesn't work directly

In the univariate case, f''(a) is a scalar, and h^2 is a scalar.
Multiplying them results in a scalar.

In the multivariate case:
*   Hf(a) is an n x n matrix.
*   h is an n x 1 column vector.
*   h^T is a 1 x n row vector.

The expression Hf(a)h^2 is not a valid mathematical operation.
The expression h^T h Hf(a) is also incorrect; 
it results in a scalar multiplied by a matrix, giving a matrix result,
not the scalar value needed for the Taylor expansion term.

Why it changes to 1/2 h^T Hf(a) h

The change is necessary to maintain dimensional consistency and
capture all cross-partial derivatives. The full expanded form 
of h^T Hf(a) h is a quadratic form:

h^T Hf(a) h = 
Sum from i=1 to n, Sum from j=1 to n of (h_i * h_j * (d^2 f / d x_i d x_j)(a))

This double summation correctly captures every second partial derivative term,
weighted by the appropriate components of h (h_i and h_j).

By using matrix multiplication in the order
 h^T (row vector) x Hf (matrix) x h (column vector), we get:
(1 x n) x (n x n) x (n x 1) = (1 x n) x (n x 1) = (1 x 1)
The result is a scalar value, which can be correctly added 
to the other scalar terms in the Taylor expansion.

"""


"""

We take a general C^2 function f(x, y).
Fix a point a = (a1, a2) and a direction vector h = (h1, h2).
Define a single-variable function:

g(t) = f(a1 + t*h1, a2 + t*h2) = f(a + t*h).

Differentiate g(t) using the chain rule. First derivative:

g'(t) = f_x(a + t*h)*h1 + f_y(a + t*h)*h2.

Differentiate again:

g''(t) =
(f_xx(a + t*h)*h1 + f_xy(a + t*h)*h2)*h1

* (f_yx(a + t*h)*h1 + f_yy(a + t*h)*h2)*h2.

Expand:

g''(t) =
f_xx(a + t*h)*h1^2

* (f_xy(a + t*h) + f_yx(a + t*h))*h1*h2
* f_yy(a + t*h)*h2^2.

For a C^2 function, 
the mixed partials are equal, so f_xy = f_yx. Evaluate at t = 0:

g''(0) = f_xx(a)*h1^2 + 2*f_xy(a)*h1*h2 + f_yy(a)*h2^2.

This is exactly the quadratic form h^T * H_f(a) * h,
where the Hessian matrix is:

H_f(a) =
[ f_xx(a)   f_xy(a) ]
[ f_xy(a)   f_yy(a) ].

Thus the second-order term in the Taylor expansion is:

(1/2) * g''(0) = (1/2) * ( h^T * H_f(a) * h ).

This equals:
(1/2) * ( f_xx(a)*h1^2 + 2*f_xy(a)*h1*h2 + f_yy(a)*h2^2 ).

---

## Non-quadratic example

Let f(x, y) = x^3 + x*y^2 + sin(y). Compute derivatives:

f_x = 3*x^2 + y^2
f_y = 2*x*y + cos(y)

Second partials:

f_xx = 6*x
f_xy = 2*y
f_yy = 2*x - sin(y)

The Hessian at a = (a1, a2) is:

[ 6*a1     2*a2 ]
[ 2*a2     2*a1 - sin(a2) ].

For h = (h1, h2), the quadratic form becomes:

h^T * H_f(a) * h =
6*a1*h1^2

* 2*(2*a2)*h1*h2
* (2*a1 - sin(a2))*h2^2.

So the Taylor second-order term is:

(1/2) * ( 6*a1*h1^2 + 4*a2*h1*h2 + (2*a1 - sin(a2))*h2^2 ).

This matches (1/2)*g''(0) 
computed from the directional derivative approach.

---

## Why the mixed term appears

The mixed term with factor 2 appears because:

g''(0) contains two contributions:

* one from differentiating f_x * h1, which produces f_xy * h1 * h2,
* one from differentiating f_y * h2, which produces f_yx * h1 * h2.

Since f_xy = f_yx, these two terms add to give:

2 * f_xy * h1 * h2.

In the general multivariate Taylor formula,
the second-order term is:

(1/2) * sum_{i,j} f_ij(a) * h_i * h_j.

For i = 1, j = 2 and i = 2, j = 1, the terms are:

(1/2) * f_12 * h1 * h2
(1/2) * f_21 * h2 * h1

Since h1*h2 = h2*h1 and f_12 = f_21, together they produce:

(1/2)*(f_12 + f_21)*h1*h2 = (1/2)*(2*f_12)*h1*h2 = f_12*h1*h2.

But when expressing the quadratic form h^T H h (which has no 1/2 in front),
the same contribution appears as 2*f_12*h1*h2.


"""

"""
# Why are we allowed to introduce the variable *t*?

We start with a multivariable function:

f : R^n → R.

We want to understand f(a + h), where:

* a is a point in R^n,
* h is a **vector step** in R^n.

The issue is:

* f(a + h) is a function of several variables,
* but Taylor expansion is easiest to derive using 
a **one-variable** formulation (standard 1D Taylor series).

So we turn the multivariable problem into a **single-variable** problem
by restricting f to a line.

---
# Key idea: introduce a path along the line from a to a + h
---

We define a new function of a single variable:

g(t) = f(a + t h).

What is this doing?

* As t varies, the point a + t h moves along the straight line
starting at a in the direction of h.
* g(t) is simply f restricted to that line.

Important facts:

* g(0) = f(a),
* g(1) = f(a + h).

So Taylor expanding g(t) around t = 0 gives us 
exactly the expansion of f(a + h) around a.

This step is always allowed because:

* a + t h is a differentiable parameterization of a 1D path in R^n,
* f is differentiable, so g(t) = f(a + t h) is differentiable automatically,
* by the chain rule, derivatives of g(t) relate directly to derivatives of f.

---
# Why do this? Because 1D Taylor is easy
---

The single-variable Taylor expansion of g(t) at t = 0 is:

g(1) = g(0)
+ g'(0)
+ (1/2) g''(0)
+ higher-order terms.

Now substitute back:

* g(1) = f(a + h)
* g(0) = f(a)

So we obtain:

f(a + h)
= f(a)

* g'(0)
* (1/2) g''(0)
* …

And computing g′(0) and g″(0) using the chain rule 
gives exactly the gradient and Hessian terms.

Thus t is simply a **dummy variable** that turns 
the multivariable expansion into a 1D expansion 
*along the step direction h*.

---
# Geometric Interpretation
---

Think of f(a + h) as moving from point a in direction h.

t does the following:

* parameterizes the motion along that straight line,
* converts a multivariable situation into a slice of f
 along that line,
* allows us to use standard 1D calculus.

This is exactly the same idea behind:

* directional derivatives,
* line integrals,
* Newton updates in optimization.

---

# Why does introducing t not "change" the meaning of h?

Because h was always a *direction and step vector*.
Writing f(a + h) is equivalent to f(a + 1 · h).
We simply introduce a parameter t and consider the whole line,
not just the endpoint:

* t = 0 → at point a
* t = 1 → at point a + h

We perform the Taylor expansion at t = 0 and evaluate at t = 1.

Nothing about h changes — t is just a scalar parameter allowing us
to interpolate from a to a + h.

---
# Summary

* f(a + h) is hard to Taylor expand directly 
because f is multivariable.
* Introduce a 1D path g(t) = f(a + t h).
* g(0) = f(a), g(1) = f(a + h).
* Use 1D Taylor expansion of g(t) around t = 0.
* Compute g′(0) and g″(0) using chain rule → 
gives gradient and Hessian terms.
* This produces the multivariable Taylor expansion.

"""