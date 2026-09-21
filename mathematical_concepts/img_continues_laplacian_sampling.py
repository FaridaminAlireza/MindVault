"""
USING THE CONTINUOUS LAPLACIAN MODEL WITH A SAMPLED IMAGE

 INTRODUCTION

In digital image processing, 
an image is stored as a discrete array of pixels: f[m,n]


However, many theoretical results in image processing
are developed by treating the image as a continuous function: f(x,y)

This is especially common when 
deriving differentiation and
the Laplacian in the frequency domain.

For the continuous image:
∇²f(x,y) = ∂²f/∂x² + ∂²f/∂y²

The continuous Fourier-transform property gives:
F{∇²f(x,y)}
    = -4π²(u² + v²) F(u,v)

Therefore, the frequency-domain Laplacian filter is:
H_L(u,v) = -4π²(u² + v²)


The question is:
If the actual image is sampled and stored as pixels,
how can we use this continuous formula?

The answer is that we evaluate the continuous frequency-domain
formula at the discrete frequency locations provided by the DFT.


1. START WITH THE CONTINUOUS IMAGE

Imagine that there is an underlying continuous image: f(x,y)

This image exists conceptually at every position (x,y).

For example, we might have:
f(x,y) = some continuous brightness distribution

The continuous Laplacian is:
∇²f(x,y) = ∂²f/∂x² + ∂²f/∂y²


2. SAMPLE THE CONTINUOUS IMAGE

A digital camera or scanner 
does not store every possible value of f(x,y).

Instead, it samples the image on a grid.

If the sampling distances are Δx and Δy,
the samples are:

f[m,n] = f(mΔx, nΔy)

For example:


          x →
    •     •     •     •
    •     •     •     •
    •     •     •     •
    •     •     •     •


Each dot represents one pixel.

The digital image is therefore:


f[m,n]


rather than the continuous function:


f(x,y)


3. TAKE THE DFT OF THE SAMPLED IMAGE

We now take the 2-D DFT of the sampled image:


F[u,v] = DFT{f[m,n]}


The result is also discrete.

Instead of having a continuous frequency plane
with every possible (u,v), 
we have a finite grid of frequency samples:


          v
          ↑
    •  •  •  •  •
    •  •  •  •  •
    •  •  •  •  •
    •  •  •  •  •
          → u


Each point corresponds to one DFT frequency.

4. THE CONTINUOUS FORMULA STILL GIVES THE FILTER

The continuous mathematical derivation gave us:


H_L(u,v) = -4π²(u² + v²)


This formula describes the frequency response of the continuous
Laplacian.

We can evaluate this formula at each of the discrete frequency
locations produced by the DFT.

In other words:


continuous frequency plane
         ↓
choose the DFT frequency points
         ↓
evaluate -4π²(u² + v²) at those points
         ↓
obtain a discrete filter H[u,v]


5. FREQUENCY COORDINATES OF THE DFT

Suppose the image has M rows and N columns.

The DFT gives discrete frequency indices.

If the spatial sampling intervals are Δx and Δy, the physical
frequency coordinates are related to the DFT indices by:


u = k / (NΔx)

v = l / (MΔy)


where k and l are the corresponding frequency indices.

After accounting for frequency wrapping or centering, these give
positive and negative frequencies around the frequency origin.

For every frequency point, calculate:


D² = u² + v²


and then:


H_L[u,v] = -4π²D²


or equivalently:


H_L[u,v] = -4π²(u² + v²)


6. MULTIPLY THE DFT BY THE FILTER

Once the filter has been evaluated at all the DFT frequency points,
multiply it point-by-point with the image DFT:


G[u,v] = H_L[u,v] F[u,v]


Therefore:


G[u,v] = -4π²(u² + v²) F[u,v]


This is the sampled implementation of the continuous Laplacian
relationship.

7. TAKE THE INVERSE DFT

Finally, take the inverse DFT:


g[m,n] = IDFT{G[u,v]}


The result is a discrete image representing samples of the
Laplacian:


g[m,n] ≈ ∇²f(x,y)


at the image sampling locations.

8. SIMPLE NUMERICAL EXAMPLE

Suppose one of the DFT frequency points corresponds to:


u = 2
v = 3


Then:


D² = u² + v²

   = 2² + 3²

   = 4 + 9

   = 13


The continuous Laplacian filter evaluated at this frequency is:


H_L(u,v)
  = -4π²(13)

  = -52π²


Suppose the image DFT at this frequency is:


F(u,v) = 10


Then:


G(u,v)
  = H_L(u,v) F(u,v)

  = (-52π²)(10)

  = -520π²


The same calculation is performed at every DFT frequency point.

9. WHAT SAMPLING IS DOING


It is important to understand what sampling changes and what it
does not change.

The continuous theory gives us:


H_L(u,v) = -4π²(u² + v²)


Sampling does NOT mean that we have to replace this formula with a
finite-difference formula.

Instead, sampling means that we only have a finite set of image
samples and therefore a finite set of DFT frequency samples.

Conceptually:


CONTINUOUS FILTER

H_L(u,v) = -4π²(u² + v²)

             ↓
     evaluate only at
     DFT frequency points

             ↓

DISCRETE FILTER

H_L[u,v] = values of the continuous
           formula at those points


 10. WHY THE BOOK CAN USE THE CONTINUOUS FORMULA

This explains why a textbook can discuss a digital image while
writing:


F{∇²f(x,y)}
  = -4π²(u² + v²)F(u,v)


The book is using a continuous mathematical model to derive the
frequency-domain behavior.

The actual digital image is sampled.

Then the DFT provides discrete frequency samples where the
continuous frequency-domain expression can be evaluated.

So there are two levels:


THEORETICAL LEVEL

continuous image
      ↓
continuous Fourier transform
      ↓
continuous Laplacian formula

H_L(u,v) = -4π²(u² + v²)


COMPUTATIONAL LEVEL

sampled image
      ↓
DFT
      ↓
evaluate H_L(u,v) at DFT frequencies
      ↓
multiply
      ↓
inverse DFT
      ↓
sampled result


 11. DO NOT CONFUSE THIS WITH THE DISCRETE LAPLACIAN

There is another approach.

Instead of starting from the continuous Laplacian and then sampling
its frequency response, we can approximate the derivatives directly
using neighboring pixels.

For example, the standard 4-neighbor discrete Laplacian is:


∇²f[m,n] ≈
    f[m+1,n]
  + f[m-1,n]
  + f[m,n+1]
  + f[m,n-1]
  - 4f[m,n]


Its frequency-domain response is:


H_L[u,v]
  = -4[sin²(πu/M) + sin²(πv/N)]


This is a different mathematical model.

Therefore:


CONTINUOUS MODEL

H_L(u,v) = -4π²(u² + v²)


DISCRETE FINITE-DIFFERENCE MODEL

H_L[u,v]
  = -4[sin²(πu/M) + sin²(πv/N)]


Both are legitimate, but they come from different derivations.

12. WHY THEY LOOK SIMILAR AT LOW FREQUENCIES



The connection between the two becomes clearer using:


sin(x) ≈ x


for small x.

Therefore, at low frequencies:


sin(πu/M) ≈ πu/M


and:


sin(πv/N) ≈ πv/N


So the discrete finite-difference response behaves approximately
like a quadratic function of frequency, just as the continuous
Laplacian does.

This is why the continuous formula provides a useful description
of the behavior of the discrete image-processing operation.

13. THE MAIN IDEA



The most important point is:


A digital image can be treated as samples of an underlying
continuous image.


The continuous model is used to derive the mathematical behavior:


∇²f
  ↔
-4π²(u² + v²)F


The sampled image is then transformed using the DFT.

The continuous frequency response is evaluated at the DFT's discrete
frequency locations:


H[u,v] = -4π²(u² + v²)


and applied as:


G[u,v] = H[u,v]F[u,v]


Finally:


g[m,n] = IDFT{G[u,v]}


Thus:


continuous theory
      ↓
sampling
      ↓
discrete image
      ↓
DFT
      ↓
evaluate continuous filter
      ↓
frequency-domain multiplication
      ↓
inverse DFT
      ↓
discrete output


This is how a continuous mathematical model can be used to process
a sampled digital image.

"""