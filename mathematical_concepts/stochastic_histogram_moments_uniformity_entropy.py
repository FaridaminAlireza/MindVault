"""
HISTOGRAM MOMENTS, UNIFORMITY, AND ENTROPY

INTRODUCTION

A normalized image histogram can be treated
as a probability distribution.

Suppose an image has gray levels z_i,
where i goes from 0 to L-1.

The normalized histogram is:
p(z_i) = number of pixels with gray 
level z_i / total number of pixels

Because p(z_i) represents probabilities:
sum p(z_i) = 1

Once we interpret the histogram as a probability distribution,
we can calculate statistical quantities such as:

1. Mean: where the histogram is centered
2. Variance: how spread out the histogram is
3. Third moment: how asymmetric the histogram is
4. Uniformity: how concentrated or spread out the histogram is
5. Entropy: how uncertain or unpredictable the gray level is

---
1. FIRST MOMENT: MEAN

The mean gray level is:

m = sum [ z_i * p(z_i) ]

The mean tells us where the histogram is centered.
For example, if most pixels are around gray level 100,
then the mean will be around 100.

---
2. SECOND MOMENT: VARIANCE

Variance measures how far the gray levels
are spread around the mean.

variance = sum [ (z_i - m)^2 * p(z_i) ]

The square is important because otherwise 
positive and negative deviations would cancel.

For example:
A pixel 10 units below the mean has:

(z_i - m) = -10

A pixel 10 units above the mean has:

(z_i - m) = +10

After squaring:

(-10)^2 = 100
(+10)^2 = 100

Therefore both contribute positively to the variance.

---
3. THIRD CENTRAL MOMENT: SKEWNESS

The third central moment is:

mu_3 = sum [ (z_i - m)^3 * p(z_i) ]

The important difference from variance is the power of 3.
Because the exponent is odd:

positive deviations remain positive
negative deviations remain negative

For example:

(+2)^3 = +8
(-2)^3 = -8

Therefore the third moment preserves information
about which side of the mean 
contains more of the tail of the distribution.

POSITIVE SKEWNESS
If the histogram has a longer tail toward higher gray levels,
then the third moment tends to be positive.

Example: Most pixels are relatively dark, 
but a smaller number of very bright pixels extend the right side.

Those bright pixels have:
z_i - m > 0
and therefore:
(z_i - m)^3 > 0
So: mu_3 > 0
Positive skewness means a longer/right-side positive tail.

NEGATIVE SKEWNESS
If the histogram has a longer tail toward lower gray levels,
then the third moment tends to be negative.

Example: The dark pixels extending toward the left have:

z_i - m < 0
and therefore:
(z_i - m)^3 < 0
So: mu_3 < 0
Negative skewness means a longer/left-side negative tail.

SYMMETRIC HISTOGRAM
For a symmetric histogram, 
positive and negative contributions cancel.

Therefore: mu_3 = 0

Conceptually:
negative contribution + positive contribution = 0

So:
positive third moment  -> longer right tail
negative third moment  -> longer left tail
zero third moment      -> symmetric distribution

---
4. UNIFORMITY

A common histogram measure called uniformity is:

U = sum [ p(z_i)^2 ]
It measures how concentrated the probability mass is.

The important idea is:
large probability values become even larger when squared.

For a gray level image, the more gray levels you spread
the probability across, the less concentrated 
the distribution becomes. And because uniformity uses squares,
spreading the probability out makes the sum smaller.

For example:

0.8^2 = 0.64
0.1^2 = 0.01
0.05^2 = 0.0025

Therefore a histogram with one dominant gray level produces 
a large uniformity value.

EXTREME CASE 1: ALL PIXELS HAVE ONE GRAY LEVEL

Suppose:

p(z_1) = 1
and every other probability is zero.

Then:
U = 1^2 + 0^2 + 0^2 + ...
U = 1
This is maximum concentration.

EXTREME CASE 2: PERFECTLY UNIFORM HISTOGRAM

Suppose there are L gray levels and
every gray level is equally likely.

Then:
p(z_i) = 1/L

Therefore:
U = L * (1/L)^2

U = 1/L
This is the minimum uniformity value.

For example, if there are 8 equally likely gray levels:

p(z_i) = 1/8
U = 8 * (1/8)^2
U = 1/8


High U:
probability is concentrated in a small number of gray levels.
Low U:
probability is distributed across many gray levels.
-> So uniformity is essentially measuring concentration.

---
5. ENTROPY

Entropy is:
H = -sum [ p(z_i) * log2(p(z_i)) ]

Entropy measures the average information or
uncertainty associated with the random variable.

To understand this formula, first understand 
the information contained in one outcome.

---
INFORMATION CONTENT OF ONE OUTCOME

The information associated 
with an outcome having probability p is:

I(p) = -log2(p)

The rarer an event is, 
the more information its occurrence gives us.

Examples:

p = 1/2
I = -log2(1/2)
I = 1 bit

p = 1/4
I = -log2(1/4)
I = 2 bits

p = 1/8
I = -log2(1/8)
I = 3 bits

p = 1/16
I = -log2(1/16)
I = 4 bits

The reason is:

1/2 = 1/(2^1)
1/4 = 1/(2^2)
1/8 = 1/(2^3)
1/16 = 1/(2^4)

Therefore:
p = 1/(2^k)
gives:
I(p) = k bits

---
WHY DOES A BIT CORRESPOND TO DIVIDING POSSIBILITIES BY TWO

A bit corresponds to a binary decision.

A binary question has two possible answers: YES, NO
Therefore one question can distinguish between: 2 possibilities

Two questions can distinguish between: 2 * 2 = 4 possibilities
Three questions: 2 * 2 * 2 = 8 possibilities

In general: number of possibilities = 2^n
where n is the number of binary questions/bits.

---
WHAT IF THE PROBABILITY IS NOT A POWER OF TWO?

The logarithm still works.

For example:

p = 1/10

Then:
I(p) = -log2(1/10)
I(p) = log2(10)
I(p) approximately 3.32 bits

This means that a probability of 1/10 contains 
the same amount of information as
approximately 3.32 binary decisions.

The value does not have to be an integer 
because information is an average/ideal quantity.

if the result is 3.32 bits, it 
does NOT mean you can literally ask 3.32 questions.
The 3.32 bits is the ideal amount of binary information 
represented by one observation. Over many observations, 
an average of 3.32 bits per observation can be approached
using efficient coding.



Another example:

p = 0.3
I(p) = -log2(0.3)
I(p) approximately 1.737 bits
A 0.3-probability event therefore 
carries about 1.737 bits of information.

The general relationship is:
I(p) = -log2(p)
or equivalently:
I(p) = log2(1/p)

The second form makes 
the interpretation especially clear.

---
FROM INFORMATION TO ENTROPY

Information tells us how much information 
ONE particular outcome carries:

I(p_i) = -log2(p_i)

But a random variable has multiple possible outcomes.

Some outcomes are common.
Some outcomes are rare.

Therefore we want the AVERAGE information.
The average of a quantity is:
average = sum [ probability * value ]
Therefore:
H = sum [ p_i * I(p_i) ]

Substitute:
I(p_i) = -log2(p_i)
and we get:
H = sum [ p_i * (-log2(p_i)) ]

Therefore:
H = -sum [ p_i * log2(p_i) ]
This is the entropy formula.

---
EXAMPLE OF ENTROPY

Suppose a random variable has four outcomes:
A: p = 1/2
B: p = 1/4
C: p = 1/8
D: p = 1/8

First check that the probabilities add to 1:
1/2 + 1/4 + 1/8 + 1/8 = 1

Information of A:
I(A) = -log2(1/2) = 1 bit

Information of B:
I(B) = -log2(1/4) = 2 bits

Information of C:
I(C) = -log2(1/8) = 3 bits

Information of D:
I(D) = -log2(1/8) = 3 bits

Now calculate the average information:

H = (1/2)(1) + (1/4)(2) + (1/8)(3) + (1/8)(3)
H = 0.5 + 0.5 + 0.375 + 0.375
H = 1.75 bits

Therefore: H = 1.75 bits per observation
This means that although individual outcomes 
contain 1, 2, or 3 bits of information, 
the average information is 1.75 bits.

---
ENTROPY AND A UNIFORM DISTRIBUTION

Suppose there are L equally likely outcomes.
Then: p_i = 1/L
Entropy becomes: H = -sum [ (1/L) * log2(1/L) ]
There are L identical terms:
H = -L * (1/L) * log2(1/L)
Therefore: H = -log2(1/L)
Since: 1/L = L^(-1)
we get: H = log2(L)

Therefore the maximum entropy for 
L equally likely outcomes is:
H_max = log2(L)

Example:

2 equally likely outcomes:
H = log2(2) = 1 bit

4 equally likely outcomes:
H = log2(4) = 2 bits

8 equally likely outcomes:
H = log2(8) = 3 bits

10 equally likely outcomes:
H = log2(10) = 3.32 bits

So entropy reaches its maximum when the probability 
is distributed uniformly across the possible outcomes.

---
 ENTROPY VS UNIFORMITY

Uniformity: U = sum [ p_i^2 ]

Entropy: H = -sum [ p_i * log2(p_i) ]

They behave in opposite directions
 with respect to concentration.

If one gray level dominates:
U is high
H is low

If probability is spread evenly
across many gray levels:
U is low
H is high

For example, with two gray levels:
Case 1:
p = [1, 0]
U = 1^2 + 0^2 = 1
H = 0

Case 2:
p = [1/2, 1/2]
U = (1/2)^2 + (1/2)^2
U = 1/2
H = 1 bit

Therefore:
more concentration -> higher uniformity, lower entropy
more spread -> lower uniformity, higher entropy
xw

#
"""