"""
2-D DFT
PERIODICITY AND CONJUGATE SYMMETRY

1. THE 2-D DFT

For an M×N image: f(x,y)

the 2-D DFT is: 
F(u,v) = ΣΣ f(x,y) e^[-j2π(ux/M + vy/N)]
where
x = 0,...,M-1
y = 0,...,N-1

and
u = 0,...,M-1
v = 0,...,N-1

The inverse transform is:

f(x,y) = (1/MN) ΣΣ F(u,v) e^[j2π(ux/M + vy/N)]

---
2. PERIODICITY OF THE 2-D DFT

We wish to prove: 
F(u+M,v) = F(u,v) and F(u,v+N) = F(u,v)

PROOF FOR THE u DIRECTION
Start with: 
F(u+M,v) = ΣΣ f(x,y) e^[-j2π((u+M)x/M + vy/N)]

Expand:
= ΣΣ f(x,y) e^[-j2π(ux/M + vy/N)] e^[-j2πMx/M]

Since: Mx/M = x
we obtain:
= ΣΣ f(x,y) e^[-j2π(ux/M + vy/N)] e^[-j2πx]

Because x is an integer: e^[-j2πx] = 1

Thus:
F(u+M,v) = ΣΣ f(x,y) e^[-j2π(ux/M + vy/N)]
= F(u,v)

Therefore: F(u+M,v)=F(u,v)

---
PROOF FOR THE v DIRECTION is done similarly.
---
RESULT

The frequency domain repeats every:

M samples horizontally and N samples vertically.

Thus: 

F(u+kM,v+lN) = F(u,v)
for any integers k and l.

---
3. PERIODICITY OF THE IMAGE

The inverse DFT implies:
f(x+M,y)=f(x,y) and f(x,y+N)=f(x,y)

Proof is identical.

Substituting x+M or y+N into the inverse DFT 
produces factors: e^(j2πu) or e^(j2πv) 
which are equal to 1.

Therefore the DFT assumes the image repeats infinitely:

... image image image ...

in both directions.

---
4. CONJUGATE SYMMETRY

Complex conjugate of a number:
(Complex conjugation changes the sign of the 
imaginary part of a complex number 
while keeping the real part unchanged.
Example: z = 3 + 4j -> z* = 3 - 4j
Geometrically, z* is the mirror image of z 
across the real axis in the complex plane.)

Complex conjugate of a function:
(For a complex-valued function, 
the conjugate is obtained by taking 
the complex conjugate of 
the function value at every point.
Example: f(x) = 3 + 4j + (2 - j)x
Then: f*(x) = 3 - 4j + (2 + j)x
In general, if: f(x) = a(x) + jb(x)
where a(x) and b(x) are real functions, then:
f*(x) = a(x) - jb(x)
For the Fourier transform, if:
F(u,v) = A(u,v) + jB(u,v)
then: F*(u,v) = A(u,v) - jB(u,v)
which is exactly the quantity that appears in
the conjugate symmetry property:
F(M-u,N-v) = F*(u,v) for real-valued images.)


Assume: f(x,y) is real-valued.
Then: f*(x,y)=f(x,y)

We will prove: F(M-u,N-v) = F*(u,v)

This is the 2-D conjugate symmetry property.

---
STEP 1
WRITE F(M-u,N-v)

Substitute: (M-u,N-v) into the DFT: 

F(M-u,N-v) = ΣΣ f(x,y) e^[-j2π((M-u)x/M + (N-v)y/N)]

Expand: = ΣΣ f(x,y) e^[-j2πMx/M] e^[j2πux/M] e^[-j2πNy/N] e^[j2πvy/N]

Since: e^[-j2πx]=1 and e^[-j2πy]=1

we obtain:
F(M-u,N-v) = ΣΣ f(x,y) e^[j2π(ux/M + vy/N)]

---
STEP 2
COMPUTE F*(u,v)

Start with:

F(u,v) = ΣΣ f(x,y) e^[-j2π(ux/M + vy/N)]

Take the complex conjugate:

F*(u,v) = ΣΣ f*(x,y) [e^(-j2π(ux/M + vy/N))]*

Because the image is real: f*(x,y)=f(x,y)
and: [e^(-jθ)]* = e^(jθ)

Thus:
F*(u,v) = ΣΣ f(x,y) e^[j2π(ux/M + vy/N)]
This is exactly the same expression obtained for:
F(M-u,N-v)

Therefore: F(M-u,N-v) = F*(u,v)

which proves conjugate symmetry.

---
5. MAGNITUDE SYMMETRY

Since conjugate numbers have identical magnitude:
|F(M-u,N-v)| = |F(u,v)|

Thus the magnitude spectrum is symmetric about the origin.

---
6. PHASE SYMMETRY

Let:
F(u,v) = A e^(jφ)

Then: F(M-u,N-v) = A e^(-jφ)

Therefore:
Magnitude: same
Phase: opposite sign
Hence: φ(M-u,N-v) = -φ(u,v)

---
7. CENTERED SPECTRUM VIEW
In image processing we often shift
the origin to the center using:

(-1)^(x+y) or fftshift.

Then the origin moves from:

(0,0) to: (M/2,N/2)

The conjugate symmetry becomes visually:
mirror symmetry about the center point.

Every bright point at one side of 
the spectrum has a matching point 
on the opposite side.
"""