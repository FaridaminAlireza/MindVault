"""
Differentiability

The expression
f(x+h) = f(x) + L(h) + r(h)
is one of the *cleanest and most powerful* ways to define 
differentiability in higher dimensions (and it also 
works in one dimension). 

Derivation of f(x+h) = f(x) + L(h) + r(h)

staring from the definition of the derivative,
f'(x) = lim_(h->0) f(x+h) - f(x) / h

That means 
(f(x+h) - f(x) ) / h = f'(x) + ε(h)
where ε(h) -> 0 as h -> 0

Now mulitply both sides by h:
f(x+h) - f(x) = f'(x) h + ε(h) h
Define r(h) = ε(h) h

Then  f(x+h) = f(x) + f'(x) h + r(h)
r(h) / h = ε(h) -> 0

---
The Concept

A function f is differentiable at (x) 
if, when you zoom in very closely around (x),
the function begins to look like a linear map.

To formalize that, we write:

f(x+h) = f(x) + L(h) + r(h)

where:

1. (L(h)) is a linear function of (h)
This is the best linear approximation of (f) near (x).

In multiple dimensions, (L(h)) is:
L(h) = Df(x)  h
i.e., matrix multiplication by the Jacobian.

In 1D, this is simply:
L(h) = f'(x) h

---
2. (r(h)) is the *error term*

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
Why this matters

This definition captures the idea that:
> Differentiable functions are locally linear.
It also ensures The derivative is unique.

---
In One Dimension (Simple Case)
For ( f: R -> R ):


f(x+h) = f(x) + f'(x)h + r(h),
lim_{h->0} r(h)/h = 0

This is just the familiar fact that the
tangent line approximates the function.
---

In Higher Dimensions

For ( f:R^n -> R^m):

L(h) = Df(x)  h

is a linear map represented by the Jacobian matrix at (x).

Differentiability means the nonlinear part is negligible.

---
Intuition Summary

Imagine taking a small step (h) from point (x).

* The *main* change in (f) comes from the linear part (L(h)).
* The remainder (r(h)) becomes insignificant relative to (|h|).

Thus:
Differentiability = linear approximation + vanishing error


Differentiability Example 
via the formula f(x+h) = f(x) + L(h) + r(h)

---
One-dimensional examples

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

Connection to the classical limit:
(f(a+h) - f(a))/h = (2ah + h^2)/h = 2a + h -> 2a.

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
→ same value → derivative exists

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

---
Multivariable examples

Example A: f(x,y) = x^2 + y^2 at (a,b)
Compute:
f(a+h1, b+h2) = (a+h1)^2 + (b+h2)^2
= a^2 + b^2 + 2a h1 + 2b h2 + h1^2 + h2^2.
So:
L(h) = 2a h1 + 2b h2 = gradient dot h,
r(h) = h1^2 + h2^2.
Check:
r(h)/||h|| = sqrt(h1^2 + h2^2) = ||h|| -> 0.
Thus differentiable.

Example B: f(x,y) = x y at (0,0)
f(x+h1, y+h2) = (x+h1) (y+h2) = xy + x h2 + h1 y + h1 h2
Candidate linear part L(h) = x h2 + y h1 = 0.
r(h) = h1 h2.
Check:
|h1 h2|/||h|| = |h1 h2| / sqrt(h1^2 + h2^2)

lim (h1,h2)->(0,0) |h1 h2| / sqrt(h1^2 + h2^2):

- Use the inequality: |h1 h2| ≤ (h1^2 + h2^2) / 2
Then:
0 ≤ 
|h1 h2| / sqrt(h1^2 + h2^2) ≤ (h1^2 + h2^2) / (2 sqrt(h1^2 + h2^2))
- Simplify the right-hand side:
(h1^2 + h2^2) / (2 sqrt(h1^2 + h2^2)) = (1/2) sqrt(h1^2 + h2^2)
So: 0 ≤ |h1 h2| / sqrt(h1^2 + h2^2) ≤ (1/2) sqrt(h1^2 + h2^2)
As (h1,h2) → (0,0): sqrt(h1^2 + h2^2) → 0
- Therefore, by the squeeze theorem:
lim (h1,h2)->(0,0) |h1 h2| / sqrt(h1^2 + h2^2) = 0
So differentiable at (0,0).

Example C: F(x,y) = (x^2, xy) at (1,2)
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

---
Subtle counterexample: 
partial derivatives exist but function isn’t differentiable
Define:
f(x,y) = (x^2 y)/(x^4 + y^2) except f(0,0) = 0.

Note that the follwing quotient rules 
are only valid for (x,y) ≠ (0,0).
(
∂f/∂x = [(2x y)(x⁴ + y²) − (x² y)(4x³)] / (x⁴ + y²)²
= [2x y (y² − x⁴)] / (x⁴ + y²)²

∂f/∂y = [x²(x⁴ + y²) − (x² y)(2y)] / (x⁴ + y²)²
= [x² (x⁴ − y²)] / (x⁴ + y²)²
)

At the point (0,0), 
we must use the definition of partial derivatives,
plugging in h → 0 along the axes. When we do that,
the function along the axes is zero, 
so the derivative is zero.
-> Partial derivatives along axes are 0.

But along the curve y = x^2:
f(x, x^2) = (x^4)/(2x^4) = 1/2.

What happens as x → 0?
The point (x, x²) → (0,0)
But f(x, x²) → 1/2
-> This does not go to 0 as (x,y)->(0,0). 

Therefore f is not differentiable at (0,0).
Differentiability requires:
lim_((x,y) -> (0,0)) f(x,y) = f(0,0)
But along this path, the limit = 1/2 ≠ 0

So f is not continuous at (0,0)
Therefore f is not differentiable at (0,0)

-> This shows partial derivatives existing 
does not imply differentiability.

---
Uniqueness of the linear map
If two linear maps L1 and L2 satisfy the 
differentiability condition, subtract the
two approximations and divide by ||h||.
The difference tends to 0, and because a
linear map that shrinks faster than ||h|| must 
be identically zero, we conclude L1 = L2. 
Thus the derivative is unique.

f(x+h) = f(x) + L1(h) + r1(h)
f(x+h) = f(x) + L2(h) + r2(h)
with:
r1(h)/||h|| → 0 and r2(h)/||h|| → 0

Subtract the two expressions
(L1(h) + r1(h)) = (L2(h) + r2(h))
So: L1(h) − L2(h) = r2(h) − r1(h)

Divide by ||h||
(L1(h) − L2(h)) / ||h|| = (r2(h) − r1(h)) / ||h||
Right-hand side → 0 (difference of two things going to 0)
So: (L1(h) − L2(h)) / ||h|| → 0

Define a new linear map
Let:
L(h) = L1(h) − L2(h)
Then:
L(h)/||h|| → 0

If a linear map satisfies:
L(h)/||h|| → 0
then L must be identically zero

So the only possibility: L ≡ 0

---
Differentiability implies continuity
If f(x+h) = f(x) + L(h) + r(h), 
then as h->0, both L(h)->0 and r(h)->0.
Hence f(x+h)->f(x). So differentiability
implies continuity.

---
Summary of differentiability theory
* Differentiability means the function admits 
a linear approximation whose error is o(||h||).
* In 1D, the derivative is the coefficient
multiplying h in the expansion.
* In multiple dimensions, the derivative is the Jacobian 
(or gradient for scalar outputs).
* Partial derivatives alone do not guarantee differentiability.
* Differentiability implies continuity.
* The derivative (or linear approximation L) is unique.
"""