"""
HOMOMORPHIC FILTERING

INTRODUCTION

Homomorphic filtering is a frequency-domain 
image enhancement technique used to:

1. Correct non-uniform illumination.
2. Enhance image contrast.
3. Emphasize fine details and edges.

The key idea is that an image can be modeled as the product of:

f(x,y) = i(x,y) * r(x,y)
where:
"*" means ordinary multiplication
i(x,y) = illumination component
r(x,y) = reflectance component

Because the image is formed by multiplication,
ordinary linear filtering cannot easily 
separate these two components.

Homomorphic filtering transforms 
the multiplication into addition, 
making the components easier to manipulate.

--
ILLUMINATION AND REFLECTANCE COMPONENTS
1. Illumination Component

The illumination component represents 
the amount of light falling on the scene.

Examples:
- Sunlight on a landscape.
- A lamp shining on an object.
- Shadows in an image.
- Brightness gradients across a photograph.

Characteristics:
- Changes slowly over space.
- Produces smooth intensity variations.
- Corresponds mainly to low frequencies.

Example:
Imagine a white wall 
illuminated more strongly on the left than the right.

Although the wall itself is uniform, 
the brightness changes gradually because of lighting.

This gradual variation belongs to the illumination component.


2. Reflectance Component

Reflectance describes how objects reflect light.

Examples:
- Texture of fabric.
- Human hair.
- Printed text.
- Tree bark.
- Edges between objects.

Characteristics:
- Changes rapidly over space.
- Produces abrupt intensity transitions.
- Corresponds mainly to high frequencies.

Example:
Black letters printed on white paper.
The transition from black to white happens suddenly.
This rapid change belongs to the reflectance component.

--
IMAGE FORMATION MODEL

A common model for image formation is:

f(x,y) = i(x,y) * r(x,y)

where:

f(x,y) = observed image
i(x,y) = illumination
r(x,y) = reflectance

Interpretation:

Observed image =
 Lighting effects × Object properties


EXAMPLE
Suppose a page is photographed under uneven lighting.

Illumination: Left side brighter than right side.
Reflectance: Text printed on the page.
Observed image:
Brightness variation from lighting
*
Dark letters from printing

The image combines both effects multiplicatively.


WHY IS THIS A PROBLEM?
--

Often we want:
- More uniform brightness.
- Better visibility of details.
- Reduced shadows.

But illumination and reflectance are mixed together.
Since:
f = i * r
a normal filter cannot easily separate them.


THE LOGARITHM TRICK
--

Take the logarithm of both sides:
ln(f) = ln(i*r)
Using: ln(ab) = ln(a) + ln(b)
gives: ln(f) = ln(i) + ln(r)

Now multiplication becomes addition.
This is the key idea behind homomorphic filtering.

Define:
z(x,y) = ln[f(x,y)]

Then: z(x,y) = ln[i(x,y)] + ln[r(x,y)]
Now illumination and reflectance contribute additively.

This allows linear filtering methods to be applied.

FREQUENCY INTERPRETATION
--
After the logarithm:

Low frequencies: Mainly illumination.

High frequencies: Mainly reflectance.

Therefore:
Reduce low frequencies to suppress illumination variations.
Boost high frequencies to enhance detail.


PROCESS OF HOMOMORPHIC FILTERING
--

Step 1
Start with image: f(x,y)

Step 2
Take logarithm: z(x,y) = ln[f(x,y)]
Multiplication becomes addition.

Step 3
Compute Fourier transform:
Z(u,v)

Step 4
Apply homomorphic filter:
S(u,v) = H(u,v) Z(u,v)

Step 5
Compute inverse Fourier transform:
s(x,y)

Step 6
Take exponential:
g(x,y) = exp[s(x,y)]
This reconstructs the image.

Final result:
- Reduced illumination effects.
- Enhanced contrast.
- Sharper details.

--
HOMOMORPHIC FILTER FUNCTION

A commonly used filter is:

H(u,v) =
(H_high - H_low) * [1 - exp(-c(D^2/D0^2))]
+ H_low

where:
D      = distance from frequency origin
D0     = cutoff frequency
c      = controls slope
H_low  = gain for low frequencies
H_high = gain for high frequencies

Meaning of Parameters
H_low < 1
Reduces low frequencies.
Therefore: Illumination variations are suppressed.

H_high > 1
Amplifies high frequencies.
Therefore: Reflectance details are enhanced.

D0 Controls transition location.
Small D0: More aggressive filtering.
Large D0: More gradual filtering.

c
Controls steepness.
Large c:
Sharper transition.
Small c:
Smoother transition.


FILTER SHAPE
--

Near frequency origin:
H ≈ H_low
Low frequencies are attenuated.


Far from origin:
H ≈ H_high
High frequencies are amplified.

--
Typical behavior:

Gain

H_high
  |
  |                 ___________
  |               /
  |             /
  |           /
  |         /
  |_______/
  |
  +-> D

      H_low

--
WHY IT WORKS

Illumination:
Slow variations
→ Low frequencies

Reflectance:
Rapid variations
→ High frequencies

Homomorphic filtering:
Attenuates low frequencies
and
boosts high frequencies.

Therefore:
Lighting effects decrease,
details become more visible.


PRACTICAL EXAMPLES

1. Document Images
Problem: Uneven page illumination.
Result: More uniform background and clearer text.


2. Medical Images
Problem: Brightness variations caused by imaging system.
Result: Improved visibility of structures.

3. Satellite Images
Problem: Lighting differences across terrain.
Result: Enhanced surface details.

4. Face Images
Problem: Shadows on the face.
Result: More uniform brightness and stronger facial details.


ADVANTAGES
--
- Simultaneously normalizes illumination.
- Enhances contrast.
- Improves detail visibility.
- Frequency-domain implementation.
- Works well for many real-world images.

LIMITATIONS
--
- Assumes illumination is mainly low-frequency.
- Assumes reflectance is mainly high-frequency.
- Can amplify noise.
- Parameter selection is important.
- Logarithm requires positive pixel values.

--
SUMMARY

Image model:f(x,y) = i(x,y) * r(x,y)

where:
i(x,y) = illumination
r(x,y) = reflectance

Illumination:
- Slow variation
- Low frequencies

Reflectance:
- Rapid variation
- High frequencies

Homomorphic filtering:

1. Take logarithm.
2. Convert multiplication to addition.
3. Transform to frequency domain.
4. Suppress low frequencies.
5. Enhance high frequencies.
6. Apply inverse transform.
7. Take exponential.

Main goal:
Reduce uneven lighting while 
enhancing image details and contrast.
"""


"""
SMALL NUMERICAL EXAMPLE

1. START WITH A SMALL IMAGE
Suppose our observed image is:

    x →
      20   30   40   50
      20   30   40   50
      20   30   40   50
      20   30   40   50

This image is getting gradually brighter 
from left to right.

For simplicity, imagine that there 
is also some fine detail inside the image.

The image formation model is: f(x,y) = i(x,y) × r(x,y)

where:
i(x,y) = illumination
r(x,y) = reflectance

---
2. TAKE THE LOGARITHM


We calculate:
z(x,y) = ln[f(x,y)]

For example:
ln(20) = 2.996
ln(30) = 3.401
ln(40) = 3.689
ln(50) = 3.912

So the image becomes approximately:

      2.996   3.401   3.689   3.912
      2.996   3.401   3.689   3.912
      2.996   3.401   3.689   3.912
      2.996   3.401   3.689   3.912


WHY DO THIS?

Originally: f = i × r
After logarithm: ln(f) = ln(i × r)
Using: ln(ab) = ln(a) + ln(b)
we get: ln(f) = ln(i) + ln(r)
Therefore: z(x,y) = ln(i(x,y)) + ln(r(x,y))
The illumination and reflectance components are now ADDITIVE.

---
3. TRANSFORM TO THE FREQUENCY DOMAIN

Now calculate the Fourier transform:
Z(u,v) = Fourier{z(x,y)}

We don't need to calculate every DFT value here
to understand the filtering process.

The important idea is:
The slowly changing brightness
(left side → right side)
produces mainly LOW frequencies.

Fine details and sharp changes
produce mainly HIGH frequencies.

The center of a centered Fourier
spectrum represents low frequencies.
Farther away from the center 
represents higher frequencies.

---
4. SUPPRESS LOW FREQUENCIES

Now we apply a homomorphic filter:
S(u,v) = H(u,v) Z(u,v)

Suppose we choose:
H_low  = 0.5
H_high = 2.0

Conceptually:
LOW FREQUENCY: Z × 0.5
HIGH FREQUENCY: Z × 2.0
So:
low frequencies → reduced
high frequencies → increased
Since Low frequencies contain mainly:
illumination variations
High frequencies contain mainly:
reflectance/detail variations
Therefore: 
illumination effect ↓
detail/contrast ↑

---
5. WHAT DOES THE FILTER DO?

Imagine the frequency spectrum contained:

LOW FREQUENCY COMPONENT
        amplitude = 10

HIGH FREQUENCY COMPONENT
        amplitude = 2

After filtering:
Low: 10 × 0.5 = 5
High: 2 × 2 = 4

Therefore the relative contribution 
of the high-frequency detail 
becomes much larger.

Before filtering:
low  = 10
high = 2

After filtering:
low  = 5
high = 4

The illumination variation has been weakened,
while the detail has been strengthened.

---
6. INVERSE FOURIER TRANSFORM

Now calculate:

s(x,y) = InverseFourier{S(u,v)}

This takes us back into the spatial domain.

Remember:
We are still in the LOGARITHMIC domain.
So s(x,y) is approximately:
s(x,y) = filtered ln(f(x,y))

The image now has:
- reduced slow brightness variation
- enhanced rapid intensity changes

But the pixel values are still logarithmic.

---
7. TAKE THE EXPONENTIAL

Finally: g(x,y) = exp[s(x,y)]
As the inverse operation of logarithm is exponential:
exp(ln(f)) = f


THE WHOLE PROCESS
---

Original image:
      f(x,y)
        |
        | logarithm
        v

z(x,y) = ln[f(x,y)]

        |
        | Fourier transform
        v

       Z(u,v)

        |
        | multiply by H(u,v)
        |
        | low frequencies × 0.5
        | high frequencies × 2
        v
      S(u,v)

        |
        | inverse Fourier transform
        v
       s(x,y)
        |
        | exponential
        v
      g(x,y)


WHAT HAPPENED PHYSICALLY?
---

Before:

IMAG = illumination × reflectance
After logarithm: 
LOG IMAGE = log(illumination) + log(reflectance)

Then frequency filtering:
LOW FREQUENCIES
→ illumination
→ reduce them

HIGH FREQUENCIES
→ reflectance/detail
→ increase them

Finally:
return from logarithmic values
to ordinary intensity values.


---
A VERY IMPORTANT POINT

The statement:
"low frequencies = illumination"
"high frequencies = reflectance"

is an APPROXIMATION.

It is not mathematically true that illumination contains
ONLY low frequencies and reflectance contains ONLY high
frequencies.

Real images can have:
illumination → some high-frequency components
reflectance → some low-frequency components

Homomorphic filtering works because illumination is
USUALLY much smoother than reflectance.

Therefore their frequency content tends to be different.

"""

"""
HOW DOES THE LOGARITHM HELP IN HOMOMORPHIC FILTERING?

The most important idea is:
The logarithm changes a MULTIPLICATIVE mixture into an
ADDITIVE mixture.

That makes the two effects much easier to manipulate
with a linear filter.


1. THE ORIGINAL PROBLEM
The observed image is: f(x,y) = i(x,y) × r(x,y)
where:
i(x,y) = illumination
r(x,y) = reflectance
We only observe f(x,y).

We do NOT have i and r separately.
So the image contains two effects multiplied together:
illumination × reflectance

For example:
illumination = 2
reflectance  = 5
image intensity = 2 × 5 = 10

If illumination changes:
illumination = 4
reflectance  = 5
image intensity = 4 × 5 = 20

The observed intensity changed, even though the object
(reflectance) did not change.

---
2. THE LOGARITHM CHANGES THE WAY THEY ARE MIXED

Take the logarithm:
ln(f) = ln(i × r)
Using: ln(a × b) = ln(a) + ln(b)
we get: ln(f) = ln(i) + ln(r)
This is the key transformation.

The information has not magically been separated.
They are still mixed. But they are now mixed
ADDITIVELY instead of MULTIPLICATIVELY.

---
3. WHY IS ADDITION BETTER?

Because our filtering operation is LINEAR.
For a linear transformation T:
T(a + b) = T(a) + T(b)
So after taking the logarithm:
ln(f) = ln(i) + ln(r)

we can conceptually write:
T[ln(f)] = T[ln(i) + ln(r)]
= T[ln(i)] + T[ln(r)]
This is the important mathematical advantage.

A linear filter can act on the SUM of the two
components in a predictable way.

---
4. NOW USE THEIR DIFFERENT FREQUENCIES

We still don't know which exact pixel values belong
to illumination or reflectance.

But we know something useful:
ILLUMINATION usually changes slowly.

Example: 100 → 102 → 104 → 106 → 108
Slow spatial change → low frequencies

REFLECTANCE can change rapidly.
Example: 100 → 100 → 100 → 20 → 20 → 20
Rapid spatial change → high frequencies

Therefore:
ln(i) → mainly low frequencies

ln(r) → mainly high frequencies

This is what allows us to use a frequency filter.

5. THE FILTER CAN NOW ACT ON THE TWO CONTRIBUTIONS
---
We take:

Z(u,v) = F{ln(f)}
Conceptually:
Z = F{ln(i)} + F{ln(r)}

Then apply:
S(u,v) = H(u,v) × Z(u,v)


Suppose:
H is small at low frequencies
H is large at high frequencies


Then approximately:
illumination contribution → reduced

reflectance/detail contribution → enhanced

We didn't need to know i and r separately.

---
6. WHY NOT JUST FILTER f DIRECTLY?

Because originally: f = i × r
The two effects are MULTIPLICATIVELY mixed.

A linear filter does not give us the nice relationship:
T(i × r) = T(i) × T(r)
That is NOT generally true.

But after logarithm:
ln(f) = ln(i) + ln(r)

and for a linear filter:
T[ln(i) + ln(r)] = T[ln(i)] + T[ln(r)]

This is the real reason the logarithm is useful.


---
In summary:

The logarithm does NOT separate illumination and reflectance.
Instead, it converts their multiplicative relationship into
an additive relationship, which is compatible with the
linearity of Fourier-based filtering.

Then we exploit the fact that illumination is usually
low-frequency and reflectance/detail is usually
high-frequency.
"""