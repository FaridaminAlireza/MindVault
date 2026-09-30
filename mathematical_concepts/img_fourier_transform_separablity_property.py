"""
SEPARABILITY AND THE FAST FOURIER TRANSFORM (FFT)

1. THE BASIC PROBLEM

Suppose we have a 2-D discrete image: f(x,y) with
x = 0,1,...,M-1
y = 0,1,...,N-1

Its 2-D Discrete Fourier Transform (DFT) is
F(u,v) =
sum_{x=0}^{M-1} sum_{y=0}^{N-1}
f(x,y) exp[-j 2*pi (ux/M + vy/N)]

where
u = 0,1,...,M-1
v = 0,1,...,N-1

The important question is:
Can we calculate this 2-D transform more efficiently?

The answer is YES.
The reason is the SEPARABILITY of the Fourier transform.

---
2. WHAT DOES "SEPARABLE" MEAN?

Separability means that a 2-D operation can be broken into
two independent 1-D operations.

For the Fourier transform, notice: exp[-j 2*pi (ux/M + vy/N)]
contains a sum inside the exponent.
Using exp(a+b) = exp(a) exp(b)
we get exp[-j 2*pi (ux/M + vy/N)] =
exp[-j 2*pi ux/M] exp[-j 2*pi vy/N]

Therefore:
F(u,v) =
sum_x sum_y f(x,y) exp[-j 2*pi ux/M] exp[-j 2*pi vy/N]

The x part and y part are now separated.
This is the key idea of separability.

---
3. FIRST TRANSFORM IN THE x DIRECTION

For each fixed y, take a 1-D DFT along x:

G(u,y) =
sum_{x=0}^{M-1} f(x,y) exp[-j 2*pi ux/M]

So instead of doing the complete 2-D transform at once,
we first transform every ROW of the image.

Then we have an intermediate image:

    f(x,y)
       |
       | 1-D DFT along x
       v
    G(u,y)

---
4. THEN TRANSFORM IN THE y DIRECTION

Now take a 1-D DFT along y:
F(u,v) = sum_{y=0}^{N-1} G(u,y) exp[-j 2*pi vy/N]

So:

    image
      |
      | DFT of every row
      v
    intermediate result
      |
      | DFT of every column
      v
    2-D Fourier transform

Therefore:

    2-D DFT
    =
    1-D DFTs along rows
    +
    1-D DFTs along columns

This is called SEPARABILITY.

---
5. WHY IS THIS USEFUL?

A direct 2-D DFT requires approximately: 
M^2 N^2 operations.

That becomes very expensive for large images.
For example: M = N = 1024
would involve an enormous number of calculations.

Separability lets us replace the 2-D calculation with many
1-D calculations.

For a square image of size N x N:

    N rows x N-point DFT
    +
    N columns x N-point DFT

So we perform: 2N one-dimensional N-point DFTs.

This is already a major simplification.

---
6. BUT A 1-D DFT IS STILL EXPENSIVE

A direct N-point DFT is

X(k) = sum_{n=0}^{N-1} x(n) exp[-j 2*pi kn/N]

For each k, there are N terms.
There are N possible values of k.

Therefore: N x N = N^2
operations are required approximately.

So even after using separability, 
an image transform still requires many calculations.
(2N . N^2 )

This is where the FFT becomes important.

---
7. WHAT IS THE FFT?

FFT = Fast Fourier Transform.

DFT:
    Direct calculation
    approximately O(N^2)
FFT:
    Exploits mathematical structure
    approximately O(N log2 N)
So:
    DFT = mathematical transform
    FFT = fast algorithm for calculating the DFT
---
8. THE BASIC IDEA BEHIND THE FFT

Consider the N-point DFT:
X(k) = sum_{n=0}^{N-1} x(n) W_N^(kn)

where W_N = exp(-j 2*pi/N)

Suppose N is even.

Separate the samples into:
even n
odd n

For the even samples:
n = 2r

For the odd samples:
n = 2r + 1

Then:

X(k) = sum_{r=0}^{N/2-1} x(2r) W_N^(2rk) + 
       sum_{r=0}^{N/2-1} x(2r+1) W_N^((2r+1)k)

Because

 W_N^(2k) = exp(-j 2*pi (2k)/N)= exp(-j 2*pi k/(N/2))
this is exactly the Fourier factor for an N/2-point DFT.


Therefore we can write:

    X(k) = E(k) + W_N^k O(k)

where

    E(k) = sum_{r=0}^{N/2-1} x(2r) W_(N/2)^(rk)

and

    O(k) = sum_{r=0}^{N/2-1} x(2r+1) W_(N/2)^(rk)


So instead of calculating ONE N-point DFT,

we calculate:

    ONE N/2-point DFT of the even samples

and

    ONE N/2-point DFT of the odd samples.


9. THE PROCESS CAN BE REPEATED
------------------------------

Each N/2-point DFT can again be separated:

    N/2
       |
       v
    N/4 + N/4

Then:

    N/4
       |
       v
    N/8 + N/8

and so on.

Eventually we reach:

    N
    |
    N/2 + N/2
    |
    N/4 + N/4 + N/4 + N/4
    |
    N/8 + ...
    |
    ...
    |
    1-point DFTs


This repeated decomposition is
the fundamental idea behind the FFT.


10. WHY DOES THIS GIVE N log2(N)?
---------------------------------
At each level, all N samples are still involved.

But the number of levels is: log2(N)

because we repeatedly divide N by 2:
N
N/2
N/4
N/8
...
1

Therefore: number of levels = log2(N)

and approximately N operations are performed at each level.

Thus: FFT complexity = O(N log2 N)

Compare:
Direct DFT: O(N^2)

FFT: O(N log2 N)


11. SIMPLE EXAMPLE: N = 8
--------------------------

Suppose we have:

    x(0), x(1), x(2), x(3),
    x(4), x(5), x(6), x(7)


First split into even and odd indices:

    EVEN:
    x(0), x(2), x(4), x(6)

    ODD:
    x(1), x(3), x(5), x(7)


Then split again:

    x(0), x(4)
    x(2), x(6)

    x(1), x(5)
    x(3), x(7)


Then:

    x(0)     x(4)
    x(2)     x(6)
    x(1)     x(5)
    x(3)     x(7)


Eventually everything becomes a 1-point transform.

The FFT then combines these small transforms together
to reconstruct the complete 8-point DFT.


12. THE "BUTTERFLY"
-------------------

The basic FFT combination is often called a BUTTERFLY.

Suppose we have:

    A
    B

The FFT combines them approximately as:

    X = A + W B

    Y = A - W B

where W is the appropriate Fourier factor.

Diagrammatically:

             A -----------+------ X = A + WB
                          |
                          |
             B -- W ------+------ Y = A - WB


This small operation is repeated many times.

The entire FFT is essentially a huge collection of these
small butterfly operations.

---
13. NOW CONNECT THIS TO A 2-D IMAGE


Remember that the 2-D DFT is separable.

Therefore:

    2-D DFT
    =
    DFT of rows
    +
    DFT of columns


But instead of calculating each 1-D DFT directly,
we use the FFT.

Therefore:

    2-D FFT

    =
    FFT of every row
    +
    FFT of every column


For an M x N image:

    Step 1:
    Apply a 1-D FFT to every row.

    Step 2:
    Apply a 1-D FFT to every column.

The result is:

    F(u,v)



14. A SMALL CONCEPTUAL EXAMPLE
------------------------------

Imagine a 4 x 4 image:

    a b c d
    e f g h
    i j k l
    m n o p


First apply a 1-D FFT to each row:

    FFT(a b c d)
    FFT(e f g h)
    FFT(i j k l)
    FFT(m n o p)


Now the result is an intermediate 4 x 4 array.

Then apply a 1-D FFT to each column:

    FFT(column 1)
    FFT(column 2)
    FFT(column 3)
    FFT(column 4)


The final array is:

    F(u,v)


This is exactly the same 2-D DFT that we would obtain
using the original 2-D DFT equation.

The difference is that we calculated it much more efficiently.

---
17. WHY THIS MATTERS FOR IMAGE PROCESSING


Images can be large.

For example:

    1024 x 1024 image

A direct 2-D DFT is extremely expensive.

Using:

    separability
    +
    FFT

makes frequency-domain image processing practical.

This is why operations such as:

    Fourier filtering
    low-pass filtering
    high-pass filtering
    frequency-domain enhancement
    image restoration

can be implemented efficiently.
"""