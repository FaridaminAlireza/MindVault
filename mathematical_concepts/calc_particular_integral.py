"""
PARTICULAR INTEGRAL: INTUITIVE NUMERICAL EXAMPLE

---

1. THE EQUATION

---

Consider a simple spring-mass system under a constant force:

d^2x/dt^2 - 3 dx/dt + 2 x = 5

* x(t) = position of the mass
* LHS = natural dynamics of the system
* RHS = constant external force 5

This is a second-order linear differential equation with constant coefficients.

---

2. COMPLEMENTARY FUNCTION (FREE MOTION)

---

Solve the homogeneous equation first (ignore the RHS):

d^2x/dt^2 - 3 dx/dt + 2 x = 0

Characteristic equation:

m^2 - 3m + 2 = 0 => m = 1, 2

Complementary function:

x_c(t) = C1 e^t + C2 e^{2t}

* This represents the **natural motion** (transients) of the system.
* Alone, it does **not** satisfy the actual equation with forcing.

Test by plugging x_c into full equation (take C1=1, C2=0 for example):

x_c'' - 3 x_c' + 2 x_c = e^t - 3 e^t + 2 e^t = 0

❌ Does NOT equal 5, so we need the particular integral.

---

3. PARTICULAR INTEGRAL (FORCED RESPONSE)

---

* RHS is constant 5, so try constant guess: x_p = A
* Substitute into LHS: x_p'' - 3 x_p' + 2 x_p = 0 - 0 + 2A = 5
* Solve: 2A = 5 => A = 2.5

So particular integral:

x_p = 2.5

* Represents the **steady-state position** of the system due to the constant force.
* Does **not** add new arbitrary constants.

---

4. GENERAL SOLUTION

---

x(t) = x_c + x_p = C1 e^t + C2 e^{2t} + 2.5

* Complementary function (C1 e^t + C2 e^{2t}) → transient/free motion
* Particular integral (2.5) → steady-state/forced motion

---

5. APPLY INITIAL CONDITIONS

---

Suppose:

x(0) = 0, x'(0) = 0

x(0) = C1 + C2 + 2.5 = 0 => C1 + C2 = -2.5
x'(0) = C1 + 2C2 = 0 => C1 = -5, C2 = 2.5

Final solution:

x(t) = -5 e^t + 2.5 e^{2t} + 2.5

---

6. BEHAVIOR AS t → ∞

---

* In a **damped system**, roots would be negative (e.g., m = -1, -2),
so complementary function decays:
  x_c = C1 e^{-t} + C2 e^{-2t} → 0
* Particular integral remains constant: x_p = 2.5

Hence, as t → ∞:

x(t) → x_p = 2.5

✅ The system eventually settles at the steady-state position determined by the constant force.

---

7. INTUITION

---

* Complementary function: transient/free motion, depends on initial conditions,
dies out over time.
* Particular integral: forced/steady-state response,
independent of initial conditions.
* Ignoring x_p would give the wrong long-term solution;
only the complementary function cannot account for constant forcing.

---

8. SUMMARY

---

1. Solve homogeneous equation → get x_c (transients)
2. Guess x_p based on RHS → forced response
3. Add: x = x_c + x_p
4. Apply initial conditions for constants
5. Long-term behavior = particular integral

This shows clearly why the **particular integral is essential**
even though the number of independent constants equals the order of the equation.
"""