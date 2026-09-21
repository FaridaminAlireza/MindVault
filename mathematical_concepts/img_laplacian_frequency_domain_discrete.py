"""
THE LAPLACIAN IN THE FREQUENCY DOMAIN
---

1. INTRODUCTION

The Laplacian is a second-order derivative operator.
Its purpose is to measure how rapidly image
intensity changes in space.

For a discrete image, we cannot take an infinitesimally
small derivative. Instead, derivatives are approximated
using differences between neighboring pixels.

Because differences respond strongly to rapid changes,
the discrete Laplacian is useful for:

* Edge enhancement
* Sharpening
* Highlighting fine detail
* Detecting regions of rapid intensity change

Unlike gradient operators,
which measure change in a specific direction,
the Laplacian combines the second differences
in the x and y directions.

For the standard 4-neighbor Laplacian,
the result is isotropic with respect to the
horizontal and vertical axes of the discrete grid,
although discrete rotational symmetry is not perfect.

---
2. THE DISCRETE SPATIAL-DOMAIN LAPLACIAN

For a continuous image f(x,y):

    Laplacian(f) =
    d²f/dx² + d²f/dy²

For a discrete image f[m,n],
we approximate the second derivatives
using second differences.

In the x-direction:

    d²f/dx²
    ≈
    f[m+1,n] - 2f[m,n] + f[m-1,n]

In the y-direction:

    d²f/dy²
    ≈
    f[m,n+1] - 2f[m,n] + f[m,n-1]

Therefore the discrete Laplacian is:

    Laplacian(f[m,n]) =

    f[m+1,n]
    + f[m-1,n]
    + f[m,n+1]
    + f[m,n-1]
    - 4f[m,n]

---
3. DISCRETE LAPLACIAN MASK

The previous equation corresponds to:

     0   1   0
     1  -4   1
     0   1   0

Therefore:

    Laplacian(f) = f * h

where h is the discrete Laplacian mask.

This is a convolution operation.

This immediately suggests that we can use
the convolution theorem:

    convolution in spatial domain
    ⇔
    multiplication in frequency domain

---
4. WHY STUDY THE LAPLACIAN IN THE FREQUENCY DOMAIN?

The advantage is that spatial operations such as
convolution and discrete differences become
multiplication in the frequency domain.

In spatial processing:

* Compute differences between neighboring pixels.
* Combine the second differences.
* Or apply a Laplacian mask.

In frequency processing:

* Transform the image to the frequency domain.
* Multiply by the frequency response of the
  discrete Laplacian.
* Transform back.

---
5. DISCRETE FOURIER TRANSFORM

For an M x N image, the 2D DFT is:

    F[u,v] =
    sum over m,n of

    f[m,n]
    exp(-j2π(um/M + vn/N))

The inverse DFT reconstructs the image:

    f[m,n] =
    1/(MN)
    sum over u,v of

    F[u,v]
    exp(+j2π(um/M + vn/N))

The important point is that the DFT represents
the image as a collection of discrete frequency
components.

---
6. DISCRETE DIFFERENTIATION

In the continuous case:

    d/dx
    ⇔
    j2πu

But in the discrete case, we approximate
the derivative using a difference.

For example, use the forward difference:

    g[m,n] = f[m+1,n] - f[m,n]

We now derive what this operation becomes
in the frequency domain.

---
7. DFT OF THE DISCRETE FIRST DIFFERENCE

Take the 2D DFT:

    G[u,v] =
    DFT{f[m+1,n] - f[m,n]}

By linearity:

    G[u,v] =
    DFT{f[m+1,n]}
    -
    DFT{f[m,n]}

The second term is simply:

    F[u,v]

For the first term, shifting the image by one pixel
in the x-direction produces a frequency-domain
multiplication factor:

    exp(+j2πu/M)

Therefore:

    DFT{f[m+1,n]}
    =
    exp(+j2πu/M) F[u,v]

Thus:

    G[u,v] =
    [exp(+j2πu/M) - 1] F[u,v]

Therefore:

    ------------------------------------------------
    forward difference in x
    ⇔
    multiplication by
    [exp(+j2πu/M) - 1]
    ------------------------------------------------

Similarly, for the y-direction:

    f[m,n+1] - f[m,n]

becomes:

    [exp(+j2πv/N) - 1] F[u,v]

Therefore:

    ------------------------------------------------
    forward difference in y
    ⇔
    multiplication by
    [exp(+j2πv/N) - 1]
    ------------------------------------------------

This is the discrete equivalent of:

    d/dx ⇔ j2πu

    d/dy ⇔ j2πv

---
8. DISCRETE SECOND DIFFERENCE

The discrete second derivative in x is:

    f[m+1,n]
    - 2f[m,n]
    + f[m-1,n]

We can obtain its frequency-domain multiplier
by applying the first-difference idea twice.

For the second difference:

    Dxx =
    f[m+1,n]
    - 2f[m,n]
    + f[m-1,n]

Its DFT becomes:

    DFT{Dxx} =

    [
      exp(+j2πu/M)
      - 2
      + exp(-j2πu/M)
    ]
    F[u,v]

Use:

    exp(jθ) + exp(-jθ) = 2 cos(θ)

Therefore:

    DFT{Dxx} =

    [2 cos(2πu/M) - 2]
    F[u,v]

Using:

    cos(θ) - 1 = -2 sin²(θ/2)

we obtain:

    2 cos(θ) - 2
    =
    -4 sin²(θ/2)

Therefore:

    ------------------------------------------------
    DFT{d²f/dx² (discrete)}

    =
    -4 sin²(πu/M) F[u,v]
    ------------------------------------------------

Similarly:

    ------------------------------------------------
    DFT{d²f/dy² (discrete)}

    =
    -4 sin²(πv/N) F[u,v]
    ------------------------------------------------

This is the key difference from the continuous case.

Continuous:

    -4π²u²

Discrete:

    -4 sin²(πu/M)

---
9. DERIVING THE DISCRETE LAPLACIAN

The discrete Laplacian is:

    Laplacian(f) = Dxx + Dyy

where:

    Dxx =
    f[m+1,n]
    - 2f[m,n]
    + f[m-1,n]

and:

    Dyy =
    f[m,n+1]
    - 2f[m,n]
    + f[m,n-1]

Therefore:

    DFT{Laplacian(f)}

    =
    DFT{Dxx}
    +
    DFT{Dyy}

Substitute the previous results:

    =
    [-4 sin²(πu/M)] F[u,v]

    +
    [-4 sin²(πv/N)] F[u,v]

Factor out F[u,v]:

    =
    -4[
        sin²(πu/M)
        +
        sin²(πv/N)
      ]
      F[u,v]

Therefore:

    ------------------------------------------------
    DISCRETE FREQUENCY-DOMAIN LAPLACIAN

    L[u,v] =
    -4[
        sin²(πu/M)
        +
        sin²(πv/N)
      ]

    and:

    DFT{Laplacian(f)}
    =
    L[u,v] F[u,v]
    ------------------------------------------------

This is the discrete counterpart of the
continuous result:

    -4π²(u²+v²) F(u,v)

---
10. WHY DOES THE DISCRETE FORMULA LOOK DIFFERENT?

Continuous Laplacian:

    -4π²(u²+v²)

Discrete Laplacian:

    -4[
        sin²(πu/M)
        +
        sin²(πv/N)
      ]

Why?

Because the discrete image does not contain
continuous derivatives.

It contains samples.

Therefore:

    continuous derivative
    →
    discrete difference

and consequently:

    continuous frequency multiplier
    →
    discrete frequency multiplier

For low frequencies, the two become very similar.

Recall:

    sin(x) ≈ x

for small x.

Therefore:

    sin(πu/M) ≈ πu/M

and:

    sin(πv/N) ≈ πv/N

So:

    -4[
        sin²(πu/M)
        +
        sin²(πv/N)
      ]

approximately becomes:

    -4π²[
        (u/M)²
        +
        (v/N)²
      ]

This is why the discrete result resembles
the continuous Laplacian at low frequencies.

---
11. WHY DOES THE DISCRETE LAPLACIAN EMPHASIZE
    HIGH FREQUENCIES?

The discrete multiplier is:

    L[u,v] =
    -4[
        sin²(πu/M)
        +
        sin²(πv/N)
      ]

At the frequency origin:

    u = 0
    v = 0

Therefore:

    sin(0) = 0

and:

    L[0,0] = 0

Thus the constant or DC component is removed.

As we move away from the origin,
the sine terms generally increase,
so the magnitude of the Laplacian response increases.

Therefore:

    low frequencies
    →
    weak response

    high frequencies
    →
    strong response

This is why the discrete Laplacian behaves
as a highpass operator.

---
12. RADIAL INTERPRETATION

For the continuous Laplacian we could write:

    D² = u² + v²

and:

    H(u,v) = -4π²D²

For the discrete Laplacian, the corresponding
quantity is:

    D_discrete² =
    sin²(πu/M)
    +
    sin²(πv/N)

Therefore:

    H_L[u,v] =
    -4 D_discrete²

or:

    H_L[u,v] =
    -4[
        sin²(πu/M)
        +
        sin²(πv/N)
      ]

This shows that the response depends on the
discrete frequency coordinates through their
sine terms.

For the 4-neighbor Laplacian, the frequency response
has the symmetry of the discrete grid rather than
perfect continuous rotational symmetry.

---
13. LAPLACIAN FILTER SHAPE

At the frequency origin:

    u = 0
    v = 0

Therefore:

    H_L[0,0] = 0

Moving away from the origin:

    sin²(πu/M)
    and/or
    sin²(πv/N)

increase.

Therefore the magnitude of the Laplacian response
generally increases away from the origin.

Unlike a lowpass filter, the Laplacian is weakest
at the center and strongly responds to higher
frequencies.

Because this is a discrete frequency domain,
the response is periodic and bounded.

This is another important difference from
the continuous formula.

---
14. SHARPENING USING THE LAPLACIAN

The Laplacian highlights rapid intensity changes.

To sharpen an image, we combine the original image
with a Laplacian-derived image.

Suppose we use:

    sharpened image
    =
    original image
    -
    Laplacian image

The sign depends on the particular definition
of the Laplacian mask.

Our Laplacian mask is:

     0   1   0
     1  -4   1
     0   1   0

Its frequency response is negative:

    H_L[u,v] =
    -4[
        sin²(πu/M)
        +
        sin²(πv/N)
      ]

Therefore:

    G[u,v]
    =
    F[u,v]
    -
    H_L[u,v] F[u,v]

Factor out F[u,v]:

    G[u,v]
    =
    [1 - H_L[u,v]] F[u,v]

Substitute H_L:

    G[u,v]
    =
    {
      1
      +
      4[
        sin²(πu/M)
        +
        sin²(πv/N)
      ]
    }
    F[u,v]

Therefore the discrete sharpening filter is:

    ------------------------------------------------
    H_sharp[u,v] =
    1
    +
    4[
      sin²(πu/M)
      +
      sin²(πv/N)
    ]
    ------------------------------------------------

---
15. INTERPRETING THE DISCRETE SHARPENING FILTER

The multiplier is:

    H_sharp[u,v] =
    1
    +
    4[
      sin²(πu/M)
      +
      sin²(πv/N)
    ]

At the frequency origin:

    u = 0
    v = 0

Therefore:

    H_sharp[0,0] = 1

So the DC component is preserved.

At low frequencies:

    sin²(πu/M)
    and
    sin²(πv/N)

are small.

Therefore:

    H_sharp ≈ 1

Low frequencies remain almost unchanged.

At higher frequencies, the sine terms become larger.

Therefore:

    H_sharp > 1

Higher-frequency components are amplified.

Therefore:

    fine detail
    edges
    texture

are enhanced.

---
16. CONNECTION BETWEEN CONTINUOUS AND DISCRETE FORMS

Continuous first derivative:

    d/dx
    ⇔
    j2πu

Discrete forward difference:

    f[m+1,n] - f[m,n]
    ⇔
    [exp(j2πu/M) - 1]

Continuous second derivative:

    d²/dx²
    ⇔
    -4π²u²

Discrete second difference:

    f[m+1,n]
    - 2f[m,n]
    + f[m-1,n]

    ⇔

    -4 sin²(πu/M)

Continuous Laplacian:

    ∇²
    ⇔
    -4π²(u²+v²)

Discrete Laplacian:

    ∇²_discrete
    ⇔

    -4[
      sin²(πu/M)
      +
      sin²(πv/N)
    ]

Therefore the overall idea is unchanged:

    spatial differentiation
    →
    frequency-domain multiplication

but the exact multiplier changes because
we are working with discrete samples.
    
---
17. WHY THE DISCRETE LAPLACIAN IS USEFUL

The discrete Laplacian provides a direct connection
between spatial filtering and frequency filtering.

Spatial domain:

    apply the Laplacian mask

         0   1   0
         1  -4   1
         0   1   0

Frequency domain:

    multiply F[u,v] by

    -4[
      sin²(πu/M)
      +
      sin²(πv/N)
    ]

The two operations produce the same result
under the corresponding DFT/circular-convolution
conditions.

---
KEY PROPERTIES OF THE DISCRETE LAPLACIAN FILTER:

* It is a second-order difference operator.
* It measures local curvature/change.
* It uses neighboring pixels.
* The standard 4-neighbor version uses:

      0   1   0
      1  -4   1
      0   1   0

* It is a convolution operation.
* Convolution becomes multiplication under the DFT.
* Its frequency response is:

      H_L[u,v] =
      -4[
        sin²(πu/M)
        +
        sin²(πv/N)
      ]

* It is zero at the DC frequency.
* It suppresses low frequencies relative to
  higher-frequency components.
* It behaves as a highpass-type operator.
* It is useful for edge enhancement and sharpening.
* The corresponding sharpening filter is:

      H_sharp[u,v] =
      1
      +
      4[
        sin²(πu/M)
        +
        sin²(πv/N)
      ]

* At low frequencies, the discrete formula
  approaches the continuous behavior because:

      sin(x) ≈ x

  for small x.
"""