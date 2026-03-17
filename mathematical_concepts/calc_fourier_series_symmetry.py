"""
Fourier Series Symmetry: Even and Odd Harmonics
===============================================

1. Case 1: f(t + T/2) = f(t)  (Half-period repetition)
------------------------------------------------------

This condition means the function repeats every T/2 even though the Fourier
series is written with period T.

Start with the cosine Fourier coefficient:

a_n = (2/T) ∫_0^T f(t) cos(nωt) dt

Split the integral into two halves:

a_n = (2/T)[ ∫_0^(T/2) f(t)cos(nωt)dt + ∫_(T/2)^T f(t)cos(nωt)dt ]

Transform the second integral using the substitution:

u = t − T/2

Then

∫_(T/2)^T f(t)cos(nωt)dt
= ∫_0^(T/2) f(u + T/2) cos(nω(u + T/2)) du

Using the symmetry:

f(u + T/2) = f(u)

Now simplify the cosine.

Since

ω = 2π / T

cos(nω(u + T/2))
= cos(nωu + nπ)

Using the identity

cos(x + nπ) = (-1)^n cos(x)

So

cos(nω(u + T/2)) = (-1)^n cos(nωu)

Thus the second integral becomes

∫_0^(T/2) f(u)(-1)^n cos(nωu) du


Now combine both halves of the original integral:

a_n =
(2/T)[
∫_0^(T/2) f(t)cos(nωt)dt
+
(-1)^n ∫_0^(T/2) f(t)cos(nωt)dt
]

Factor the integral:

a_n =
(2/T)(1 + (-1)^n) ∫_0^(T/2) f(t)cos(nωt)dt


Result:

If n is odd:

(-1)^n = -1
1 + (-1) = 0

Therefore

a_n = 0


If n is even:

(-1)^n = 1
1 + 1 = 2

Therefore

a_n = (4/T) ∫_0^(T/2) f(t)cos(nωt)dt


The same reasoning applies to the sine coefficients b_n.

Conclusion:

If

f(t + T/2) = f(t)

then the Fourier series contains only EVEN harmonics:

n = 2, 4, 6, 8, ...


------------------------------------------------------
2. Mirror Case: f(t + T/2) = −f(t)
------------------------------------------------------

This symmetry means the function flips sign every half period.

Start again from the cosine coefficient:

a_n = (2/T) ∫_0^T f(t)cos(nωt)dt

Split the integral into two halves:

a_n =
(2/T)[
∫_0^(T/2) f(t)cos(nωt)dt
+
∫_(T/2)^T f(t)cos(nωt)dt
]

Use the substitution again:

u = t − T/2

Then

∫_(T/2)^T f(t)cos(nωt)dt
=
∫_0^(T/2) f(u + T/2) cos(nω(u + T/2)) du


Apply the symmetry:

f(u + T/2) = −f(u)

And use again:

cos(nω(u + T/2)) = cos(nωu + nπ) = (-1)^n cos(nωu)

Thus the second integral becomes

∫_0^(T/2) [ −f(u) ] [ (-1)^n cos(nωu) ] du

= ∫_0^(T/2) (-1)^(n+1) f(u)cos(nωu) du


Now combine both halves:

a_n =
(2/T)[
∫_0^(T/2) f(t)cos(nωt)dt
+
(-1)^(n+1) ∫_0^(T/2) f(t)cos(nωt)dt
]

Factor the integral:

a_n =
(2/T)(1 + (-1)^(n+1)) ∫_0^(T/2) f(t)cos(nωt)dt


Result:

If n is even:

(-1)^(n+1) = -1
1 + (-1) = 0

Therefore

a_n = 0


If n is odd:

(-1)^(n+1) = 1
1 + 1 = 2

Therefore

a_n = (4/T) ∫_0^(T/2) f(t)cos(nωt)dt


Conclusion:

If

f(t + T/2) = −f(t)

then the Fourier series contains only ODD harmonics:

n = 1, 3, 5, 7, ...


------------------------------------------------------
Summary
------------------------------------------------------

Symmetry condition           Harmonics present

f(t + T/2) = f(t)            Even harmonics only
f(t + T/2) = −f(t)           Odd harmonics only
"""