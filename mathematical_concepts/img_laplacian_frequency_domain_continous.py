"""
THE LAPLACIAN IN THE FREQUENCY DOMAIN
---
1. INTRODUCTION

The Laplacian is a second-order derivative operator.
Its purpose is to measure how rapidly image 
intensity changes in space.

Because derivatives respond strongly to rapid changes,
the Laplacian is useful for:

* Edge enhancement
* Sharpening
* Highlighting fine detail
* Detecting regions of rapid intensity change

Unlike gradient operators, 
which measure change in a specific direction, 
the Laplacian measures change equally in all directions.
Therefore, it is an isotropic operator.
"Isotropic" means: 
the response is independent of direction.

---
2. THE SPATIAL-DOMAIN LAPLACIAN

For a continuous image: f(x,y)
the Laplacian is defined as:
∇²f(x,y) = d²f/dx² + d²f/dy²

Interpretation:
The Laplacian measures curvature.

---
Example:

Suppose intensity changes slowly:
10 11 12 13 14
The slope is nearly constant.
The second derivative is small.
Therefore:
Laplacian is small.


Now suppose:
10 10 10 100 100
The intensity changes abruptly.
The slope changes suddenly.
The second derivative becomes large.
Therefore:
Laplacian is large.

---
3. WHY STUDY THE LAPLACIAN IN THE FREQUENCY DOMAIN?

The advantage is that 
differentiation becomes multiplication.
Instead of calculating derivatives directly,
we multiply by a simple function.

In spatial processing:
* Compute second derivatives.
* Apply Laplacian masks.

In frequency processing:
* Transform image to frequency domain.
* Apply an equivalent frequency-domain operation.
* Transform back.

---
4. FOURIER TRANSFORM PROPERTY OF DERIVATIVES

The key result is:
Differentiation in space ⇔ Multiplication in frequency
This is the foundation of the Laplacian frequency-domain formula.

For a first derivative:
d/dx becomes multiplication by: j2πu in the frequency domain.

Similarly:
d/dy becomes multiplication by: j2πv

---
(For continuous Fourier transform)
5. FOR THE SECOND DERIVATIVE

Let:
F(u,v) be the Fourier transform of: f(x,y)

First derivative:
Fourier[d f/dx] = j2πu F(u,v)

Take another derivative:
Fourier[d²f/dx²] = (j2πu)² F(u,v)

---
6. SIMPLIFYING THE SQUARE

Recall: j² = -1

Therefore:

(j2πu)² = -4π²u²

Thus: 
Fourier[d²f/dx²] = -4π²u² F(u,v)

Similarly:
Fourier[d²f/dy²] = -4π²v² F(u,v)

---
7. DERIVING THE LAPLACIAN FORMULA

The Laplacian is:

d²f/dx² + d²f/dy²

Using linearity:

Fourier[Laplacian(f)]

= Fourier[d²f/dx²] + Fourier[d²f/dy²]

Substitute previous results:

= -4π²u²F(u,v) + -4π²v²F(u,v)

Factor out F(u,v):

= -4π²(u²+v²)F(u,v)

This is the fundamental 
frequency-domain Laplacian formula for continous domain

---
9. WHY DOES THIS EMPHASIZE HIGH FREQUENCIES?

Observe the factor:
(u²+v²)


Near the center:
u ≈ 0
v ≈ 0
Therefore:
(u²+v²) ≈ 0
Low frequencies are multiplied 
by a very small number.

Far from the center:
u and v are large.
Therefore:
(u²+v²)
becomes large.
High frequencies are amplified strongly.


Thus:
low frequencies → weak response

high frequencies → strong response

This is why the Laplacian behaves
as a highpass operator.

---
10. RADIAL INTERPRETATION

Distance from the frequency origin is:
D² = u² + v²

Therefore the Laplacian multiplier
may also be written as: -4π²D²

This shows that the response depends 
only on distance from the origin.

Therefore:
The Laplacian is isotropic.
Its behavior is identical in all directions.

---
11. LAPLACIAN FILTER SHAPE

At the frequency origin:
u = 0
v = 0
Therefore:
H = 0

Moving away from the center:
D increases
Therefore:
H increases proportionally to D²

Unlike lowpass filters, the Laplacian is weakest 
at the center and strongest near the outer frequencies.

---
12. SHARPENING USING THE LAPLACIAN

The Laplacian itself highlights rapid changes.
To sharpen an image, 
combine the original image with its Laplacian.

General form:

Sharpened Image = Original Image + Laplacian Image
The sign convention depends 
on the definition used for the Laplacian.

Some texts use: Original + Laplacian
Others use: Original - Laplacian
Both are equivalent after accounting for sign conventions.

---
13. FREQUENCY-DOMAIN SHARPENING FORMULA

Let:
F(u,v) be the image transform.
The Laplacian transform is: -4π²(u²+v²)F(u,v)

The sharpened image transform becomes:
G(u,v) = F(u,v) * [-4π²(u²+v²)F(u,v)]

Factor out F(u,v): G(u,v) = [1 + 4π²(u²+v²)]F(u,v)

This is the frequency-domain sharpening filter.

---
14. INTERPRETING THE SHARPENING FILTER

The multiplier is: 1 + 4π²(u²+v²)

At low frequencies:
u²+v² ≈ 0
Multiplier ≈ 1
Low frequencies remain almost unchanged.


At high frequencies:
u²+v² is large
Multiplier becomes much larger than 1
High frequencies are amplified.
Therefore:
fine detail
edges
texture
are enhanced.

---
Key properties of Laplacian Filter:

* Isotropic.
* Depends only on distance from the origin.
* Suppresses low frequencies.
* Amplifies high frequencies.
* Acts as a highpass operator.
* Useful for image sharpening.
* Frequency-domain sharpening filter:

H(u,v) = 1 + 4π²(u²+v²)

or equivalently:

H(u,v) = 1 + 4π²D²

This filter preserves low frequencies while 
increasingly amplifying higher frequencies 
as distance from the frequency origin increases.

"""