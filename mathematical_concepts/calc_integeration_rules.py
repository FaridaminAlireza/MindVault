"""
INTRODUCTION TO INTEGRATION

Integration is one of the two fundamental operations
in calculus, the other being differentiation. 
While differentiation measures the 
instantaneous rate of change of a function, 
integration measures accumulation. 
You can think of integration as the process of
adding up infinitely many tiny pieces.

The most common interpretation of an integral 
is “the area under a curve.” For a function f(x),
the definite integral from a to b, written as 
∫[a to b] f(x) dx, represents the signed area 
between the curve y = f(x) and the x-axis.

The indefinite integral ∫ f(x) dx represents 
the general antiderivative of the function,
meaning all functions whose derivative is f(x).

Integration is essentially the reverse process
of differentiation. 
If F'(x) = f(x), then ∫ f(x) dx = F(x) + C,
where C is the constant of integration.

---
BASIC INTEGRATION RULES WITH EXAMPLES

1. Constant Rule
   ∫ c dx = c x + C
   Example:
   ∫ 7 dx = 7x + C

2. Power Rule
   For any real number n ≠ -1:
   ∫ x^n dx = x^(n+1) / (n+1) + C
   Example:
   ∫ x^3 dx = x^4 / 4 + C

3. Integral of 1/x
   ∫ (1/x) dx = ln|x| + C

4. Sum Rule
   The integral of a sum is the sum of integrals.
   ∫ (f(x) + g(x)) dx = ∫ f(x) dx + ∫ g(x) dx
   Example:
   ∫ (x^2 + 3x) dx = ∫ x^2 dx + ∫ 3x dx = (x^3 / 3) + (3x^2 / 2) + C

5. Difference Rule
   ∫ (f(x) - g(x)) dx = ∫ f(x) dx - ∫ g(x) dx
   Example:
   ∫ (5x^4 - x) dx = x^5 - x^2/2 + C

6. Constant Multiple Rule
   ∫ k f(x) dx = k ∫ f(x) dx
   Example:
   ∫ 4x^3 dx = 4 ∫ x^3 dx = x^4 + C

7.  There is NO general rule for the integral
    of a product, meaning:
    ∫ f(x) g(x) dx ≠ ∫ f(x) dx * ∫ g(x) dx
    This is incorrect in general.

    The term “product of integrals” refers 
    to something else: if you have two 
    separate integrals over the same variable
    or different variables, you can multiply the results 
    after integrating them individually.

    For example: (∫ f(x) dx) * (∫ g(x) dx)
    is valid only when you compute 
    the integrals separately and then
    multiply the results afterward. 
    But there is no simple rule for ∫ f(x)g(x) dx.

    Example of valid product of 
    two separate integrals:
    Let ∫ x dx = x^2/2 + C1
    Let ∫ (x^2) dx = x^3/3 + C2
    Then the product of these integrals is:
    (x^2/2 + C1)(x^3/3 + C2)
    This is fine because the integrals were
    evaluated independently.

8. Integration by Substitution 
   (reverse chain rule)
   Used when the integrand contains
   a function and its derivative.
   If u = g(x), then:
   ∫ f(g(x)) g'(x) dx = ∫ f(u) du
   Example:
   ∫ 2x (x^2 + 1)^5 dx
   Let u = x^2 + 1, so du = 2x dx.
   Result = ∫ u^5 du = u^6 / 6 + C = (x^2 + 1)^6 / 6 + C

9. Integration of Exponential Functions
   ∫ e^x dx = e^x + C
   ∫ a^x dx = a^x / ln(a) + C

10. Integration of Trigonometric Functions
    ∫ sin(x) dx = -cos(x) + C
    ∫ cos(x) dx = sin(x) + C
    ∫ sec^2(x) dx = tan(x) + C
    ∫ csc(x)cot(x) dx = -csc(x) + C

11. Integration of Rational Functions
    (special cases)
    Example:
    ∫ 1/(x^2 + 1) dx = arctan(x) + C

12. Definite Integral Rule 
    (Fundamental Theorem of Calculus)
    If F is an antiderivative of f:
    ∫[a to b] f(x) dx = F(b) - F(a)
    Example:
    ∫[0 to 2] x^2 dx = 
    (2^3 / 3) - (0^3 / 3) = 8/3

---
SUMMARY

Integration finds accumulated quantities like area.
The common rules include constant, power, sum, difference,
constant multiple, and substitution. There is no simple rule
for the integral of a product of functions, but you may multiply
two integrals only after evaluating them separately.
"""

"""
Fubini for separable functions

A rule about **separable functions over 
independent variables**, 
i.e. functions of the form f(x) g(y).

GENERAL RULE: PRODUCT OF SEPARATE INTEGRALS
(also called “separability of integrals” 
or “Fubini for separable functions”)

If f(x) is integrable on domain A and
g(y) is integrable on domain B, then:

( ∫_A f(x) dx ) ( ∫*B g(y) dy )
= ∫∫*{A×B} f(x) g(y) dx dy.

In words:
Multiplying two **independent** integrals in x and y 
is equivalent to taking the double integral of 
the product f(x)g(y) over the rectangular region A×B.

This rule follows from **Fubini’s Theorem**,
but it *is* a perfectly valid standalone rule you can use.

---
WHY THIS IS DIFFERENT FROM ∫ f(x)g(x) dx
Because x and y are **independent**, 
the functions are separable:

f(x) depends only on x
g(y) depends only on y

But ∫ f(x)g(x) dx mixes the variables and
has no general closed rule.
---
EXAMPLE (In Gaussian case)

Let f(x) = e^(−B x²)
Let g(y) = e^(−B y²)

Then:

(∫*{−∞}^{∞} e^(−B x²) dx)(∫*{−∞}^{∞} e^(−B y²) dy)
= ∫∫_{R²} e^(−B(x² + y²)) dx dy.

Each 1D Gaussian integral is √(π/B), so:

I₂ = (√(π/B))(√(π/B)) = π/B.

---

FORMAL STATEMENT OF THE RULE

Separable Integration Rule (2D):

If 
f : A → ℝ and g : B → ℝ 
are integrable, then

∫_A f(x) dx ∫_B g(y) dy
= ∫_A ∫_B f(x) g(y) dy dx
= ∫_B ∫_A f(x) g(y) dx dy
= ∫∫_{A×B} f(x) g(y) d(x,y).

This extends naturally to higher dimensions.
"""


"""
SEPARABLE INTEGRATION RULE (Verbose VERSION)

Let f(x) be an integrable function on a domain A
(a subset of the real line).
Let g(y) be an integrable function on a domain B.

Then the following rule always holds:

(∫ over A of f(x) dx) * (∫ over B of g(y) dy)
= ∫∫ over A × B of f(x) g(y) dx dy.

In words:
If you multiply two integrals 
over independent variables (x and y),
that is the same as taking 
a double integral of the product f(x) g(y)
over the 2-dimensional region A × B.

This is NOT a formula for ∫ f(x) g(x) dx.
This is a formula for integrals where 
one function depends only on x and
the other depends only on y.

This property follows from 
Fubini’s Theorem, 
but it is itself a valid rule.

---
EXAMPLES OF THE RULE

Example 1: Gaussian case
f(x) = e^(−B x²) on (−∞, ∞)
g(y) = e^(−B y²) on (−∞, ∞)

Then:

(∫ from −∞ to ∞ e^(−B x²) dx) * (∫ from −∞ to ∞ e^(−B y²) dy)
= ∫∫ over the whole plane of e^(−B(x² + y²)) dx dy.

This evaluates to π / B.

Example 2: Simple separable function
f(x) = x
g(y) = y²
Domains: x in [0, 1], y in [0, 2]

Then:

Left side:
(∫ from 0 to 1 x dx) * (∫ from 0 to 2 y² dy)
= (1/2) * (8/3)
= 4/3.

Right side:
∫ over x=0 to 1 ∫ over y=0 to 2 of x y² dy dx
= same result 4/3.

---
n-DIMENSIONAL GENERALIZATION

If a function is fully separable,
meaning:
F(x1, x2, …, xn) = f1(x1) f2(x2) … fn(xn)

and each fi is integrable on its domain Ai, then:

The product of all n single-variable integrals
 is equal to the n-dimensional integral:

(∫ over A1 f1(x1) dx1) *
(∫ over A2 f2(x2) dx2) *
… *
(∫ over An fn(xn) dxn)
======================

∫∫…∫ over A1 × A2 × … × An of F(x1, x2, …, xn) dx1 dx2 … dxn.

This is the fully general separable integration rule.

"""

"""
2D EXAMPLE (NUMERICAL)

Let
A1 = the interval [0, 2]
A2 = the interval [1, 3]

Let
f(x) = x + 1
g(y) = 2y.

The rule says:

# (∫ over A1 of f(x) dx) * (∫ over A2 of g(y) dy)

∫∫ over A1 × A2 of f(x) g(y) dx dy.

Compute the left side:

∫ from 0 to 2 of (x + 1) dx
= [x²/2 + x] from 0 to 2
= (4/2 + 2) − 0 = 4.

∫ from 1 to 3 of 2y dy
= [y²] from 1 to 3
= 9 − 1 = 8.

Multiply them:
Left side = 4 * 8 = 32.

Now compute the right side:

∫ from x=0 to 2 ∫ from y=1 to 3 of (x + 1)(2y) dy dx.

Inner integral:
∫ from 1 to 3 of 2y dy = 8.

So right side becomes:
∫ from 0 to 2 of (x + 1)*8 dx
= 8 ∫ from 0 to 2 of (x + 1) dx
= 8 * 4 = 32.

Matches perfectly.

Here:
A1 = [0, 2]
A2 = [1, 3]
A1 × A2 = the rectangle { (x, y) | 0 ≤ x ≤ 2, 1 ≤ y ≤ 3 }

---

3D EXAMPLE (NUMERICAL)

Let
A1 = the interval [0, 1]
A2 = the interval [−1, 2]
A3 = the interval [2, 4]

Let
f1(x) = x
f2(y) = y + 1
f3(z) = 3z.

The rule says:

(∫ over A1 f1(x) dx)

* (∫ over A2 f2(y) dy)
* (∫ over A3 f3(z) dz)
  =
  ∫∫∫ over A1 × A2 × A3 of f1(x) f2(y) f3(z) dx dy dz.

Compute the left side:

1. ∫ from 0 to 1 of x dx = 1/2
2. ∫ from −1 to 2 of (y + 1) dy
   = [y²/2 + y] from −1 to 2
   = (2 + 2) − (1/2 − 1) = 4 − (−0.5) = 4.5
3. ∫ from 2 to 4 of 3z dz
   = 3[z²/2] from 2 to 4
   = 3(16/2 − 4) = 3(8 − 4) = 12.

Multiply:
Left side = (1/2) * (4.5) * (12)
= 27.

Now compute the right side:

∫ from x=0 to 1 ∫ from y=−1 to 2 ∫ from z=2 to 4 of
 x (y+1) (3z) dz dy dx.

Inner integral:
∫ from z=2 to 4 of 3z dz = 12.

So the next level becomes:
∫ from y=−1 to 2 of (y+1)*12 dy
= 12 ∫ from y=−1 to 2 of (y+1) dy
= 12 * 4.5
= 54.

Now the outer integral:
∫ from x=0 to 1 of x * 54 dx
= 54 ∫ from 0 to 1 of x dx
= 54 * (1/2)
= 27.

Matches perfectly.

Here:
A1 = [0, 1]
A2 = [−1, 2]
A3 = [2, 4]
A1 × A2 × A3 = the rectangular box
{ (x, y, z) | 0 ≤ x ≤ 1, −1 ≤ y ≤ 2, 2 ≤ z ≤ 4 }
"""


"""
A geometric interpretation** of 2D, 3D, and even 4D integrals —
 including how you can interpret the fourth dimension
 as time (or something else).

GEOMETRIC INTERPRETATION OF SEPARABLE INTEGRALS

1. **Single integral (1D)**
   ∫ f(x) dx over an interval
   represents **area under a curve** in 2D.

Example:
If f(x) = x on [0, 2],
 then the integral is the area of a triangle.

---

2. **Double integral (2D)**
   ∬ f(x, y) dx dy over a region
   represents
   **volume under a surface** in 3D.

Imagine a surface z = f(x, y) hovering above the xy-plane.
The double integral adds up the “pillars” of area dx dy 
and height f(x, y).
So:

• base = 2D region A × B
• height = f(x, y)
• result = a **3D volume**

For your separable example f(x) g(y),
the result is the same: you get a 3D volume.

---
3. **Triple integral (3D)**
   ∭ F(x, y, z) dx dy dz over a region
   represents **4D hypervolume**.

This is harder to visualize, because humans
 cannot directly see 4D objects, but the analogy is:

• A single integral = 2D area
• A double integral = 3D volume
• A triple integral = 4D “hypervolume”

You are integrating over a 3D region 
(a “box” or any 3D shape).
For each tiny 3D cell of volume dx dy dz,
you are adding F(x,y,z) times that cell.

Mathematically this makes perfect sense 
even if visualization is impossible.

---
4. **Four-dimensional integral (4D)**
   ∭∫ G(x, y, z, t) dx dy dz dt
   represents **5D hypervolume** 
   (or a 4D accumulated quantity depending
    on context).

But… in applications, the **fourth variable t
usually has a physical meaning**, so the
interpretation changes:

### Interpretation A — Pure math

The integral is a 5-dimensional “volume”
in a mathematical sense. (We can imagine
the pattern: 1D → 2D → 3D → 4D → 5D…)

### Interpretation B — Physics / engineering

The fourth variable is often **time**,
so the integral means:

You integrate some quantity over **space AND time**.

Examples:
• heat distributed in a 3D space and measured 
  over a time interval
• amount of mass passing through a region over time
• total energy consumed over a volume during a time period

In this interpretation:

∭∫ ρ(x, y, z, t) dx dy dz dt
is “total amount of something accumulated
over all space and over time.”

This is not a 5D object in the physical sense — it’s
a **total accumulated quantity** across both space and time.
---

EXAMPLES OF PHYSICAL INTERPRETATIONS

1. **Heat in a room over time**
   ρ(x, y, z, t) = heat density
   Then
   energy = ∭∫ ρ(x, y, z, t) dV dt
   tells you total heat present over 
   the whole time window.

2. **Mass flow over time**
   ρ(x, y, z, t) = mass density
   The integral means total mass
   measured throughout the process.

3. **Probability theory**
   If (X, Y, Z, T) is a random vector, then
   ∭∫ p(x, y, z, t) dx dy dz dt = 1
   is the total probability.
   Here the “volume” is probability mass
   in 4D space.

---

SUMMARY
• A 1D integral = area
• A 2D integral = volume
• A 3D integral = 4D hypervolume
• A 4D integral = 5D hypervolume (mathematically),
  but often interpreted as integrating
  over time in physics.
• A double integral computes a 3D volume.
• A triple integral computes a 4D hypervolume.
• A 4D integral can be interpreted as 
  “space + time accumulation” in applied science.

---

"""

"""
A **word-based diagram analogy** 

1D integral (∫ f(x) dx) – area under a curve:

Imagine the x-axis as a horizontal line 
and f(x) as the height at each x.
You are summing up tiny rectangles
of width dx and height f(x).
Result = total **area** under the curve.

```
Height
  ^
f(x) |       *
     |      *
     |     *
     |    *
     +-----------------> x
```

---

2D integral (∬ f(x, y) dx dy) – volume under a surface:

Now add a second horizontal axis (y).
f(x, y) = height above each (x, y) point.
You are summing tiny **pillars** of 
base dx*dy and height f(x, y).
Result = total **volume** under the surface.

```
       ^
   z=f(x,y)
       |   /\
       |  /  \
       | /    \
       |/______\______> x
      /
     /
    y
```

---

3D integral (∭ F(x, y, z) dx dy dz) – 4D hypervolume:

Now add a third horizontal axis (z).
F(x, y, z) = “height” in a 4th dimension.
You are summing tiny **3D boxes** dx*dy*dz,
each weighted by F(x, y, z).
Result = 4D hypervolume (hard to visualize,
but same principle).

```
Imagine stacking 3D volumes along 
a 4th invisible axis. Each box 
contributes to the total sum.
```

---

4D integral (∭∫ G(x, y, z, t) dx dy dz dt) 
– accumulation over space and time:

Time t is often the 4th axis.
At each moment t, you have a 3D “slice” 
(volume) of G(x, y, z, t).
Integrating over t sums all these slices 
→ total quantity across **space + time**.

```
Time
  ^
 t |
   |  slice at t1
   |  slice at t2
   |  slice at t3
   +-----------------> x, y, z axes
```

---

**Key intuition:**

* Each integral adds a “dimension” of accumulation.
* 1D → 2D = area → volume
* 2D → 3D = volume → 4D hypervolume
* 3D → 4D = 3D volume accumulated over time
 → total quantity
* You don’t have to see the 4th dimension; 
 just imagine summing slices along a new axis.

"""


"""
A **concrete 4D numerical example** 
using a simple function and time slices

---
**Setup (4D integral over space + time)**

Let:

* x ∈ [0, 1],
  y ∈ [0, 2],
  z ∈ [0, 3] (space)
* t ∈ [0, 2] (time)

Define a separable function:
G(x, y, z, t) = 
 f1(x) * f2(y) * f3(z) * f4(t), with

* f1(x) = x + 1
* f2(y) = y
* f3(z) = 2z
* f4(t) = t + 1

So the 4D integral is:

I4 = ∭∫ G(x, y, z, t) dx dy dz dt
= (∫₀¹ f1(x) dx) * 
  (∫₀² f2(y) dy) * 
  (∫₀³ f3(z) dz) * 
  (∫₀² f4(t) dt)

---
**Step 1 — compute each 1D integral**

1. ∫₀¹ f1(x) dx = ∫₀¹ (x+1) dx =
 [x²/2 + x]₀¹ = 1/2 + 1 = 3/2 = 1.5

2. ∫₀² f2(y) dy = ∫₀² y dy =
 [y²/2]₀² = 4/2 = 2

3. ∫₀³ f3(z) dz = ∫₀³ 2z dz =
 [z²]₀³ = 9 − 0 = 9

4. ∫₀² f4(t) dt = ∫₀² (t+1) dt =
 [t²/2 + t]₀² = 2 + 2 = 4

---
**Step 2 — multiply the results**

I4 = 1.5 * 2 * 9 * 4
= 1.5 * 2 = 3
3 * 9 = 27
27 * 4 = 108

---

**Interpretation**

* Each time slice t ∈ [0,2] 
represents a 3D “volume”:
∭ f1(x) f2(y) f3(z) dx dy dz =
 1.5 * 2 * 9 = 27
* Multiplying by ∫ f4(t) dt = 4 
sums all slices over time.
* So the total 4D integral I4 = 108 
represents the **accumulated quantity
over space and time**.

---

**Key takeaway**

* You can **always separate integrals**
 for independent variables (here x, y, z, t)
 using the rule:

(∫ f1(x) dx)(∫ f2(y) dy)(∫ f3(z) dz)(∫ f4(t) dt) =
 ∭∫ f1(x) f2(y) f3(z) f4(t) dx dy dz dt

* Geometrically: imagine 3D volume slices at each time,
 then sum over time → total accumulated quantity.

"""

"""
Let’s picture the **4D integral 
as stacked 3D volumes over time**:

---
**Visual analogy: 4D integral = accumulation over time**

1. **Start with a 3D volume at a fixed time t**

* Imagine a 3D rectangular box 
where x ∈ [0,1], 
      y ∈ [0,2],
      z ∈ [0,3]
* The function f1(x) f2(y) f3(z) gives a
 “height” at each point in this box

* Integrating over x, y, z gives the
  **volume of this box at time t**
  In our example, that volume = 27.

```
      z
      ^
      |       /\
      |      /  \
      |     /    \   <- 3D volume at time t
      |    /______\
      +----------------> x, y plane
```

2. **Now imagine multiple time slices**

* t ∈ [0,2], so you have many of these
3D volumes stacked along the t-axis
* Each slice has its own scaling factor
 f4(t) = t + 1
* The 4D integral sums up the “volumes”
 of all these slices along t

```
Time t
  ^
  |   slice at t=0  (volume = 27*1)
  |   slice at t=1  (volume = 27*2)
  |   slice at t=2  (volume = 27*3)
  +-----------------> x, y, z axes
```

3. **Integration over t**

* By integrating f4(t) from 0 to 2,
 you sum all these slices:
 ∫₀² f4(t) dt = 4
* Multiply by the 3D volume of the
 spatial part = 27 * 4 = 108

---

**Intuition**

* Each 3D “slice” at a specific time is
 like a snapshot of the system
* The 4D integral adds all snapshots together
 → total accumulated quantity
* Geometrically, it’s like stacking 3D volumes
 along a new axis and measuring the “hypervolume”
 of all stacks combined

"""

"""
A subtle but important distinction.

---
**1. Triple integral (∭ F(x, y, z) dx dy dz)
does NOT always mean “4D hypervolume” 
in a physical sense.**

* Mathematically, you can think of ∭ F(x, y, z) dx dy dz as
summing over a 3D domain, giving a “hypervolume” in 4D 
if F(x, y, z) is just a scalar field.
* But in applied problems, the value of F(x, y, z) 
often already represents a **physical quantity**, 
like density, mass per unit volume, or energy density.
* So the triple integral ∭ ρ(x, y, z) dx dy dz is
the **total mass** in the 3D volume — we don’t call it
“4D hypervolume”; it’s just a total scalar quantity in 3D space.

---
**2. Why we need a 4D integral when adding time**

* Suppose ρ(x, y, z, t) is **density as a function 
of space and time**.

* A triple integral ∭ ρ(x, y, z, t0) dx dy dz gives
 the total mass **at a fixed time t0**.

* If we want **total mass accumulated over a
 time interval** [t1, t2], we must sum (integrate)
 over time as well:

∭∫ ρ(x, y, z, t) dx dy dz dt

* Here dt adds a **new dimension of accumulation**,
 so we need a 4D integral.
* If we only used a triple integral over x, y, z,
 we could only capture a **single snapshot in time**.

---

**3. Can we “simulate” time with a triple integral?**

* Not really. A triple integral can only sum over 
3 independent variables.
* Time is an **independent variable**, so to integrate
 over it we need an extra integral.
* The triple integral gives you the spatial total at
 **one moment**, not the total over a duration.

---
**4. Summary / Intuition**

* Triple integral: sums over space → 
total quantity **at one instant**.
* 4D integral: sums over space + time →
 total quantity **over a time interval**.
* Calling a triple integral a “4D hypervolume”
 is purely mathematical, not necessary for physics.
* In applied contexts, the fourth integral is needed
 **only to account for time** 
 (or another independent variable).

"""