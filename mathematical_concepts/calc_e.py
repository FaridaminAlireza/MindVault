"""
the number e
* what the exponential series is,
* why it converges,
* what number e is,
* how e was historically defined,
* why the definitions are equivalent,
* main rules and properties of e.


The exponential function and the number e.

1. Power series definition of exp(x).
   The exponential function exp(x) is defined
   by the infinite series
   exp(x) = sum_{n=0 to infinity} x^n / n!.
   This series converges for every real or complex x, 
   so the exponential function is defined everywhere.

2. Proof of convergence.
   Consider a_n = x^n / n!. Apply the ratio test:
   |a_{n+1}| / |a_n| = |x| / (n+1).
   As n goes to infinity, |x|/(n+1) goes to 0, 
   which is less than 1. Therefore the series converges
   absolutely for every x. This proves that the radius
   of convergence is infinite.

3. Differentiating the series.
   Because the series converges absolutely and uniformly
   on bounded intervals, we can differentiate term-by-term:
   d/dx [sum_{n=0 to infinity} x^n/n! ] =
   sum_{n=1 to infinity} n x^{n-1}/n! = 
   sum_{n=1 to infinity} x^{n-1}/(n-1)! = 
   sum_{m=0 to infinity} x^m/m!.
   Thus exp'(x) = exp(x).
   Since exp(0) = 1, the power series is the unique solution
   of the differential equation y' = y, y(0) = 1.

4. Example: approximating e from the series.
   Take x = 1:
   e = sum_{n=0 to infinity} 1/n! =
   1 + 1 + 1/2 + 1/6 + 1/24 + 1/120 + ...
   Partial sums:
   S0 = 1
   S1 = 2
   S2 = 2.5
   S3 = 2.666666...
   S4 = 2.708333...
   S5 = 2.716666...
   The true value is approximately 2.7182818...,
   so the series converges rapidly.

5. Error bound for the series at x = 1.
   For n >= 1, n! >= 2^(n-1), 
   so 1/n! <= 1/2^(n-1).
   Therefore the tail after N satisfies
   R_N = sum_{n=N+1 to infinity} 1/n! <= sum_{n=N+1 to infinity} 1/2^(n-1) = 1/2^(N-1).
   Thus S_10 approximates e within about 1/512.

6. Is this how e was originally defined?
   One historically important and mathematically rigorous
   definition of e is indeed the convergent series
   e = sum_{n=0 to infinity} 1/n!.
   After proving the series converges to a finite number,
   that number is called e. 
   This is Euler's analytic definition from the 18th century.

However, that was not the first historical appearance of e. 
Multiple equivalent definitions appeared over time.

7. Historical definitions of e.

(1) Bernoulli’s limit (1683).
One of the earliest definitions of e came from studying compound interest:
e = lim_{n -> infinity} (1 + 1/n)^n.
This limit was discovered in the context of exponential growth.

(2) Euler’s series definition (1748).
Euler later defined
e = sum_{n=0 to infinity} 1/n!,
which is now the standard analytic definition.

(3) Differential equation definition.
One can define exp(x) as the unique solution of
y' = y with y(0) = 1. 
After solving this differential equation,
the solution has the Taylor expansion x^n/n!,
which matches the power series definition.

(4) Logarithmic definition.
Some approaches define the natural logarithm first by
ln(x) = integral from 1 to x of dt/t,
and then define e as the unique number such that ln(e) = 1.

All these definitions produce the same number.

8. Equivalence of the definitions.
   It can be proved that:
   e = lim_{n->infinity}(1 + 1/n)^n
   equals
   e = sum_{n=0 to infinity} 1/n!
   equals
   the value of x at which ln(x) = 1
   equals
   the base of the function satisfying y' = y.

Thus all definitions agree.

9. Important properties of e.

(1) exp(x) = sum x^n/n! for all real or complex x.

(2) exp'(x) = exp(x).

(3) exp(0) = 1.

(4) exp(x+y) = exp(x) exp(y). 
This can be proved using the power series 
expansion or the differential equation.

(5) exp(-x) = 1/exp(x).

(6) The function exp(x) is strictly 
increasing and continuous on the real line.

(7) The inverse function of exp(x) 
is the natural logarithm ln(x).

(8) e is irrational; 
its decimal expansion never repeats.

(9) e is transcendental;
 it is not the root of any nonzero
 algebraic polynomial with integer coefficients.

(10) exp(x) is entire, 
meaning analytic on the whole complex plane.

10. Summary.
The number e can be defined in several equivalent ways:
as the convergent series sum 1/n!, as the limit (1 + 1/n)^n,
as the base of the exponential function satisfying y' = y,
or as the number whose natural logarithm equals one.
The series representation for exp(x) converges for every
real or complex x, and it gives exp'(x) = exp(x).
Historically, Bernoulli’s limit came first, but 
Euler’s power series is the cleanest analytic definition
and underlies modern calculus.

"""