"""
COMPUTING THE INVERSE FOURIER TRANSFORM
USING A FORWARD TRANSFORM ALGORITHM

Gonzalez & Woods - Digital Image Processing
Chapter 4, Section 4.6.2


1. THE PROBLEM


We already know the 2-D forward DFT:

    F(u,v) =
        sum over x,y of
        f(x,y) exp[-j 2pi(ux/M + vy/N)]


The inverse DFT is:

    f(x,y) =
        (1/MN)
        sum over u,v of
        F(u,v) exp[+j 2pi(ux/M + vy/N)]


The problem is:

    The forward transform uses

        exp[-j...]

    while the inverse transform uses

        exp[+j...]

    So, if we already have an algorithm that computes
    the FORWARD transform, how can we use it to compute
    the INVERSE transform?

The book shows that we can do exactly this by using
the complex conjugate.

---
2. START WITH THE INVERSE TRANSFORM


Start with:

    f(x,y) =
        (1/MN)
        sum over u,v of
        F(u,v) exp[+j 2pi(ux/M + vy/N)]


Multiply both sides by MN:

    MN f(x,y) =
        sum over u,v of
        F(u,v) exp[+j 2pi(ux/M + vy/N)]


This is the starting point of the book's derivation.

---
3. TAKE THE COMPLEX CONJUGATE


Now take the complex conjugate of both sides:

    [MN f(x,y)]*

        =
    [sum over u,v of
        F(u,v) exp[+j 2pi(ux/M + vy/N)]]*


Since M and N are real numbers:

    MN f*(x,y)

        =
    sum over u,v of
        F*(u,v)
        [exp(+j 2pi(ux/M + vy/N))]*


Now use the important property:

    [exp(+j theta)]*
        =
    exp(-j theta)


Therefore:

    MN f*(x,y)

        =
    sum over u,v of
        F*(u,v)
        exp[-j 2pi(ux/M + vy/N)]


THIS IS THE KEY STEP.

---
4. LOOK AT THE RESULT

We now have:

    MN f*(x,y)
        =
    sum over u,v of
        F*(u,v)
        exp[-j 2pi(ux/M + vy/N)]


Now compare this with the FORWARD DFT:

    Forward DFT:

    G(x,y)
        =
    sum over u,v of
        g(u,v)
        exp[-j 2pi(ux/M + vy/N)]


They have EXACTLY the same form.

Our expression is:

    MN f*(x,y)
        =
    sum over u,v of
        F*(u,v)
        exp[-j 2pi(ux/M + vy/N)]


Therefore, if we give F*(u,v) to our
FORWARD DFT algorithm, the algorithm produces:

    MN f*(x,y)

In other words:

    Forward DFT of F*(u,v)
        =
    MN f*(x,y)

This is exactly the observation made by the book.

---
5. SO WHAT DO WE DO IN PRACTICE?


Suppose we have:

    F(u,v)


and want:

    f(x,y)


The book's procedure is:

STEP 1
Take the complex conjugate of the frequency-domain
image:

    F*(u,v)


STEP 2
Put F*(u,v) into the SAME algorithm that calculates
the forward DFT.


The result is:

    MN f*(x,y)


STEP 3
Take the complex conjugate of the result:

    [MN f*(x,y)]*

Since MN is real:

    = MN f(x,y)


STEP 4
Divide by MN:

    f(x,y)
    =
    [ForwardDFT{F*(u,v)}]*  1/MN


Therefore:

    f(x,y)
        =
    (1/MN)
    [ DFT{F*(u,v)} ]*


This is the inverse Fourier transform,
calculated using a forward-transform algorithm.

---
6. THE BOOK'S IDEA IN ONE LINE

The whole trick can be summarized mathematically as:

IDFT{F(u,v)}
    =
(1/MN)
[ DFT{F*(u,v)} ]*

This is the central result of Section 4.6.2.

---
7. WHY DOES THE CONJUGATE HELP?

The entire trick works because of:
[exp(+j theta)]* = exp(-j theta)

Remember:
INVERSE DFT: exp(+j theta)

But the forward DFT algorithm expects: exp(-j theta)

So we take the complex conjugate:
exp(+j theta) -> conjugate -> exp(-j theta)

Now the expression has exactly the form required
by the forward DFT algorithm.

--
8. THINK OF IT AS A TRANSFORMATION OF THE FORMULA

Before taking the conjugate:
F(u,v) exp(+j theta)
This is the inverse-transform form.

After taking the conjugate:
F*(u,v) exp(-j theta)
This is the forward-transform form.

Therefore:

    inverse-form
        |
        | take conjugate
        v
    forward-form

That is the mathematical trick used by the book.

---
9. IMPORTANT: WHY DOES THE BOOK GET f*(x,y)?

This point can initially be confusing.

After taking the conjugate of
the inverse equation,
we obtain:

MN f*(x,y)

NOT:

MN f(x,y)

That is why the forward transform gives us the
COMPLEX CONJUGATE of the desired image.

Specifically:
Forward DFT of F*(u,v) = MN f*(x,y)

So we must take another conjugate:
[MN f*(x,y)]* = MN f(x,y)

Then divide by MN: f(x,y)

This is why there are TWO 
conjugations in the procedure:

First conjugation: F(u,v) -> F*(u,v)
Second conjugation: output -> f(x,y)

---
10. VISUAL SUMMARY


Suppose we start with:

F(u,v)
    |
    |
complex conjugate
    |
    v
F*(u,v)
    |
    |
FORWARD DFT
    |
    v
MN f*(x,y)
    |
    |
complex conjugate
    |
    v
MN f(x,y)
    |
    |
divide by MN
    |
    v
f(x,y)


So the forward-transform algorithm 
has effectively been used as 
an inverse-transform algorithm.

---
11. WHY THIS MATTERS FOR FFT

This section is part of the book's "Implementation"
discussion.

The practical importance is that we may already have
an efficient algorithm for computing the forward
Fourier transform.

Later, the book discusses the FAST FOURIER TRANSFORM
(FFT).

Instead of creating a completely separate algorithm
for the inverse transform, we can use the same
forward-transform machinery.

Conceptually:

    Forward FFT:

        input
          |
          v
        FFT
          |
          v
        output


    Inverse FFT using the same idea:

        input F
          |
          v
        conjugate
          |
          v
        forward FFT
          |
          v
        conjugate
          |
          v
        divide by MN
          |
          v
        inverse


For an M x N image:

    IFFT2(F)
        =
    conjugate(
        FFT2(
            conjugate(F)
        )
    )
    / (MN)

---
12. CONNECTION WITH THE PREVIOUS SECTION ON
    SEPARABILITY

This is particularly useful for a 2-D image.

Earlier, the book explains that the 2-D DFT is
SEPARABLE.

That means:

2-D DFT
    =
1-D DFTs along rows
    +
1-D DFTs along columns


Therefore, a practical implementation can use
1-D forward-transform algorithms.

The current section says:

We can also use the SAME forward algorithm
to obtain the inverse.

So the implementation strategy becomes:

2-D inverse transform
        |
        v
conjugate the frequency image
        |
        v
2-D forward transform
        |
        v
conjugate the result
        |
        v
        divide
        by MN

---
13. THE MOST IMPORTANT PART TO UNDERSTAND

The book's trick is:
    Modify the input using complex conjugation
    so that the inverse-transform expression
    becomes mathematically identical to a
    forward-transform expression.
"""