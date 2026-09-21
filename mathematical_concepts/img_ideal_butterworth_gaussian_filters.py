"""
Butterworth and Gaussian Lowpass Filters
---
1. Introduction

In frequency-domain image processing, an image 
is transformed into its frequency representation
using the Fourier Transform.

The frequency domain separates image information into:
* Low frequencies:
  * Slow intensity changes
  * Large objects
  * General shape and illumination

* High frequencies:
  * Rapid intensity changes
  * Edges
  * Fine details
  * Noise

A lowpass filter is designed to preserve 
low frequencies while reducing high frequencies.

The main goals are:
* Image smoothing
* Noise reduction
* Removal of fine details
* Preparation for later processing

Two important lowpass filters are:
* Butterworth Lowpass Filter (BLPF)
* Gaussian Lowpass Filter (GLPF)

Both work by multiplying 
the Fourier transform of the image 
by a filter function.

The filtered image is obtained by:

1. Compute Fourier Transform.
2. Multiply by the filter.
3. Compute inverse Fourier Transform.

The only difference between filters 
is the shape of their transfer function.

---
2. Distance in the Frequency Plane

Both filters depend on distance 
from the center of the frequency plane.

After centering the Fourier transform,
the origin is located 
at the center of the spectrum.

For any frequency point:
D(u,v) represents the distance from the center.

Distance is: D(u,v) = sqrt[(u-P/2)^2 + (v-Q/2)^2]

where:
P = number of rows
Q = number of columns

Interpretation:

Small D: * Low frequencies

Large D: * High frequencies

---
 3. Ideal Lowpass Filter Review

Before Butterworth and Gaussian filters, 
it is useful to recall the ideal lowpass filter.

Definition:
H(u,v) = 1 if D <= D0
H(u,v) = 0 if D > D0
where D0 is the cutoff frequency.

Meaning:
* Frequencies inside the circle pass completely.
* Frequencies outside the circle are removed completely.

Problem:
The transition is abrupt.
The frequency response looks like a sharp cliff.
This sharp discontinuity creates ringing artifacts in the image.
The ringing occurs because a sudden cutoff in frequency 
produces oscillations in space.

Butterworth and Gaussian filters were introduced
to solve this problem.

---
4. Butterworth Lowpass Filter

Definition
The Butterworth lowpass filter is:

H(u,v) = 1 / [1 + (D(u,v)/D0)^(2n)]

where:

D(u,v) = frequency distance
D0 = cutoff frequency
n = filter order

---
5. Why This Formula?

The goal is to create a smooth transition between:
H = 1 at low frequencies and
H = 0 at high frequencies
Instead of a sudden jump, we want a gradual decrease.

Consider: (D/D0)
When D is much smaller than D0:
(D/D0) is near zero
Therefore: H approximately equals 1
Low frequencies pass almost unchanged.

Now consider: D much larger than D0
Then: (D/D0)^(2n) becomes very large.
Therefore: 1 + large number
is dominated by the large number.
So: H approaches zero.
High frequencies are attenuated.

Thus the formula naturally produces:
Low frequencies -> pass
High frequencies -> suppressed

---
6. Why Use the Power 2n?
The exponent controls how rapidly the filter changes.
Suppose n = 1 Then the transition is gentle.
Suppose n = 10 Then the transition becomes much steeper.

As n increases: Butterworth approaches the ideal filter.
Therefore:

Small n:
* Smooth transition
* Less ringing

Large n:
* Sharper transition
* More ringing

The factor 2 is used so the exponent is always even.
An even exponent makes the response depend only 
on distance magnitude.
Positive and negative frequencies are treated identically.

---
7. Show That H = 0.5 at D = D0

Substitute: D = D0
into the Butterworth formula.
Then: (D/D0) = 1
and: 1^(2n) = 1
Therefore:
H = 1/(1+1)
H = 1/2
H = 0.5

This means: The cutoff frequency is defined as 
the point where the response falls to 50%.

---
8. Effect of Butterworth Order

Order n determines slope.
Example: n = 1 Very gradual transition.
n = 2 Moderate transition.
n = 10 Very sharp transition.
As n increases: Frequency response becomes
more rectangular.

This causes the filter to behave 
more like the ideal lowpass filter.

Consequently:
* Better frequency separation
* More ringing in the image
---
9. Ringing and the Butterworth Filter

Every abrupt change in frequency creates 
oscillations in the spatial domain.

The sharper the transition:
* More oscillation
* More ringing

Therefore: Low-order Butterworth filters generally 
produce less ringing than high-order Butterworth filters.

---
10. Gaussian Lowpass Filter

Definition: The Gaussian lowpass filter is:

H(u,v) = exp[-D(u,v)^2 / (2D0^2)]

where:

D(u,v) = distance from center
D0 = cutoff parameter

---
11. Why the Gaussian Formula?

The Gaussian function is one of the
smoothest functions in mathematics.

It has no sharp corners. It decreases gradually and continuously.

Desired properties:
At D = 0: Exponent becomes zero.
Since: exp(0) = 1 
we obtain: H = 1
The center frequency passes completely.

As D increases: D^2 increases.
The exponent becomes more negative.
The exponential becomes smaller.
Thus: Higher frequencies are attenuated.

As D approaches infinity:
Exponent approaches negative infinity.
exp(-infinity)
approaches zero.

Therefore: Very high frequencies are
almost completely removed.

---
12. Why Use D Squared?

The Gaussian curve should depend only on distance magnitude.

Squaring D provides:
* Circular symmetry
* Positive values
* Smooth decay

The response is identical in all directions.

---
13. Why Divide by 2D0^2?

This term controls the spread of the Gaussian.

Large D0:
* Wide Gaussian
* More frequencies pass

Small D0:
* Narrow Gaussian
* Stronger smoothing
Therefore D0 controls the effective cutoff.

---
14. Proof That the Gaussian Has No Abrupt Transition

Consider the Gaussian formula.

Every derivative exists.
The function is smooth everywhere.
There are:
* No jumps
* No corners
* No discontinuities

Because the frequency response changes smoothly,
the corresponding spatial-domain behavior is also smooth.
This is the main reason Gaussian filtering produces little ringing.

---
15. Comparing Ideal, Butterworth, and Gaussian Filters

Ideal Filter:

Characteristics:
* Abrupt cutoff
* Perfect frequency separation
Advantages:
* Simple concept
Disadvantages:
* Strong ringing


Butterworth Filter:

Characteristics:

* Adjustable transition
* Controlled by order n
Advantages:
* Flexible
* Can approximate ideal filter
Disadvantages:
* High orders may still ring

---

Gaussian Filter:

Characteristics:
* Infinitely smooth transition
Advantages:
* Minimal ringing
* Excellent smoothing behavior
Disadvantages:
* Less sharp frequency separation

---
16. Spatial-Domain Interpretation

Removing high frequencies means:
* Edges become softer
* Fine texture is reduced
* Noise decreases

Large D0:
* Weak smoothing
* More details remain

Small D0:
* Strong smoothing
* More blur

---
17. Key Intuition

Think of the frequency plane as a city.
The center contains slow-changing information.
The outer regions contain rapid changes and fine detail.

A lowpass filter acts like a gate.
Ideal filter: * Slams the gate shut at a specific radius.
Butterworth filter: * Gradually closes the gate.
Gaussian filter: * Closes the gate even more smoothly.

Because nature generally behaves smoothly 
rather than abruptly, the Gaussian filter 
often produces the most visually pleasing results.

"""

"""
HIGHPASS FILTERS:
FORMULAS AND KEY PROPERTIES

1. PURPOSE
A highpass filter does the opposite of a lowpass filter.
It attenuates low frequencies and preserves high frequencies.

As a result:
* Edges become more visible.
* Fine details are enhanced.
* Slow intensity variations are reduced.
* Sharp transitions are emphasized.

---
2. GENERAL RELATIONSHIP WITH LOWPASS FILTERS

Most highpass filters are obtained 
directly from their lowpass counterparts:
HPF(D) = 1 - LPF(D)

where:
HPF = highpass filter
LPF = corresponding lowpass filter

Consequences:
At D = 0:
LPF = 1
therefore:
HPF = 0
The DC component 
(average image intensity) is removed.

As D becomes large:
LPF approaches 0
therefore:
HPF approaches 1
High frequencies pass.

---
3. IDEAL HIGHPASS FILTER (IHPF)

Formula:
H(D) = 0    if D <= D0
H(D) = 1    if D > D0

where: D0 = cutoff frequency

Characteristics:
* Removes all frequencies inside the cutoff circle.
* Passes all frequencies outside the cutoff circle.
* Produces the strongest ringing among highpass filters.

---
4. BUTTERWORTH HIGHPASS FILTER (BHPF)

Obtained from the Butterworth lowpass filter:
H(D) = 1 - 1/[1 + (D/D0)^(2n)]

Equivalent form:
H(D) = 1/[1 + (D0/D)^(2n)]

where:

D0 = cutoff frequency
n  = filter order

Properties:
At D = 0:
H = 0

At D = D0:
H = 0.5

At very large D:
H approaches 1

Increasing n:
* Makes the transition sharper.
* Makes the filter more similar to the Ideal Highpass Filter.
* Increases ringing.

---
5. GAUSSIAN HIGHPASS FILTER (GHPF)

Obtained from the Gaussian lowpass filter:

H(D) = 1 - exp[-D^2/(2D0^2)]

Properties:

At D = 0:
H = 0

At large D:
H approaches 1

Characteristics:
* Smoothest transition among common highpass filters.
* Produces the least ringing.
* Frequently preferred when edge enhancement is desired without strong artifacts.

---
6. EFFECT OF CUTOFF FREQUENCY D0

Small D0:
* More frequencies pass.
* Stronger sharpening.
* More noise may be enhanced.

Large D0:
* Fewer frequencies pass.
* Weaker sharpening.
* Less noise amplification.

---
7. EFFECT ON IMAGE CONTENT

Low frequencies contain:
* Average brightness
* Large smooth regions
* Illumination variations

High frequencies contain:
* Edges
* Fine texture
* Small details
* Noise

Therefore:
Highpass filtering removes much of 
the smooth background information and
emphasizes abrupt changes.

---
9. Key points

Highpass filters suppress low frequencies
and preserve high frequencies.

Ideal Highpass:
* Sharpest transition
* Strongest ringing

Butterworth Highpass:
* Adjustable sharpness using n
* Moderate ringing

Gaussian Highpass:
* Smoothest transition
* Least ringing

Increasing n in a Butterworth Highpass Filter 
makes the transition sharper and increases ringing,
just as in the Butterworth Lowpass Filter.


| Filter               | Frequency Transition | Spatial Oscillation | Ringing |
| -------------------- | -------------------- | ------------------- | ------- |
| Ideal LPF/HPF        | Abrupt               | Strong              | Strong  |
| Butterworth (low n)  | Smooth               | Weak                | Little  |
| Butterworth (high n) | Sharp                | Stronger            | More    |
| Gaussian             | Smoothest            | Minimal             | Minimal |

"""