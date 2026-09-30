"""
IMPLICIT SURFACE APPROXIMATION:
FROM FUNCTION ERROR TO GEOMETRIC ERROR

1. Polynomial interpolation error

Suppose G is the original function
and F is a polynomial approximant
of degree p.

The interpolation error theorem gives

|F(t) - G(t)| <= 1/(p+1)! * max |G^(p+1)(t)| * |product from i=0 to p of (t - t_i)|

For a sufficiently small voxel size h, the product term is O(h^(p+1)).

Therefore, |F(t) - G(t)| = O(h^(p+1))

Interpretation:

The polynomial F approximates the
function G with an error that decreases
like h^(p+1) as the voxel size decreases.


2. Why function error is not yet geometric surface error

For an implicit representation, G : R^3 -> R
the actual surface is not the function values themselves.

The surface is the zero level set:
S_G = {x in R^3 | G(x) = 0}

Similarly, the approximating surface is
S_F = {x in R^3 | F(x) = 0}

Therefore, we want to know:

How far apart are the surfaces
S_F and S_G geometrically?

The interpolation theorem only gives

|F(x) - G(x)| = O(h^(p+1))

which is a FUNCTION error.

We need to convert this function
error into a GEOMETRIC distance error.


3. Choose a point on the approximating surface
Choose a point x such that F(x) = 0
Therefore, x is on the approximating surface S_F.


4. Find a corresponding point on the true surface

We look for a nearby point x + d
that lies on the true surface.

Therefore, G(x + d) = 0

Important: F(x) = 0
but generally, F(x + d) != 0
because x+d is on the TRUE surface,
not necessarily on the approximating surface.

Likewise, G(x + d) = 0
but generally, G(x) != 0.

5. Why move in the normal direction?

The gradient of an implicit function
is normal to its corresponding level surface.

For the approximating surface, F(x) = 0,

the normal direction is n = grad F(x) / ||grad F(x)||
This is a unit normal vector.

We therefore assume that the corresponding
true-surface point can be reached approximately
by moving along this normal direction:

d = delta * grad F(x) / ||grad F(x)||

where delta is an unknown scalar.

The length of d is ||d|| = |delta|.


6. Taylor expansion of F

Expand F around the point x:

F(x + d) = F(x) + grad F(x) . d + higher-order terms
Since x is on the approximating surface,

F(x) = 0.

Therefore, F(x + d) approximately equals

grad F(x) . d


7. Substitute the normal direction

We have

d = delta * grad F(x) / ||grad F(x)||

Therefore,

grad F(x) . d

=
grad F(x) . [ delta * grad F(x) / ||grad F(x)||]

Pull delta outside the dot product:

=
delta * [grad F(x) . grad F(x)]/ ||grad F(x)||

But
grad F(x) . grad F(x) = ||grad F(x)||^2

Therefore,
grad F(x) . d = delta * ||grad F(x)||

Thus, F(x + d) approximately equals delta * ||grad F(x)||

Taking absolute values gives

|F(x + d)|
approximately equals
|delta| * ||grad F(x)||

Since ||d|| = |delta|,

we obtain

|F(x + d)|
approximately equals
||d|| * ||grad F(x)||


Therefore,

||d||
approximately equals

|F(x + d)| / ||grad F(x)||


This is the key relation that
converts function error into
geometric distance error.


8. Now use the fact that x+d
   is on the true surface

By construction,

G(x + d) = 0.

Therefore,

F(x + d) - G(x + d) = F(x + d) - 0

= F(x + d).

Taking absolute values gives

|F(x + d) - G(x + d)| = |F(x + d)|


9. Apply the interpolation error

The interpolation theorem says

|F(y) - G(y)| = O(h^(p+1))

for points y inside the voxel.

We can choose

y = x + d.

Therefore,

|F(x + d) - G(x + d)| = O(h^(p+1)).

But from the previous step,

|F(x + d) - G(x + d)| = |F(x + d)|.

Hence,

|F(x + d)| = O(h^(p+1)).


10. Substitute into the
    geometric-distance formula

We already obtained ||d||
approximately equals
|F(x + d)| / ||grad F(x)||

and now we know

|F(x + d)| = O(h^(p+1)).

Therefore,

||d|| = O(h^(p+1)) / ||grad F(x)||


11. Why do we need a lower bound on the gradient?

Assume there exists some constant

epsilon > 0

such that

||grad F(x)|| >= epsilon.

Then

1 / ||grad F(x)|| <= 1 / epsilon.

Therefore, the denominator remains
bounded away from zero.

It cannot become arbitrarily small.

Thus,

||d|| = O(h^(p+1)).


12. Final result

Function approximation error:

|F - G| = O(h^(p+1))

leads to geometric surface error:

||d|| = O(h^(p+1))

provided that

||grad F|| >= epsilon > 0.


Therefore:

FUNCTION ERROR
        |
        v
|F-G| = O(h^(p+1))
        |
        v
At x+d, where G(x+d)=0:
|F(x+d)| = O(h^(p+1))
        |
        v
Taylor expansion along
the normal direction:
|F(x+d)|
approximately equals
||d|| ||grad F||
        |
        v
If ||grad F|| >= epsilon:
        |
        v
||d|| = O(h^(p+1))


13. Important distinction

There are three different points/
conditions that must be kept separate:

x:

    F(x) = 0

    x is on the approximating surface.


x+d:

    G(x+d) = 0

    x+d is on the true surface.


F(x+d):

    generally NOT zero.

This last quantity is especially important.

It measures how far the point x+d
is from satisfying the approximating
surface equation F=0.

Because F and G are close,

|F(x+d) - G(x+d)| = O(h^(p+1)).

Since G(x+d)=0,

|F(x+d)| = O(h^(p+1)).

This function-value error is then
converted into the geometric distance ||d||.


14. Why low variation of the gradient magnitude is desirable

We have approximately

||d|| = |F(x+d)| / ||grad F(x)||.

Suppose the function approximation
error is similar everywhere.

If ||grad F|| is very different
at different parts of the surface,
then the resulting geometric error
will also be very different.

For example:

Region A:

||grad F|| = 10

Then

||d|| approximately |F(x+d)| / 10

This produces a relatively small
geometric displacement.


Region B:

||grad F|| = 0.1

Then

||d|| approximately
|F(x+d)| / 0.1

This produces a much larger
geometric displacement.

Therefore, in practice one tries
to construct F such that

||grad F||

does not vary too much over
different regions of the surface.

This helps produce a more uniform
distribution of geometric approximation error.


MAIN IDEA

The complete argument is:

1. Polynomial interpolation gives

   |F-G| = O(h^(p+1)).

2. The surfaces are zero level sets,
   so function error alone is not
   directly a geometric distance error.

3. Start with a point x satisfying

   F(x)=0.

4. Move from x along the normal
   direction by a displacement d.

5. Choose x+d so that

   G(x+d)=0.

6. Taylor expansion gives

   |F(x+d)|
   approximately equals
   ||d|| ||grad F(x)||.

7. Because G(x+d)=0,

   |F(x+d)|
   =
   |F(x+d)-G(x+d)|.

8. The interpolation theorem gives

   |F(x+d)| = O(h^(p+1)).

9. If

   ||grad F|| >= epsilon > 0,

   then

   ||d|| = O(h^(p+1)).

Therefore, the geometric error
between the implicit surfaces has
the same order as the polynomial
interpolation error.
"""