"""
DYNAMIC RANGE COMPRESSION

INTRODUCTION

Dynamic range compression means reducing the difference between
very large intensity values and very small intensity values.

In image processing, it is often used when an image contains
both extremely bright and extremely dark regions.

The goal is to make the image easier to display and easier
to analyze.


WHAT IS DYNAMIC RANGE?
Dynamic range is the ratio between the largest and smallest
intensity values.

Example:
Minimum intensity = 1
Maximum intensity = 1000
Dynamic range: 1000 / 1 = 1000
This is a very large dynamic range.

Another example:
Minimum intensity = 50
Maximum intensity = 200
Dynamic range: 200 / 50 = 4
This is a much smaller dynamic range.

--
WHY IS A LARGE DYNAMIC RANGE A PROBLEM?

Suppose an image contains:

Pixel A = 10
Pixel B = 100
Pixel C = 1000
Pixel D = 10000

If displayed directly:

- Very bright pixels dominate.
- Dark regions become difficult to see.
- Small differences among dark pixels are hidden.

The display device may not be able to show the full range.

--
IDEA OF COMPRESSION

We want to: Reduce large intensity differences
while Preserving useful visual information.

For example:
Original values:
10
100
1000
10000

After compression:
10
20
30
40

The largest values are "squeezed together."


--
LOG TRANSFORMATION

The most common dynamic range compression method is:

s = c log(1 + r)

where:
r = input intensity
s = output intensity
c = scaling constant

EXAMPLE
Original intensities:
1
10
100
1000

Take logarithms:
log(1)    = 0
log(10)   = 1
log(100)  = 2
log(1000) = 3

Notice:
Original range: 1 → 1000
Compressed range: 0 → 3
A huge range became much smaller.

WHY DOES THE LOG DO THIS?
The logarithm grows slowly.

Example:

Input:
1
10
100
1000
10000

Log output:
0
1
2
3
4

Each tenfold increase produces only a small increase
in the output.

Therefore:
Large values are compressed strongly.
Small values are compressed much less.

--
RELATION TO HOMOMORPHIC FILTERING

In homomorphic filtering, 
the logarithm is used mainly to:

Convert: f = i × r
into: ln(f) = ln(i) + ln(r)

However, the logarithm also 
performs dynamic range compression.

Example:
Original values:
10
100
1000

After logarithm:
2.3
4.6
6.9

The large differences become much smaller.

Therefore homomorphic filtering has two effects:

1. Converts multiplication into addition.
2. Compresses the dynamic range.

REAL-WORLD EXAMPLE

Imagine a scene containing:
- A bright window.
- A darker room interior.

Intensity values:
Window = 10000
Room    = 100
Ratio: 10000 / 100 = 100

After logarithm:
log(10000) = 4
log(100)   = 2
Ratio becomes: 4 / 2 = 2

The brightness difference is greatly reduced.
Now details inside the room become easier to see.

"""