"""
FOURIER TRANSFORM SCALING PROPERTY
==================================

The property is:

f(ax, by)  <-> (1 / |ab|) F(u/a, v/b)

For positive a and b, this becomes:

f(ax, by) <-> (1 / ab) F(u/a, v/b)

If the image is compressed in space,
its Fourier transform expands in frequency.

If the image is expanded in space,
its Fourier transform becomes compressed in frequency.

---
1. START WITH THE 2-D CONTINUOUS FOURIER TRANSFORM

The 2-D Fourier transform is:

F(u,v) = integral integral f(x,y) exp[-j2pi(ux + vy)] dx dy
We want to find the Fourier transform of: g(x,y) = f(ax, by)

So: 
G(u,v) = integral integral g(x,y) exp[-j2pi(ux + vy)] dx dy


Substitute: g(x,y) = f(ax,by)

Therefore:

G(u,v) = integral integral f(ax,by) exp[-j2pi(ux + vy)] dx dy


---
2. CHANGE THE VARIABLES

We want to get back to the original function f.
Define:
x' = ax
y' = by

Therefore:
x = x'/a
y = y'/b


Now differentiate:
dx = dx'/a
dy = dy'/b

Therefore:
dx dy
= (1/ab) dx' dy'

For positive a and b.

---
3. SUBSTITUTE EVERYTHING

Starting with:

G(u,v) = integral integral f(ax,by) exp[-j2pi(ux + vy)] dx dy


Since:
ax = x'
by = y'

we get:
G(u,v) = 
integral integral f(x',y') exp[-j2pi(u x'/a + v y'/b)] (1/ab) dx' dy'


Take the constant outside:

G(u,v)
=
(1/ab)
integral integral
f(x',y')
exp[-j2pi((u/a)x' + (v/b)y')]
dx' dy'


---
4. RECOGNIZE THE FOURIER TRANSFORM
Recall the definition:

F(p,q) =
integral integral
f(x',y')
exp[-j2pi(px' + qy')]
dx' dy'

Compare this with:

integral integral
f(x',y')
exp[-j2pi((u/a)x' + (v/b)y')]
dx' dy'


We can identify:
p = u/a
q = v/b

Therefore the integral is:
F(u/a, v/b)


So:

G(u,v) =(1/ab) F(u/a, v/b)


Therefore:
f(ax,by) <-> (1/ab) F(u/a,v/b)

More generally, if a or b can be negative:
f(ax,by) <-> (1/|ab|) F(u/a,v/b)


---
5. WHAT DOES THIS MEAN?

There are TWO effects.
A. FREQUENCY COORDINATES ARE SCALED
The original Fourier transform is: F(u,v)
After spatial scaling: F(u/a,v/b)
So the frequency coordinates are 
divided by a and b.


B. THE AMPLITUDE IS ALSO SCALED
There is an additional factor: 1/|ab|
This comes from the change of variables:
dx dy = (1/|ab|) dx' dy'


---
6. SIMPLE 1-D INTUITION
First consider: g(x) = f(ax)
The Fourier transform becomes:
G(u) = (1/|a|) F(u/a)
Suppose: a = 2
Then: g(x) = f(2x)
This compresses the function in space.
Its Fourier transform is:
G(u)= (1/2) F(u/2)
Notice: u becomes u/2.
Therefore the spectrum is stretched 
along the frequency axis.
So:
SPATIAL DOMAIN: f(x)
---> compressed ---> f(2x)
FREQUENCY DOMAIN: F(u)
---> expanded ---> F(u/2)

---
7. WHY DO THEY MOVE IN OPPOSITE DIRECTIONS?

This is one of the most important ideas.
Suppose a function becomes narrower in space.
A narrow spatial function requires 
a wider range of frequencies
to represent its rapid spatial variation.

Therefore:
narrower in space -> wider in frequency

Conversely:
wider in space -> narrower in frequency

This is the spatial-frequency scaling relationship.

---
8. 2-D EXAMPLE
Suppose: g(x,y) = f(2x,3y)
Then: a = 2, b = 3

The scaling property gives:

g(x,y) <-> (1/6) F(u/2,v/3)

Therefore:
x direction:
 spatial scale = 2
 frequency scale = 1/2

y direction:
 spatial scale = 3
 frequency scale = 1/3


So the transformation is:

f(2x,3y) <-> (1/6) F(u/2,v/3)


---
In Summary: 

translation
    -> moves the image
    -> changes Fourier phase

scaling
    -> stretches/compresses the image
    -> stretches/compresses the frequency spectrum
    -> changes its amplitude by 1/|ab|


The key step in the proof is the change of variables:
x' = ax
y' = by
which gives:
x = x'/a
y = y'/b
and: dx dy = (1/|ab|) dx' dy'

At the same time, the Fourier exponential
exp[-j2pi(ux + vy)] becomes
exp[-j2pi((u/a)x' + (v/b)y')]

That is exactly the Fourier transform evaluated at:(u/a,v/b)

Therefore: f(ax,by) <-> (1/|ab|) F(u/a,v/b)

---
The two important consequences are:
1. Spatial scaling by a,b
   produces inverse frequency scaling by 1/a,1/b.

2. The change of variables produces the amplitude factor
   1/|ab|.
"""