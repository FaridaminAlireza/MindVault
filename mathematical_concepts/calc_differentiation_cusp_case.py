"""
A cusp happens when:

The function approaches a point continuously (f(x) → f(x₀))
But the slope from the left and right are finite but unequal,
often with opposite signs

GENERAL PRINCIPLE

If a function has the form
f(x) = sqrt(g(x))
and g(x₀) = 0 
while g(x) behaves like (x − x₀)² near x₀, then
sqrt(g(x)) behaves like |x − x₀|.

Absolute-value behavior produces a cusp, 
and a cusp prevents differentiability.

----
Example 1:  f(x) = sqrt(1 + sin x)
is NOT differentiable at
x₀ = 3π/2 + 2kπ,  k ∈ Z.

A function f is differentiable at x₀ if the limit
f′(x₀) = lim (h → 0) [ f(x₀ + h) − f(x₀) ] / h
exists and is finite.

For f(x) = sqrt(1 + sin x):
Since sin(x₀) = −1, we have
f(x₀) = sqrt(1 − 1) = 0.

Therefore, the derivative at x₀ would be
f′(x₀) = lim (h → 0) sqrt(1 + sin(x₀ + h)) / h

So we only need to study this limit.

Use the sine addition formula:

sin(x₀ + h) = sin x₀ cos h + cos x₀ sin h

At x₀ = 3π/2 + 2kπ:
sin x₀ = −1
cos x₀ = 0

Thus,
1 + sin(x₀ + h)
= 1 − cos h

Removing the square root:
Recall the trigonometric identity:

1 − cos h = 2 sin²(h / 2)

Therefore,
sqrt(1 + sin(x₀ + h))
= sqrt(2) · |sin(h / 2)|

Substitute this into the difference quotient:

sqrt(1 + sin(x₀ + h)) / h
= sqrt(2) · |sin(h / 2)| / h

Write:

|sin(h / 2)| / h
= (|h / 2| / h) · (|sin(h / 2)| / |h / 2|)

So the full expression becomes:

sqrt(2)/2 · (|h| / h) · (|sin(h / 2)| / |h / 2|)


TAKING the limit:

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

The non-differentiability is caused by
the square root creating an absolute-value 
behavior near points where 1 + sin x = 0.
This produces a cusp.

---
EXAMPLE 2: g(x) = sqrt(1 − cos x)

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
8. Example 3: g(x) = (x - 2)^2

g(x) = (x - 2)^2
f(x) = sqrt(g(x)) = sqrt((x - 2)^2) = |x - 2|

Check derivative near x = 2:

For x > 2: f(x) = x - 2 → derivative f'(x) = 1
For x < 2: f(x) = 2 - x → derivative f'(x) = -1
At x = 2: left-hand derivative = -1, right-hand derivative = 1

Since the left-hand and right-hand derivatives are not equal,
the derivative at x = 2 does not exist.

This shows that sqrt(g(x)) behaves like |x - 2| near x = 2 and
has a sharp corner at x = 2.


"""