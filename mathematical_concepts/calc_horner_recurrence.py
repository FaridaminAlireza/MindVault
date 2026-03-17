"""
Horner's method — the recurrence computers actually use to evaluate a polynomial

You wrote a polynomial like
f(x) = a_n x^n + a_{n-1} x^{n-1} + ... + a_1 x + a_0.
Computers almost always evaluate this using Horner’s rule,
which rewrites the polynomial to expose a simple recurrence
and needs only n multiplications and n additions.

Why Horner’s rule works (derivation)
Start from the polynomial and factor x repeatedly:

f(x) = a_n x^n + a_{n-1} x^{n-1} + ... + a_1 x + a_0
= x (a_n x^{n-1} + a_{n-1} x^{n-2} + ... + a_1) + a_0
= x ( x (a_n x^{n-2} + ... + a_2) + a_1 ) + a_0
= (((a_n x + a_{n-1}) x + a_{n-2}) x + ... ) x + a_0.

Define a sequence b_k by computing from the top coefficient down:
b_n = a_n,
for k = n-1, n-2, ..., 0:
b_k = b_{k+1} * x + a_k.
After doing those steps, b_0 = f(x).
This recurrence is exactly what Horner’s method implements.

Algorithm (procedural)

1. Set result = a_n.
2. For k = n-1 down to 0:
   result = result * x + a_k
3. result now equals f(x)

Cost: exactly n multiplications and n additions.

Worked example — careful step-by-step arithmetic
Take the polynomial
f(x) = 3 x^4 - 5 x^3 + 0 x^2 + 2 x - 1
so coefficients are a_4 = 3, a_3 = -5, a_2 = 0,
a_1 = 2, a_0 = -1. Evaluate at x = 2.

Using the recurrence:

1. b_4 = a_4 = 3.
2. b_3 = b_4 * 2 + a_3 = 3*2 + (-5). Compute: 3*2 = 6.
Then 6 + (-5) = 1. So b_3 = 1.
3. b_2 = b_3 * 2 + a_2 = 1*2 + 0 = 2. So b_2 = 2.
4. b_1 = b_2 * 2 + a_1 = 2*2 + 2 = 6. So b_1 = 6.
5. b_0 = b_1 * 2 + a_0 = 6*2 + (-1) = 11. So b_0 = 11.
   Therefore f(2) = 11.

You can check by expanding: 3*2^4 - 5*2^3 + 0 + 2*2 - 1 =
48 - 40 + 0 + 4 - 1 = 11.

Notes

* Efficiency: Horner uses O(n) operations (n multiplies, n adds).
Naively computing powers separately can cost much more.
* Numerical stability: Horner is generally better
than naive power evaluation,
but floating-point rounding and cancellation
can still cause errors for ill-conditioned inputs.
* Works for derivatives too (see next section).
* Integer vs floating point: for exact integer results,
use integers with
sufficient width (big integers) to avoid overflow.

Short Python implementation (plain text)
def horner_eval(coeffs, x):
# coeffs is [a_n, a_{n-1}, ..., a_0]
result = coeffs[0]           # a_n
for a in coeffs[1:]:
result = result * x + a
return result

# Example

coeffs = [3, -5, 0, 2, -1]  # 3 x^4 -5 x^3 + 0 x^2 + 2 x - 1
print(horner_eval(coeffs, 2))  # prints 11

---

1. Computing f'(x) alongside f(x) with almost no extra work

You can compute f(x) and f'(x) in a single pass through the coefficients using
a small companion recurrence (often called synthetic differentiation).
The idea: while you form the Horner sequence for f,
 maintain a second accumulator that builds the derivative.

Let coefficients be a_n, a_{n-1}, ..., a_0
and let x be the evaluation point.
Initialize:
b = a_n        # this will become f after the loop
c = 0          # this will become f' after the loop

Then for k = n-1 down to 0 do:
c = c * x + b
b = b * x + a_k

After the loop:
f(x) = b
f'(x) = c

Explanation / derivation sketch:

* b implements the usual Horner recurrence: b_k = b_{k+1} * x + a_k.
* c accumulates sums of the b_{k+1} terms in the pattern that yields
the derivative; algebraically this corresponds to differentiating
the nested Horner form.

Worked example (same polynomial as above)
f(x) = 3 x^4 -5 x^3 + 0 x^2 + 2 x - 1, x = 2.
Coefficients: a_4 = 3, a_3 = -5, a_2 = 0, a_1 = 2, a_0 = -1.

Initialize:
b = a_4 = 3
c = 0

k = 3:
c = c * 2 + b = 0*2 + 3 = 3
b = b * 2 + a_3 = 3*2 + (-5) = 1

k = 2:
c = 3 * 2 + b = 6 + 1 = 7
b = 1 * 2 + 0 = 2

k = 1:
c = 7 * 2 + b = 14 + 2 = 16
b = 2 * 2 + 2 = 6

k = 0:
c = 16 * 2 + b = 32 + 6 = 38
b = 6 * 2 + (-1) = 11

Result:
f(2) = b = 11
f'(2) = c = 38

Check by analytic derivative:
f'(x) = 12 x^3 - 15 x^2 + 0 + 2
f'(2) = 12*8 - 15*4 + 2 = 96 - 60 + 2 = 38  (matches)

Simple Python implementation that returns both:
def horner_with_derivative(coeffs, x):
# coeffs = [a_n, a_{n-1}, ..., a_0]
b = coeffs[0]   # a_n
c = 0.0
for a in coeffs[1:]:
c = c * x + b
b = b * x + a
return b, c   # (f(x), f'(x))

---

2. Demonstrate Horner with floating-point coefficients 
and show rounding error

Floating-point arithmetic is finite-precision. 
When coefficients differ greatly in magnitude or 
when cancellation occurs, Horner's method can produce results with
significant rounding error — sometimes catastrophic cancellation.
Here is a simple, dramatic example that shows the effect.

Consider the polynomial:
f(x) = 1e20 x^2 + 1 * x + (-1e20)

Evaluate at x = 1.

Exact arithmetic:
f(1) = 1e20 * 1^2 + 1*1 + (-1e20) = 1

But in IEEE 754 double precision, 1e20 + 1 is equal to 1e20
(because 1 is far smaller than 1e20 and cannot change
the 53-bit significand). Horner's method does:

Coefficients: a_2 = 1e20, a_1 = 1, a_0 = -1e20
x = 1

Step-by-step using double-precision semantics
(rounded at each operation):
b = a_2 = 1e20
b = b * x + a_1 = 1e20 * 1 + 1 -> computed as 1e20
(the +1 is lost to rounding)
b = b * x + a_0 = 1e20 * 1 + (-1e20) -> = 0

So Horner returns 0 instead of 1. 
That's catastrophic cancellation:
two huge terms nearly equal cancel 
and the small difference (1) is lost
because of limited precision.

A small Python demonstration 
(plain text code; run in 
a standard Python shell using IEEE doubles):
coeffs = [1e20, 1.0, -1e20]   # a_2, a_1, a_0
def horner_eval(coeffs, x):
r = coeffs[0]
for a in coeffs[1:]:
r = r*x + a
return r

print(horner_eval(coeffs, 1.0))   
# likely prints 0.0 on most systems

If you want the correct exact result, you can:

* use higher-precision arithmetic 
(Python's decimal module, or a big-floating library,
or Python's fractions/integers where possible),
* reorder or factor the polynomial analytically
to avoid cancellation if a closed form exists,
* or use compensated summation techniques in
more advanced numerical libraries.

Example using decimal for exactness
(conceptual, plain text):
from decimal import Decimal, getcontext
getcontext().prec = 50
coeffs = [Decimal('1e20'),
Decimal('1'), Decimal('-1e20')]
def horner_decimal(coeffs, x):
r = coeffs[0]
for a in coeffs[1:]:
r = r * x + a
return r

print(horner_decimal(coeffs, Decimal('1'))) 
# prints Decimal('1')

Explanation of why this happens

* Floating point stores numbers with a fixed number of significant bits.
If two operands differ hugely in magnitude, adding the small one may change
no significant digits of the large one, so the small one is effectively
ignored (rounded away).
* Cancellation occurs when you subtract nearly equal large numbers;
the leading digits cancel leaving a small difference which may have
far fewer accurate bits than either original operand.
* Horner itself does not create cancellation; it simply performs
the polynomial evaluation in a numerically efficient way.
But it cannot avoid inherent issues of floating-point arithmetic.
When coefficients or x cause near-cancellation, results can be inaccurate.

Practical tips to reduce floating-point error

* Rescale variables if possible
(evaluate polynomial at a transformed x).
* Use higher precision if required
(decimal, mpfr, or arbitrary-precision libraries).
* Reorder operations only when numerically justified — 
in general Horner is already a good choice.
* Use compensated algorithms or libraries designed for
numerically sensitive computations.

"""