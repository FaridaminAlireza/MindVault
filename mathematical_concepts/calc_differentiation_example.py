"""
CLAIM
The function
f(x) = sqrt(1 + sin x)
is NOT differentiable at
x₀ = 3π/2 + 2kπ,  k ∈ Z.

---
1. DEFINITION OF THE DERIVATIVE

A function f is differentiable at x₀ if the limit

f′(x₀) = lim (h → 0) [ f(x₀ + h) − f(x₀) ] / h

exists and is finite.

For f(x) = sqrt(1 + sin x):

Since sin(x₀) = −1, we have
f(x₀) = sqrt(1 − 1) = 0.

Therefore, the derivative at x₀ would be

f′(x₀) = lim (h → 0) sqrt(1 + sin(x₀ + h)) / h

So we only need to study this limit.

---

2. EXACT TRIGONOMETRIC SIMPLIFICATION 
(NO APPROXIMATIONS)

Use the sine addition formula:

sin(x₀ + h) = sin x₀ cos h + cos x₀ sin h

At x₀ = 3π/2 + 2kπ:

sin x₀ = −1
cos x₀ = 0

Thus,

1 + sin(x₀ + h)
= 1 − cos h

This equality is exact — no Taylor series
or approximation is used.

---
3. REMOVING THE SQUARE ROOT

Recall the trigonometric identity:

1 − cos h = 2 sin²(h / 2)

Therefore,

sqrt(1 + sin(x₀ + h))
= sqrt(2) · |sin(h / 2)|

Substitute this into the difference quotient:

sqrt(1 + sin(x₀ + h)) / h
= sqrt(2) · |sin(h / 2)| / h

---
4. REWRITING THE EXPRESSION

Write:

|sin(h / 2)| / h
= (|h / 2| / h) · (|sin(h / 2)| / |h / 2|)

So the full expression becomes:

sqrt(2)/2 · (|h| / h) · (|sin(h / 2)| / |h / 2|)

---
5. TAKING THE LIMIT

As h → 0:

|sin(h / 2)| / |h / 2| → 1

But:

|h| / h =  1  if h > 0
|h| / h = −1  if h < 0

Hence:

Right-hand limit (h → 0⁺):
= sqrt(2)/2

Left-hand limit (h → 0⁻):
= −sqrt(2)/2

The two one-sided limits are
NOT equal.

---

6. CONCLUSION

Since the left-hand and right-hand limits differ,
the limit defining the derivative does not exist.

Therefore:

f(x) = sqrt(1 + sin x)
is NOT differentiable at
x = 3π/2 + 2kπ.

The non-differentiability is caused by the square root creating 
an absolute-value behavior near points where 1 + sin x = 0.
This produces a cusp.

---
7. ANOTHER EXAMPLE AND THE GENERAL APPROACH

Example:

g(x) = sqrt(1 − cos x)

At x = 0:

g(0) = 0
1 − cos x = 2 sin²(x / 2)

So:

g(x) = sqrt(2) · |sin(x / 2)|

Then:

[g(h) − g(0)] / h
= sqrt(2) · |sin(h / 2)| / h

This expression has different left- and right-hand limits at 0,
so g is not differentiable at 0.

---
GENERAL PRINCIPLE

If a function has the form

f(x) = sqrt(g(x))

and g(x₀) = 0 while g(x) behaves like (x − x₀)² near x₀, then

sqrt(g(x)) behaves like |x − x₀|.

Absolute-value behavior produces a cusp, 
and a cusp prevents differentiability.

"""