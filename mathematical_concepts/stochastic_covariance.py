"""
Variance, covariance, and covariance functions

1. Basic definitions

Variance of a random variable X:
Var(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2.
Intuition: average squared deviation from the mean.

Covariance of two random variables X and Y:
Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y].
Intuition: measures linear co-movement. If positive, 
X and Y tend to be above/below their means together;
if negative, when one is above its mean the other tends
to be below.

Correlation:
Corr(X,Y) = Cov(X,Y) / (sqrt(Var(X)) sqrt(Var(Y))).
Range: [-1, 1]. Dimensionless.

2. Simple numeric example (step by step)
   Take paired observations (population view):
   X = [1, 2, 3]
   Y = [2, 4, 5]

Step A — compute means exactly:
mean_X = (1 + 2 + 3) / 3 = 6 / 3 = 2.
mean_Y = (2 + 4 + 5) / 3 = 11 / 3.

Step B — compute deviations and products 
(use fractions for exactness):
For i=1: (x1 - mean_X) = 1 - 2 = -1.
(y1 - mean_Y) = 2 - 11/3 = (6/3 - 11/3) = -5/3.
product1 = (-1) * (-5/3) = 5/3.

For i=2: (x2 - mean_X) = 2 - 2 = 0.
(y2 - mean_Y) = 4 - 11/3 = (12/3 - 11/3) = 1/3.
product2 = 0 * (1/3) = 0.

For i=3: (x3 - mean_X) = 3 - 2 = 1.
(y3 - mean_Y) = 5 - 11/3 = (15/3 - 11/3) = 4/3.
product3 = 1 * (4/3) = 4/3.

Step C — sum products:
sum_products = 5/3 + 0 + 4/3 = (5/3 + 4/3) = 9/3 = 3.

Step D — population covariance (divide by N = 3):
Cov(X,Y) = sum_products / 3 = 3 / 3 = 1.

Step E — population variances:
Var(X) = E[(X-mean_X)^2] = 
((-1)^2 + 0^2 + 1^2) / 3 =
(1 + 0 + 1) / 3 = 2/3 ≈ 0.6666667.
Var(Y) = ((-5/3)^2 + (1/3)^2 + (4/3)^2) / 3
= ((25/9) + (1/9) + (16/9)) / 3
= (42/9) / 3 = (14/3) / 3 = 14/9 ≈ 1.5555556.

Step F — correlation:
Corr(X,Y) = Cov(X,Y) / sqrt(Var(X) Var(Y))
= 1 / sqrt((2/3) * (14/9))
= 1 / sqrt(28/27)
= 1 / (sqrt(28)/sqrt(27))
= sqrt(27) / sqrt(28)
= (sqrt(9*3)) / (sqrt(4*7))
= (3 * sqrt(3)) / (2 * sqrt(7))
Numerically: sqrt(28/27) ≈ sqrt(1.037037) ≈ 1.018370
Corr ≈ 1 / 1.018370 ≈ 0.98198 (approx).

(Notes: above used population formulas dividing by N.
Sample covariance/variance commonly divide by N-1;
adjust if you want sample estimates.)

3. Covariance function for a stochastic process
   Let (X_t)_{t in T} be a stochastic process (index set T could be time R+ or integers).
   Define the covariance function C(s,t) as:
   C(s, t) = Cov(X_s, X_t) = E[(X_s - E[X_s])(X_t - E[X_t])] = E[X_s X_t] - E[X_s] E[X_t].

Important properties of a covariance function C(s,t):

* Symmetry: C(s,t) = C(t,s).
* Positive semidefinite: for any finite set of times t1,...,tn and any real numbers a1,...,an,
  sum_{i,j} a_i a_j C(t_i, t_j) >= 0.
* Variance at time t is the diagonal: Var(X_t) = C(t,t).
* If the process has zero mean (E[X_t]=0 for all t), then C(s,t) = E[X_s X_t].

A common special case: stationary process (strict or weak). For weak stationarity:
mean is constant and covariance depends only on lag h = t - s:
C(s,t) = γ(h) where γ(h) = Cov(X_t, X_{t+h}).

4. Example: covariance function of Brownian motion (standard)
   Definition of standard Brownian motion (B_t)_{t >= 0}:

* B_0 = 0 (almost surely).
* Continuous paths.
* Independent increments: for 0 <= s < t, increment B_t - B_s is independent of the past up to time s.
* Gaussian increments with mean 0 and variance equal to the increment length:
  B_t - B_s ~ Normal(0, t - s).
* In particular Var(B_t) = t and E[B_t] = 0.

Goal: compute C(s,t) = Cov(B_s, B_t) for s, t >= 0.

Step-by-step derivation (assume w.l.o.g. t >= s; if not swap):
Start with Cov(B_s, B_t) = E[B_s B_t] - E[B_s] E[B_t].
Brownian has zero mean, so E[B_s] = 0 and E[B_t] = 0. Thus
Cov(B_s, B_t) = E[B_s B_t].

Use decomposition for t >= s:
B_t = B_s + (B_t - B_s).
Then
E[B_s B_t] = E[B_s (B_s + (B_t - B_s))]
= E[B_s^2] + E[B_s (B_t - B_s)].

By independent increments, B_s is independent of (B_t - B_s). Also E[B_t - B_s] = 0.
Therefore E[B_s (B_t - B_s)] = E[B_s] * E[B_t - B_s] = 0 * 0 = 0.

So E[B_s B_t] = E[B_s^2] = Var(B_s) = s.

Conclusion (for t >= s):
Cov(B_s, B_t) = s = min(s, t).

Because the argument is symmetric, for any s,t >= 0:
Cov(B_s, B_t) = min(s, t).

If the Brownian motion has variance parameter σ^2 (i.e., increments ~ Normal(0, σ^2 (t-s))), then:
Cov(B_s, B_t) = σ^2 min(s, t).

5. Remarks and consequences

* Variance function: Var(B_t) = C(t,t) = min(t,t) = t (for standard Brownian). So variance grows linearly with time.
* Correlation between B_s and B_t (t >= s, standard Brownian):
  Corr(B_s, B_t) = Cov(B_s, B_t) / sqrt(Var(B_s) Var(B_t))
  = s / sqrt(s * t)
  = sqrt(s / t) = sqrt(min(s,t) / max(s,t)).
  Example numeric:
  take s = 2, t = 5:
  Cov(B_2, B_5) = min(2,5) = 2.
  Var(B_2) = 2, Var(B_5) = 5.
  Corr = 2 / sqrt(2 * 5) = 2 / sqrt(10).
  Compute sqrt(10) step by step:
  10 = 100/10 so sqrt(10) ≈ 3.162277660168379...
  Thus Corr ≈ 2 / 3.162277660168379 ≈ 0.6324555320336759.
* The covariance function min(s,t) is continuous and positive semidefinite (it is a valid kernel). It uniquely characterizes the second-order structure of Brownian motion (together with zero mean and Gaussianity it determines the finite-dimensional distributions).
* Interpretation: B_s is perfectly correlated with B_t when s = t (corr = 1), and correlation decreases as the time gap grows; the correlation depends only on the ratio s/t when t >= s.

6. Quick proof that C(s,t)=min(s,t) is positive semidefinite (sketch)
   Let t1 < t2 < ... < tn and coefficients a1,...,an. Consider linear combination L = sum_i a_i B_{t_i}.
   Because Brownian has independent Gaussian increments, L is Gaussian with variance
   Var(L) = sum_{i,j} a_i a_j min(t_i, t_j).
   Variance is always >= 0, so the kernel min(s,t) is positive semidefinite. That shows it's a valid covariance function.

7. Summary (short)

* Variance measures spread: Var(X) = E[X^2] - (E[X])^2.
* Covariance measures linear co-movement: Cov(X,Y) = E[XY] - E[X]E[Y].
* For a stochastic process X_t the covariance function is C(s,t) = Cov(X_s, X_t).
* For standard Brownian motion B_t (B_0=0, independent Gaussian increments, Var(B_t)=t):
  Cov(B_s, B_t) = min(s, t).
  For scaled Brownian with variance parameter σ^2:
  Cov(B_s, B_t) = σ^2 min(s, t).

End.

"""


"""
Correlation shows **how strongly 
and in what direction two variables
move together** in a *linear* sense.


1. **Definition**
   Correlation between X and Y is:
   Corr(X,Y) = Cov(X,Y) / (sqrt(Var(X)) sqrt(Var(Y))).

It is always in the range:
-1 ≤ Corr(X,Y) ≤ 1.

2. **What correlation tells you**

A) **Direction of relationship**

* Positive correlation (> 0):
  When X increases relative to its mean,
  Y tends to increase relative to its mean.
* Negative correlation (< 0):
  When X increases, Y tends to decrease.
* Zero correlation (= 0):
  No linear relationship — knowing X tells you
  nothing about the linear behavior of Y.

B) **Strength of relationship**

* |Corr| close to 1 → strong linear relationship.
* |Corr| close to 0 → weak linear relationship.
* Exactly ±1 → perfect linear relationship.

Note: correlation ONLY measures
*linear* relationships —variables may be
strongly related nonlinearly even if correlation = 0.

---
3. **Examples**
   Example 1: perfect positive correlation
   X = [1, 2, 3]
   Y = [2, 4, 6]
   Here Y = 2X exactly, so Corr(X,Y) = +1.

Example 2: negative correlation
X = [1, 2, 3]
Y = [6, 4, 2]
Here Y decreases exactly when X increases.
Corr(X,Y) = -1.

Example 3: zero correlation but dependent
X uniformly distributed on [-1,1].
Y = X^2.
Y clearly depends on X, but the relationship 
is nonlinear and symmetric.
Corr(X,Y) = 0.

---
4. **Intuition**
   Correlation answers:
   “If X is above its average, 
   is Y likely to be above its average too?”

* If yes → positive correlation.
* If no → negative correlation.
* If there is no consistent pattern
 → correlation near zero.

---
5. **Important facts**

* Correlation does *not* imply causation.
* Correlation is unaffected by scale:
  Corr(X, aY + b) = Corr(X,Y) if a > 0.
* Correlation only depends on covariance shape,
 not magnitude.
 
---

When the relationship between variables is **nonlinear**,
the standard Pearson correlation (Corr(X,Y) = Cov(X,Y)/sqrt(Var(X)Var(Y)))
may **fail to detect dependence**. For example, with Y = X² 
and X symmetric around 0, Pearson correlation is zero even though
Y clearly depends on X.

Here’s a step-by-step guide for measuring correlation in nonlinear cases:

---

### 1) **Spearman rank correlation**

* Idea: instead of raw values, use **ranks** of the data.
* Definition:

  1. Replace each X_i and Y_i by their ranks R(X_i) and R(Y_i) 
  (smallest value → rank 1, etc.)
  2. Compute Pearson correlation of the ranks:
     ρ_s = Corr(R(X), R(Y))
* Properties:

  * Detects **monotonic relationships** (increasing or decreasing)
  even if nonlinear.
  * Value between -1 and 1, like Pearson correlation.

**Example**:
X =      [-2, -1, 0, 1, 2]
Y = X² = [4, 1, 0, 1, 4]

* Pearson correlation: Corr(X,Y) = 0
* Spearman rank correlation: non-zero 
(≈0.9 negative monotonicity if you consider
the decreasing part).

---

### 2) **Kendall tau correlation**

* Another **rank-based measure**:

  * Measures the number of concordant and discordant pairs.
  * Useful for monotonic relationships.
* Like Spearman, it detects monotonicity but is sometimes 
more robust with small samples or ties.

---

### 3) **Mutual Information**

* Captures **any dependency**, linear or nonlinear.
* Definition:
  MI(X,Y) = ∑_x ∑_y p(x,y) log(p(x,y) / (p(x)p(y)))
* Properties:

  * MI = 0 ⇔ X and Y are independent.
  * MI > 0 detects **any type of dependence**, not just linear.
  * Non-negative, but not bounded like correlation. 
  Often normalized to [0,1] for interpretability.

---

### 4) **Distance correlation**

* A newer method:

  * Measures dependence based on distances between points.
  * Zero **iff X and Y are independent**, unlike Pearson.
  * Works for multidimensional data too.

---

### 5) **Summary table**

| Method                    | Detects  | Range  | Notes                                 |
| ------------------------- | -------- | ------ | ------------------------------------- |
| Pearson correlation       | Linear   | [-1,1] | Only linear relationships             |
| Spearman rank correlation | Monotone | [-1,1] | Ranks → good for nonlinear monotone   |
| Kendall tau               | Monotone | [-1,1] | Robust for ties and small samples     |
| Mutual Information        | Any      | [0,∞]  | Needs density estimation; not bounded |
| Distance correlation      | Any      | [0,1]  | Zero only if independent              |

---
Correlation in Brownian motion


1. **Brownian motion properties**
   Let B_t be standard Brownian motion:

* B_0 = 0
* Independent increments: B_t - B_s ~ Normal(0, t-s) for t > s
* E[B_t] = 0, Var(B_t) = t
* Covariance function: Cov(B_s, B_t) = min(s, t)

---
2. **Correlation formula**
   Corr(B_s, B_t) = Cov(B_s, B_t) / sqrt(Var(B_s) * Var(B_t))

Step by step:

* Assume t >= s
* Cov(B_s, B_t) = min(s, t) = s
* Var(B_s) = s, Var(B_t) = t

Corr(B_s, B_t) = s / sqrt(s * t) = sqrt(s / t)

---
3. **Interpretation**

* Correlation depends on ratio s/t
* Perfect correlation at same time: s = t → Corr = 1
* Correlation decreases as t increases relative to s

Example:

* s = 2, t = 5
* Corr(B_2, B_5) = sqrt(2/5) ≈ 0.632

Intuition: earlier value B_s partially explains later
value B_t, but independent increments reduce correlation.

---
4. **Why correlation is linear in BM**

* BM has Gaussian increments, and covariance fully determines dependence
* Correlation is determined by covariance: linear scaling with min(s,t)
* Nonlinear measures (Spearman, mutual information) give similar 
qualitative dependence here because bivariate Gaussian joint distribution

---
5. **Summary**

* Cov(B_s, B_t) = min(s, t)
* Corr(B_s, B_t) = sqrt(min(s,t)/max(s,t))
* Perfect correlation at same time, decreasing as gap increases
* Linear correlation arises naturally from Gaussian property of Brownian motion


"""