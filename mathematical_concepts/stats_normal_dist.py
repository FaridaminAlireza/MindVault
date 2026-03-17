"""
From Bernoulli to Binomial, Poisson, 
and Normal Distributions 

===================
1. BINOMIAL DISTRIBUTION


Definition:
A Binomial random variable X counts the number of successes in n
independent Bernoulli trials, each with success probability p.

Key idea:
Each trial has only two outcomes: success (1) or failure (0).

Indicator variable representation:
Let Xi = 1 if trial i is a success, 0 otherwise.
Then:
X = X1 + X2 + ... + Xn

Expectation:
E[Xi] = p
Using linearity of expectation:
E[X] = E[X1 + ... + Xn] = np

Variance:
Var(Xi) = p(1 - p)
Since trials are independent:
Var(X) = Var(X1 + ... + Xn) = np(1 - p)

Binomial probability mass function:
P(X = k) = n! / (k!(n-k)!) * p^k * (1-p)^(n-k)

===================
2. POISSON DISTRIBUTION


Motivation:
Used to model the number of rare events occurring in
a fixed time or space interval.

Poisson as a limit of Binomial:
Start with Binomial(n, p)
Let n -> infinity
Let p -> 0
Keep lambda = np fixed

Why divide the rate by n?
The rate lambda is per unit time.
If we divide the unit into n subintervals, then:

* Each subinterval has probability p = lambda / n
* This ensures the expected number of events remains lambda

Poisson probability mass function:
P(X = k) = (lambda^k * e^(-lambda)) / k!

Mean and variance:
E[X] = lambda
Var(X) = lambda

Why mean equals variance?
Because Poisson counts independent rare events.
Each contributes both to average count
and variability in the same way.

===================
3. NORMAL DISTRIBUTION

Definition:
A continuous distribution describing symmetric,
bell-shaped behavior.

Parameters:
Mean = mu
Variance = sigma^2

Density function shape:
Bell curve centered at mu
Width controlled by sigma

===================
4. DERIVING NORMAL FROM BINOMIAL (DE MOIVRE–LAPLACE)

Goal:
Approximate Binomial(n, p) for large n using a Normal distribution.

Key insight:
For large n, Binomial probabilities cluster 
tightly around the mean np.

Why k is near np:

* The mean of X is np
* The variance is np(1-p)
* Most probability mass lies within 
a few standard deviations of np
* Far-away values are exponentially unlikely

Important clarification:

* n is the number of trials
* k is the number of successes
* k varies from 0 to n
* k ≈ np means "most likely values of k"

===================
5. USING LOGARITHMS

We start from:
P(X = k) = n! / (k!(n-k)!) * p^k * (1-p)^(n-k)

Take logarithms:
log P(X = k) = log n! - log k! - log (n-k)! + k log p + (n-k) log(1-p)

Why logs?

* Products become sums
* Factorials become smooth functions
* Enables Taylor expansion

===================
6. STIRLING APPROXIMATION

For large m:
log m! ≈ m log m - m + (1/2) log(2πm)

Apply this to:
n!
k!
(n-k)!

After simplification, many linear terms cancel.

===================
7. TAYLOR EXPANSION AROUND THE MEAN

Define:
f(k) = log P(X = k)

Expand around k = np:
k = np + h

Taylor expansion:
f(k) ≈ f(np) + f'(np)h + (1/2)f''(np)h^2

Key result:
f'(np) = 0 because probability is maximized at the mean.

So:
f(k) ≈ f(np) - (k - np)^2 / (2np(1-p))

This quadratic term determines the bell shape.

===================
8. RETURNING FROM LOG-PROBABILITY TO PROBABILITY

Since:
P(X = k) = exp(f(k))

We get:
P(X = k) ≈ exp(f(np)) * exp(-(k - np)^2 / (2np(1-p)))

Why exp(f(np)) is a constant:

* It does not depend on k
* It only scales the height of the curve
* The shape is entirely determined
by the quadratic term

The constant is fixed by normalization.

===================
9. WHERE PI COMES FROM


To ensure probabilities sum to 1:
Sum over k is approximated by an integral for large n.

This leads to the Gaussian integral:
Integral of exp(-x^2 / (2σ^2)) dx = sqrt(2πσ^2)

That is where π appears.
It comes purely from normalization, not from Taylor expansion.

===================
10. GAUSSIAN INTEGRAL PROOF

Define:
I = integral from -infinity to infinity of exp(-x^2) dx

Square it:
I^2 = double integral of exp(-(x^2 + y^2)) dx dy

Switch to polar coordinates:
x = r cos θ
y = r sin θ

===================
11. JACOBIAN EXPLANATION

Why Jacobian appears:

* dx dy represents a tiny rectangle
* In polar coordinates, area becomes a sector
* Sector area = r dr dθ

Jacobian determinant:
|∂(x,y)/∂(r,θ)| = r

So:
dx dy = r dr dθ

Integral becomes:
Integral from 0 to 2π dθ times integral
from 0 to infinity r exp(-r^2) dr

The angular part gives 2π
The radial part gives 1/2

Result:
I^2 = π
So:
I = sqrt(π)

===================
12. FINAL BINOMIAL → NORMAL APPROXIMATION


For large n:
Binomial(n, p) ≈ Normal(mean = np, variance = np(1-p))

Approximate probability:
P(X = k) ≈ (1 / sqrt(2πnp(1-p))) * exp(-(k - np)^2 / (2np(1-p)))

===================
13. HOW TO USE NORMAL WITH BINOMIAL PARAMETERS

Given:
n trials
success probability p

Compute:
mean = np
variance = np(1-p)
standard deviation = sqrt(np(1-p))

Then:

* Convert k to a z-score:
  z = (k - np) / sqrt(np(1-p))
* Use Normal distribution tables or CDF

Optional:
Continuity correction:
Use k ± 0.5 for better accuracy

===================
14. BIG PICTURE RELATIONSHIP

Bernoulli:
Single trial, two outcomes

Binomial:
Sum of many Bernoulli trials

Poisson:
Limit of Binomial for rare events

Normal:
Limit of Binomial (and Poisson) for large sample sizes

Core idea:
When many independent random contributions are 
added together, the distribution becomes Normal.

===================
BINOMIAL TO NORMAL – INTUITION

1) Why Normal appears
- Binomial counts many independent small effects
- Each trial adds 0 or 1
- The total is a sum of many independent contributions
- By averaging effects, randomness smooths out

2) Why symmetry appears
- Deviations above and below the mean are equally likely
- Large deviations require many unlikely outcomes

3) Why quadratic exponent
- Probability decreases fastest near the peak
- Log-probability is smooth
- Any smooth peak looks quadratic when zoomed in

4) Why variance controls width
- Large variance → wide bell
- Small variance → narrow bell

5) Big idea
Normal distribution is not special — it is inevitable
It is what randomness looks like at large scale
===================


BINOMIAL TO NORMAL – FORMAL PROOF OUTLINE

1) Start with Binomial PMF
P(X = k) = n! / (k!(n-k)!) * p^k * (1-p)^(n-k)

2) Take logarithm
f(k) = log n! - log k! - log(n-k)! + k log p + (n-k) log(1-p)

3) Apply Stirling approximation
log m! ≈ m log m - m + (1/2) log(2πm)

4) Simplify f(k)
Obtain a smooth function of k

5) Expand around the maximum
Mean = np
Set k = np + h
Taylor expand:
f(k) ≈ f(np) + (1/2) f''(np) h^2

6) Compute second derivative
f''(np) = -1 / (np(1-p))

7) Exponentiate
P(X = k) ≈ exp(f(np)) * exp(-(k-np)^2 / (2np(1-p)))

8) Normalize
Use Gaussian integral:
Integral exp(-x^2 / (2σ^2)) dx = sqrt(2πσ^2)

9) Final result
Binomial(n,p) ≈ Normal(mean=np, variance=np(1-p))
"""