"""
covariance and covariance matrices

────────────────────────────────────────
COVARIANCE — WHAT AND WHY
────────────────────────────────────────

Covariance measures 
how two random variables move together.

Let X and Y be random variables.
The **population covariance** is:

Cov(X, Y) = E[(X − μ_X)(Y − μ_Y)]

Where:

* μ_X = E[X] (mean of X)
* μ_Y = E[Y] (mean of Y)

Interpretation:

* Cov > 0 → 
When X is above average, 
Y tends to be above average 
→ positive relationship

* Cov < 0 → When X is above average,
Y tends to be below average →
negative relationship

* Cov ≈ 0 → No linear relationship

Unit:

* The units of covariance are 
the product of units of X and Y 
(e.g. meters * seconds), so 
raw covariance can be difficult
to interpret directly.

────────────────────────────────────────
DERIVATION OF SAMPLE COVARIANCE FORMULA
────────────────────────────────────────

Given n paired samples (x_i , y_i) for i = 1..n:

We estimate covariance using:

Cov(X, Y) ≈ (1 / (n − 1)) * Σ[(x_i − x̄)(y_i − ȳ)]

Why (n − 1) instead of n?

* Using n → biased estimator for finite samples
* (n − 1) corrects this via 
Bessel’s correction to 
keep expected covariance unbiased

Mean subtraction is crucial because:

* It centers the data
* Measures co-variability from 
the "average behavior" 
rather than absolute values

────────────────────────────────────────
SELF-COVARIANCE = VARIANCE
────────────────────────────────────────

Cov(X, X) = Var(X)

Thus covariance generalizes variance.

────────────────────────────────────────
COVARIANCE MATRIX
────────────────────────────────────────

For a vector random variable:

X = [X₁, X₂, …, X_d]^T

The covariance matrix Σ is:

Σ = E[(X − μ)(X − μ)^T]

Expanding produces a d×d matrix:

Σ =
[ Cov(X₁,X₁)  Cov(X₁,X₂)  …  Cov(X₁,X_d)
Cov(X₂,X₁)  Cov(X₂,X₂)  …  Cov(X₂,X_d)
⋮               ⋮           ⋱     ⋮
Cov(X_d,X₁)  Cov(X_d,X₂)  …  Cov(X_d,X_d) ]

Properties:

* Σ is symmetric → Cov(X_i, X_j) = Cov(X_j, X_i)
* Σ is positive semidefinite
* Diagonal entries = variances
* Off-diagonal entries = cross-covariances

────────────────────────────────────────
INSIGHTFUL NUMERICAL EXAMPLE
────────────────────────────────────────

Suppose we measure 
height (cm) and weight (kg) for 3 people:

X = height = [170, 180, 160]
Y = weight = [65, 80, 60]

Step 1: Means

x̄ = (170 + 180 + 160) / 3 = 170
ȳ = (65 + 80 + 60) / 3 = 68.33̅

Step 2: Deviations

i | x_i | x_i − x̄ | y_i | y_i − ȳ | (x_i−x̄)(y_i−ȳ)
---+-----+----------+-----+---------+----------------
1 | 170 |    0     |  65 |  -3.33  |  0
2 | 180 |   10     |  80 |  11.67  | 116.7
3 | 160 |  -10     |  60 |  -8.33  | 83.3

Sum of cross-products = 200

Step 3: Sample covariance

Cov(X, Y) = 200 / (3 − 1) = 100

→ Positive covariance → 
Taller people weigh more in this sample

Step 4: 
We also need variances for the matrix

Var(X) = Σ(x_i − x̄)² / (n−1)
= (0² + 10² + (-10)²) / 2
= 200 / 2 = 100

Var(Y) = Σ(y_i − ȳ)² / (n−1)
= ((-3.33)² + (11.67)² + (-8.33)²) / 2
≈ 216.67 / 2 = 108.33

Step 5: Covariance matrix

Σ =
[ 100      100
100   108.33 ]

Interpretation:

* Diagonal: height variance = 100,
 weight variance = 108.33
* Off-diagonals: covariance = 100 →
linear positive relationship

────────────────────────────────────────
KEY INTUITIONS AT A GLANCE
────────────────────────────────────────

| Term                 | Why it exists                            |
| -------------------- | ---------------------------------------- |
| (x_i − x̄)(y_i − ȳ)  | Measures co-movement from average        |
| Sum of those terms   | Aggregates relationships from each point |
| Divide by (n − 1)    | Makes unbiased estimator                 |
| Matrix form          | Stores all pairwise covariance relations |
| Diagonal = variances | Each variable with itself                |
| Symmetry of matrix   | Cov(X,Y) must equal Cov(Y,X)             |

────────────────────────────────────────
SHORT TAKEAWAY
────────────────────────────────────────
Covariance quantifies 
how variables move together.
Covariance matrices extend that idea 
to many variables, forming the foundation of:

* Principal Component Analysis (PCA)
* Multivariate Gaussian distributions
* Portfolio optimization
* State estimation (Kalman Filters)
* Machine learning representations

"""

"""
Expansion of Σ = E[(X − μ)(X − μ)^T], an algebraic derivation


1. Algebraic expansion (symbolic)
   Let X be a d-dimensional random vector
   X = [X1, X2, …, Xd]^T
   and μ = E[X] = [μ1, μ2, …, μd]^T.

Form the centered vector:
X − μ = [X1 − μ1, X2 − μ2, …, Xd − μd]^T.

The outer product (X − μ)(X − μ)^T is the d×d matrix whose (i,j) entry is
(X − μ)_i · (X − μ)_j = (Xi − μi)(Xj − μj).

(Outer product:
The outer product of two vectors is 
a matrix formed by multiplying each element
of one vector by each element of the other vector.
More formally:
If a is an m×1 column vector and
b is an n×1 column vector, 
then their outer product is:
a bᵀ = an m×n matrix where the (i,j) entry is:
(a bᵀ)_{ij} = a_i · b_j)
Intuition:
It captures pairwise relationships between 
components of two vectors — which is why 
covariance matrices are built 
from outer products of centered data vectors.)



Taking expectation elementwise:
Σ = E[(X − μ)(X − μ)^T]
means the (i,j) entry of Σ is
Σ_{ij} = E[(Xi − μi)(Xj − μj)].

But by definition that scalar is
exactly Cov(Xi, Xj). Therefore
Σ_{ij} = Cov(Xi, Xj).

So Σ = [ Cov(Xi, Xj) ]_{i=1..d, j=1..d}.

Properties visible from this expansion:

* Symmetry: 
Σ_{ij} = E[(Xi−μi)(Xj−μj)] = 
         E[(Xj−μj)(Xi−μi)] = Σ_{ji}.
* Diagonal entries: 
Σ_{ii} = E[(Xi−μi)^2] = Var(Xi).
* Positive semidefinite: for any vector a,
 a^T Σ a = E[(a^T (X−μ))^2] ≥ 0.

2. Concrete numeric example (full arithmetic)
Two-dimensional example (d = 2).
 Three samples (n = 3).

Samples (each x_k is a column vector):
x1 = [170, 65]^T
x2 = [180, 80]^T
x3 = [160, 60]^T

Compute the sample mean μ (componentwise):
μ1 = mean of first components (heights) =
 (170 + 180 + 160) / 3 = 510 / 3 = 170.
μ2 = mean of second components (weights) = 
(65 + 80 + 60) / 3 = 205 / 3. 
(Keep exact fraction: 205/3.)

So
μ = [170, 205/3]^T.

Compute centered vectors s_k = x_k − μ:

s1 = x1 − μ = [170 − 170, 65 − 205/3]^T
= [0,  (195/3 − 205/3)]^T
= [0, −10/3]^T.

s2 = x2 − μ = [180 − 170, 80 − 205/3]^T
= [10, (240/3 − 205/3)]^T
= [10, 35/3]^T.

s3 = x3 − μ = [160 − 170, 60 − 205/3]^T
= [−10, (180/3 − 205/3)]^T
= [−10, −25/3]^T.

Form the outer products 
s_k s_k^T for each sample (2×2 matrices).
Compute exactly:

s1 s1^T =
[ 0 * 0,     0 * (−10/3)
(−10/3)*0, (−10/3)*(−10/3) ]

= [ 0,        0
0,      100/9 ].
(Explanation: (−10/3)^2 = 100/9.)

s2 s2^T =
[ 10 * 10,      10 * (35/3)
(35/3) * 10,  (35/3)*(35/3) ]

= [ 100,       350/3
350/3,    1225/9 ].
(Explanation: 35^2 = 1225, so (35/3)^2 = 1225/9.)

s3 s3^T =
[ (−10)*(−10),  (−10)*(−25/3)
(−25/3)*(−10), (−25/3)*(−25/3) ]

= [ 100,        250/3
250/3,     625/9 ].
(Explanation: (−25)^2 = 625, 
so (−25/3)^2 = 625/9. 
Note signs: products are positive here.)

Sum these outer-product matrices elementwise:

Sum_{k=1..3} s_k s_k^T =
[ 0 + 100 + 100,          0 + 350/3 + 250/3
0 + 350/3 + 250/3,     100/9 + 1225/9 + 625/9 ].

Compute each entry:

(1,1): 0 + 100 + 100 = 200.
(1,2) and (2,1): 0 + 350/3 + 250/3 =
 (350 + 250) / 3 = 600 / 3 = 200.

(2,2): (100 + 1225 + 625) / 9 =
 1950 / 9 = 650 / 3.  
 (Because 1950/9 simplifies dividing 
 numerator and denominator by 3 → 650/3.)

So the sum matrix is:
[ 200,   200
200, 1950/9 ].
(And 1950/9 = 650/3 ≈ 216.6666667.)

Now apply expectation / averaging.
Two common conventions:

A) Population covariance formula (using 1/n):
Σ_population_estimate = 
(1/n) * Σ_{k=1..n} s_k s_k^T = (1/3) * (sum matrix).

Divide each entry by 3:

Σ_population_estimate =
[ 200/3,   200/3
200/3,  (1950/9) / 3 ].

Simplify (1950/9)/3 = 1950/27 = 650/9.

So
Σ_population_estimate =
[ 200/3,   200/3
200/3,   650/9 ].

Numerical approximations:
200/3 ≈ 66.6666667
650/9 ≈ 72.2222222

B) Sample (unbiased) 
covariance formula (using 1/(n−1)):
Σ_sample_unbiased = 
(1/(n − 1)) * Σ_{k=1..n} s_k s_k^T =
(1/2) * (sum matrix).

Divide each entry by 2:

Σ_sample_unbiased =
[ 200/2,  200/2
200/2, (1950/9) / 2 ].

Simplify:
200/2 = 100.
(1950/9)/2 = 1950/18 =
 325/3 ≈ 108.3333333.

So
Σ_sample_unbiased =
[ 100,    100
100,   325/3 ].

Numerical approximations:
100.0
325/3 ≈ 108.3333333

Verification with scalar formula:

* Cov(sample X, sample Y) (unbiased) =
sum_i (x_i − x̄)(y_i − ȳ) / (n − 1) =
200 / 2 = 100. (Matches off-diagonal.)
* Var(X) = 
200 / 2 = 100.
 (Matches Σ_{11}.)
* Var(Y) = 
(1950/9) / 2 = 325/3 ≈ 108.3333.
 (Matches Σ_{22}.)

3. Summary of connection to the symbolic expansion
* The outer product (X − μ)(X − μ)^T has
 (i,j) entry (Xi − μi)(Xj − μj).
* Taking expectation E[·] converts 
each entry to E[(Xi − μi)(Xj − μj)], 
which is exactly Cov(Xi, Xj).
* With finite samples, replacing expectation 
by an empirical average over samples gives 
either the population empirical covariance (1/n)
or the unbiased sample covariance (1/(n−1))
depending on convention. The numeric example
above demonstrates both.

"""