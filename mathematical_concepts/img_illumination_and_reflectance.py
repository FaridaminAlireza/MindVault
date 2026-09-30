"""
An image f(x, y) can be expressed as 
the product of illumination and reflectance components:
f(x, y) = i(x, y)r(x, y). 
"""

"""
IMAGE FORMATION MODEL

Introduction

In digital image processing, 
we often represent the brightness recorded by a camera as:
f(x, y) = i(x, y) r(x, y)

This is called the illumination-reflectance model.

It describes a simple idea:
observed image = illumination × reflectance

The two components represent different physical aspects of the scene.

i(x, y) = illumination falling on the scene
r(x, y) = fraction of that illumination reflected by the object
f(x, y) = brightness/intensity recorded in the image

---
WHERE DOES THIS EQUATION COME FROM?

Imagine shining a lamp onto a piece of paper.
The amount of light reaching the paper 
depends on the illumination.

Let: i(x, y) = amount of light arriving at position (x, y)
Now suppose the paper reflects only part of that light.
For example: r(x, y) = 0.8
means that approximately 80% of the incident light is reflected.
Therefore, the amount of light leaving the surface is:
reflected light = incident light × reflectance
So: f(x, y) = i(x, y) r(x, y)

This is essentially a physical model of 
how image brightness is produced.

---
DOES f(x,y) = i(x,y)r(x,y) HAVE A RELATION TO FREQUENCY?


The equation itself is NOT a frequency-domain equation.
However, the model becomes very useful 
when we move into the frequency domain. Because 
illumination and reflectance tend to have different spatial
variation.

Slow spatial changes correspond mainly to low spatial frequencies.
Rapid spatial changes correspond mainly to high spatial frequencies.

---
WHY IS THE MODEL MULTIPLICATIVE?

Suppose the illumination doubles: i -> 2i
while reflectance stays the same.
Then: f = (2i)r = 2ir
The entire observed brightness doubles.

This makes physical sense: 
if you shine twice as much light on the same
surface, approximately twice as much light is
reflected toward the camera.

Therefore multiplication is a natural way 
to model the interaction between 
illumination and surface reflectance.

---
WHY IS THIS DIFFICULT FOR FREQUENCY FILTERING?

Frequency-domain filtering is particularly 
convenient for additive signals.

For example: f(x,y) = a(x,y) + b(x,y)
can conceptually be transformed into:
F(u,v) = A(u,v) + B(u,v)
So we can more directly manipulate the components.

But the illumination-reflectance model is:
f(x,y) = i(x,y) r(x,y)
It is MULTIPLICATIVE, not additive.
This makes it harder to separate the two components
directly using ordinary frequency-domain filtering.

---
THIS IS WHY THE LOGARITHM IS INTRODUCED

The logarithm converts multiplication into addition.
Starting with: f(x,y) = i(x,y) r(x,y)

Take the logarithm:
ln(f(x,y)) = ln(i(x,y) r(x,y))
Using: ln(ab) = ln(a) + ln(b)
we get: ln(f(x,y)) = ln(i(x,y)) + ln(r(x,y))

Now define:
z(x,y) = ln(f(x,y))
p(x,y) = ln(i(x,y))
q(x,y) = ln(r(x,y))

Then: z(x,y) = p(x,y) + q(x,y)
This is much easier to work with using frequency-domain filtering.

We can transform it: Z(u,v) = P(u,v) + Q(u,v)

Now we have converted 
the multiplicative image formation model 
into an additive model.

---
In short:
    f(x,y) = i(x,y)r(x,y)
    is a spatial-domain physical model.
    i(x,y) describes how much light reaches the surface.
    r(x,y) describes how much of that light the surface reflects.
    f(x,y) is the resulting image intensity.
    The equation itself is not about frequency.
    Its connection to frequency comes from the different spatial
    variation patterns of illumination and reflectance.
    This is the foundation of homomorphic filtering.
"""

"""
GRAYSCALE CONVERSION FROM RGB

A color pixel has three channel values:
R = red channel
G = green channel
B = blue channel

Example:
R = 60
G = 20
B = 10

METHOD 1: SIMPLE AVERAGE

Treat all three channels equally.

    Gray = (R + G + B) / 3

    Gray = (60 + 20 + 10) / 3
         = 90 / 3
         = 30

METHOD 2: WEIGHTED AVERAGE

Give different importance to each channel.
A common formula is: Gray = 0.299R + 0.587G + 0.114B

For our example:
Gray = 0.299(60) + 0.587(20) + 0.114(10) ≈ 31

Green receives the largest weight 
because human vision is more sensitive to green.

METHOD 3: MAXIMUM CHANNEL

Use the strongest channel:
Gray = max(R, G, B)
Gray = max(60, 20, 10) = 60

This is simple, but it does not represent 
perceived brightness very accurately.

METHOD 4: MINIMUM CHANNEL

Use the weakest channel:

Gray = min(R, G, B)
Gray = min(60, 20, 10)= 10

This can be useful for some specific image-processing operations,
but it is not a normal perceptual grayscale conversion.

METHOD 5: LUMINANCE-BASED CONVERSION

Instead of thinking of grayscale as simply "averaging RGB",
we can define it as an estimate of perceived brightness.

Conceptually: Gray = weighted combination of R, G, B

For example: Gray = 0.2126R + 0.7152G + 0.0722B

Then: Gray = 0.2126(60) + 0.7152(20) + 0.0722(10) ≈ 28

COMPARISON FOR THE SAME PIXEL
Input:
R = 60
G = 20
B = 10

Simple average: 30
Weighted RGB: 31
Luminance formula: 28
Maximum: 60
Minimum: 10


IMPORTANT IDEA
There is NOT one universal mathematical operation that "is"
grayscale.

Grayscale conversion is a way of reducing:
3 values per pixel to 1 value per pixel

For example:
RGB image:
R(x,y)
G(x,y)
B(x,y)
-->
f(x,y)

The exact calculation depends 
on the chosen conversion method.

For image-processing theory,
the important idea is:

    COLOR IMAGE
        |
        | combine color channels
        v
    GRAYSCALE IMAGE
        |
        v
    one intensity value f(x,y)
        |
        v
    spatial image processing
        |
        v
    Fourier transform / filtering / etc.

AND THIS CONNECTS TO THE ILLUMINATION-REFLECTANCE MODEL:
For a grayscale image: f(x,y) = i(x,y) * r(x,y)
Here f(x,y) is already a single image intensity value.
The detailed wavelength information has been collapsed into
the grayscale representation.

"""
