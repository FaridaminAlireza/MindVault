"""
BUTTERWORTH LOWPASS FILTER:
OSCILLATIONS AND THE RINGING EFFECT

1. INTRODUCTION

The Butterworth Lowpass Filter (BLPF) is used to reduce high-frequency components of an image.

Its frequency-domain formula is:

H(D) = 1 / [1 + (D/D0)^(2n)]

where:

D  = distance from the center of the frequency plane
D0 = cutoff frequency
n  = filter order

The important parameter here is n.

As n increases, the Butterworth filter becomes sharper and approaches the Ideal Lowpass Filter.

This increasing sharpness is directly related to the ringing effect.

---

2. WHAT HAPPENS AS n INCREASES?

---

For a small n, the transition from passing frequencies to suppressing frequencies is gradual.

For a large n, the transition becomes very sharp.

Conceptually:

Small n:

H
1 |████████
|        ███
|           ███
0 |--------------████
+---------------------> D

Large n:

H
1 |██████████████████
|                  |
|                  |
0 |------------------████
+---------------------> D

Therefore:

n increases
|
v
transition becomes sharper
|
v
filter approaches Ideal Lowpass Filter

---

3. IMPORTANT: THE FREQUENCY FILTER ITSELF DOES
   NOT OSCILLATE BETWEEN POSITIVE AND NEGATIVE

---

The Butterworth frequency response is:

H(D) = 1 / [1 + (D/D0)^(2n)]

Since:

D >= 0
D0 > 0

and:

(D/D0)^(2n) >= 0

we always have:

H(D) >= 0

Therefore, the gray-level profile through the center of the frequency-domain Butterworth filter does NOT alternate between positive and negative values.

As n increases, it becomes sharper, but it remains nonnegative.

So we must distinguish between two different things:

1. Frequency-domain filter H(u,v)
2. Spatial-domain filter h(x,y)

---

4. FROM FREQUENCY DOMAIN TO SPATIAL DOMAIN

---

The frequency-domain filter H(u,v) is transformed into a spatial-domain filter by taking its inverse Fourier transform:

H(u,v)
|
| inverse Fourier transform
v
h(x,y)

The function h(x,y) is the spatial-domain impulse response or filter kernel.

This is where positive and negative oscillations can appear.

---

5. SPATIAL-DOMAIN OSCILLATIONS

---

For a high-order Butterworth filter, the spatial-domain impulse response can contain alternating positive and negative regions.

Conceptually:

```
      positive
         +
         |
         |\
         | \
```

-------------|--------/---------/--------> x
|   \    /  \       /  
|    _*/    _*___/
|
-
negative

So the spatial-domain kernel can behave approximately like:

positive
negative
positive
negative
positive
...

These oscillations become stronger as the frequency-domain cutoff becomes sharper.

---

6. WHY DOES A SHARP CUTOFF PRODUCE OSCILLATIONS?

---

The important relationship is:

Sharp frequency-domain transition
|
v
Oscillatory spatial-domain response

A sudden change in frequency space requires oscillatory behavior in the spatial domain.

The Ideal Lowpass Filter is the extreme example.

Its frequency response is:

H(D) = 1    if D <= D0
H(D) = 0    if D > D0

There is an abrupt jump at D0.

When we take the inverse Fourier transform of this sharp cutoff, the spatial-domain response becomes sinc-like and oscillatory.

Conceptually:

```
    +
    |
    |\
    | \
```

--------|--------/------/------/------> x
|   \    /  \    /  \    /  
|    _*/    _*/    __/
|
-

Therefore, the sharper the frequency-domain cutoff, the stronger the tendency for oscillations in the spatial domain.

---

7. CONNECTION WITH BUTTERWORTH ORDER n

---

The Butterworth filter provides a smooth transition.

For low n:

low n
|
v
smooth frequency transition
|
v
weaker spatial oscillations
|
v
less ringing

For high n:

high n
|
v
sharp frequency transition
|
v
stronger spatial oscillations
|
v
more ringing

Therefore:

n increases
|
v
Butterworth becomes closer to Ideal Lowpass
|
v
spatial-domain oscillations become stronger
|
v
ringing becomes stronger

---

8. WHAT IS RINGING?

---

Ringing is the appearance of oscillating bright and dark regions near sharp transitions in an image.

Suppose the original image contains a sharp edge:

0  0  0  0  100  100  100  100

Ideally, we would like the filtered result to remain approximately:

0  0  0  0  100  100  100  100

But an oscillatory spatial filter can produce something like:

0  -5  8  95  105  98  102  100

Notice the values around the edge:

-5
8
95
105
98
102

The values alternate around the correct transition.

There is:

undershoot
|
v
negative deviation

followed by:

overshoot
|
v
positive deviation

followed by additional smaller oscillations.

---

9. WHY ARE NEGATIVE VALUES IMPORTANT?

---

A spatial-domain filter kernel can contain negative coefficients.

For example:

[-1, 2, -1]

When convolution is performed, these coefficients multiply neighboring pixels.

The negative coefficients subtract information.

The positive coefficients add information.

Therefore, an oscillatory kernel can repeatedly:

add
subtract
add
subtract

around an image edge.

This produces the overshoot and undershoot that appear as ringing.

---

10. NEGATIVE VALUES ARE NOT THE SAME THING AS
    RINGING

---

This distinction is important.

Negative values in the spatial-domain kernel are not themselves the ringing effect.

Instead:

negative and positive kernel values
|
v
oscillatory spatial response
|
v
overshoot and undershoot near image edges
|
v
visible ripples
|
v
RINGING

---

11. BUTTERWORTH FILTER AND RINGING

---

The relationship can therefore be summarized as:

Butterworth order n increases
|
v
frequency-domain transition becomes sharper
|
v
filter approaches Ideal Lowpass
|
v
spatial-domain kernel becomes more oscillatory
|
v
positive and negative lobes become more pronounced
|
v
overshoot and undershoot near edges increase
|
v
RINGING BECOMES STRONGER

---

12. COMPARISON OF FILTER ORDERS

---

Low-order Butterworth:

n is small

Frequency response:

* gradual transition

Spatial response:

* weak oscillations

Image:

* little ringing

High-order Butterworth:

n is large

Frequency response:

* sharp transition

Spatial response:

* stronger positive/negative oscillations

Image:

* stronger ringing

Ideal Lowpass:

n can be thought of as approaching infinity

Frequency response:

* abrupt cutoff

Spatial response:

* strong oscillations

Image:

* strong ringing

---

13. GAUSSIAN FILTER FOR COMPARISON

---

The Gaussian Lowpass Filter has a very smooth frequency response:

H(D) = exp[-D^2 / (2D0^2)]

There is no abrupt cutoff.

Therefore its spatial-domain response is also smooth and does not have the same oscillatory behavior.

Consequently:

Gaussian
|
v
very smooth frequency transition
|
v
no significant oscillatory spatial response
|
v
very little ringing

---

14. THE MAIN IDEA TO REMEMBER

---

Do not say:

"Higher n makes the Butterworth frequency profile oscillate
between positive and negative."

That is incorrect.

Instead say:

"Higher n makes the Butterworth frequency response sharper.
The sharper frequency response produces stronger positive and
negative oscillations in its spatial-domain impulse response,
which produces more ringing near sharp image transitions."

The complete chain is:

n increases
|
v
sharper frequency-domain cutoff
|
v
stronger spatial-domain oscillations
|
v
positive/negative lobes
|
v
overshoot/undershoot near edges
|
v
ringing effect

This distinction between the frequency-domain filter H(u,v) and
the spatial-domain impulse response h(x,y) is essential for
understanding why Butterworth filters can produce ringing.

- zero-phase shift filters

- Recall that a spatial representation
of a frequency domain filter is obtained by (1) multiplying H(u, v) by (-1)^(u+v)
for centering; (2) computing the inverse DFT; and (3) multiplying the real part
of the inverse DFT by (-1)^ (u+v).

-spot size of a filter, in high freq ideal filter,
whether different values of D, have different spot size of filter.

"""

