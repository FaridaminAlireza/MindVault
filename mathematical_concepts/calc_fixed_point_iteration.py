"""
Fixed-Point Iteration Methods for Solving Equations

---

## 1. Introduction

Fixed-point iteration is a numerical method to solve equations of the form:

f(x) = 0

The main idea is to rewrite the equation as a fixed-point problem:

x = g(x)

where a solution x* satisfies g(x*) = x*.

---

## 2. Fixed-Point Iteration Algorithm

Given an initial guess x0, define the sequence:

x_{n+1} = g(x_n), n = 0, 1, 2, ...

If the sequence converges, x_n -> x*, and x* solves f(x) = 0.

---

## 3. Convergence Theorem (Banach Fixed-Point Theorem)

Let g(x) be defined on [a, b] and satisfy:

1. Mapping into itself: g(x) in [a, b] for all x in [a, b]
2. Contraction: |g'(x)| <= L < 1 for all x in [a, b]

Then there exists a unique fixed point x* in [a, b], 
and for any x0 in [a, b], the iteration x_{n+1} = g(x_n) converges to x*.

---

## 4. Proof of Convergence

Using the Mean Value Theorem:

|x_{n+1} - x*| = |g(x_n) - g(x*)| = |g'(\xi_n)| |x_n - x*| <= L |x_n - x*|

Iterating:

|x_n - x*| <= L^n |x_0 - x*| -> 0 as n -> infinity

---

## 5. Example 1: cos(x) = x

**Step 1: Choose g(x)**

x = cos(x) => g(x) = cos(x)

**Step 2: Check derivative**

g'(x) = -sin(x), |g'(x)| <= sin(1) ~ 0.84 < 1 on [0, 1]

**Step 3: Iteration**

x0 = 0.5

x1 = cos(0.5) = 0.8776
x2 = cos(0.8776) = 0.6390
x3 = cos(0.6390) = 0.8027
x4 = cos(0.8027) = 0.6948
x5 = cos(0.6948) = 0.7682

**Result:** x* ≈ 0.739085

---

## 6. Example 2: tan(x) = tanh(x)

**Step 1: Choose g(x)**

x = arctan(tanh(x)) => g(x) = arctan(tanh(x))

**Step 2: Check derivative**

g'(x) = sech^2(x)/(1 + tanh^2(x)) <= 1 near x* ~ 0.391

**Step 3: Iteration**

x0 = 0.5
x1 = arctan(tanh(0.5)) ≈ 0.4321
x2 = arctan(tanh(0.4321)) ≈ 0.4079
x3 = arctan(tanh(0.4079)) ≈ 0.3960
x4 = arctan(tanh(0.3960)) ≈ 0.3910

**Result:** x* ≈ 0.3910

> Only solution exists in [-π/2, π/2] due 
to periodicity of tan(x) and bounded tanh(x).

---

## 7. Example 3: sqrt(3) using Fixed-Point / Newton's Method

Equation: x^2 - 3 = 0

**Step 1: Rewrite as fixed-point**

x_{n+1} = 0.5 * (x_n + 3/x_n)

**Step 2: Initial guess**
x0 = 1.5

**Step 3: Iteration**

x1 = 0.5 * (1.5 + 3/1.5) = 1.75
x2 = 0.5 * (1.75 + 3/1.75) ≈ 1.7321
x3 = 0.5 * (1.7321 + 3/1.7321) ≈ 1.73205

**Result:** x* ≈ 1.73205

**Step 4: Convergence Check**

g'(x) = 0.5 * (1 - 3/x^2)

g'(sqrt(3)) = 0 => fast convergence

**Derivation:**

From f(x) = x^2 - 3 = 0
x_{n+1} = x_n - f(x_n)/f'(x_n) = x_n - (x_n^2 - 3)/(2 x_n) = 0.5*(x_n + 3/x_n)

> This is Newton's method disguised as fixed-point iteration.

---

## 8. General Fixed-Point Iteration for Roots

For x^m = A:

f(x) = x^m - A = 0

Newton's method / fixed-point:

x_{n+1} = x_n - (x_n^m - A)/(m x_n^{m-1}) = ((m-1)x_n + A/x_n^{m-1})/m

> This formula generalizes square roots to m-th roots.

---

## 9. Practical Algorithm

1. Rewrite f(x) = 0 as x = g(x)
2. Choose interval [a, b]
3. Verify |g'(x)| < 1
4. Choose initial guess x0 in [a, b]
5. Iterate until |x_{n+1} - x_n| < ε

---

## 10. Summary

* Fixed-point iteration transforms f(x)=0 into x=g(x)
* Convergence requires |g'(x*)| < 1
* Iteration: x_{n+1} = g(x_n)
* Convergence is linear (or faster if derivative = 0)
* Choice of g(x) is crucial
* Examples: cos(x)=x, tan(x)=tanh(x), sqrt(3), general m-th roots
* Visualization: stair-step diagrams help understand convergence

"""

"""
Fixed-Point Iteration Methods for Solving Equations
(Second explaination)
---
## 1. Introduction

Fixed-point iteration is a numerical method to solve equations of the form:

f(x) = 0

The main idea is to rewrite the equation as a fixed-point problem:

x = g(x)

where a solution x* satisfies g(x*) = x*.

Geometrically, this corresponds to finding the **intersection of y = x and
y = g(x)**. Each iteration moves along the stair-step path from the current
guess to the curve y = g(x) and then horizontally to y = x.

---
## 2. Approaches to Derive Iterative Expressions

Several techniques can be used to derive fixed-point iteration formulas:

### 2.1 Direct Algebraic Rearrangement

* Isolate x in terms of other expressions in the equation.
* Example: Solve x^2 - 3 = 0

x^2 - 3 = 0 => x = sqrt(3) => simple iteration x_{n+1} = sqrt(3) (trivial) 
or more practical x_{n+1} = 3/x_n

**Iteration (x_{n+1} = 3/x_n)**

* x0 = 1.5
* x1 = 3/1.5 = 2
* x2 = 3/2 = 1.5
* Converges slowly, shows importance of formula choice.

**Geometric interpretation:** Each iteration find
the intersection between y = x and y = 3/x.

---

### 2.2 Averaging / Babylonian Method

* Take the arithmetic mean of x_n and the rearranged value
to stabilize and accelerate convergence.
* Example: Compute sqrt(3) using Newton's-inspired iteration:

x_{n+1} = 0.5*(x_n + 3/x_n)

**Iteration:**

* x0 = 1.5
* x1 = 0.5*(1.5 + 3/1.5) = 1.75
* x2 ≈ 1.7321
* x3 ≈ 1.73205

**Geometric interpretation:** Iteration moves along the curve 
y = 0.5*(x + 3/x) to intersect with y = x, converging quickly to x*.

---

### 2.3 Newton-Raphson Method

* General method for f(x) = 0
* Iteration: x_{n+1} = x_n - f(x_n)/f'(x_n)
* Leads to a fixed-point iteration x_{n+1} = g(x_n) 
by defining g(x) = x - f(x)/f'(x)

**Example:** Solve x^2 - 3 = 0

* f(x) = x^2 - 3, f'(x) = 2x
* x_{n+1} = x_n - (x_n^2 - 3)/(2 x_n) = 0.5*(x_n + 3/x_n)
* Same as Babylonian method.

**Geometric interpretation:** Each Newton step approximates the intersection of
y = x and the tangent of y = x - f(x)/f'(x) near x*.

---

### 2.4 Function Transformation

* Transform the equation f(x)=0 into a bounded function for iteration.
* Example: Solve cos(x) = x
* g(x) = cos(x)
* Iteration: x_{n+1} = cos(x_n)
* Converges linearly: x0 = 0.5, x1 ≈ 0.8776, x2 ≈ 0.6390, ..., x* ≈ 0.739085

**Geometric interpretation:** The intersection of y = cos(x) and y = x gives
the fixed point. Iteration follows the stair-step along y = cos(x) 
to approach the intersection.

---

### 2.5 Inverse Functions / Trigonometric Transformations

* For equations like tan(x) = tanh(x), define g(x) using 
the inverse function of one side.
* Example: x = arctan(tanh(x))
* Iteration: x_{n+1} = arctan(tanh(x_n))
* Converges to x* ≈ 0.3910

**Geometric interpretation:** The curve y = arctan(tanh(x)) intersects
y = x at the solution. Each iteration moves along y = arctan(tanh(x)) to converge.

---

## 3. Relation to y = x Intersection

* All fixed-point iterations can be visualized as finding the intersection
between the line y = x and the curve y = g(x).
* Iteration moves vertically from x_n to the curve y = g(x_n), 
then horizontally to y = x, repeating this stair-step path until convergence.
* Convergence depends on the slope of g(x) at the intersection
point: |g'(x*)| < 1 ensures the stair-step approaches the intersection
rather than diverging.

---

## 4. Practical Algorithm

1. Rewrite f(x) = 0 as x = g(x)
2. Choose interval [a, b]
3. Verify |g'(x)| < 1 for convergence
4. Choose initial guess x0 in [a, b]
5. Iterate until |x_{n+1} - x_n| < ε
6. Optionally visualize using the intersection of y = x and y = g(x)

---

## 5. Summary

* Fixed-point iteration transforms f(x)=0 into x=g(x)
* Techniques to derive g(x): direct algebraic, averaging/Babylonian,
Newton-Raphson, function transformation, inverse functions
* Geometric interpretation: iteration finds intersection of y = x and y = g(x)
* Convergence requires |g'(x*)| < 1
* Examples:

  * cos(x) = x => g(x) = cos(x) => x* ≈ 0.739085
  * tan(x) = tanh(x) => g(x) = arctan(tanh(x)) => x* ≈ 0.3910
  * sqrt(3) => g(x) = 0.5*(x + 3/x) => x* ≈ 1.73205
* Stair-step diagrams illustrate convergence visually and
 confirm the geometric interpretation.

"""