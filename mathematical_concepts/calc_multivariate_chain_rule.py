"""
Multivariable Chain Rule

The multivariable chain rule is a way to differentiate a function
that depends on multiple variables, each of which may also depend
on other variables.

**General Form**

Suppose we have a function:

z = f(x, y)

and x and y are themselves functions of t:

x = g(t), y = h(t)

Then, the derivative of z with respect to t is:

dz/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt)

* ∂f/∂x and ∂f/∂y are partial derivatives.
* dx/dt and dy/dt are ordinary derivatives of x and y w.r.t t.

Intuition: Change in z comes from changes in x and y through t.

---

2. **Example 1 (Single parameter t)**

Let:

z = x^2 + y^3, x = t^2, y = sin(t)

Step 1: Compute partial derivatives of z

∂z/∂x = 2x, ∂z/∂y = 3y^2

Step 2: Compute derivatives of x and y w.r.t t

dx/dt = 2t, dy/dt = cos(t)

Step 3: Apply the chain rule

dz/dt = (∂z/∂x)(dx/dt) + (∂z/∂y)(dy/dt) = (2x)(2t) + (3y^2)(cos(t))

Step 4: Substitute x = t^2 and y = sin(t)

dz/dt = 4t^3 + 3 sin^2(t) cos(t)

---

3. **Example 2 (Two variables)**

Suppose z = f(x, y) and x, y depend on two variables s and t:

z = x^2 + y^2, x = s t, y = s + t

The partial derivatives w.r.t s and t are:

∂z/∂s = (∂z/∂x)(∂x/∂s) + (∂z/∂y)(∂y/∂s)

∂z/∂t = (∂z/∂x)(∂x/∂t) + (∂z/∂y)(∂y/∂t)

Step 1: Partial derivatives of z w.r.t x and y

∂z/∂x = 2x, ∂z/∂y = 2y

Step 2: Partial derivatives of x and y

∂x/∂s = t, ∂x/∂t = s, ∂y/∂s = 1, ∂y/∂t = 1

Step 3: Apply the chain rule

∂z/∂s = (2x)(t) + (2y)(1) = 2xt + 2y

∂z/∂t = (2x)(s) + (2y)(1) = 2xs + 2y

Step 4: Substitute x = st and y = s + t

∂z/∂s = 2s t^2 + 2s + 2t

∂z/∂t = 2s^2 t + 2s + 2t

---

4. **Key Takeaways**

5. Compute partial derivatives of the outer function first.

6. Multiply by the derivative of the inner function w.r.t the variable of interest.

7. Sum contributions from all paths through which the variable affects the function.

---


"""