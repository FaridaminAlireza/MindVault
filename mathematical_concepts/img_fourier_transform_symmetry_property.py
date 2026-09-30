
"""
WHY IS THERE SYMMETRY AROUND THE ORIGIN?

The important point is: F(-u,-v) = F*(u,v)

This does NOT mean that 
F(-u,-v) and F(u,v) are the same complex number.

They are complex conjugates.

For example:
F(u,v) = 3 + 4j
Then:
F*(u,v) = 3 - 4j

Therefore: F(-u,-v) = 3 - 4j

These are different complex numbers.

But their magnitudes are the same:

|F(u,v)| = sqrt(3² + 4²) = 5
|F(-u,-v)| = sqrt(3² + (-4)²) = 5

Therefore: |F(-u,-v)| = |F(u,v)|

THIS is what we mean by symmetry around the origin.

For every frequency point: (u,v)
there is an opposite point: (-u,-v)
and these two points have the same magnitude.

So, in the magnitude spectrum:
(u,v)  <----->  (-u,-v)
have equal brightness/intensity.

The complex values themselves are not equal.
They are conjugates: F(-u,-v) = F*(u,v)

PHASE 
If: F(u,v) = A e^(jφ) then: F(-u,-v) = A e^(-jφ)

So: 
Magnitude: same
Phase: opposite sign

Therefore:

COMPLEX SPECTRUM:
F(-u,-v) = F*(u,v) → conjugate symmetry

MAGNITUDE SPECTRUM:
|F(-u,-v)| = |F(u,v)| → symmetry around the origin

So when we say that the Fourier spectrum of a real image 
is symmetric around the origin, 
we usually mean that its MAGNITUDE spectrum is symmetric.
"""