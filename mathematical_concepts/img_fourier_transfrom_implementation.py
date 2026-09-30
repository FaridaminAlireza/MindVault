"""
FOURIER TRANSFORM IMPLEMENTATION

INTRODUCTION
When working with real digital images,
we must know how the transform is actually computed
on a computer.The goal is to move from theory 
to actual computation.

* For an image of size M x N, the 2-D DFT is computed 
for every frequency coordinate (u,v).
* For each frequency coefficient,
all image pixels contribute to the calculation.
* As image size grows, the number of calculations becomes very large.
* Without efficient algorithms, Fourier-based image processing 
would be too slow for practical use.

---
IMPORTANT FOURIER TRANSFORM PROPERTIES

1. Linearity

In linear algebra,  a transformation T 
is called linear if it satisfies both:
1. Additivity  T(x+y)=T(x)+T(y)
2. Homogeneity (Scalability) T(ax)=aT(x)

for any vectors x,y and scalar a,
these two properties together imply:
T(ax+by)=aT(x)+bT(y)
which is the defining property of 
a linear transformation.

If: f1(x,y) <-> F1(u,v) and f2(x,y) <-> F2(u,v)
then: a*f1(x,y) + b*f2(x,y) <-> a*F1(u,v) + b*F2(u,v)
Meaning: The transform of a weighted sum is 
the weighted sum of the transforms.

This allows separate components to 
be processed independently and then combined.

(FOR THE FOURIER TRANSFORM
    The inputs are usually functions (signals/images).

    We can write: F{f(x) + g(x)} = F{f(x)} + F{g(x)}
    Or more compactly:
    F{f + g} = F{f} + F{g}
    Here: 
    - f(x) and g(x) are functions.
    - F is the Fourier transform operator.

    The "thing" being transformed is the entire function,
    not the variable x.

    For example: f(x) = sin(x)
    Here, x is the input/coordinate, while f is the
    function itself.

    The Fourier transform operates on the whole function f,
    not directly on the variable x.
)

2. Translation (Shifting)

SHIFTING PROPERTY OF THE FOURIER TRANSFORM

The shifting property says:
If: f(x) <--> F(u)
then shifting the function in the spatial domain:
f(x - x0)
produces a phase shift in the Fourier domain:
F(u) * exp(-j 2 pi u x0)

Therefore: 
Fourier{f(x - x0)} = F(u) * exp(-j 2 pi u x0)


SIMPLE EXAMPLE
Suppose:
f(x) = a signal 
and its Fourier transform is: F(u)
Now shift the signal to the right by 3 units:
g(x) = f(x - 3)
Its Fourier transform becomes:
G(u) = F(u) * exp(-j 2 pi u * 3)
So: G(u) = F(u) * exp(-j 6 pi u)

IMPORTANT IDEA
Spatial shift: f(x)  -->  f(x - x0)
causes: Frequency-domain phase change:
F(u)  -->  F(u) * exp(-j 2 pi u x0)

The magnitude does NOT change:
|G(u)| = |F(u)|
Only the PHASE changes.

* Moving an image or signal in space 
does not change which frequencies are present.
* Shifting an image in space changes 
the phase of its Fourier transform.

Therefore: Image position mainly affects phase information.

3. Frequency Shifting

Multiplying an image by (-1)^(x+y)
moves the Fourier spectrum origin 
from the upper-left corner to the center.

Before shifting: Low frequencies are at the corner.
After shifting: Low frequencies are at the center.

This makes the spectrum easier to visualize and filter.

4. Conjugate Symmetry

For real-valued images:
F(-u,-v) = conjugate(F(u,v))

Meaning: Part of the spectrum 
contains redundant information.

Knowing one side of the spectrum 
determines the other side.

5. Convolution Property

Spatial-domain convolution:

g(x,y) = f(x,y) * h(x,y)

corresponds to:

G(u,v) = F(u,v)H(u,v)

Meaning:
Convolution in the spatial domain becomes 
multiplication in the frequency domain.

This is the foundation of 
frequency-domain filtering.

6. Multiplication Property

Multiplication in the spatial domain corresponds
to convolution in the frequency domain.

This is essentially the reverse of the convolution property.

---
IMPLEMENTING FREQUENCY-DOMAIN FILTERING

A typical frequency-domain filtering procedure is:

Step 1: Start with image f(x,y).
Step 2: Multiply by (-1)^(x+y) to center the spectrum.
Step 3: Compute the DFT: F(u,v)
Step 4: Multiply by a filter: H(u,v)
Result: G(u,v) = H(u,v)F(u,v)
Step 5: Compute the inverse DFT.
Step 6: Multiply again by (-1)^(x+y) to restore the image arrangement.
Step 7: Take the real part and display the result.

The main idea is:
Spatial convolution is replaced by 
simple frequency-domain multiplication.

---
COMPUTATIONAL COST OF THE DFT

The direct computation of the DFT is expensive.
For an image with MN pixels:
The amount of computation grows approximately as:
(MN)^2
This becomes extremely large for typical image sizes.

Example:
512 x 512 image
MN = 262,144
Direct DFT computation requires 
a very large number of arithmetic operations.

---
FAST FOURIER TRANSFORM (FFT)

The FFT is not a different transform.
It computes exactly the same DFT.
The difference is that 
it computes the result much more efficiently.

Main idea: Break one large transform 
into many smaller transforms.

* Compute the smaller transforms.
* Combine the results efficiently.
* This divide-and-conquer approach
greatly reduces computation time.

COMPUTATIONAL ADVANTAGE OF FFT
--

Direct DFT: Approximately: (MN)^2 operations
FFT: Approximately: MN log2(MN) operations
This is a dramatic reduction in computational cost.

Example: 
For a 512 x 512 image:
Direct DFT: Very large computational cost.
FFT: Only a few million operations.
Because of this improvement, 
Fourier-based image processing becomes practical.


Without FFT:
- Frequency-domain filtering would be very slow.
- Large image transforms would be impractical.
- Many image-processing applications would not be feasible.
With FFT:
- Fourier transforms can be computed quickly.
- Large images can be processed efficiently.
- Frequency-domain filtering becomes practical.
- Most modern image-processing software relies
on FFT algorithms.


"""