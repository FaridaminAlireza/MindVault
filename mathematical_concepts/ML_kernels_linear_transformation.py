"""
1. What precisely is a linear combination of feature vectors 

A feature vector is a vector of numbers representing 
an object. A linear combination of feature vectors means 
you multiply each vector by a scalar and then add the results.

Given feature vectors x1, x2, …, xn and scalars a1, …, an,
a linear combination is:
v = a1 x1 + a2 x2 + … + an xn.

Example A (house features):
xA = [100, 3, 10]
xB = [80, 2, 5]

Linear combination: 2 xA + 3 xB
2 xA = [200, 6, 20]
3 xB = [240, 6, 15]
Sum = [440, 12, 35]

Example B (2D vectors):
v1 = [1, 2]
v2 = [3, 4]
Linear combination: 0.5 v1 − 2 v2
0.5 v1 = [0.5, 1]
−2 v2 = [-6, -8]
Sum = [-5.5, -7]

A linear combination gives another vector in
the same space and represents any vector you
can make from scaling and adding the originals.
---

2. Importance of linear combinations in
quadratic forms for the dot-product kernel

The dot-product kernel is simply k(xi, xj) = xi · xj.

If you form a linear combination
v = a1 x1 + a2 x2 + … + an xn,
then its squared length is:
v · v = sum over i,j of ai aj (xi · xj).
(The double summation is similar to a nested
'for loop' over n=1..n and j=1..n  
with the statment  ai aj (xi.xj))


Define the kernel (Gram) matrix K where K[i,j] = xi · xj.
Then the squared length of the linear combination is:
v · v = a^T K a.

This is a quadratic form.
It shows:

* how the lengths of linear combinations depend
 on all pairwise similarities between feature vectors,
* why kernels must produce positive semidefinite matrices 
(so that a^T K a is always >= 0),
* and how kernel methods compute inner products without
explicitly constructing the transformed features.

Numeric illustration:
x1 = [1, 2], x2 = [3, 4]
Kernel matrix K =
[  5  11
  11  25 ]

Take a = [2, 1]
Compute Ka = [21, 47]
Compute a^T (Ka) = 2*21 + 1*47 = 89

Direct check: 2 x1 + 1 x2 = [5, 8];
squared length = 5^2 + 8^2 = 89.

---
A kernel matrix made from pairwise dot products
is always positive semi-definite.
This means: 
for any vector of coefficients a = [a1, a2, ... , an],
the value a^T K a is always greater than or equal to zero.

Reason:
A kernel matrix K is defined by K[i,j] = xi · xj,
where xi are real vectors. Take any coefficients
a1, ..., an and form the linear combination:
v = a1 x1 + a2 x2 + ... + an xn.

Now compute:
a^T K a = sum over i,j of ai aj (xi · xj).

But this is exactly equal to:
v · v

And v · v is the dot product of a vector with itself.
A vector dotted with itself is always non-negative,
because: v · v = (length of v)^2.

Since squared length can never be negative,
we have:
a^T K a = v · v >= 0
for all choices of a.

Therefore, every kernel matrix formed from 
dot products is automatically positive semi-definite.
---

K(x, z) = ⟨φ(x), φ(z)⟩_H  — Hilbert space and feature map

A kernel can be written as:
K(x, z) = inner product of φ(x) and φ(z) in a Hilbert space H.

What this means:

1. Feature map φ
   The function φ maps the original input x into a
   (possibly very high-dimensional) feature space.
   Example:
   If x is a real number, and the kernel is the 
   polynomial kernel K(x,z) = (1 + xz)^2,
   then one possible feature map is:
   φ(x) = [1, sqrt(2) x, x^2].

Often φ is very large or infinite-dimensional,
and we never compute it directly.
Instead, we compute K(x,z), which gives the same
result as the inner product of φ(x) and φ(z).

2. Hilbert space H
   A Hilbert space is basically a vector space with:

* an inner product (to measure angles, dot-products, projections),
* completeness (limits of Cauchy sequences stay inside the space).

Euclidean space R^n is a simple example of a Hilbert space.
But Hilbert spaces can be infinite-dimensional, such as 
spaces of functions.

The point:
φ(x) does NOT have to live in regular finite-dimensional R^n.
It can live in a huge or infinite-dimensional Hilbert space H.
The kernel trick lets us work *as if* we are doing inner products
in that large space without ever leaving the original input space.

3. Why write K this way
   The expression
   K(x, z) = ⟨φ(x), φ(z)⟩_H
   means the kernel computes the similarity 
   between x and z in the feature space.
   If we tried to compute φ(x) explicitly,
   it might be very expensive or impossible.
   But computing K(x,z) directly is easy.

4. Why this matters for SVMs and kernel methods
   When training an SVM (or any kernel machine),
   the algorithm needs only inner products between feature vectors.
   Because those inner products equal K(x,z), we never compute φ(x)
   explicitly.
   This is the “kernel trick.”

5. Positive semi-definiteness
   The reason every valid kernel must be positive semi-definite is that:
   K(x, z) is literally an inner product in some Hilbert space.
   Inner products automatically generate positive semi-definite Gram matrices.

6. Example with numbers
   Let x = 2, z = 3, and 
   use the polynomial kernel K(x,z) = (1 + xz)^2.
K(x,z) = (1 + xz)^2 = 1 + x^2 z^2 + 2 xz
With the feature map φ(x) = [1, sqrt(2)*x, x^2], we have:
φ(2) = [1, 2√2, 4]
φ(3) = [1, 3√2, 9]

Compute the inner product:
1*1 + (2√2)*(3√2) + 4*9
= 1 + (2*3*2) + 36
= 1 + 12 + 36
= 49

And indeed:
K(2,3) = (1 + 2*3)^2 = (1 + 6)^2 = 49

So K(x, z) matches the inner product 
in the feature space without needing
to compute φ(x) explicitly.

---
every valid kernel is *equivalent* to
a dot product in some feature space,
but not always in the original space

Is a kernel always a dot product of its pairs?

A kernel K(x, z) does not always look like 
a dot product in the original input space.
However, if K is a valid (Mercer) kernel, then:

K(x, z) = ⟨φ(x), φ(z)⟩

for some feature map φ into some Hilbert space.

This means:

1. A kernel may not look like a dot product.
   Examples:
   K(x,z) = exp( -||x - z||^2 / (2σ^2) )   (RBF kernel)
   K(x,z) = min(x, z)                      (Brownian kernel)
   K(x,z) = (1 + x · z)^d                  (polynomial kernel)

None of these look like dot products in the original space.

2. But every *valid* kernel is always a dot product in some
 (possibly huge or infinite-dimensional) Hilbert space.
   There always exists a feature map φ such that:
   K(x,z) = ⟨φ(x), φ(z)⟩_H.

3. The feature map φ is often impossible to write down.
   For the RBF kernel, φ(x) is infinite-dimensional.
   The kernel trick avoids explicitly computing φ.

4. So in brief
* In the input space: not always a dot product.
* In some transformed feature space: always a dot product.

If a function cannot be written as a dot product in 
some Hilbert space, then it is not a valid kernel 
and will not produce a positive semi-definite Gram matrix.

---
A Hilbert space is not the dot product itself.
A Hilbert space is the *type of space* where 
those transformed features live.

More precisely:

1. A Hilbert space is a vector space 
with an inner product and completeness.
It generalizes Euclidean space (like R^n),
but can also be infinite-dimensional.

2. When we talk about kernels, we say there
exists a feature map φ(x) that sends x into
some Hilbert space H.

3. In that Hilbert space, we can compute an inner product:
   ⟨φ(x), φ(z)⟩_H

4. The kernel is defined to be exactly that inner product:
   K(x, z) = ⟨φ(x), φ(z)⟩_H

So the Hilbert space is:

* the space containing φ(x), φ(z), etc.
* the space where the dot product (inner product) is defined.

You can think of it like this:

Original data x lives in input space X.
We transform x → φ(x), which lives in a Hilbert space H.
In H, we can take inner products.
The kernel lets us compute that inner product without
constructing φ(x).

So:
A Hilbert space is not the dot product.
It is the environment (the mathematical space) in which
dot products of transformed features are defined.

---
Example: Polynomial kernel of degree 2
Kernel definition:
K(x, z) = (1 + x · z)^2

This kernel is a valid Mercer kernel and has
a finite-dimensional feature map φ that makes
K(x, z) equal to an inner product ⟨φ(x), φ(z)⟩
in a feature space.

1. Feature map for scalar inputs (x is a real number)
   If x ∈ R (a scalar), one valid feature map is:
   φ(x) = [1, sqrt(2) x, x^2]

Check algebraically that the inner product equals the kernel:
⟨φ(x), φ(z)⟩ = 1*1 + (sqrt(2) x)(sqrt(2) z) + x^2 z^2
= 1 + 2 x z + x^2 z^2
= (1 + x z)^2
So K(x, z) = ⟨φ(x), φ(z)⟩.

Numeric scalar example:
Let x = 2, z = 3.
φ(2) = [1, 2√2, 4]
φ(3) = [1, 3√2, 9]
Inner product: 1*1 + (2√2)*(3√2) + 4*9 =
 1 + (2*3*2) + 36 = 1 + 12 + 36 = 49.
Kernel directly: (1 + 2*3)^2 = (1 + 6)^2 = 49.
They match.

2. Feature map for 2D vectors (x = [x1, x2])
   For x ∈ R^2, expand (1 + x·z)^2 = 1 + 2(x·z) + (x·z)^2.
   A convenient explicit feature map φ(x) that
   reproduces this (one correct choice) is:
   φ(x) = 
   [1, sqrt(2) x1, sqrt(2) x2, x1^2, sqrt(2) x1 x2, x2^2 ]
   This is a 6-dimensional vector. The sqrt(2) factors ensure
   cross-terms combine correctly in the inner product.

Check structure: when you take ⟨φ(x), φ(z)⟩ you get
1 + 2(x1 z1 + x2 z2) + (x1^2 z1^2 + 2 x1 x2 z1 z2 + x2^2 z2^2)
which equals (1 + x·z)^2.

Numeric 2D example:
Let x = [1, 2], z = [3, 4].

Compute φ(x):
φ(x) 
= [1, sqrt(2)*1, sqrt(2)*2, 1^2, sqrt(2)*1*2, 2^2 ]
= [1, √2, 2√2, 1, 2√2, 4]

Compute φ(z):
φ(z) 
= [1, sqrt(2)*3, sqrt(2)*4, 3^2, sqrt(2)*3*4, 4^2 ]
= [1, 3√2, 4√2, 9, 12√2, 16]

Inner product ⟨φ(x), φ(z)⟩ =
1*1 + (√2)*(3√2) + (2√2)*(4√2) + 1*9 + (2√2)*(12√2) + 4*16
= 1 + 3*2 + (2*4)*2 + 9 + (2*12)*2 + 64
= 1 + 6 + 16 + 9 + 48 + 64
= 144

Direct kernel:
x·z = 1*3 + 2*4 = 3 + 8 = 11
K(x,z) = (1 + 11)^2 = 12^2 = 144
They match.

3. Gram matrix for a small dataset 
and positive semidefiniteness

   Take three points in 
   R^2: p1 = [1,2], p2 = [3,4], p3 = [0,1].
   Compute pairwise kernels 
   K_ij = (1 + pi · pj)^2 to build Gram matrix K.

Example computations (showing the process):

* p1·p1 = 1*1 + 2*2 = 5 → K11 = (1 + 5)^2 = 36
* p1·p2 = 1*3 + 2*4 = 11 → K12 = (1 + 11)^2 = 144
* p1·p3 = 1*0 + 2*1 = 2 → K13 = (1 + 2)^2 = 9
* p2·p2 = 3*3 + 4*4 = 25 → K22 = (1 + 25)^2 = 676
* p2·p3 = 3*0 + 4*1 = 4 → K23 = (1 + 4)^2 = 25
* p3·p3 = 0*0 + 1*1 = 1 → K33 = (1 + 1)^2 = 4

Gram matrix
K = [ 36   144   9
      144  676   25
      9    25    4 ]

This K is positive semidefinite

4. (summary)
* The polynomial kernel K(x,z) = (1 + x·z)^2 is exactly
an inner product ⟨φ(x), φ(z)⟩ in a finite-dimensional feature space.
* We can either compute K directly (cheap) or map to φ(x) and
compute an explicit dot product (explicit, sometimes more costly).
* Kernel methods use K directly (kernel trick). For polynomial kernels
of finite degree you can write φ explicitly; for kernels like RBF 
you cannot (it's infinite-dimensional), yet the kernel still represents
an inner product in some Hilbert space.

---
Brownian kernel and RBF (Gaussian) kernel — 
definitions, examples, proofs they are inner products 
(positive semidefinite), and applications

Applications of Brownian kernel:

* Modeling stochastic processes with Brownian motion covariance 
(Gaussian process models of random walk / integrated noise).
* Nonparametric regression when the prior on functions is a Brownian motion 
(e.g., smoothing splines connection).
* Time-series / functional data contexts where cumulative or
 integrated behavior is natural.

---
RBF (Radial Basis Function) / Gaussian kernel

Definition (Euclidean input x, z in R^d):
K_G(x, z) = exp( - ||x - z||^2 / (2 σ^2) )
Equivalent common form uses parameter
 γ = 1/(2σ^2): K(x,z) = exp( -γ ||x-z||^2 ).

Example (numeric, 2D points):
Let x1 = [1,2], x2 = [3,4], choose σ = 1 (so 2σ^2 = 2).
Compute squared distance: ||x1 - x2||^2 = (1-3)^2 + (2-4)^2 = 4 + 4 = 8.
K_G(x1,x2) = exp( -8 / 2 ) = exp(-4) ≈ 0.018315.

Applications of RBF kernel:

* Support Vector Machines with RBF kernel:
 flexible nonlinear boundary, widely used default kernel.
* Gaussian Process regression with squared-exponential kernel:
 smooth function priors, interpolation, uncertainty quantification.
* Kernel density estimation variants, kernel PCA, manifold learning — 
 generally anywhere flexible, infinitely-smooth similarity is desirable.
* RBF is universal: with appropriate parameters it can approximate any
 continuous function on compact sets (powerful for nonparametric learning).

Comparison, feature maps, and intuitive differences

Feature maps (explicit):
* Brownian kernel: finite,
 explicit feature map φ(t) = 1_{[0,t]} in L^2([0,∞)).
Feature vectors are “cumulative indicators”;
 the RKHS functions generated are integrated / non-smooth 
 (Brownian sample paths are nowhere differentiable).
* RBF kernel: feature map is infinite-dimensional.
One constructive viewpoint is random Fourier features:
 φ(x) = (sqrt(2) cos(w·x + b))_w as a function indexed
 by w with w drawn from Gaussian spectral density.
 Another viewpoint: φ(x) = k(x, ·) in the RKHS 
 (function-valued feature).

Smoothness and behavior:
* Brownian kernel produces functions with roughness
 like Brownian motion (not differentiable). 
 It encodes cumulative / integrated structure and grows with time.
* RBF kernel produces very smooth functions 
(infinitely differentiable) and enforces local,
 rapidly decaying similarity with distance.


Short worked examples summary (raw numbers)

Brownian example:
Times: t1=1, t2=2
K_B = [ [1, 1],
[1, 2] ]
For any a = [a1, a2], a^T K_B a =
 E[(a1 B_1 + a2 B_2)^2] >=0.

RBF example:
Points x1=[1,2], x2=[3,4], σ=1
||x1-x2||^2 = 8
K_G(x1,x2) = exp(-8/2) = exp(-4) ≈ 0.018315.
Gram matrix with self-similarity K_G(x1,x1)=1, K_G(x2,x2)=1:
K = [ [1, 0.018315],
[0.018315, 1] ]
This matrix is PSD (eigenvalues 1±0.018315 positive).
"""
