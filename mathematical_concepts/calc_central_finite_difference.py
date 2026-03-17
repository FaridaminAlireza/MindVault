"""
Finite Differences, Central Differences, and Order of Accuracy

---
SECTION 1: What is Δ² f_i ?

Definition:

Delta squared f_i is defined as

Δ² f_i = f(x_i + h) - 2 f(x_i) + f(x_i - h)

This quantity is called the *second central finite difference* 
of the function f at the point x_i.

Meaning:

* It is a discrete approximation of the second derivative f''(x_i)
* It measures curvature (how much the function bends)
* It uses three points: left, center, and right

If the function is linear, Δ² f_i = 0
If the function is convex (curving upward), Δ² f_i > 0
If the function is concave (curving downward), Δ² f_i < 0

---

SECTION 2: Derivation of Δ² f_i Using Taylor Expansion

Step 1: Taylor expansion of f(x_i + h)

f(x_i + h) =
f(x_i)

* h f'(x_i)
* (h^2 / 2) f''(x_i)
* (h^3 / 6) f'''(x_i)
* (h^4 / 24) f''''(x_i)
* higher order terms

Step 2: Taylor expansion of f(x_i - h)

f(x_i - h) =
f(x_i)

* h f'(x_i)

- (h^2 / 2) f''(x_i)

* (h^3 / 6) f'''(x_i)

- (h^4 / 24) f''''(x_i)
- higher order terms

Step 3: Add the two expansions

f(x_i + h) + f(x_i - h) =
2 f(x_i)

* h^2 f''(x_i)
* (h^4 / 12) f''''(x_i)
* higher order terms

Odd powers of h cancel because of symmetry.

Step 4: Subtract 2 f(x_i)

f(x_i + h) - 2 f(x_i) + f(x_i - h) =
h^2 f''(x_i)

* (h^4 / 12) f''''(x_i)
* higher order terms

Step 5: Divide by h^2

( f(x_i + h) - 2 f(x_i) + f(x_i - h) ) / h^2 =
f''(x_i)

* (h^2 / 12) f''''(x_i)
* O(h^4)

Conclusion:

The finite difference approximation equals
the true second derivative plus an error 
proportional to h^2.

---

SECTION 3: Why the Error is O(h^2)

Meaning of O(h^2):

O(h^2) means the error shrinks proportionally
to h squared as h goes to zero.

Why exactly h^2?

* The Taylor expansion contains powers of h
* Because the stencil is symmetric, all odd powers of h cancel
* The first non-zero error term comes from h^4
* After dividing by h^2, the leading error term is proportional to h^2

Therefore:

* No O(1) error
* No O(h) error
* Leading error term is O(h^2)

This is why the method is called second-order accurate.

---

SECTION 4: What is the Central Difference Method?

Definition:

The central difference method approximates derivatives
using points on both sides of x_i.

First derivative (central difference):

f'(x_i) approximately equals
( f(x_i + h) - f(x_i - h) ) / (2 h)

Second derivative (central difference):

f''(x_i) approximately equals
( f(x_i + h) - 2 f(x_i) + f(x_i - h) ) / h^2

Why "central"?

* x_i is the center point
* The stencil is symmetric around x_i

This symmetry causes cancellation of odd error terms and improves accuracy.

---

SECTION 5: Comparison with Forward and Backward Differences

Forward difference (first derivative):

( f(x_i + h) - f(x_i) ) / h

Taylor expansion gives:

= f'(x_i) + (h / 2) f''(x_i) + O(h^2)

Error order: O(h)

Backward difference:

( f(x_i) - f(x_i - h) ) / h

Error order: O(h)

Central difference:

( f(x_i + h) - f(x_i - h) ) / (2 h)

Taylor expansion gives:

= f'(x_i) + (h^2 / 6) f'''(x_i) + O(h^4)

Error order: O(h^2)

Summary table (textual):

Forward difference   -> first-order accurate
Backward difference  -> first-order accurate
Central difference   -> second-order accurate

---

SECTION 6: Why Δ f_i Represents the First Derivative

Definition of derivative:

f'(x) is defined as the limit as h goes to zero of

( f(x + h) - f(x) ) / h

Finite differences:

* Replace the limit with a small but finite h
* This gives an approximation instead of the exact derivative

Discrete grid:

x_i = x_0 + i h
f_i = f(x_i)

Forward difference:

Δ f_i = f_{i+1} - f_i

Central difference:

Δ f_i = f_{i+1} - f_{i-1}

Relation to derivative:

Δ f_i is proportional to h times f'(x_i)

As h goes to zero:
finite difference -> exact derivative

Thus:

Finite differences are discrete versions of derivatives.

---

SECTION 7: Relation Between First and Second Differences

First difference measures slope.
Second difference measures change in slope.

Discrete analogy:

Second difference =
difference of first differences

Δ² f_i = (f_{i+1} - f_i) - (f_i - f_{i-1})

This mirrors calculus:

Second derivative =
derivative of first derivative

---

SECTION 8: Example

Let f(x) = x^2

Compute:

f(x_i + h) = (x_i + h)^2
f(x_i - h) = (x_i - h)^2

Δ² f_i =
(x_i + h)^2 - 2 x_i^2 + (x_i - h)^2

Simplifying:

= 2 h^2

Divide by h^2:

= 2

Which is exactly f''(x) = 2

The method is exact for quadratic polynomials.

---

SECTION 9: Key Takeaways

* Δ² f_i is the second central finite difference
* It approximates the second derivative
* Central differences use symmetry
* Symmetry cancels odd error terms
* The error is O(h^2)
* Finite differences converge to derivatives as h -> 0
* This framework is fundamental in numerical analysis,
 PDEs, and physics

---
Connection to:

* Formal consistency and convergence proofs
* Discrete Laplacian in multiple dimensions
* Stability analysis
* Connection to PDE solvers
"""