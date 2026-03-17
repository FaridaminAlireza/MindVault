"""
Example: Fourier Series with Period T = 4

Function definition over one period:

f(t) =
0   for -2 < t < 0
1   for 0 < t < 2

The function repeats every 4 units (T = 4).

--------------------------------------------------
1. General Fourier Series Formula

For a function with period T:

f(t) =
a0/2 + Σ [ a_n cos(nω0 t) + b_n sin(nω0 t) ]

where the fundamental angular frequency is:

ω0 = 2π / T

--------------------------------------------------
2. Substitute T = 4

ω0 = 2π / 4
ω0 = π / 2

So the Fourier series terms will use:

cos(nπt/2)
sin(nπt/2)

This is how the period T = 4 enters the series.

--------------------------------------------------
3. Compute a0

Formula:

a0 = (2/T) ∫_{-T/2}^{T/2} f(t) dt

Since T = 4:

a0 = (2/4) ∫_{-2}^{2} f(t) dt
a0 = (1/2) ∫_{-2}^{2} f(t) dt

Split the integral:

a0 = (1/2)[ ∫_{-2}^{0} 0 dt + ∫_{0}^{2} 1 dt ]

First integral = 0
Second integral = 2

So:

a0 = (1/2)(2)
a0 = 1

Constant term:

a0/2 = 1/2

--------------------------------------------------
4. Compute a_n

Formula:

a_n = (2/T) ∫_{-T/2}^{T/2} f(t) cos(nω0 t) dt

Substitute T = 4:

a_n = (1/2) ∫_{-2}^{2} f(t) cos(nπt/2) dt

Split integral:

a_n = (1/2)[ ∫_{-2}^{0} 0 dt + ∫_{0}^{2} cos(nπt/2) dt ]

So:

a_n = (1/2) ∫_{0}^{2} cos(nπt/2) dt

Integrate:

∫ cos(at) dt = sin(at)/a

Here a = nπ/2.

Evaluate from 0 to 2:

sin(nπ) = 0
sin(0) = 0

Therefore:

a_n = 0

--------------------------------------------------
5. Compute b_n

Formula:

b_n = (2/T) ∫_{-T/2}^{T/2} f(t) sin(nω0 t) dt

Substitute T = 4:

b_n = (1/2) ∫_{-2}^{2} f(t) sin(nπt/2) dt

Split integral:

b_n = (1/2)[ ∫_{-2}^{0} 0 dt + ∫_{0}^{2} sin(nπt/2) dt ]

So:

b_n = (1/2) ∫_{0}^{2} sin(nπt/2) dt

Integrate:

∫ sin(at) dt = -cos(at)/a

Evaluate from 0 to 2:

cos(nπ) = (-1)^n
cos(0) = 1

So:

b_n = (1/2)[ -( (-1)^n - 1 ) / (nπ/2) ]

Simplify:

b_n = (1 - (-1)^n) / (nπ)

--------------------------------------------------
6. Final Fourier Series

f(t) =
1/2 + Σ ( (1 - (-1)^n) / (nπ) ) sin(nπt/2)

--------------------------------------------------
7. Simplified Pattern

If n is even:

b_n = 0

If n is odd:

b_n = 2/(nπ)

So the Fourier series becomes:

f(t) =
1/2 +
(2/π)[
sin(πt/2)
+ (1/3)sin(3πt/2)
+ (1/5)sin(5πt/2)
+ ...
]

--------------------------------------------------
8. Where T = 4 Appears

The period T = 4 affects three things:

1) Fundamental frequency:
ω0 = 2π/T = π/2

2) Coefficient factor:
2/T = 1/2

3) Integration limits:
[-T/2, T/2] = [-2, 2]

These changes adapt the general Fourier series to a period of 4.

"""