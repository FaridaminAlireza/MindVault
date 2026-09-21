"""
PART 1 — DISCRETE DIFFERENTIATION AND THE DFT

---
1. The basic idea

For a continuous function:

    df(x)/dx

has Fourier transform:

    j 2 pi u F(u)

In a discrete image, 
we cannot take an infinitesimally small derivative. 
Instead, we approximate the derivative using differences.

For example, the forward difference is:

    df/dx  ≈  f[x+1] - f[x]

We want to find the DFT of this difference.

---
2. Define the DFT

For an N-point discrete signal:

    F[k] = sum from n=0 to N-1 of
           f[n] exp(-j 2 pi k n / N)

Let: g[n] = f[n+1] - f[n]

We want to find G[k].

---
3. Take the DFT of the difference

By definition:

    G[k] =
    sum from n=0 to N-1 of
    g[n] exp(-j 2 pi k n / N)

Substitute:

    g[n] = f[n+1] - f[n]

Therefore:

    G[k] =
    sum of f[n+1] exp(-j 2 pi k n/N)
    -
    sum of f[n] exp(-j 2 pi k n/N)

---
4. Focus on the first sum

Consider:
    sum of f[n+1] exp(-j 2 pi k n/N)

Make the change of variable:

    m = n+1

Therefore:

    n = m-1

Substitute:

    exp(-j 2 pi k n/N)

becomes:

    exp(-j 2 pi k (m-1)/N)

Separate the exponent:

    exp(-j 2 pi k m/N)
    exp(+j 2 pi k/N)


Therefore the first sum becomes:

    exp(+j 2 pi k/N)
    sum of f[m] exp(-j 2 pi k m/N)


But the sum is exactly F[k].

Therefore:

    first sum =
    exp(+j 2 pi k/N) F[k]

---
5. Put everything together

We had:

    G[k] =
    first sum - second sum

Therefore:

    G[k] =
    exp(+j 2 pi k/N) F[k] - F[k]

Factor out F[k]:

    G[k] =
    [exp(+j 2 pi k/N) - 1] F[k]

Therefore:

    -----------------------------
    DFT{f[n+1] - f[n]}
    =
    [exp(+j 2 pi k/N) - 1] F[k]
    -----------------------------

This is the discrete equivalent of the continuous result:

    Fourier{df/dx} = j 2 pi u F(u)

---
6. Why is this similar to j 2 pi u?

For small values of k/N:

    exp(j theta) - 1 ≈ j theta

where:

    theta = 2 pi k/N

Therefore:

    exp(+j 2 pi k/N) - 1
    ≈
    j 2 pi k/N

So the discrete result approaches
the continuous result:

    G[k] ≈ j 2 pi (k/N) F[k]


The important idea is:

    DIFFERENTIATION
           ↓
    DIFFERENCE IN DISCRETE DOMAIN
           ↓
    MULTIPLICATION IN FREQUENCY DOMAIN

---
7. Central difference

Another common discrete derivative is:

    g[n] = (f[n+1] - f[n-1]) / 2

Its DFT is:

    G[k] =
    [exp(+j 2 pi k/N) - exp(-j 2 pi k/N)] / 2
    F[k]

Using:

    exp(j theta) - exp(-j theta)
    =
    2j sin(theta)

we get:

    G[k] =
    j sin(2 pi k/N) F[k]

So:

    -------------------------
    DFT{central difference}
    =
    j sin(2 pi k/N) F[k]
    -------------------------


---
8. 2D version

For an image f[m,n], a forward difference 
in the x-direction is:

    g[m,n] = f[m+1,n] - f[m,n]

Its 2D DFT is:

    G[u,v] =
    [exp(+j 2 pi u/M) - 1] F[u,v]

Similarly, in the y-direction:

    g[m,n] = f[m,n+1] - f[m,n]

gives:

    G[u,v] =
    [exp(+j 2 pi v/N) - 1] F[u,v]

Therefore:

    x-difference
    ↔
    multiplication by [exp(+j 2 pi u/M) - 1]

    y-difference
    ↔
    multiplication by [exp(+j 2 pi v/N) - 1]
"""