"""
POISSON DISTRIBUTION (FROM BERNOULLI)
---
1. BACKGROUND AND MOTIVATION

---
The Poisson distribution models the number of times an
event occurs in a fixed interval of time or space.

Typical examples:

* Number of emails received per hour
* Number of phone calls per minute
* Number of radioactive decays per second
* Number of defects on a sheet of material

The key idea:
Events are rare, occur independently,
and we only care about how many occur in a given interval.

---

2. BERNOULLI RANDOM VARIABLE

---

A Bernoulli random variable models a single trial with two outcomes.

Let X ~ Bernoulli(p)

Possible values:
X = 1 (success) with probability p
X = 0 (failure) with probability 1 - p

Expectation:
E[X] = p

Variance:
Var(X) = p(1 - p)

---

3. BINOMIAL DISTRIBUTION (FROM BERNOULLI)

---

A Binomial random variable counts the number of successes in
 n independent Bernoulli trials.

Let:
X = X1 + X2 + ... + Xn
where each Xi ~ Bernoulli(p), independent

Then:
X ~ Binomial(n, p)

Probability mass function:
P(X = k) = C(n, k) p^k (1 - p)^(n - k)

Expectation:
E[X] = np

Variance:
Var(X) = np(1 - p)

---

4. WHY WE MOVE FROM BINOMIAL TO POISSON

---

Binomial assumes:

* A fixed number of trials
* Each trial has the same probability

But in many real-world problems:

* Time is continuous
* Number of opportunities is very large
* Probability per opportunity is very small

This motivates taking a limit of the Binomial distribution.

---

5. DIVIDING TIME INTO SMALL INTERVALS

---

Assume we observe events over 1 unit of time.

Divide this interval into n equal subintervals:
Each subinterval has length 1/n

Assume:

* At most one event can occur in a very small subinterval
* Events in different subintervals are independent

Each subinterval is treated as a Bernoulli trial.

---

6. WHY THE PROBABILITY IS λ / n

---

Let λ be the event rate:
λ = expected number of events per unit time

If we look at an interval of length 1/n:
Expected number of events in that interval is:
λ * (1/n) = λ / n

For very small intervals:
Probability of one event ≈ expected number of events
Probability of two or more events ≈ 0

Thus:
p_n = λ / n

This is why we divide λ by n, even though λ is already “per unit time”.

If we did NOT divide by n:

* Expected events would grow without bound
* No meaningful limiting distribution would exist

---

7. BINOMIAL MODEL USED FOR THE LIMIT

---

Let:
X_n ~ Binomial(n, λ / n)

This models:

* n tiny intervals
* each interval has a small chance of an event

Expectation:
E[X_n] = n * (λ / n) = λ

Variance:
Var(X_n) = n * (λ / n) * (1 - λ / n)
= λ(1 - λ / n)

---

8. TAKING THE POISSON LIMIT

---

We now let n → ∞.

The probability mass function of X_n is:
P(X_n = k) = C(n, k) (λ / n)^k (1 - λ / n)^(n - k)

As n → ∞:

* C(n, k) (1 / n)^k → 1 / k!
* (1 - λ / n)^n → e^(-λ)
* (1 - λ / n)^(-k) → 1

Combining all limits:
P(X = k) = (λ^k e^(-λ)) / k!

---

9. POISSON DISTRIBUTION (DEFINITION)

---

A random variable X has a Poisson distribution with parameter λ > 0 if:

P(X = k) = (λ^k e^(-λ)) / k!
for k = 0, 1, 2, ...

---

10. WHY THIS IS A VALID DISTRIBUTION

---

Non-negativity:
All terms are non-negative.

Sum to 1:
Sum over k from 0 to infinity:
e^(-λ) * sum(λ^k / k!) = e^(-λ) * e^(λ) = 1

---

11. EXPECTATION OF POISSON

---

E[X] = sum k * (λ^k e^(-λ)) / k!

Rewrite:
k * (λ^k / k!) = λ * (λ^(k-1) / (k-1)!)

Thus:
E[X] = λ e^(-λ) * sum(λ^j / j!)
= λ e^(-λ) e^(λ)
= λ

---

12. VARIANCE OF POISSON

---

Use:
Var(X) = E[X^2] - (E[X])^2

First compute:
E[X(X - 1)] = λ^2

Then:
E[X^2] = E[X(X - 1)] + E[X]
= λ^2 + λ

Thus:
Var(X) = (λ^2 + λ) - λ^2
= λ

---

13. WHY MEAN = VARIANCE = λ

---

Key reasons:

* Events occur independently
* No clustering or regular spacing
* Only randomness is whether events occur at all

From the Binomial limit:
Mean → λ
Variance → λ

From structure:
Poisson is a sum of infinitely many Bernoulli variables
with tiny probabilities:
Each contributes equally to mean and variance.

---

14. INTERPRETATION OF λ

---

λ is:

* Expected number of events per unit interval
* The mean of the distribution
* The variance of the distribution

If λ = 5:
On average, 5 events occur
Typical fluctuations are of size sqrt(5)

---

15. EXAMPLES

---

Example 1: Emails
λ = 2 emails/hour

Probability of exactly 3 emails:
P(X = 3) = (2^3 e^(-2)) / 3! ≈ 0.18

Probability of no emails:
P(X = 0) = e^(-2) ≈ 0.135

Example 2: Radioactive decay
λ = 4 decays/minute
Mean = 4
Variance = 4
Standard deviation = 2

---

16. POISSON VS BINOMIAL

---

Binomial:

* Fixed number of trials
* Probability p
* Finite n

Poisson:

* Random number of events
* Rate λ
* Limit of Binomial as n → ∞, p → 0, np → λ

---

17. WHEN POISSON IS NOT APPROPRIATE

---

Poisson fails when:

* Events are dependent
* Events cluster (variance > mean)
* Events are too regular (variance < mean)
* Rate λ is not constant

---

18. BIG PICTURE CONNECTION

---
Bernoulli → Binomial → Poisson

Bernoulli:
Single yes/no event

Binomial:
Count of successes in finite trials

Poisson:
Count of events in continuous time/space via a limit

"""