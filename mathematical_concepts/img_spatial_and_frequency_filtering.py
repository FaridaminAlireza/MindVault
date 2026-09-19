"""
PART: SPATIAL AND FREQUENCY DOMAIN FILTERING

Introduction

A filter can be described in two equivalent ways:

1. In the spatial domain, using a filter function or kernel h(x,y).
2. In the frequency domain, using a frequency response H(u,v).

The two descriptions are related by the Fourier transform: 
h(x,y) <-> H(u,v)

This means that a spatial filter and 
its frequency-domain representation are 
two descriptions of the same filter.

1. SPATIAL FILTERING AS CONVOLUTION

If f(x,y) is an image and h(x,y) is a spatial filter,
the filtered image is: g(x,y) = f(x,y) * h(x,y)
Here, * means convolution.

For a discrete image, 
convolution can be written conceptually as:

g(x,y) = sum over m,n of f(m,n) h(x-m,y-n)

The basic operation is:
1. Take a value from the image.
2. Multiply it by the corresponding value of the shifted filter.
3. Add the products.
4. Repeat this at every image location.
This is the usual sliding-window interpretation of convolution.

---
2. VIEWING AN IMAGE AS A COLLECTION OF IMPULSES

An image can also be viewed as a collection of impulses.
Each pixel is treated as an impulse whose strength 
is equal to its gray-level value.

For an image containing several nonzero pixels:
f(x,y) = sum over k of ak delta(x-xk,y-yk)

where:
ak = intensity of pixel k
(xk,yk) = position of pixel k
delta = impulse function

For example, if an image contains two bright pixels:
pixel 1: intensity 2 at position (1,0)
pixel 2: intensity 1 at position (2,2)
then: f(x,y) = 2 delta(x-1,y) + delta(x-2,y-2)

---
3. CONVOLUTION OF AN IMAGE WITH A FILTER

Start with the normal convolution:
g(x,y) = f(x,y) * h(x,y)

Substitute the impulse representation of the image:
g(x,y) = [sum over k of ak delta(x-xk,y-yk)] * h(x,y)

Using the distributive property of convolution:
g(x,y) = sum over k of ak [delta(x-xk,y-yk) * h(x,y)]

Now use the impulse property:
delta(x-xk,y-yk) * h(x,y) = h(x-xk,y-yk)

Therefore:
g(x,y) = sum over k of ak h(x-xk,y-yk)

---
WHAT THIS FORMULA MEANS

The formula: g(x,y) = sum over k of ak h(x-xk,y-yk)
can be understood in four steps:

1. Find a pixel with intensity ak.
2. Take a copy of the filter h.
3. Shift that copy so that it is centered 
at the pixel position (xk,yk).
4. Multiply the copy by the pixel intensity ak.

Then repeat this for every pixel and
add all the copies together.

---
THIS PRODUCE BLURRING

Suppose h(x,y) is a blurring filter.

A single impulse is a very sharp point:
delta(x,y)

After convolution:
delta(x,y) * h(x,y) = h(x,y)

Therefore, a single sharp pixel 
becomes the shape of the filter.

If h is spread out, the originally sharp pixel
becomes spread out.

For an entire image, 
every pixel produces a shifted copy of h:

g(x,y) = sum over k of ak h(x-xk,y-yk)
The copies overlap and add together.
This produces the blurred image.

---
4. THE IMPULSE RESPONSE

The response of a filter to 
an impulse is particularly important.

If the input is:

f(x,y) = delta(x,y)

then: g(x,y) = delta(x,y) * h(x,y)
and therefore: g(x,y) = h(x,y)

So h(x,y) is called the impulse response of the system.

This is why examining what a filter does 
to a single impulse tells us a great deal
about the filter itself.

---
5. CONNECTION BETWEEN SPATIAL AND FREQUENCY DOMAIN FILTERS

Suppose: f(x,y) <-> F(u,v)
and: h(x,y) <-> H(u,v)

The convolution theorem states:
f(x,y) * h(x,y) <-> F(u,v) H(u,v)

Therefore:

spatial convolution ->
frequency-domain multiplication

So filtering can be performed in either domain:

Spatial domain: g(x,y) = f(x,y) * h(x,y)
Frequency domain: G(u,v) = F(u,v) H(u,v)

---
A frequency-domain filter H(u,v) 
corresponds to a spatial-domain filter h(x,y).

They are Fourier transform pairs:
h(x,y) <-> H(u,v)

Therefore, if we design a filter in the frequency domain,
we can obtain its spatial-domain filter 
by taking the inverse Fourier transform:

h(x,y) = inverse Fourier transform of H(u,v)
Conversely:
H(u,v) = Fourier transform of h(x,y)

---
6. WHY FREQUENCY-DOMAIN FILTERING CAN BE FASTER

Direct spatial convolution can 
require many multiplications and additions.

For a 1D signal with N points and a filter with M points,
the direct approach is roughly proportional to: N times M
For large filters, this can become expensive.

Using the FFT, frequency-domain filtering
involves approximately:

FFT of image -> FFT of filter -> multiply the two spectra ->
inverse FFT

The FFT has approximately: N log N
computational complexity rather than: 
N squared for a direct Fourier transform.

---
WHEN SPATIAL FILTERING MAY STILL BE BETTER

Frequency-domain filtering is not automatically 
faster for every filter.
For very small spatial kernels, such as:
3 by 3
5 by 5
7 by 7

direct spatial filtering can be very efficient.

For very large filters, frequency-domain filtering
becomes increasingly attractive.

Therefore, the choice depends on the image size,
filter size, implementation, and hardware.

---
7. THE FREQUENCY DOMAIN AS A LABORATORY

The frequency domain is useful not only 
because of computational efficiency.
It also provides a way to 
understand the structure of an image.

Low spatial frequencies are associated mainly with:
* smooth intensity variations
* large-scale structures
* gradual changes

High spatial frequencies are associated mainly with:
* edges
* fine details
* fine texture
* rapid intensity changes

Therefore, frequency-domain filtering allows us to ask:

Which frequencies should I keep?
Which frequencies should I remove?
Which frequencies should I strengthen?

For example:
Low-pass filtering:
keep low frequencies and 
suppress high frequencies.

High-pass filtering:
suppress low frequencies and
keep or emphasize high frequencies.

---
8. THE IDEAL LOW-PASS FILTER

An ideal low-pass filter makes an abrupt decision.

H(u,v) = 1 inside the cutoff
H(u,v) = 0 outside the cutoff

The cutoff is usually described using 
the distance from the center of the frequency domain:
D = square root of ((u-u0) squared + (v-v0) squared)

Then:
H(u,v) = 1 if D is less than or equal to D0
H(u,v) = 0 if D is greater than D0

Here:
D0 = cutoff frequency

The filter therefore keeps frequencies inside a circle 
and removes frequencies outside it.

---
WHY AN IDEAL LOW-PASS FILTER PRODUCES RINGING

The problem with the ideal low-pass filter is
its abrupt transition:
from 1 inside the cutoff to 0 outside the cutoff

An abrupt cutoff in the frequency domain 
produces an oscillating spatial-domain impulse response.

In the 1D case, the impulse response has the form:

h(x) = sin(2 pi D0 x) / (pi x)
This is a sinc-like function.

Instead of smoothly decreasing to zero, it oscillates:

positive
negative
positive
negative
...

These oscillations are responsible for ringing.

---
9. RINGING IN AN IMAGE

Consider a sharp edge.

Without ringing:
dark -> smooth transition -> bright

With ringing:
dark -> undershoot -> overshoot -> transition -> bright

The oscillations appear around the sharp transition.

In a 2D image, these oscillations can appear as 
bright and dark rings around structures or edges.

The important relationship is:

sharper frequency cutoff -> stronger spatial oscillations -> more ringing

A smoother frequency-domain transition 
generally produces less ringing.

---
A FIVE-IMPULSE EXAMPLE PRODUCES RINGING

Suppose the image consists of five bright pixels
on a black background.

Each pixel is treated as an impulse:
f(x,y) = sum from k=1 to 5 of ak delta(x-xk,y-yk)

After filtering:
g(x,y) = sum from k=1 to 5 of ak h(x-xk,y-yk)

If h is an ideal low-pass filter's impulse response,
then each pixel produces:
a shifted and scaled oscillating function.
Therefore, the output is the sum of five oscillating copies.

When these copies overlap, their oscillations can
interfere with one another.
If the ringing is strong enough, 
the interference creates visible distortion.

---
10. POWER SPECTRUM

The Fourier transform of an image is generally complex:
F(u,v) = real part + imaginary part

The magnitude spectrum is:
M(u,v) = magnitude of F(u,v)

The power spectrum is:
P(u,v) = magnitude of F(u,v) squared

The power spectrum tells us 
how strongly different spatial frequencies 
are present in the image.

It is not simply a binary map.
If: P(u,v) = 0 that frequency has no power.

If P is small, the frequency component is weak.
If P is large, the frequency component is strong.

---
11. WHY THE FOURIER IMAGE IS USUALLY BLACK AND WHITE

The actual Fourier transform F(u,v) 
is generally complex-valued.
However, when we display the magnitude or power spectrum
as an image, we map numerical values to grayscale.

For example:
low value -> dark
high value -> bright

Therefore, a black-and-white Fourier spectrum 
does not mean that its values are only 0 and 1.

The grayscale image is simply 
a visual representation of 
numerical frequency values.

---
12. POWER IN A REGION OF THE FREQUENCY DOMAIN

A particular region of the frequency domain
contains a range of frequencies.

For example, a circular ring can represent
a range of distances from the center.

The total power in that region can be calculated as:
total power = sum of |F(u,v)| squared over the region

This tells us how much image energy is contained 
in that range of spatial frequencies.

A radial analysis can therefore divide
the frequency domain into concentric rings:

ring 1: very low frequencies
ring 2: low frequencies
ring 3: medium frequencies
ring 4: high frequencies
...

and measure the power in each ring.

This produces a radial description of how 
the image's energy is distributed across 
spatial frequencies.
"""