"""
""
Fixed-Point Iteration Methods for Solving Equations
---
## 1. Introduction

Fixed-point iteration is a numerical method to
solve equations of the form: f(x) = 0
The main idea is to rewrite the equation as 
a fixed-point problem: x = g(x)
where a solution x* satisfies g(x*) = x*.

Geometrically, this corresponds to finding 
the **intersection of y = x and y = g(x)**. 
Each iteration moves along the stair-step path 
from the current guess to the curve y = g(x) 
and then horizontally to y = x.

---
## 2. Approaches to Derive Iterative Expressions

Several techniques can be used to 
derive fixed-point iteration formulas:

### 2.1 Direct Algebraic Rearrangement

* Isolate x in terms of other expressions in the equation.
* Example: Solve x^2 - 3 = 0

x^2 - 3 = 0 => x = sqrt(3) => 
simple iteration x_{n+1} = sqrt(3) (trivial) 
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

* Take the arithmetic mean of x_n and
the rearranged value to stabilize and
accelerate convergence.

Example:
Goal: solve x^3 = a

Step 1: Write as a root-finding problem
f(x) = x^3 - a = 0

Step 2: Compute derivative
f'(x) = 3x^2

Step 3: Apply Newton’s method
x_(n+1) = x_n - f(x_n) / f'(x_n)

Substitute f and f':
x_(n+1) = x_n - (x_n^3 - a) / (3x_n^2)

Step 4: Simplify

Split the fraction:
x_(n+1) = x_n - (x_n^3)/(3x_n^2) + a/(3x_n^2)

Simplify terms:
= x_n - x_n/3 + a/(3x_n^2)

Combine:
= (2/3)x_n + a/(3x_n^2)

Step 5: Final iteration formula

x_(n+1) = (1/3)(2x_n + a/(x_n^2))

Interpretation:

* 2x_n is the current estimate (weighted more)
* a/(x_n^2) is the correction term
* the average (with weights) gives a stable and
fast method to compute the cube root of a.
# ---
* Example: Compute sqrt(3) using Newton's-inspired iteration:

x_{n+1} = 0.5*(x_n + 3/x_n)

**Iteration:**

* x0 = 1.5
* x1 = 0.5*(1.5 + 3/1.5) = 1.75
* x2 ≈ 1.7321
* x3 ≈ 1.73205

**Geometric interpretation:** 
Iteration moves along the curve 
y = 0.5*(x + 3/x) to intersect 
with y = x, converging quickly to x*.
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

**Geometric interpretation:** 
Each Newton step approximates the intersection of
y = x and the tangent of y = x - f(x)/f'(x) near x*.

---
Function Transformation Example

* Transform the equation f(x)=0 into a bounded function for iteration.
* Example: Solve cos(x) = x
* g(x) = cos(x)
* Iteration: x_{n+1} = cos(x_n)
* Converges linearly: x0 = 0.5,
 x1 ≈ 0.8776, x2 ≈ 0.6390, ..., x* ≈ 0.739085

**Geometric interpretation:** 
The intersection of y = cos(x) and y = x gives
the fixed point. Iteration follows the stair-step along y = cos(x) 
to approach the intersection.

---
Inverse Functions / Trigonometric Transformations Example

* For equations like tan(x) = tanh(x), define g(x) using 
the inverse function of one side.
* Example: x = arctan(tanh(x))
* Iteration: x_{n+1} = arctan(tanh(x_n))
* Converges to x* ≈ 0.3910

**Geometric interpretation:** 
The curve y = arctan(tanh(x)) intersects
y = x at the solution. Each iteration moves
along y = arctan(tanh(x)) to converge.

---

## 3. Relation to y = x Intersection

* All fixed-point iterations can be visualized as
finding the intersection between the line y = x 
and the curve y = g(x).
* Iteration moves vertically from x_n to 
the curve y = g(x_n), then horizontally to y = x,
repeating this stair-step path until convergence.
* Convergence depends on the slope of g(x) at 
the intersection point: |g'(x*)| < 1 ensures the 
stair-step approaches the intersection
rather than diverging.

---
## 4. Practical Algorithm

1. Rewrite f(x) = 0 as x = g(x)
2. Choose interval [a, b]
3. Verify |g'(x)| < 1 for convergence
4. Choose initial guess x0 in [a, b]
5. Iterate until |x_{n+1} - x_n| < ε
6. Optionally visualize using the 
intersection of y = x and y = g(x)


## 5. Convergence Theorem 
(Banach Fixed-Point Theorem)

Let g(x) be defined on [a, b] and satisfy:
1. Mapping into itself: g(x) in 
[a, b] for all x in [a, b]
2. Contraction: |g'(x)| <= L < 1 
for all x in [a, b]

Then there exists a unique fixed point
x* in [a, b], 
and for any x0 in [a, b], 
the iteration x_{n+1} = g(x_n) converges to x*.

"""