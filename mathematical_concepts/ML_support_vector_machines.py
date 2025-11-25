"""
Support Vector Machines (SVM)
---

1. Introduction
Support Vector Machines (SVM) are supervised machine learning algorithms
used for classification and regression tasks. They are particularly effective
for high-dimensional data and problems where the goal is to find a clear 
boundary between different classes.

SVM works by finding the *optimal hyperplane* that best separates
the data points of different classes. This hyperplane is chosen such
that the *margin* (the distance between the nearest data points of each
class and the hyperplane) is maximized.

---
2. Core Concept
The key idea in SVM is to represent data points as vectors 
in an n-dimensional space (where n is the number of features),
and then find the hyperplane that best divides the dataset into
different classes.

* For a 2D dataset, the hyperplane is a line.
* For a 3D dataset, it becomes a plane.
* In higher dimensions, it’s called a hyperplane.

The data points that are closest to the hyperplane and influence
its position and orientation are called support vectors.

Mathematically, for a linear SVM, the decision boundary is defined as:

w · x + b = 0  

where

* w is the weight vector (normal to the hyperplane),
* x is the feature vector, and
* b is the bias term.

A point is classified using the sign of (w · x + b).

---
3. Prerequisites to Learn SVM
Before studying SVM, it helps to understand the following:
* Linear Algebra: Concepts like vectors, dot products, and hyperplanes.
* Calculus: Gradients and optimization.
* Probability & Statistics: For understanding kernels and regularization.
* Machine Learning Basics: Concepts like supervised learning, overfitting,
 and cross-validation.
* Optional but useful: Understanding of convex optimization (since SVMs 
use optimization to find the optimal hyperplane).
---

4. Types of SVM

1. Linear SVM:
   Used when the data is linearly separable.
   Example: Separating two classes with a straight line in 2D space.

2. Non-Linear SVM:
   Used when data cannot be separated by a straight line.
   In this case, SVM uses kernel functions to map the data
    into higher dimensions where a linear separator can be found.

   Common kernel functions:
   * Linear Kernel
   * Polynomial Kernel
   * Radial Basis Function (RBF) Kernel
   * Sigmoid Kernel

---

5. Example

*Linear Example:*
Suppose you have two features: exam score and project score.
You want to classify whether a student will pass or fail.
If the data points (students) can be separated by a straight line,
 SVM finds that line with the largest margin between pass and fail examples.

*Non-linear Example:*
In a case like classifying circular data 
(e.g., inner circle = class A, outer ring = class B),
SVM with an RBF kernel maps the data into higher-dimensional
space where it becomes linearly separable.
---
6. Approach of SVM

Step-by-step process:

1. Input data: Training data with features and labels.
2. Choose kernel: Depending on whether data is linearly separable or not.
3. Train SVM: Find the optimal hyperplane that maximizes the margin between classes.
4. Regularization: Control the trade-off between maximizing margin and
minimizing classification error (using the parameter C).
5. Predict: Use the trained model to classify new data points.

---
7. Applications of SVM

* Text Classification: Spam detection, sentiment analysis.
* Image Classification: Face recognition, handwriting detection.
* Bioinformatics: Cancer classification using gene expression data.
* Finance: Credit scoring, stock market prediction.
* Anomaly Detection: Identifying outliers in security or industrial systems.

---
8. Advantages and Disadvantages

*Advantages:*

* Works well with high-dimensional data.
* Effective when there is a clear margin of separation.
* Memory efficient since only support vectors are used
in the decision function.

*Disadvantages:*

* Not suitable for very large datasets
 (training is computationally expensive).
* Hard to choose the right kernel.
* Performance drops when data is heavily noisy
or overlapping.

---

9. Summary
Support Vector Machines are powerful classification and regression models
that aim to find the best separating hyperplane between data classes.
They rely on geometric intuition, optimization, and kernel tricks to
handle both linear and non-linear problems effectively.
---

Simple Example in Python:

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load data
X, y = datasets.load_iris(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = (
train_test_split(X, y, test_size=0.3, random_state=42))

# Train SVM with RBF kernel
model = SVC(kernel='rbf', C=1.0, gamma='scale')
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
```

This example trains an SVM on the Iris dataset 
and evaluates its accuracy.

---
In short: SVM finds the optimal separating hyperplane with the largest margin,
works in both linear and non-linear spaces (thanks to kernels),
and is widely used in classification tasks across industries.

"""


"""
Linear SVM — mathematical derivation

1. Problem statement (hard-margin linear SVM)
   Given training data 
   {(x_i, y_i)} for i = 1..n, x_i ∈ R^d, y_i ∈ {+1, −1}.
   For the linearly separable case the SVM finds a
   hyperplane w·x + b = 0 that separates the classes and
   maximizes the margin. The margin is 2/||w||,
   so maximizing margin is equivalent to minimizing ||w||^2.

Primal optimization problem (hard margin):
    minimize over (w, b) (1/2) ||w||^2
    subject to y_i (w·x_i + b) ≥ 1 for all i = 1..n

2. Form Lagrangian
   Introduce Lagrange multipliers α_i ≥ 0 (one per constraint).
    The Lagrangian L(w,b,α) is: 
    L(w,b,α) = (1/2) ||w||^2 − sum_{i=1}^n α_i [ y_i (w·x_i + b) − 1 ]

This mixes primal variables (w,b) and dual variables α.

3. Stationarity conditions (partial derivatives = 0)
   Set derivatives of L wrt w and b to zero 
   (these eliminate primal variables in favor of α):

∂L/∂w = 0  =>  w − sum_{i=1}^n α_i y_i x_i = 0
⇒ w = sum_{i=1}^n α_i y_i x_i

∂L/∂b = 0  =>  − sum_{i=1}^n α_i y_i = 0
⇒ sum_{i=1}^n α_i y_i = 0

So the optimal w is a linear combination of training vectors weighted 
by α_i y_i. Only those with α_i > 0 matter (these are the support vectors).

4. Write the dual objective
   Plug w expression back into L and
   remove w,b to get the dual 
   (an optimization in α only). Compute:

L(w,b,α) = (1/2) ||w||^2 − sum_i α_i [ y_i (w·x_i + b) − 1 ]
But after substitution and simplification, the dual becomes

Dual problem (quadratic program):
maximize over α ≥ 0   W(α) = sum_{i=1}^n α_i − (1/2) sum_{i=1}^n sum_{j=1}^n α_i α_j y_i y_j (x_i·x_j)
subject to             sum_{i=1}^n α_i y_i = 0

This is a convex QP in α. The kernelized version will replace x_i·x_j by K(x_i,x_j).

5. KKT conditions and support vectors
   Karush–Kuhn–Tucker (KKT) complementary slackness tells us:
   α_i ≥ 0
   y_i (w·x_i + b) − 1 ≥ 0
   α_i [ y_i (w·x_i + b) − 1 ] = 0  (complementary slackness)

Thus either α_i = 0 (point is not a support vector) or y_i (w·x_i + b) = 1 (point lies exactly on the margin). The points with α_i > 0 are support vectors; they determine w and b.

6. Recover w and b
   Once α* solved:
   w* = sum_i α*_i y_i x_i
   To find b, pick any support vector x_s with 0 < α_s:
   y_s (w*·x_s + b) = 1  ⇒  b = y_s − w*·x_s
   If multiple support vectors exist, average b over them for numerical stability.

7. Prediction
   For a new point x:
   f(x) = sign( w*·x + b ) = sign( sum_i α*_i y_i (x_i·x) + b )

A worked linear example (simple 2-point symmetric case, solved fully)
Take two training points in R^1 (or R^2 but only x-axis matters):
x1 = (1, 0)  with y1 = +1
x2 = (−1, 0) with y2 = −1

These are symmetric across the origin; the obvious separator is the y-axis x=0.

Step A — compute Gram matrix of dot-products:
x1·x1 = 1
x2·x2 = 1
x1·x2 = −1

Dual objective:
maximize α1 + α2 − (1/2)[ α1^2 (1) + α2^2 (1) + 2 α1 α2 (y1 y2 (x1·x2)) ]

Compute the cross term coefficient:
y1 y2 (x1·x2) = (+1)*(−1)*(−1) = +1

So sum in the quadratic term = α1^2 + α2^2 + 2 α1 α2 = (α1 + α2)^2.

Constraint: sum α_i y_i = α1*(+1) + α2*(−1) = α1 − α2 = 0 ⇒ α1 = α2.

Let α = α1 = α2 ≥ 0. Then objective
W(α) = 2α − (1/2) (2α)^2 = 2α − (1/2)*4α^2 = 2α − 2α^2

Maximize wrt α: derivative dW/dα = 2 − 4α = 0 ⇒ α = 1/2. This gives α1 = α2 = 0.5.

Recover w:
w = sum α_i y_i x_i = 0.5*(+1)*(1,0) + 0.5*(−1)*(−1,0)
= 0.5*(1,0) + 0.5*(1,0) = (1,0)

Find b using e.g. x1:
y1 (w·x1 + b) = 1 ⇒ (+1)(1·1 + b) = 1 ⇒ 1 + b = 1 ⇒ b = 0

So decision function is sign((1,0)·x + 0) = sign(x_1); boundary x_1 = 0, as expected. All calculations consistent.

Soft-margin remark
If data is not perfectly separable introduce slack variables ξ_i ≥ 0 and C > 0 and solve:
minimize (1/2)||w||^2 + C sum_i ξ_i
subject to y_i (w·x_i + b) ≥ 1 − ξ_i
This gives box constraints 0 ≤ α_i ≤ C in the dual.

Kernel SVM — how the kernel trick arises (mathematical steps)

1. Motivation
   If data is not linearly separable in input space, map each input x to a feature space via φ: R^d → H (possibly high- or infinite-dimensional). Solve linear SVM in H. But explicitly computing φ and inner-products in H may be expensive or impossible. The kernel trick avoids explicit φ by using K(x, z) = φ(x)·φ(z).

2. Dual in the feature space
   Everything in the dual depends only on dot-products x_i·x_j. Replace x_i·x_j by φ(x_i)·φ(x_j) = K(x_i, x_j). The dual becomes:

   maximize over α ≥ 0   W(α) = sum_i α_i − (1/2) sum_i sum_j α_i α_j y_i y_j K(x_i, x_j)
   subject to              sum_i α_i y_i = 0

3. Classifier using kernels
   After solving for α*, the classifier for a test point x is:
   f(x) = sign( sum_i α*_i y_i K(x_i, x) + b )

Again only support vectors (α*_i > 0) contribute.

4. Common kernels and their feature maps (examples)

* Linear kernel: K(x,z) = x·z  (φ is identity)
* Polynomial degree p with constant c: K(x,z) = (x·z + c)^p (explicit φ has monomials up to degree p)
* Radial Basis Function (RBF, Gaussian): K(x,z) = exp( − ||x−z||^2 / (2σ^2) ). This corresponds to an infinite-dimensional φ.

5. KKT and complementary slackness carry through; α bounded by C for soft-margin versions.

Simple kernel example (polynomial kernel degree 2) — illustrative mapping and kernel equality
Take 2-d inputs x = (x1, x2). Consider polynomial kernel with c = 0 and degree 2:
K(x, z) = (x·z)^2.

Define explicit feature map φ(x) that realizes K:
φ(x) = ( x1^2, sqrt(2) x1 x2, x2^2 )   (a 3-dimensional vector)

Compute φ(x)·φ(z):
= x1^2 z1^2 + 2 x1 x2 z1 z2 + x2^2 z2^2
= (x1 z1 + x2 z2)^2 = (x·z)^2 = K(x,z)

So evaluating K(x,z) is equivalent to taking inner products in feature space without explicitly mapping to φ if you compute (x·z)^2.

Worked kernel toy example (XOR-like separability via degree-2 polynomial)
Consider the four points in R^2:
x1 = (1, 1)  with y1 = −1
x2 = (1, −1) with y2 = +1
x3 = (−1, 1) with y3 = +1
x4 = (−1, −1)with y4 = −1

This is the XOR pattern: label = +1 if the coordinates have opposite signs; −1 if same sign. XOR is not linearly separable in R^2 but becomes separable in φ(x) for degree-2 polynomial because φ(x) = (x1^2, √2 x1 x2, x2^2) maps all four points to:
φ(1,1)   = (1, √2, 1)
φ(1,−1)  = (1, −√2, 1)
φ(−1,1)  = (1, −√2, 1)
φ(−1,−1) = (1, √2, 1)

Observe: φ(1,1) = φ(−1,−1) and φ(1,−1) = φ(−1,1). In φ-space the two classes separate along the middle coordinate sign (the √2 x1 x2 component): the class +1 points have the middle coordinate negative; class −1 points have it positive. So a linear separator in φ-space that depends only on the second component (√2 x1 x2) suffices.

We can show a separating hyperplane in φ-space:
choose w_φ = (0, w2, 0) with w2 < 0, and b = 0.
Then w_φ·φ(x) = w2 * (√2 x1 x2). For x with x1 x2 = +1 (same signs), √2 x1 x2 = ±√2; for x1 x2 = −1 (opposite signs), the sign flips. So we can classify XOR via this linear rule in φ-space. Using kernel K(x,z) = (x·z)^2 we never compute φ explicitly in practice; we compute K values and solve the dual.

Dual with kernel (symbolic)
Dual objective becomes:
maximize α sum_i α_i − (1/2) sum_{i,j} α_i α_j y_i y_j K(x_i, x_j)
subject to sum_i α_i y_i = 0, α_i ≥ 0 (and ≤ C if soft-margin).
Solve this QP numerically (e.g., with any QP solver or libsvm/scikit-learn). The important point is: every occurrence of inner-product x_i·x_j is replaced by K(x_i,x_j). The solution α* then yields classifier:
f(x) = sign( sum_i α*_i y_i K(x_i, x) + b )

Interpretation & insights (why kernel trick is powerful)
• The primal SVM in feature space might be an enormous or infinite-dimensional optimization; the dual depends only on inner products, so replacing inner products with kernels avoids explicit high-dimensional computations.
• Support vectors are those training points that are “critical” — they lie on or inside the margin. Complexity at prediction time depends on number of support vectors, not original dimensionality.
• Kernel choice encodes prior assumptions about which functions separate the classes (e.g., RBF gives very flexible non-linear boundaries; polynomial gives specific polynomial decision boundaries).

KKT conditions, geometric margin, and complementary slackness — recap mathematically
KKT conditions for soft-margin (primal variables w,b,ξ and dual α, μ for ξ constraints):

* Stationarity: w = sum_i α_i y_i x_i
* sum_i α_i y_i = 0
* α_i ≥ 0, μ_i ≥ 0, ξ_i ≥ 0
* primal feasibility: y_i (w·x_i + b) ≥ 1 − ξ_i
* complementary slackness: α_i [ y_i (w·x_i + b) − 1 + ξ_i ] = 0
* α_i (C − α_i) = 0 effectively in box-constrained dual (0 ≤ α_i ≤ C)
  Meaning: α_i = 0 ⇒ point outside margin and not an SV; 0 < α_i < C ⇒ point on the margin (hard margin active); α_i = C ⇒ point inside margin or misclassified (slack active).

Practical notes for application
• Solve the dual QP using standard solvers; libraries (libsvm, scikit-learn) use efficient SMO-like algorithms.
• Scale features (standardize) before SVM training — SVM is sensitive to scale because it uses dot-products and distances.
• Tune kernel hyperparameters (e.g., C, γ for RBF, degree for polynomial) with cross-validation.
• For very large datasets, linear SVM variants (e.g., LIBLINEAR) or approximate methods are used because solving quadratic programs with n large is expensive.

Concise summary of math flow

1. Define primal (margin maximization with constraints).
2. Form Lagrangian and compute stationarity → w expressed in α.
3. Substitute back → dual QP in α (depends only on inner products x_i·x_j).
4. Solve dual (with kernel replace inner products by K).
5. Recover w (if needed) and b (from KKT/any support vector).
6. Predict using kernel-sum form: sign( sum_i α_i y_i K(x_i, x) + b ).

If you want, I can:
• Produce a fully worked numeric kernel QP for the XOR toy example (show the K matrix, write the QP, solve it symbolically for α if feasible), or
• Provide step-by-step derivation of the soft-margin dual (including the box constraints 0 ≤ α_i ≤ C), or
• Show how hinge-loss formulation relates to soft-margin SVM and its primal unconstrained optimization with regularization.

Tell me which follow-up you prefer and I’ll continue with raw-text step-by-step numeric calculations.

"""


"""
Understanding w·x + b = 0

1) Starting point: the familiar 2D line
  - In two dimensions, a line is commonly written as:
        y = a x + b
    where:
        a = slope (how steep the line is)
        b = y-intercept (where the line crosses the y-axis)
  - This formula is intuitive when you think of
    x as the input and y as the output.
  - But it only works for 2D (x, y) and
    expresses y explicitly in terms of x.

2) Limitations of y = ax + b
  - It assumes one variable is dependent (y)
    and the other is independent (x).
  - It cannot describe vertical lines like
    x = constant, because that would require infinite slope (a → ∞).
  - It does not generalize naturally to higher dimensions.
  - For example, in 3D (x, y, z), there is
    no single dependent variable — a plane involves all three coordinates.

3) General geometric form
  - The general equation of a line (in 2D) or 
  a plane (in 3D) is based on the **dot product**.
  - For any dimension, the equation
        w · x + b = 0
    defines a **hyperplane**.
    - In 2D, this represents a line.
    - In 3D, this represents a plane.
    - In nD, this represents an 
    (n−1)-dimensional flat surface (a hyperplane).

4) Understanding the notation
  - w = (w₁, w₂, ..., wₙ) is a vector called the **normal vector** of the hyperplane.
    It points perpendicular to the surface.
  - x = (x₁, x₂, ..., xₙ) is a point (or variable) in the same space.
  - The dot product w·x = w₁x₁ + w₂x₂ + ... + wₙxₙ gives a scalar.
  - b is a bias or offset term (it shifts the hyperplane away from the origin).

5) Why w·x + b = 0 defines a hyperplane
  - The equation says: all points x that make w·x + b = 0 lie on the surface.
  - For points x where w·x + b > 0, they lie on one side of the plane.
  - For points where w·x + b < 0, they lie on the opposite side.
  - The vector w determines the **orientation** of the plane.
  - The value of b determines the **position** (shift from origin).

6) How it relates to y = a x + b in 2D
  - Let’s write w = (w₁, w₂) and x = (x₁, x₂) = (x, y).
  - Then the equation w·x + b = 0 becomes:
        w₁x + w₂y + b = 0
  - Solving for y gives:
        y = -(w₁/w₂)x - (b/w₂)
  - This is exactly the same as y = a x + b form, where:
        a = -w₁/w₂   and   intercept = -b/w₂
  - So w·x + b = 0 is a more **general** and **symmetric** representation.
  - It can easily handle vertical lines (when w₂ = 0)
  and higher-dimensional analogues.

7) Geometric interpretation
  - The shortest distance from the origin to the hyperplane w·x + b = 0 is |b| / ||w||.
  - The normal vector w shows the direction perpendicular to the plane.
  - Every point x on the plane satisfies the same dot-product relationship with w.

8) Why this matters in machine learning and geometry
  - In ML, equations like w·x + b = 0 describe 
  decision boundaries in classifiers (e.g., logistic regression, SVMs).
  - The sign of (w·x + b) tells which class a point belongs to:
        +1 side if w·x + b > 0
        -1 side if w·x + b < 0
  - It’s powerful because it works in any number of dimensions without special cases.

Summary:
  - y = ax + b is a special case of w·x + b = 0 in 2D.
  - w·x + b = 0 generalizes the idea of a line to any number of dimensions.
  - It defines a hyperplane using vector geometry rather than slope–intercept form.
 
"""