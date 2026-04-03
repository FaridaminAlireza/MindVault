"""
SLOPE FIELDS, ODEs, MULTIVARIATE FUNCTIONS

An ordinary differential equation (ODE) involves
derivatives with respect to one independent variable only.
The function can depend on that one variable.
You can have many dependent variables, 
but still only one independent variable.

The simplest ODEs are first-order ODEs, written:

dy/dx = f(x, y)

This means:
At each point (x, y), the slope of the solution
curve is given by f(x, y).

An ODE does NOT specify a 3D surface.
It specifies a field of directions in the 2D plane.

---
2. WHAT IS A SLOPE FUNCTION?

A “slope function” is simply the function 
on the right-hand side of the ODE:

slope = dy/dx = f(x, y)

It is called a slope function because:

* it tells you the slope of the solution curve at each point (x, y)
* it allows you to plot arrows showing the direction of motion

Example:
If f(x, y) = x·y², then at point (1, 2) the slope is:

slope = 1 * (2^2) = 4

meaning the solution passing through (1, 2)
is rising steeply.

---
3. HOW TO DRAW A SLOPE FIELD

To draw the slope field for the ODE:

dy/dx = f(x, y)

you do the following:

1. Pick a grid of points in the xy-plane
   Example: x = −2 to 2, y = −2 to 2

2. At each grid point (x, y), compute the slope:
   m = f(x, y)

3. The direction vector for slope m is (1, m)

4. Normalize the vector so it is short:
   V = (1, m) / sqrt(1 + m^2)

5. Draw that small arrow centered at (x, y)

Doing this for many points produces a “direction field” —
a visualization of how all solutions behave.

This requires ONLY the function f(x, y).
It does NOT use derivatives of f, Hessians, 
or second-order information.

---
4. MULTIVARIATE FUNCTION VS ODE SLOPE FUNCTION

The SAME function f(x, y) can have TWO completely
different interpretations.

 Interpretation A — multivariable function (surface):

You define:

z = f(x, y)

This describes a 3D surface.
The output z is a height.

Example:
z = x y²
is a 3D surface that curves upward as |y| increases.

 Interpretation B — ODE slope function:

You define:
dy/dx = f(x, y)

Now the SAME formula f(x,y) means something totally different:

* It is the slope of a curve
* It exists entirely in the 2D xy-plane
* No z-axis is involved

So:

z = f(x, y)       →  describes height  
dy/dx = f(x, y)   →  describes slope  

The formula is identical, but
the geometry and meaning are entirely different.

This is like the difference between:
* asking “How tall is the hill here?”
* vs “What direction should I walk here?”

---
6. EXAMPLES TO SHOW THE DIFFERENCE

 Example 1 — f(x, y) = x + y

As a surface:
z = x + y   → a tilted plane in 3D

As an ODE:
dy/dx = x + y   → slope increases as x or y increases

These two interpretations are unrelated.

 Example 2 — f(x, y) = sin(xy)

As a surface:
z varies sinusoidally based on xy

As an ODE:
dy/dx = sin(xy)
meaning the slope oscillates depending on the product xy.

 Example 3 — f(x, y) = y

As a surface:
z = y → flat vertical sheet

As an ODE:
dy/dx = y
which has exponential solutions:
y = Ce^x

---
7. SLOPE FIELD LIVES IN 2D, NOT 3D

Even though f(x, y) *could* be plotted as a 3D surface,
when used in an ODE:

dy/dx = f(x, y)

f(x, y) is NOT used as a height.
It is used as a number that controls 
the direction of a tangent vector.

A direction is an orientation in the xy-plane,
not a spatial point.

Thus:

* Slope field uses the plane (x, y)
* Surface uses space (x, y, z)
These are independent descriptions.

---

8. APPLYING ALL THIS TO f(x, y) = x y²

---

Given the formula:

```
f(x, y) = x y²
```

You can interpret it in two different ways:

A. AS A SURFACE:
z = x y²
→ parabolic sheets stretching along x

B. AS AN ODE:
dy/dx = x y²
→ slope increases with x
→ slope increases rapidly as |y| increases
→ slope is zero when x = 0 or y = 0
→ produces the slope field you saw earlier

----
The direction field:
In many differential‑equation and dynamical‑system problems,
 the direction field (or vector field) comes from an ODE of the form

dy/dx = f(x, y)

This equation gives a slope, not a full 2‑D vector.
A slope is just one number, but a vector must have two components.
So we need to *convert the slope into a vector*.
The simplest non‑zero vector with slope f(x, y) is:

(1, f(x, y))

Why? Because slope = rise/run = f(x, y)

If we choose “run” = 1, then “rise” must be f(x, y).
So the vector (1, f(x, y)) points in the correct slope direction.

Any scalar multiple like (2, 2f) or 
(0.5, 0.5f) points in the same direction.
Direction fields only care about direction,
not magnitude, so (1, f) is just the simplest choice.

The field vectors in a direction field are often normalized so 
that each vector has magnitude 1, which makes the plot readable.

1. From an ODE:
   dy/dx = f(x, y)

2. To draw a vector at point (x, y) 
that shows the slope, we choose:
   v = (dx, dy) = (1, f(x, y))
   This is because slope = rise/run = f(x, y). 
   By choosing run = 1, rise = f(x, y), 
   the vector points in the correct slope direction.

3. Magnitude of this vector:
   |v| = sqrt(1^2 + f(x, y)^2)
   Different vectors have different lengths depending on f(x, y).

4. To make the field visually uniform, we normalize the vector:
   v_hat = v / |v| = (1, f(x, y)) / sqrt(1 + f(x, y)^2)
   Now all vectors have magnitude 1 
   but still point in the same slope direction.

Key point: Normalization does not change direction, only length.
The vector (1, f(x, y)) shows the slope direction,
and normalization makes the field easier to visualize.
"""