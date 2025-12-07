"""
General solutions of tan x = tan θ, sin x = sin θ, and cos x = cos θ
Equations relating trigonometric functions of two angles 
e.g. 
tan x = tan θ,
sin x = sin θ,
cos x = cos θ 
— all reduce to the idea 
“angles are equal up to the function’s period and its symmetry.” 


1. tan x = tan θ
   General solution:
   x = θ + kπ,  for any integer k.

The tangent function has period π: 
tan(u + π) = tan u for all u where tan is defined.
So any x that differs from θ by 
an integer multiple of π gives 
the same tangent value. 
Conversely, if tan x = tan θ 
then tan(x − θ) = 0, so x − θ = kπ.

Notes / domain caution:
Tangent is undefined where 
cosine is zero (x = π/2 + kπ). 
The formula x = θ + kπ covers those cases 
consistently: if θ is such that tan θ is undefined,
then x = θ + kπ are exactly the places where 
tan x is also undefined 
(so the equality of the two “undefined” values 
is understood in the usual limiting sense).

In practical solving one usually interprets 
tan equality through x = θ + kπ.

Example A — explicit numeric (general form):
Let θ = π/6 (30°). Then solutions:
x = π/6 + kπ.
Solutions in [0, 2π):
for k = 0 → x = π/6
for k = 1 → x = π/6 + π = 7π/6
(k = 2 gives > 2π, k = −1 gives negative)
So x ∈ {π/6, 7π/6} in [0, 2π).

Example B — when θ = π/2 (where tan is undefined):
θ = π/2. The formula gives x = π/2 + kπ, 
i.e. x = π/2, 3π/2, ... 
which are precisely the cos = 0 locations.

2. sin x = sin θ
   General solution:
   x = θ + 2kπ  
   or  x = π − θ + 2kπ,  for any integer k.

The sine function has period 2π 
and the symmetry sin(π − u) = sin u. 
So if sin x = sin θ, 
either x differs from θ by a full period (x = θ + 2kπ)
or x is the supplement of θ plus full periods (x = π − θ + 2kπ).
One can also derive this from 
sin x − sin θ = 2 cos((x+θ)/2) sin((x−θ)/2) and
 set the appropriate factor to zero.

Notes:
No hidden domain issues — sine defined everywhere.
The two families can coincide for special θ 
(for example if θ = π/2 then
 π − θ = π/2, 
 so both families give the same set).

Example A 
θ = π/6:
General solutions:
x = π/6 + 2kπ   or
x = π − π/6 + 2kπ = 5π/6 + 2kπ.
Solutions in [0, 2π):
from first family: π/6
from second family: 5π/6
also add their +2π repeats if needed 
(but within [0, 2π) only those two).
So x ∈ {π/6, 5π/6} in [0, 2π).

Example B  
θ = 2.3 (radians, arbitrary):
Compute π − θ = π − 2.3 ≈ 0.84159265...
General solutions:
x = 2.3 + 2kπ  or 
x ≈ 0.84159265 + 2kπ.
Solutions in [0, 2π): x ≈ 2.3 and x ≈ 0.8416.

3. cos x = cos θ
   General solution:
   x = θ + 2kπ  or  
   x = −θ + 2kπ,  for any integer k.
   (Equivalently x = ±θ + 2kπ.)

Cosine has period 2π and is even: cos(−u) = cos u. 
So equality happens either 
when x equals θ modulo 2π, or 
when x equals −θ modulo 2π. 
Another common equivalent form uses 
x = θ + 2kπ or 
x = 2π − θ + 2kπ (since −θ ≡ 2π − θ (mod 2π)).

Notes:
Cosine is defined everywhere; 
the two families may reduce to one 
if θ ≡ −θ (mod 2π), i.e. θ ≡ 0 or π (mod 2π).

Example A
θ = π/6:
General solutions:
x = π/6 + 2kπ  or
x = −π/6 + 2kπ ≡ 11π/6 + 2(k−1)π.
Solutions in [0, 2π):
x = π/6 and x = 11π/6.
So x ∈ {π/6, 11π/6} in [0, 2π).

Example B
 θ = π:
The two families coincide because −π ≡ π (mod 2π).
General solutions: 
x = π + 2kπ; in [0, 2π) that is x = π only.

Extra worked example solving all three for a given θ
Let θ = π/3 (60°).
tan x = tan(π/3) 
→ x = π/3 + kπ  
→ in [0,2π): x = π/3, 4π/3.
sin x = sin(π/3) 
→ x = π/3 + 2kπ  or  x = π − π/3 + 2kπ = 2π/3 + 2kπ  
→ in [0,2π): x = π/3, 2π/3.
cos x = cos(π/3) 
→ x = π/3 + 2kπ  or  x = −π/3 + 2kπ = 5π/3 + 2(k−1)π  
→ in [0,2π): x = π/3, 5π/3.

"""

"""
How calculators and computers solve equations like
tan x = tan θ, sin x = sin θ, cos x = cos θ 

Calculators do not solve these by reasoning 
about trigonometric identities like we do. 
Instead, they generally follow one of these approaches
depending on the function and the mode the problem is in:

---

# 1. When solving forward (input → trig value)

Example: You type sin(0.75).

They convert angles to radians (if needed)
They compute the trig function 
using numerical series expansions, such as:

* Taylor / Maclaurin series
* CORDIC algorithm (in small embedded calculators)
* Polynomial approximations 
like Chebyshev polynomials (faster for CPUs)

Example (sin):

sin x = x − x³/3! + x⁵/5! − x⁷/7! + …
Computers use optimized versions to get exact results very fast.


# 2. When solving inverse equations

Example: You enter:

x = sin⁻¹(0.5)

The calculator:

Finds the principal value only
(usually within a specific limited range)

| Function | Principal Range Returned |
| -------- | ------------------------ |
| sin⁻¹(x) | [-π/2, +π/2]             |
| cos⁻¹(x) | [0, π]                   |
| tan⁻¹(x) | (-π/2, +π/2)             |

So:

sin⁻¹(0.5) gives only π/6 (or 30°), NOT 5π/6.

That’s why calculators don’t list all solutions — 
they stick to the principal branch 
where each inverse trig function is one-to-one.


# 3. Solving equations (like sin x = sin θ)

Computers do not automatically expand
to the full general solution:
Wrong assumption: Calculator → All solutions
Reality: Calculator → ONE solution only
They either:
 Rearrange as an inverse trig function
 Return one result based on 
 internal principal range rules

Example:

Solve sin x = sin(40°)

Calculator gives:
x = 40°   (only principal angle)
But the full real mathematics
gives infinitely many:
x = 40° + 360°k   or 
x = 180° − 40° + 360°k

So we have to use trig identities to
get all solutions.


# 4. When solving numerically (general equations)

If you ask a calculator or computer to solve something like:

sin x = 0.32

It will often use Newton’s method or
similar root-finding algorithms.
But again:
 Only finds one nearby solution
 Doesn’t give the periodic solutions automatically

You must add:

* For sine: + 2πk and π − x + 2πk
* For cosine: + 2πk and −x + 2πk
* For tangent: + πk


Why calculators don’t give all solutions
Because trig functions are periodic and
not one-to-one, inverse functions would be
infinite-valued unless restricted.

To keep them usable in real-world applications 
(navigation, physics, engineering), they must:

* enforce a *principal range* for inverse functions
* give a single consistent answer

So calculators leave the job of adding 
the correct periodic solutions to the human.



Two Solution details — step-by-step, algebraic
(All numeric entries rounded to 4 decimals)

NEWTON’S METHOD
Problem: solve sin x = 0.5 algebraically.
Define f(x) = sin x − 0.5.
Then f′(x) = cos x.
Newton update: x_{n+1} = x_n − f(x_n)/f′(x_n).
Choose initial guess x0 = 1.0000.

Iter 0: x0 = 1.0000
f(x0) = sin(1.0000) − 0.5 = 0.3415
f′(x0) = cos(1.0000) = 0.5403
x1 = 1.0000 − 0.3415/0.5403 = 0.3680

Iter 1: x1 = 0.3680
f(x1) = sin(0.3680) − 0.5 = −0.1402
f′(x1) = cos(0.3680) = 0.9330
x2 = 0.3680 − (−0.1402)/0.9330 = 0.5183

Iter 2: x2 = 0.5183
f(x2) = sin(0.5183) − 0.5 = −0.0046
f′(x2) = cos(0.5183) = 0.8687
x3 = 0.5183 − (−0.0046)/0.8687 = 0.5236

Iter 3: x3 = 0.5236
f(x3) = sin(0.5236) − 0.5 = −0.0000
f′(x3) = cos(0.5236) = 0.8660
x4 = 0.5236 − (−0.0000)/0.8660 = 0.5236

Iter 4: x4 ≈ 0.5236 stable.
Converged solution x ≈ 0.5236 (π/6).

Algebraic note: Newton linearizes f at x_n.
Solve f(x_n)+f′(x_n)(x−x_n)=0 for x.
That gives the update formula used above.

TAYLOR (MACLAURIN) SERIES FOR sin(x)
Series formula: sin x = x − x^3/3! + x^5/5! − x^7/7! + …
We approximate sin(0.5) with terms to x^7.

x = 0.5 (radians).

Term n=1: x = 0.5 → 0.5000
Term n=3: −x^3/3! = −0.0208 → −0.0208
Term n=5: x^5/5! = 0.0003 → 0.0003
Term n=7: −x^7/7! = −0.0000 → −0.0000

Partial sums after each term:
S1 = 0.5000
S2 = 0.4792
S3 = 0.4794
S4 = 0.4794

True sin(0.5) = 0.4794 (rounded)
Approx with terms up to x^7 = 0.4794 (rounded)
Absolute error ≈ 0.0000 (rounded)

Algebraic derivation for terms:
General term = (−1)^k x^{2k+1}/(2k+1)!.
Plug k = 0,1,2,3 for terms shown.

Practical remarks (algebraic)
Newton finds one root near initial guess.
Convergence is quadratic near root.
Taylor gives polynomial approximation.
Truncation error equals next dropped term.
For x small, few terms suffice.



# The full algebraic explanation for
sin x = x − x³/3! + x⁵/5! − x⁷/7! + …
(the Maclaurin Series for sin x)


We look for a polynomial that equals sin x near x = 0.
A Maclaurin series is simply 
a Taylor series centered at 0:

For any function f(x):

f(x) = f(0)
+ f′(0)x
+ f″(0)x²/2!
+ f‴(0)x³/3!
+ …

General formula:

f(x) = Σ [ f⁽ⁿ⁾(0) / n! ] xⁿ
(sum from n = 0 to ∞)

We apply this to f(x) = sin x

---

# Compute derivatives of sin x

| n | derivative                          | expression | evaluated at x=0 |
| - | ----------------------------------- | ---------- | ---------------- |
| 0 | f(x)                                | sin x      | sin(0) = 0       |
| 1 | f′(x)                               | cos x      | cos(0) = 1       |
| 2 | f″(x)                               | −sin x     | −sin(0) = 0      |
| 3 | f‴(x)                               | −cos x     | −cos(0) = −1     |
| 4 | f⁽⁴⁾(x)                             | sin x      | sin(0) = 0       |
| 5 | f⁽⁵⁾(x)                             | cos x      | cos(0) = 1       |
| … | pattern repeats every 4 derivatives |            |                  |

So derivatives at zero follow repeating pattern:

0, 1, 0, −1, 0, 1, 0, −1, …

---

# Plug those derivative values into series formula

sin x =
f(0)

* f′(0)x
* f″(0)x²/2!
* f‴(0)x³/3!
* f⁽⁴⁾(0)x⁴/4!
* …

= 0

* (1)x/1!
* 0·x²/2!
* (−1)x³/3!
* 0·x⁴/4!
* (1)x⁵/5!
* …

→ Terms where derivative is 0 disappear

Final:

sin x =
x − x³/3! + x⁵/5! − x⁷/7! + x⁹/9! − …

Only odd powers of x
Signs alternate + − + − …


# Why it works
This polynomial:

• has the same value as sin x at x=0
• has all the same derivatives at x=0
• is infinitely differentiable
• converges for all real x
Thus the infinite series exactly equals sin x.

# Compact Form
Using index k:
sin x = Σₖ₌₀→∞ [ (−1)ᵏ · x^(2k+1) / (2k+1)! ]
The series is the unique infinite polynomial that matches
the curvature (derivatives) of sin x at x=0 —
so as you add more terms, the approximation becomes exact.

"""