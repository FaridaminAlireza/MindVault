"""
FOURIER TRANSFORM TRANSLATION PROPERTIES

This note proves the two translation properties of the 2-D DFT and
explains why (-1)^(x+y) appears when the frequency shift is M/2, N/2.

---
1. THE 2-D DFT

For an M x N image f(x,y), the 2-D DFT is:

F(u,v)
=
sum over x=0,...,M-1
sum over y=0,...,N-1
f(x,y) exp[-j2pi(ux/M + vy/N)]

We use:
f(x,y) <-> F(u,v)
to denote a Fourier transform pair.

---
2. SPATIAL-DOMAIN TRANSLATION PROPERTY

Suppose we shift the image by (x0,y0):
g(x,y) = f(x-x0, y-y0)

We want to find G(u,v).
By the definition of the DFT:

G(u,v) =
sum sum
g(x,y) exp[-j2pi(ux/M + vy/N)]

Substitute: g(x,y) = f(x-x0,y-y0)

Therefore:
G(u,v) =
sum sum
f(x-x0,y-y0)
exp[-j2pi(ux/M + vy/N)]


CHANGE OF VARIABLES:

Let:

x' = x - x0
y' = y - y0
Therefore:
x = x' + x0
y = y' + y0

Substitute into the Fourier exponential:

G(u,v) =
sum sum
f(x',y')
exp[-j2pi(u(x'+x0)/M + v(y'+y0)/N)]

SEPARATE THE EXPONENTIAL:

Expand: u(x'+x0)/M + v(y'+y0)/N =
ux'/M + ux0/M + vy'/N + vy0/N

Therefore:
G(u,v) =
sum sum
f(x',y')
exp[-j2pi(ux'/M + vy'/N)]
exp[-j2pi(ux0/M + vy0/N)]

The second exponential does not depend on x' or y',
so it can be taken outside the summation:

G(u,v) =
exp[-j2pi(ux0/M + vy0/N)] *
sum sum
f(x',y')
exp[-j2pi(ux'/M + vy'/N)]

But the remaining summation is exactly F(u,v).

Therefore:
G(u,v) =
F(u,v)
exp[-j2pi(ux0/M + vy0/N)]


FINAL RESULT
f(x-x0, y-y0) <-> F(u,v) exp[-j2pi(ux0/M + vy0/N)]


This is the SPATIAL-DOMAIN TRANSLATION PROPERTY.


IMPORTANT CONSEQUENCE:

The extra factor is: exp[-j2pi(ux0/M + vy0/N)]
This factor has magnitude 1.
Therefore: |G(u,v)| = |F(u,v)|
So translating an image changes 
the PHASE of its Fourier transform,
but does not change its MAGNITUDE.


---
3. FREQUENCY-DOMAIN TRANSLATION PROPERTY

The second property works in the opposite direction.
Suppose we multiply the image by a complex exponential:

g(x,y) = f(x,y) exp[j2pi(u0 x/M + v0 y/N)]

We will prove that this shifts the Fourier transform.

We want to calculate G(u,v).


START WITH THE DFT:

G(u,v) =
sum sum
g(x,y)
exp[-j2pi(ux/M + vy/N)]

Substitute g(x,y):

G(u,v)
=
sum sum
f(x,y)
exp[j2pi(u0 x/M + v0 y/N)]
exp[-j2pi(ux/M + vy/N)]


COMBINE THE EXPONENTIALS:
Using: exp(A) exp(B) = exp(A+B)

we get:

G(u,v) =
sum sum
f(x,y)
exp[j2pi(u0 x/M + v0 y/N) -j2pi(ux/M + vy/N)]

Group the x terms and y terms:

G(u,v) =
sum sum
f(x,y)
exp[-j2pi((u-u0)x/M + (v-v0)y/N)]

Now compare this with the definition 
of the Fourier transform:

F(a,b) =
sum sum
f(x,y)
exp[ -j2pi(ax/M + by/N)]

If we identify:
a = u-u0
b = v-v0

then:

G(u,v) = F(u-u0, v-v0)

Therefore:

f(x,y) exp[j2pi(u0 x/M + v0 y/N)] <-> F(u-u0, v-v0)

This is the FREQUENCY-DOMAIN TRANSLATION PROPERTY.

---
4. WHAT DOES "FREQUENCY-DOMAIN TRANSLATION" MEAN?

The original spectrum is: F(u,v)
After multiplying the image by: exp[j2pi(u0 x/M + v0 y/N)]
the new spectrum is: F(u-u0, v-v0)

So the entire Fourier spectrum is shifted by: (u0,v0)

Therefore:
multiplication by a complex exponential ->
translation of the Fourier spectrum

---
5. THE SPECIAL CASE u0 = M/2, v0 = N/2

Now consider:
u0 = M/2
v0 = N/2

The spatial-domain multiplication factor is:
exp[j2pi(u0 x/M + v0 y/N)]

Substitute u0 and v0:
=
exp[j2pi((M/2)x/M + (N/2)y/N)]

Simplify:
(M/2)x/M = x/2
(N/2)y/N = y/2

Therefore:
=
exp[j2pi(x/2 + y/2)] = exp[jpi(x+y)]

For integer k: exp(jpi k) = (-1)^k

Therefore:

exp[jpi(x+y)]= (-1)^(x+y)


Hence:

exp[j2pi((M/2)x/M + (N/2)y/N)] = (-1)^(x+y)


So the frequency-domain translation property becomes:
f(x,y)(-1)^(x+y) <-> F(u-M/2, v-N/2)

This is the mathematical reason for the commonly used
(-1)^(x+y) factor in image processing.


---
6. WHY DOES (-1)^(x+y) CENTER THE FOURIER SPECTRUM?

The ordinary DFT places the zero-frequency component at:
(u,v) = (0,0)

If we multiply the image by: (-1)^(x+y)
we are multiplying it by the complex exponential 
corresponding to:
u0 = M/2
v0 = N/2

The frequency-domain translation property 
tells us that the spectrum is shifted by: (M/2, N/2)
Therefore the zero-frequency component moves from:
(0,0) to: (M/2,N/2)

This is called CENTERING the Fourier spectrum.

---
7. A SMALL EXAMPLE OF (-1)^(x+y)

Because x and y are integers,
(-1)^(x+y) alternates between +1 and -1.

For example:

x y     x+y     (-1)^(x+y)

0 0      0          +1
0 1      1          -1
0 2      2          +1
0 3      3          -1

1 0      1          -1
1 1      2          +1
1 2      3          -1
1 3      4          +1

So the image is multiplied by a checkerboard pattern:

+1  -1  +1  -1
-1  +1  -1  +1
+1  -1  +1  -1
-1  +1  -1  +1

This checkerboard multiplication shifts the Fourier spectrum to
the center.


---
8. THE TWO TRANSLATION PROPERTIES TOGETHER


PROPERTY 1: SHIFT THE IMAGE


f(x-x0,y-y0) <-> F(u,v) exp[-j2pi(ux0/M + vy0/N)]

Meaning:

SHIFT in spatial domain ->
PHASE CHANGE in frequency domain

The magnitude does not change:
|G(u,v)| = |F(u,v)|


PROPERTY 2: SHIFT THE SPECTRUM

f(x,y) exp[j2pi(u0 x/M + v0 y/N)] <-> F(u-u0,v-v0)


Meaning:
MULTIPLICATION by a complex exponential ->
SHIFT in frequency domain

Special case:
u0 = M/2
v0 = N/2

gives:
f(x,y)(-1)^(x+y) <-> F(u-M/2,v-N/2)

This shifts the Fourier spectrum so that the 
zero-frequency component is at the center.
"""

"""
For the spatial translation property, 
you can think of it literally 
as moving the objects in the image.

Original image:

+----------------+
|                |
|   ███          |
|   ███          |
|                |
+----------------+
   object


Shift to the right:

+----------------+
|                |
|          ███   |
|          ███   |
|                |
+----------------+
          object


g(x,y) = f(x-x0, y-y0)
The object's shape and intensity values 
stay the same, but its (x,y) coordinates change.

"""