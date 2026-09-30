"""
BILINEAR INTERPOLATION
Parametric View

1. Basic idea

Bilinear interpolation can be understood 
as two successive linear interpolations.

We have four known values at the corners of a rectangle:

Q12 -------- Q22
 |            |
 |      P     |
 |            |
Q11 -------- Q21

We want to estimate the value at the interior point P.

The key idea is:

1. Interpolate along the bottom edge.
2. Interpolate along the top edge.
3. This gives two intermediate values.
4. Interpolate between those two values.

So we are NOT interpolating between two line equations.

We first use the lines to obtain two values.
Then we interpolate between those values.

2. First interpolation: bottom edge

Suppose the horizontal position of P is x.
Define: tx = (x - x0) / (x1 - x0)

The parameter tx tells us where x lies between x0 and x1.

If: tx = 0 we are at the left endpoint.
If: tx = 1 we are at the right endpoint.
If: tx = 0.5 we are halfway between them.

Now interpolate between Q11 and Q21:
R1 = (1 - tx) Q11 + tx Q21

Graphically:
Q11 ----- R1 ----- Q21
R1 is now just a value.

It is the interpolated value at x
on the bottom edge.

3. Second interpolation: top edge

We do exactly the same thing on the top edge.

R2 = (1 - tx) Q12 + tx Q22

Graphically:
Q12 ----- R2 ----- Q22
Again, R2 is just a value.

It is the interpolated value at x
on the top edge.

4. What do we have now?
After these two interpolations, we have:
R2
 |
 |
 |
R1

- R1 is the value at the desired x
on the bottom edge.
- R2 is the value at the desired x
on the top edge.
- They are no longer line equations.
They are simply two values.

5. Third step: interpolate between R1 and R2

Now we move vertically.

Define:
ty = (y - y0) / (y1 - y0)

Again, ty tells us the relative vertical position.

Then interpolate between R1 and R2:
f(x,y) = (1 - ty) R1 + ty R2


So conceptually:
R2
 |
 P
 |
R1

We use R1 and R2 as the two
endpoints of another interpolation.

6. Why use the parametric form?

We could write explicit line equations.
For example, the bottom line could be written as:

y = ax + b

and then we could evaluate that line
at the desired x.

We would have to calculate its slope,
intercept, and so on.

The parametric form avoids this extra work.

Instead, we calculate:
t = relative position between endpoints
and then simply use:
value = (1 - t) A + t B

So we only need:
A = first value
B = second value
t = relative position


7. What does the parameter t mean?
The parameter t represents position
between two endpoints.

For example:

A ----------- B
0             1

If t = 0: result = A
If t = 0.5: result = halfway between A and B
If t = 1: result = B

Therefore: (1 - t) A + t B

is simply a convenient way
of moving from A to B.

8. Important point

- The parametric form does NOT mean
that there is no line.
- It is another way of representing
the line segment.

For example: P(t) = (1 - t) P0 + t P1

describes every point on the line
segment between P0 and P1.

At t = 0: P = P0
At t = 1: P = P1

For values between 0 and 1,
P lies between the two endpoints.

9. Why this is useful in bilinear interpolation

The same idea works even when the
values are not ordinary numbers.

A and B could represent:

scalar values
2D points
3D points
colors
texture coordinates
vectors
surface properties

The same interpolation rule applies:
(1 - t) A + t B
"""