"""
1. 1D Discrete Fourier Transform (DFT)

Forward DFT:
F(u) = sum from x=0 to M-1 of: 
f(x) * exp( -j*2*pi*u*x/M )

where:
* f(x) is the original signal
* F(u) is the frequency representation
* M is the number of samples
* u is the frequency index

Inverse DFT:
f(x) = (1/M) * sum from u=0 to M-1 of: 
F(u) * exp( +j*2*pi*u*x/M )

Interpretation:
f(x) -> position/spatial domain
F(u) -> frequency domain

The DFT changes the representation 
but does not lose information.

---
2. 2D Discrete Fourier Transform

Forward DFT:

F(u,v) =
sum over x=0..M-1
sum over y=0..N-1
f(x,y) * exp( -j*2*pi*(u*x/M + v*y/N) )


Inverse DFT:

f(x,y) =
(1/(M*N))*
sum over u=0..M-1
sum over v=0..N-1
F(u,v) * exp( +j*2*pi*(u*x/M + v*y/N) )


Interpretation:

f(x,y) -> image
F(u,v) -> 2D frequency content
u -> horizontal frequency
v -> vertical frequency

---
3. Separability of the 2D DFT

The exponential can be written as:
exp( -j*2*pi*(u*x/M + v*y/N) )

= exp( -j*2*pi*u*x/M ) * exp( -j*2*pi*v*y/N )
---
4. If we
1. Apply DFT to rows
2. Apply DFT to columns
This produces exactly the same result as a full 2D DFT.


1. Apply DFT to rows
After transforming only rows:

R(u,y) =
sum over x
f(x,y) * exp( -j*2*pi*u*x/M )

R(u,y) tells us:
"How much horizontal frequency u exists in row y?"
The vertical coordinate y is still untouched.


2. Apply DFT to columns
Now transform vertically:

F(u,v) =
sum over y
R(u,y) * exp( -j*2*pi*v*y/N )

For each horizontal frequency u,
measure how that frequency changes vertically.

This is how combined horizontal/vertical 
frequencies are captured.

---
5. Frequency Resolution

Suppose:

M = number of samples
delta_x = spacing between samples
Total sampled length: L = M * delta_x

Smallest nonzero frequency: 1/L

The first non-constant Fourier basis 
contains (u=1), exactly one cycle across 
the entire observed length L. 
Frequency is cycles per unit length, 
so that basis has frequency 1/L. 
The DFT then samples frequencies at integer 
multiples of this fundamental frequency.

Therefore: delta_f = 1/(M*delta_x)
which is the spacing between neighboring DFT frequency bins.

Physical frequency corresponding to DFT index u:
f_u = u/(M*delta_x)

---

6. Complex Representation

A Fourier coefficient is complex:

F(u,v) = a + j*b

or

F(u,v) = |F(u,v)| * exp(j*phi(u,v))

where:
|F(u,v)| = magnitude
phi(u,v) = phase


Spectrum: S(u,v) = |F(u,v)|

How strong each frequency is.

Large magnitude
-> frequency strongly present

Small magnitude
-> frequency weakly present

Phase: 
phi(u,v) = atan( Imaginary(F) / Real(F) )

Where the frequency pattern is positioned.

Magnitude:
"What pattern exists?"

Phase:
"Where is that pattern located?"

---
7. Power Spectrum

Power: P(u,v) = |F(u,v)|^2
Energy associated with each frequency.

---
8. Complex Conjugate Rules

If: z = a + jb
then z* = a - jb

Important rules:

(a+b)* = a* + b*

(a-b)* = a* - b*

(ab)* = a* b*

(a/b)* = a* / b*

(z*)* = z

(exp(j*theta))* = exp(-j*theta)

If a is real:

a* = a

---
9. Conjugate Symmetry

If f(x,y) is real:

F(u,v) = F*(-u,-v)

Equivalent finite DFT form:

F(u,v) = F*( M-u , N-v )
(indices interpreted modulo M and N)

Consequences:

Magnitude: |F(u,v)| = |F(-u,-v)|

Phase: phase(-u,-v) = -phase(u,v)

---
10. Spectrum Centering

Multiply image by: (-1)^(x+y)

Equivalent form:
(-1)^(x+y) = exp(j*pi*x) * exp(j*pi*y)

Define:
g(x,y) = f(x,y) * (-1)^(x+y)

Its DFT becomes:

G(u,v) = F(u-M/2 , v-N/2)

(modulo M,N)

Meaning:
The entire spectrum shifts by half its width and height.

Why This Centers the Spectrum:

Originally:

DC component = F(0,0)

After multiplication:

DC moves to:

(M/2 , N/2)

Therefore:
low frequencies move to the center
high frequencies move toward the edges

This is why Fourier spectra are 
usually displayed after centering.


But, Why DC Is Normally in the Corner:

The DFT stores frequencies using indices:

0,1,2,...,M-1
and
0,1,2,...,N-1

The DC component is: F(0,0)
which is the first element of the array.

Therefore when displayed as an image:
DC appears in the upper-left corner.

This is an indexing convention,
not a physical property.
"""