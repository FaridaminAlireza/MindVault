"""
STIRLING’S APPROXIMATION

1. What problem Stirling’s approximation solves

The factorial function is defined as:

n! = 1 * 2 * 3 * ... * n

Factorials grow extremely fast. Even for moderately large n,
the exact value of n! becomes very large and difficult to
compute, store, or manipulate.

Stirling’s approximation provides a simple formula that closely
approximates n! for large n. It is especially useful in
asymptotic analysis, probability,
statistics, physics, and computer science.

---

2. Basic Stirling’s approximation formula

The standard approximation is:
n! is approximately equal to sqrt(2 * pi * n) * (n / e)^n
The accuracy improves as n becomes larger.

---

3. Logarithmic form

In many applications, we work with logarithms of factorials
instead of factorials themselves.

The logarithmic form of Stirling’s approximation is:

log(n!) is approximately equal to
n * log(n) - n + 0.5 * log(2 * pi * n)

This form is widely used because:

* It avoids numerical overflow
* It simplifies probability and statistics calculations
* It is common in maximum likelihood and information theory

---

4. Intuition behind the approximation

4.1 Approximating factorial using sums and integrals

Take the logarithm of the factorial:

log(n!) = log(1) + log(2) + ... + log(n)

This is a sum of log(k) from k = 1 to n.

This sum can be approximated by an integral:

sum of log(k) ≈ integral of log(x) dx from 1 to n

The integral of log(x) is:

x * log(x) - x

Evaluating between 1 and n gives approximately:

n * log(n) - n

This explains the dominant growth terms
in Stirling’s approximation.

---

4.2 Origin of the sqrt(2 * pi * n) factor

The missing correction factor comes from:

* The error between the discrete sum and the continuous integral
* A more precise analysis using the Euler–Maclaurin formula
* Asymptotic analysis of the Gamma function

This correction contributes 
the 0.5 * log(2 * pi * n) term in the
logarithmic form, which becomes 
the sqrt(2 * pi * n) factor when exponentiated.

---

5. More accurate versions (Stirling series)

Stirling’s approximation can be refined
into an asymptotic expansion:

n! ≈ sqrt(2 * pi * n) * (n / e)^n *
(1 + 1/(12n) + 1/(288n^2) - 139/(51840n^3) + ...)

Important notes:

* This is an asymptotic series, not a convergent one
* Adding just the first correction term 
often gives excellent accuracy
* Adding too many terms can reduce accuracy

---

6. Error bounds

There are rigorous bounds for Stirling’s approximation:

sqrt(2 * pi * n) * (n / e)^n < n! <
sqrt(2 * pi * n) * (n / e)^n * exp(1 / (12n))

This shows the approximation is mathematically well
controlled and very tight.

---

7. Accuracy examples

For small n:

* n = 5, exact value = 120,
approximation ≈ 118 (about 1.6% error)

For moderate n:

* n = 10, error is under 1%

For large n:

* n = 50 or 100, the approximation is extremely accurate,
 with negligible relative error

Even for modest values of n, Stirling’s approximation
 works very well.

---

8. Relation to the Gamma function

The factorial function can be extended to 
non-integer values using the Gamma function:

n! = Gamma(n + 1)

Stirling’s approximation generalizes to:

Gamma(z) ≈ sqrt(2 * pi) * z^(z - 0.5) * exp(-z)

for large z.

This form is widely used in physics, statistics, and complex analysis.

---

9. Applications

9.1 Probability and statistics

* Approximating binomial coefficients
* Simplifying likelihood functions
* Deriving entropy formulas

9.2 Information theory

* Derivation of Shannon entropy
* Analysis of typical sets

9.3 Physics

* Statistical mechanics
* Boltzmann entropy
* Partition functions

9.4 Algorithms and computer science

* Asymptotic growth rates
* Analysis of combinatorial algorithms
* Complexity estimates

---

10. Probabilistic and geometric interpretation

Stirling’s approximation reflects behavior similar to:

* Gaussian distributions
* The central limit theorem

The dominant exponential term captures growth,
while the square root term reflects fluctuations around the mean.

---

11. When not to use Stirling’s approximation

* For very small n (below about 5), exact factorials are better
* When exact combinatorial values are required
* When asymptotic behavior is not acceptable

---

12. Summary

Stirling’s approximation provides a simple and powerful estimate:

n! ≈ sqrt(2 * pi * n) * (n / e)^n

Key takeaways:

* Extremely accurate for large n
* Central to asymptotic analysis
* Fundamental in probability, statistics, physics, and computing

---

"""