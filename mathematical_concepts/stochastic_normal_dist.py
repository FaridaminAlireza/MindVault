"""
Step 1: What is the Gaussian (Normal) Distribution?

The Gaussian distribution is a probability distribution:

f(x) = (1 / sqrt(2πσ^2)) * exp(-(x - μ)^2 / (2σ^2))

* μ = mean (center)
* σ^2 = variance (spread)
* Bell-shaped curve: highest at μ, decreases as you move away.

Intuition: Many small independent effects add together, forming a bell curve.

---
Step 2: Intuition from “maximum entropy”

If we want a continuous distribution with a
given mean μ and variance σ^2 and no other assumptions,
the most “spread out” (least biased) distribution is Gaussian.
Exponentials naturally arise when maximizing under 
constraints (mean, variance).

---
Step 3: Derivation “from scratch”

Assume f(x) ≥ 0, 
integrates to 1, 
symmetric around mean (μ = 0),
smoothly decaying. 

Guess:
f(x) = A * exp(-B * x^2)

Step 3a: Normalize

∫ f(x) dx = ∫ A * exp(-B * x^2) dx = 1

∫ exp(-B * x^2) dx = sqrt(π / B)

So A * sqrt(π / B) = 1 → A = sqrt(B / π)

Normalized Gaussian: f(x) = sqrt(B / π) * exp(-B * x^2)

Step 3b: Relate B to variance

σ^2 = ∫ x^2 f(x) dx

∫ x^2 exp(-B x^2) dx = sqrt(π) / (2 B^(3/2))

Multiply by A → σ^2 = 1 / (2B) → B = 1 / (2σ^2)

Final Gaussian: f(x) = (1 / sqrt(2πσ^2)) * exp(-(x - μ)^2 / (2σ^2))

---

Step 4: Example

Measurement errors:

* μ = 0 cm, σ = 0.1 cm

f(x) = (1 / sqrt(2π * 0.1^2)) * exp(-x^2 / (2 * 0.1^2))

* Most errors around 0, errors > 0.3 cm are rare.

---

Step 5: Relation to RBF Kernel

RBF kernel: K(x, y) = exp(-γ * ||x - y||^2)

Similarity to Gaussian:

* Gaussian: exp(-(x - μ)^2 / (2σ^2)) → probability
* RBF kernel: exp(-γ * (x - y)^2) → similarity

Both use squared distance inside an exponential → bell-shaped curve.

---

Step 6: Summary

Gaussian PDF: 
f(x) = (1 / sqrt(2πσ^2)) * exp(-(x - μ)^2 / 2σ^2) → probability

RBF Kernel: 
K(x, y) = exp(-γ * ||x - y||^2) → similarity measure

Key link: Both have the Gaussian form e^-(distance)^2.

"""

"""
step-by-step derivation of the Gaussian integral 
I = ∫_{−∞}^{∞} e^{−B x^2} dx

---
## PREREQUISITES (what you should know before following the derivation)

1. Improper integrals: 
definition and how to evaluate limits 
of integrals on unbounded domains.
* You must know how to write 
∫*{−∞}^{∞} f(x) dx as
lim*{R→∞} ∫_{−R}^{R} f(x) dx.

2. Fubini/Tonelli theorem:
   * Tonelli: 
   if a function is nonnegative on a product domain,
   then the double integral equals the iterated integrals
   and we may interchange sums/limits/integrals.
   * Fubini: 
   if the double integral of the absolute value 
   is finite (absolute integrability), then 
   iterated integrals equal the double integral
   and you may change the order of integration.
   * We will invoke Tonelli/Fubini to justify turning
   a product of integrals into a double integral and
   to swap integration order.

3. Polar coordinates in the plane:

   * The change of variables 
   (x, y) → (r, θ) with 
   x = r cos θ,
   y = r sin θ.
   * Jacobian/differential area element:
   dx dy = r dr dθ.
   * r ≥ 0, θ ∈ [0, 2π).
   * You should be comfortable computing
    ∫_{0}^{2π} dθ = 2π.

4. Basic 1D substitution rule:

   * If u = g(x) is differentiable and invertible
    on the domain, then ∫ f(g(x)) g'(x) dx = ∫ f(u) du.

5. Elementary integrals:

   * ∫_{0}^{∞} e^{−u} du = 1.
   * Familiarity with square-root 
   and properties of positive real numbers.

If any of these points feels shaky, 
review integration basics, 
change of variables, and
Tonelli/Fubini before proceeding.

---
## THE PROBLEM AND ASSUMPTIONS

We want to evaluate I = ∫_{−∞}^{∞} e^{−B x^2} dx.

Assume B is a complex number with Re(B) > 0, so that e^{−B x^2} decays for large |x| and the integral converges absolutely. For most applied uses B is a positive real number; from now on consider B > 0 (real) for simplicity — I will note where the complex-case difference appears.

---

## STEP-BY-STEP DERIVATION (classical method: square + polar)

Step 1 — Square the integral.
I is a single (real) number. Consider:
I^2 = ( ∫*{−∞}^{∞} e^{−B x^2} dx ) * ( ∫*{−∞}^{∞} e^{−B y^2} dy ).

We introduced a second, independent dummy variable y for the second factor. This is legitimate because each integral is just a number and dummy variable names do not matter.

Step 2 — Write the product as a double integral.
Because x and y are independent and the integrand is nonnegative when B > 0, Tonelli’s theorem applies and we may write:
I^2 = ∫*{−∞}^{∞} ∫*{−∞}^{∞} e^{−B x^2} e^{−B y^2} dx dy
= ∫*{−∞}^{∞} ∫*{−∞}^{∞} e^{−B (x^2 + y^2)} dx dy.

This integral is over the whole plane R^2.

Step 3 — Change to polar coordinates.
Set x = r cos θ, y = r sin θ. Then x^2 + y^2 = r^2 and the area element dx dy becomes r dr dθ. The entire plane corresponds to r ∈ [0, ∞), θ ∈ [0, 2π). Thus:

I^2 = ∫*{θ=0}^{2π} ∫*{r=0}^{∞} e^{−B r^2} r dr dθ.

Step 4 — Separate the θ integral and the r integral.
The integrand is independent of θ, so integrate over θ first:

I^2 = ( ∫*{0}^{2π} dθ ) * ( ∫*{0}^{∞} r e^{−B r^2} dr )
= 2π * ∫_{0}^{∞} r e^{−B r^2} dr.

Step 5 — Evaluate the r-integral by substitution.
Let u = B r^2. Then du = 2B r dr, so r dr = du / (2B).

When r goes from 0 to ∞, u goes from 0 to ∞. Therefore:

∫*{0}^{∞} r e^{−B r^2} dr = ∫*{0}^{∞} e^{−u} * (1/(2B)) du
= (1/(2B)) * ∫_{0}^{∞} e^{−u} du
= (1/(2B)) * 1
= 1/(2B).

Step 6 — Combine the results.
I^2 = 2π * (1/(2B)) = π / B.

Hence I^2 = π / B.

Step 7 — Take the positive square root.
Since I = ∫_{−∞}^{∞} e^{−B x^2} dx is a positive real number whenever B > 0, we take the positive square root:

I = sqrt(π / B).

So the final result is:
∫_{−∞}^{∞} e^{−B x^2} dx = sqrt(π / B)   (for real B > 0).

If B is complex with Re(B) > 0, the same identity holds but the square root is taken using the principal square root branch consistent with analytic continuation (the derivation requires slightly more care about contours, but the Tonelli/Fubini step uses absolute convergence because Re(B) > 0).

---

## JUSTIFICATIONS / COMMENTS (why each step is allowed)

1. Squaring is algebraically valid: I^2 is the product of the two identical real numbers.

2. Replacing the second integrand variable x by y is legitimate because the integration variable is a dummy symbol.

3. Tonelli/Fubini justification: for B > 0, the function e^{−B(x^2 + y^2)} is nonnegative and integrable over R^2; Tonelli guarantees that the double integral equals the iterated integrals and that we may form the double integral from the product of single integrals.

4. Polar change-of-variables is valid with Jacobian r because the mapping (r, θ) → (x, y) is smooth almost everywhere and covers the plane with r ≥ 0, θ ∈ [0, 2π). Standard change-of-variables theorem for integrals supplies dx dy = r dr dθ.

5. u-substitution in the r-integral is routine and justified since the substitution is monotone and differentiable on [0, ∞).

6. Taking the positive square root is valid because each single integral is positive (integrand positive for all x when B > 0).

---

## ALTERNATIVE VIEW (product-of-1D integrals approach)

Instead of starting from I and squaring, one can note directly:

∫*{−∞}^{∞} e^{−B x^2} dx * ∫*{−∞}^{∞} e^{−B y^2} dy
= ∫∫_{R^2} e^{−B(x^2+y^2)} dx dy

and then proceed with the polar calculation. This is the same as the previous approach but highlights that the double integral is separable into the product of one-dimensional integrals.

---

## EXTENSIONS

1. Standard Gaussian normalization (example):
   For the standard normal probability density function φ(x) = (1/√(2π σ^2)) e^{−(x−μ)^2/(2σ^2)}, the normalization constant comes from the Gaussian integral. For B = 1/(2σ^2) and centered at μ = 0, we need

∫_{−∞}^{∞} e^{−x^2/(2σ^2)} dx = sqrt(2π) σ.

Proof: set B = 1/(2σ^2) in the main result: sqrt(π / B) = sqrt(π * 2σ^2) = sqrt(2π) σ.

2. Multi-dimensional Gaussian (n dimensions):
   Let x ∈ R^n and consider ∫_{R^n} e^{−B ||x||^2} d^n x. Because the integral factors in Cartesian coordinates or by using spherical coordinates, one gets:

∫_{R^n} e^{−B ||x||^2} d^n x = (π / B)^{n/2}.

For example, for n = 2 this gives π / B, consistent with I^2 above. For n = 3, the integral equals (π/B)^{3/2}, etc.

3. Non-isotropic quadratic forms:
   If the exponent is −x^T A x with A positive-definite symmetric matrix, then
   ∫_{R^n} e^{−x^T A x} d^n x = (π)^{n/2} / sqrt(det(A)).
   This follows by diagonalizing A and changing variables.

---

## FULL RAW-TEXT SUMMARY (final boxed result)

Assuming B is real and B > 0 (or complex with Re(B) > 0),

I = ∫_{−∞}^{∞} e^{−B x^2} dx = sqrt(π / B).

Justification: square the integral, write the square as a double integral, convert to polar coordinates (dx dy = r dr dθ), evaluate θ-integral to get 2π, then evaluate radial integral by substitution u = B r^2 to obtain I^2 = π / B, and take positive square root.

---

## IF YOU WANT NEXT

I can provide:

* a fully rigorous proof using Tonelli/Fubini statements written out in epsilon-delta / limit-of-Riemann-sums language;
* a worked example computing the normalization constant for N(μ, σ^2);
* the derivation when B is complex (Re(B)>0) with comments about analytic continuation;
* the n-dimensional derivation with spherical coordinates and the volume element in R^n.

Tell me which of these you’d like next and I will produce it in raw text.

"""



"""
2D illustration** showing the Gaussian
PDF and RBF kernel intuitively.

### **1D Gaussian PDF (centered at 0)**

```
f(x)
^
|        *
|       * *
|      *   *
|     *     *
|    *       *
|   *         *
|  *           *
+-----------------> x
 -3 -2 -1  0  1  2  3
```

* Peak at 0 (mean μ = 0)
* Decays smoothly as x moves away
* Represents **probability density** 
of a random variable

---

### **RBF Kernel (similarity to a point at 0)**

```
K(x, 0)
^
|        *
|       * *
|      *   *
|     *     *
|    *       *
|   *         *
|  *           *
+-----------------> x
 -3 -2 -1  0  1  2  3
```

* Peak at x = 0 (point of reference)
* Decays with distance ||x - 0||
* Represents **similarity**: 
  closer points → higher value

---

### **Observation**

* Shape is **identical**: bell curve
* Difference is **meaning**:

  * Gaussian PDF → probability density
  * RBF kernel → similarity measure
* Both use `exp(-distance^2 / scaling)` form

---

"""


"""
introducing another dummy variable 
when computing (I^2) is **completely
valid** and is one of the key mathematical
tricks in the Gaussian integral proof.

We start with the one-dimensional integral:

I = ∫_{−∞}^{∞} e^{−B x²} dx
This integral involves only **one** variable, x.

Now we want to compute:

I² = 
( ∫*{−∞}^{∞} e^{−B x²} dx ) 
* ( ∫*{−∞}^{∞} e^{−B x²} dx )

This is a product of **two identical numbers**.

To write this product as a double integral,
we do the following step:

Introduce an independent dummy variable y
for the second copy:

I²
= ( ∫ e^{−B x²} dx ) ( ∫ e^{−B y²} dy )

QUESTION: WHY ARE WE ALLOWED TO DO THIS?

---
## WHY IT IS LEGAL TO INTRODUCE A NEW VARIABLE

1. Each integral is just a number.
   Example: (5)(5) = 25.
   Writing 5 as ∫ f(x) dx and 
   the other 5 as ∫ f(y) dy 
   does not change the value.

2. The variable inside an integral is a
  **dummy variable**, meaning it has 
  no meaning outside the integral.

   * ∫ f(x) dx
   * ∫ f(u) du
   * ∫ f(y) dy
     All represent the same number.
     The letter used is irrelevant.

3. When multiplying two integrals,
 if we used x in both, 
 we would run into a logical problem:

(∫ f(x) dx)(∫ f(x) dx)

This expression is ambiguous,
because the x in the first integral is
**not** the same x as in the second.

Using distinct dummy variables avoids confusion.

4. Using different dummy variables allows us to
combine the integrals via Fubini’s theorem:

(∫ f(x) dx)(∫ f(y) dy)
= ∫∫ f(x) f(y) dx dy

This step requires x and y to be treated
as **independent variables**.

---
## A CLEAR ANALOGY

Think of it like this:

I = area under the curve of e^{−B x²}.
I² = area * area = area of a rectangle.

To compute the area of that rectangle,
you use two independent axes: x and y.

That is why a second variable is needed.

---

## THE KEY POINT

You are NOT changing the mathematics.
You are simply giving the two integrals
different internal variable names so 
they can be combined.

In short:
* x is just a placeholder inside the first integral
* y is just a placeholder inside the second integral
* They are independent, so ∫ f(x) dx and ∫ f(y) dy 
represent the same number
* This allows rewriting the product as
a double integral over (x, y)

---
FINAL FORM
I² = ∫∫ e^{−B(x² + y²)} dx dy
This is why the “dummy variable trick” is essential.


QS1. WHY DOES “area * area = area of a rectangle”?

---
Let’s say:

I = ∫ f(x) dx
J = ∫ g(y) dy

Think of I and J as **pure numbers**.

Now imagine I = A and J = B.
Then I·J = A·B.

Now here is the key geometric fact:

If you have a region on the x-axis 
of width A, and a region on the y-axis
of height B, then in the xy-plane the
rectangle they form has area:

Area = A × B.

This is not a deep theorem — it’s just 
the geometric definition of a rectangle:
“width × height”.

The Gaussian trick applies this idea:
The first integral gives a “length” 
in the x direction.
The second integral gives a “length”
in the y direction.
Multiply them → 
that is the area of a rectangular region.

We convert the product into 
a **double integral** because 
a double integral literally 
computes area in the xy-plane 
weighted by the function.

---
Question 2. 
DOES IT MATTER IF THE FUNCTIONS ARE
THE SAME (f = g) OR DIFFERENT (f ≠ g)?

No — the rule works **in general**,
with same or different functions.

Here is the rule:

( ∫ f(x) dx )( ∫ g(y) dy )
= ∫∫ f(x) g(y) dx dy

This is ALWAYS true as long as
the integrals converge.

WHY?

Because the two variables x and y 
are **independent**, meaning:

* f(x) does not depend on y
* g(y) does not depend on x

So their product f(x)g(y) is
a function over the whole xy-plane.

A simple example:

Let
∫₀¹ x dx = 1/2
and
∫₀² y dy = 2.

Their product is:

(1/2)(2) = 1.

Now compute the double integral:

∫₀¹ ∫₀² x y dy dx
= ∫₀¹ x ( ∫₀² y dy ) dx
= ∫₀¹ x · 2 dx
= 2 ∫₀¹ x dx
= 2(1/2)
= 1

Same result.

This works regardless of 
whether the two functions are:

* the same (f = g)
* different (f ≠ g)
* completely unrelated

The key condition is **separability**:
 f depends only on x, g depends only on y.

WHY IT IS IMPORTANT IN THE GAUSSIAN PROOF

In the Gaussian proof, we have:

I = ∫ e^(−B x²) dx
I² = ( ∫ e^(−B x²) dx ) ( ∫ e^(−B y²) dy )

We introduce a second variable y so
that the product becomes:

I² = ∫∫ e^(−B x²) e^(−B y²) dx dy
= ∫∫ e^(−B(x² + y²)) dx dy

Now it becomes a circularly symmetric 2D problem,
which is easy to solve using polar coordinates.

## SUMMARY

1. Area × area = area of rectangle
   → because “rectangle area = width × height”.
2. The product-to-double-integral rule works for
   → same functions (f = g)
   → different functions (f ≠ g)
   as long as the variables are independent.
3. Introducing a second variable 
(dummy variable) is legitimate
   → each integral is just a number
   → dummy variables can be renamed freely
   → separating variables allows conversion
     to a double integral.

---

"""