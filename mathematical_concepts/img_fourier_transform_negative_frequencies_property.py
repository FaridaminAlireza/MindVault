"""
- WHY DO NEGATIVE FREQUENCIES APPEAR 
IN THE SECOND HALF OF THE DFT,
- AND WHY DO WE CENTER THE FOURIER SPECTRUM?

1. THE BASIC DFT

For an M-point DFT:
F(u + M) = F(u)
This means that the Fourier transform is
periodic with period M.

The DFT gives us M frequency samples:
u = 0, 1, 2, ..., M-1
But these indices can also be interpreted 
as positive and negative frequencies.

---
EXAMPLE: M = 6

The DFT produces:

DFT index: 0    1    2    3    4    5

The natural frequency interpretation is:
Frequency: 0   +1   +2   +3   -2   -1

Why?

Because the indices in the second half 
can be shifted by -M:

4 - 6 = -2
5 - 6 = -1

So:

DFT index       Frequency
--------------------------------
0                  0
1                 +1
2                 +2
3                 +3
4                 -2
5                 -1

WHY DOES u = 5 REPRESENT -1?

The DFT basis function is: e^(-j2πux/M)

For M = 6 and u = 5: e^(-j2π(5)x/6)

Since: 5 = -1 + 6 
we get: e^(-j2π(5)x/6) = e^(-j2π(-1+6)x/6)
= e^(j2πx/6) e^(-j2πx)

Since x is an integer:

e^(-j2πx) = 1

Therefore:

e^(-j2π(5)x/6) = e^(j2πx/6)
which is: e^(-j2π(-1)x/6)

Therefore: u = 5 and u = -1
represent exactly the same DFT frequency.

---
2. WHAT DOES "NEGATIVE FREQUENCY" MEAN?

Negative frequency does NOT mean
that the physical frequency 
is actually negative.

It describes the direction of
rotation of a complex sinusoid.

Positive frequency:
e^(j2πft) rotates in one direction in the complex plane.

Negative frequency:
e^(-j2πft) rotates in the opposite direction.

Therefore:
+f = one rotational direction
-f = opposite rotational direction

---
3. WHY DO REAL SIGNALS HAVE BOTH +f AND -f?

A cosine can be written using Euler's formula:

cos(2πft)
= 1/2 e^(j2πft) + 1/2 e^(-j2πft)

Therefore a real cosine contains:
+f and -f

The two complex components 
rotate in opposite directions.

Together, they produce the real cosine.

So negative frequency is a mathematical component 
that is necessary for representing real signals 
using complex exponentials.

---
4. WHY ARE NEGATIVE FREQUENCIES STORED AT THE END?

The DFT stores only:
0, 1, 2, ..., M-1

It does not store:
-M/2, ..., -1, 0, +1, ..., +M/2

separately.

Because of periodicity: F(u + M) = F(u)
we can wrap negative frequencies into the available range.

For M = 6:

-1 + 6 = 5
-2 + 6 = 4
-3 + 6 = 3
Therefore:
-1 -> 5
-2 -> 4
-3 -> 3

This is why negative frequencies appear 
at the end of the DFT array.

---
5. THE PROBLEM WITH THIS ARRANGEMENT

The DFT gives us:

0   +1   +2   +3   -2   -1

This is mathematically correct.
But it is not the most intuitive way 
to look at the frequency spectrum.

The zero-frequency component is at the beginning: 0
while the negative frequencies are at the end: -2   -1

So the frequency axis appears "split":

positive frequencies | negative frequencies

This makes it harder to see how 
the spectrum is organized around
zero frequency.


---
6. CENTERING THE FOURIER SPECTRUM

We can rearrange the DFT samples 
so that zero frequency is placed
in the center.

For M = 6:

Before centering:
0   +1   +2   +3   -2   -1

After centering:
-3   -2   -1    0   +1   +2

Now the frequency axis is arranged naturally:
negative frequencies | zero | positive frequencies
The zero-frequency component is now at the center.

---
7. WHAT DOES CENTERING ACTUALLY DO?

Centering does NOT change the Fourier information.
It only changes where the frequency samples are displayed.

For example:
Before:

index:      0    1    2    3    4    5
frequency:  0   +1   +2   +3   -2   -1

After centering:
frequency: -3   -2   -1    0   +1   +2

The same values are present.
They have simply been rearranged.

---
8. WHY IS CENTERING ESPECIALLY USEFUL FOR IMAGES?

For a 2-D image, the zero-frequency component 
is normally at: (u,v) = (0,0)
which is the corner of the Fourier spectrum.

After centering, the zero-frequency component 
moves to the center: (u,v) = (M/2, N/2)

This makes the frequency spectrum 
much easier to interpret.

We can then see:
Center = low frequencies
Farther from center = higher frequencies

---
9. CENTERING ALSO MAKES SYMMETRY EASY TO SEE

For a real image:
F(-u,-v) = F*(u,v)
Therefore: |F(-u,-v)| = |F(u,v)|

So the magnitude spectrum is 
symmetric around the origin.

Before centering, 
the origin is at the corner.
Therefore the symmetry 
can look difficult to recognize.

After centering, the origin is at the center.
Then the symmetry becomes visually obvious:

                  |
          *       |       *
                  |
    *-------------0-------------*
                  |
          *       |       *
                  |

A point at: (u,v) has a matching point at: (-u,-v)
directly opposite the center.


---
10. HOW DO WE CENTER IT?

For a 1-D signal, we can multiply the input by: (-1)^x
before taking the DFT: g(x) = f(x)(-1)^x
Since: (-1)^x = e^(jπx) we get: g(x) = f(x)e^(jπx)
The Fourier transform then becomes: G(u) = F(u - M/2)
So multiplication by (-1)^x 
shifts the Fourier spectrum by M/2.


For a 2-D image: g(x,y) = f(x,y)(-1)^(x+y)
This shifts the spectrum by: (M/2, N/2)
Therefore the zero-frequency component 
moves from the corner: (0,0)
to the center: (M/2, N/2)
Centering gives:

                 high
                  |
                  |
       high ----- 0 ----- high
                  |
                  |
                 high

where:
center = zero frequency / low frequencies
farther from center = higher frequencies
"""