"""
INTERPOLATION ERROR THEOREM

1. The problem

Suppose G(t) is a smooth function.
We approximate G(t) by a polynomial F(t) of degree p.

We choose p + 1 interpolation points:


t₀, t₁, ..., tₚ


and construct F so that


F(tᵢ) = G(tᵢ),    i = 0, ..., p.


The question is: how large can the approximation error be?


|G(t) - F(t)|


2. The interpolation error formula

The exact interpolation error formula is


G(t) - F(t) = [G⁽ᵖ⁺¹⁾(ξ) / (p + 1)!] · ∏ᵢ₌₀ᵖ (t - tᵢ)


for some point ξ in the interpolation interval.

Therefore,


|G(t) - F(t)| ≤ [max |G⁽ᵖ⁺¹⁾| / (p + 1)!] · |∏ᵢ₌₀ᵖ (t - tᵢ)|


There are three important parts:


G⁽ᵖ⁺¹⁾        → behavior of G that a degree-p polynomial cannot reproduce

(p + 1)!       → comes from differentiating t⁽ᵖ⁺¹⁾ p + 1 times

∏(t - tᵢ)      → comes from the interpolation points


The maximum appears because ξ is unknown.

3. Why does the product ∏(t - tᵢ) appear?

Define the interpolation error


E(t) = G(t) - F(t).


At every interpolation point,


F(tᵢ) = G(tᵢ).


Therefore,


E(tᵢ) = G(tᵢ) - F(tᵢ) = 0.


So the error has zeros at


t₀, t₁, ..., tₚ.


If a function has a zero at tᵢ, then its corresponding factor is (t - tᵢ).

Therefore the error contains the factors


(t - t₀)(t - t₁)...(t - tₚ)


which can be written as


∏ᵢ₌₀ᵖ (t - tᵢ).


This is why the product term appears in the error formula.

4. Simple example of the product

Suppose we use two interpolation points:


t₀ = 0,    t₁ = 1.


Then


∏ᵢ₌₀¹ (t - tᵢ) = (t - 0)(t - 1) = t(t - 1).


At the interpolation points,


t = 0  →  t(t - 1) = 0


and


t = 1  →  t(t - 1) = 0.


This is exactly what we expect because the interpolation 
error must be zero at the interpolation points.

At t = 0.5,


|t(t - 1)| = |(0.5)(-0.5)| = 0.25.


So the product also tells us how the error depends on
the location of t relative to the interpolation points.

5. Why does the (p + 1)-th derivative appear?

F is a polynomial of degree p.

For example, if p = 1,


F(t) = a + bt.


Then


F'(t) = b


and


F''(t) = 0.


Since p + 1 = 2, the second derivative vanishes.

More generally, if


deg(F) = p,


then


F⁽ᵖ⁺¹⁾(t) = 0.


This is the key reason why the (p + 1)-th derivative of G 
appears in the error formula.

The degree-p polynomial F cannot reproduce 
the (p + 1)-th-order behavior of G.

Therefore:


degree p  →  error controlled by G⁽ᵖ⁺¹⁾.


6. Examples

If F is constant,


p = 0


and the error is controlled by


G'(t).


If F is linear,


p = 1


and the error is controlled by


G''(t).


If F is quadratic,


p = 2


and the error is controlled by


G'''(t).


If F is cubic,


p = 3


and the error is controlled by


G⁽⁴⁾(t).


In general:


degree p  →  (p + 1)-th derivative.


7. Example: approximating G(t) = t²

Take


G(t) = t².


We approximate it with a linear polynomial, so


p = 1.


Choose


t₀ = 0,    t₁ = 1.


The line passing through


(0, 0)


and


(1, 1)


is


F(t) = t.


At t = 0.5,


G(0.5) = 0.25


while


F(0.5) = 0.5.


Therefore the actual error is


|G(0.5) - F(0.5)| = |0.25 - 0.5| = 0.25.


8. Applying the error formula to the example

Since p = 1, we need the second derivative:


G⁽²⁾(t) = G''(t).


For


G(t) = t²,


we have


G''(t) = 2.


Therefore,


max |G''(t)| = 2.


The error bound becomes


|G(t) - F(t)| ≤ [2 / 2!] · |(t - 0)(t - 1)|.


Since


2! = 2,


we obtain


|G(t) - F(t)| ≤ |t(t - 1)|.


At t = 0.5,


|G(0.5) - F(0.5)| ≤ |(0.5)(-0.5)| = 0.25.


The actual error is also 0.25, so the bound is exact in this example.

9. Where does the factorial (p + 1)! come from?

Define


W(t) = ∏ᵢ₌₀ᵖ (t - tᵢ).


W(t) is a polynomial of degree p + 1.

Its highest-degree term is


t⁽ᵖ⁺¹⁾.


For example,


(t - t₀)(t - t₁) = t² + lower-degree terms.


Similarly,


(t - t₀)(t - t₁)(t - t₂) = t³ + lower-degree terms.


In general,


W(t) = t⁽ᵖ⁺¹⁾ + lower-degree terms.


Now differentiate p + 1 times.

All lower-degree terms disappear.

For the highest-degree term,


d⁽ᵖ⁺¹⁾/dt⁽ᵖ⁺¹⁾ [t⁽ᵖ⁺¹⁾] = (p + 1)!.


Therefore,


W⁽ᵖ⁺¹⁾(t) = (p + 1)!.


This is exactly where the factorial comes from.

10. Seeing the factorial with simple examples

For p = 1,


W(t) = t² + ...


so


W''(t) = 2 = 2!.


For p = 2,


W(t) = t³ + ...


so


W'''(t) = 6 = 3!.


For p = 3,


W(t) = t⁴ + ...


so


W⁽⁴⁾(t) = 24 = 4!.


Therefore, in general,


W⁽ᵖ⁺¹⁾(t) = (p + 1)!.


11. How the exact error formula is obtained

The error has zeros at


t₀, t₁, ..., tₚ.


We therefore introduce


W(t) = ∏ᵢ₌₀ᵖ (t - tᵢ).


A rigorous proof constructs an auxiliary function whose zeros 
include all the interpolation points and the target point t.

Using Rolle's theorem repeatedly, one can show that there 
is some ξ in the interval such that


G(t) - F(t) = [G⁽ᵖ⁺¹⁾(ξ) / (p + 1)!] · ∏ᵢ₌₀ᵖ (t - tᵢ).


The important point is that ξ is guaranteed to exist,
but we generally do not know exactly where it is.

12. Why is ξ not simply t?

The theorem does not generally say


G(t) - F(t) = [G⁽ᵖ⁺¹⁾(t) / (p + 1)!] · ∏(t - tᵢ).


Instead, it says that there exists some intermediate point ξ such that


G(t) - F(t) = [G⁽ᵖ⁺¹⁾(ξ) / (p + 1)!] · ∏(t - tᵢ).


The point ξ is somewhere in the relevant interval.

We know that it exists, but we generally do not know its exact location.

13. Why do we use max |G⁽ᵖ⁺¹⁾|?

The exact formula contains


|G⁽ᵖ⁺¹⁾(ξ)|.


But ξ is unknown.

However, we know


|G⁽ᵖ⁺¹⁾(ξ)| ≤ max |G⁽ᵖ⁺¹⁾|.


Therefore,


|G(t) - F(t)| ≤ [max |G⁽ᵖ⁺¹⁾| / (p + 1)!] · |∏ᵢ₌₀ᵖ (t - tᵢ)|.


The maximum gives us a guaranteed upper bound without knowing ξ.

It is therefore a worst-case bound.

It does not mean that the derivative at ξ actually equals the maximum.

14. Why does G⁽ᵖ⁺¹⁾ measure approximation difficulty?

Suppose G itself is a polynomial of degree p.

Then


G⁽ᵖ⁺¹⁾(t) = 0.


Therefore the interpolation error is zero.

This makes sense because a degree-p polynomial can be 
reproduced exactly by a degree-p interpolant.

For example,


G(t) = 2t + 3


is already linear.

A linear interpolant reproduces it exactly.

Indeed,


G''(t) = 0.


So the second derivative measures the curvature that
a linear approximation cannot reproduce.

15. Why does the error become O(h⁽ᵖ⁺¹⁾)?

Suppose the interpolation points have a characteristic spacing h.

Inside a small interval, each distance is approximately


|t - tᵢ| = O(h).


There are p + 1 such factors:


|t - t₀|, |t - t₁|, ..., |t - tₚ|.


Therefore,


|∏ᵢ₌₀ᵖ (t - tᵢ)| = O(h⁽ᵖ⁺¹⁾).


If the derivative is bounded,


max |G⁽ᵖ⁺¹⁾| < ∞,


then


max |G⁽ᵖ⁺¹⁾| / (p + 1)!


acts like a constant with respect to h.

Therefore,


|G(t) - F(t)| = O(h⁽ᵖ⁺¹⁾).


This means that decreasing h makes
the interpolation error decrease at order p + 1.

16. What does O(h⁽ᵖ⁺¹⁾) mean?

The statement


|G(t) - F(t)| = O(h⁽ᵖ⁺¹⁾)


means that, for sufficiently small h,


|G(t) - F(t)| ≤ C h⁽ᵖ⁺¹⁾


for some constant C independent of h.

For example, if p = 1,


error = O(h²).


If h is divided by 2, the error decreases approximately by a factor of


2² = 4.


If p = 2,


error = O(h³).


Dividing h by 2 gives approximately


2³ = 8


times smaller error.

17. Connection to geometry processing

Now consider an implicit surface.

The original function is


G : ℝ³ → ℝ.


The true surface is the zero level set


S_G = {x ∈ ℝ³ : G(x) = 0}.


The polynomial approximant is F.

Its approximate surface is


S_F = {x ∈ ℝ³ : F(x) = 0}.


The interpolation theorem gives a function-value error:


|F(x) - G(x)| = O(h⁽ᵖ⁺¹⁾).


But we actually care about geometric error:


How far apart are S_F and S_G?


18. Converting function error into geometric error

Choose a point x on the approximate surface:


x ∈ S_F.


Therefore,


F(x) = 0.


Now find a nearby point x + d on the true surface:


x + d ∈ S_G.


Therefore,


G(x + d) = 0.


Here d is the displacement vector.

It is not a point on the surface.

We approximately move in the normal direction:


d = δ ∇F(x) / ||∇F(x)||.


Using a first-order Taylor expansion,


F(x + d) ≈ F(x) + ∇F(x) · d.


Since


F(x) = 0,


we obtain


F(x + d) ≈ ∇F(x) · d.


Substituting d,


F(x + d) ≈ δ ||∇F(x)||.


Since


||d|| = |δ|,


we obtain


||d|| ≈ |F(x + d)| / ||∇F(x)||.


19. Using the interpolation error

Because x + d lies on the true surface,


G(x + d) = 0.


Therefore,


F(x + d) - G(x + d) = F(x + d).


Hence,


|F(x + d) - G(x + d)| = |F(x + d)|.


The interpolation theorem gives


|F(x + d) - G(x + d)| = O(h⁽ᵖ⁺¹⁾).


Therefore,


|F(x + d)| = O(h⁽ᵖ⁺¹⁾).


Substitute this into


||d|| ≈ |F(x + d)| / ||∇F(x)||.


If


||∇F(x)|| ≥ ε > 0,


then the denominator cannot become arbitrarily small.

Therefore,


||d|| = O(h⁽ᵖ⁺¹⁾).


20. Complete picture

The complete reasoning is:


F(tᵢ) = G(tᵢ)
    ↓
error is zero at tᵢ
    ↓
product ∏ᵢ₌₀ᵖ(t - tᵢ)
    ↓
F has degree p
    ↓
F⁽ᵖ⁺¹⁾ = 0
    ↓
G⁽ᵖ⁺¹⁾ controls the error
    ↓
G(t) - F(t)
= [G⁽ᵖ⁺¹⁾(ξ)/(p + 1)!] · ∏(t - tᵢ)
    ↓
ξ is unknown
    ↓
replace |G⁽ᵖ⁺¹⁾(ξ)|
by max |G⁽ᵖ⁺¹⁾|
    ↓
|G - F| = O(h⁽ᵖ⁺¹⁾)
    ↓
convert function error
into spatial displacement
    ↓
||d|| ≈ |F(x + d)| / ||∇F(x)||
    ↓
if ||∇F|| ≥ ε > 0
    ↓
||d|| = O(h⁽ᵖ⁺¹⁾)


21. The formula to remember

The main interpolation error bound is


|G(t) - F(t)|
≤
[max |G⁽ᵖ⁺¹⁾| / (p + 1)!]
·
|∏ᵢ₌₀ᵖ (t - tᵢ)|.


Each part has a specific reason:


∏ᵢ₌₀ᵖ (t - tᵢ)
→ the error is zero at every interpolation point.

G⁽ᵖ⁺¹⁾
→ a degree-p polynomial has zero (p + 1)-th derivative.

(p + 1)!
→ d⁽ᵖ⁺¹⁾/dt⁽ᵖ⁺¹⁾ [t⁽ᵖ⁺¹⁾] = (p + 1)!.

max |G⁽ᵖ⁺¹⁾|
→ ξ is unknown, so we use a guaranteed upper bound.

O(h⁽ᵖ⁺¹⁾)
→ there are p + 1 factors, each of size O(h).


Therefore,


|G - F| = O(h⁽ᵖ⁺¹⁾).


For the implicit surface, this becomes


||d|| = O(h⁽ᵖ⁺¹⁾)


provided that


||∇F|| ≥ ε > 0.


"""