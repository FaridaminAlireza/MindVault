"""
2-D FOURIER TRANSFORM — ROTATION PROPERTY

ROTATION
Suppose we use polar coordinates.

Spatial coordinates:
x = r cos(theta)
y = r sin(theta)

Frequency coordinates:
u = w cos(phi)
v = w sin(phi)

Here:
r = distance from the spatial origin
theta = spatial angle

w = distance from the frequency origin
phi = frequency angle


The Fourier transform pair is:
f(x,y)  <->  F(u,v)

In polar coordinates:
f(r,theta)  <->  F(w,phi)


The rotation property says:
f(r, theta + theta0) <-> F(w, phi + theta0)

In words:
If the image is rotated by theta0,
its Fourier transform is also rotated by theta0.

---
1. START WITH THE 2-D FOURIER TRANSFORM

The continuous 2-D Fourier transform is:

F(u,v) =
integral integral
f(x,y)
exp[-j2pi(ux + vy)]
dx dy

We want to understand what happens when
the image is rotated.

Define a rotated image:
g(r,theta) = f(r, theta - theta0)

This means that the original image has been rotated
by theta0.

We want to find its Fourier transform.

---
2. WRITE THE FOURIER TRANSFORM IN POLAR COORDINATES

The 2-D Fourier transform can be written in polar coordinates.
Recall:
x = r cos(theta)
y = r sin(theta)

and:
u = w cos(phi)
v = w sin(phi)

The area element changes as:
dx dy = r dr dtheta

So:


# F(w,phi) = F(w cos(φ), w sin(φ) 
integral
integral
f(r,theta)
exp[-j2pi(ux + vy)]
r dr dtheta

Now substitute:

u = w cos(phi)
v = w sin(phi)
and:
x = r cos(theta)
y = r sin(theta)


Then:
ux + vy =
(w cos(phi))(r cos(theta))
+
(w sin(phi))(r sin(theta))

Factor out wr:

= wr[cos(phi)cos(theta) + sin(phi)sin(theta)]

Use the trigonometric identity:
cos(A-B) = cos(A)cos(B) + sin(A)sin(B)

Therefore:
ux + vy = wr cos(theta - phi)

So the Fourier transform becomes:

F(w,phi)
= F(w cos(φ), w sin(φ)) = 
integral
integral
f(r,theta)
exp[-j2pi wr cos(theta-phi)] r dr dtheta

This form is very useful because the Fourier transform
depends on the DIFFERENCE between the two angles: theta - phi.

---
3. NOW ROTATE THE IMAGE

Start with the 2-D Fourier transform in polar coordinates:

F(w,phi)
=
∫∫ f(r,theta)
    exp[-j 2pi w r cos(theta - phi)]
    r dr dtheta


Now look at the Fourier transform at a rotated frequency angle:
F(w, phi + theta_0)

Substitute phi + theta_0 into the formula:
F(w, phi + theta_0)
=
∫∫ f(r,theta)
    exp[-j 2pi w r cos(theta - (phi + theta_0))]
    r dr dtheta


Simplify the cosine:
theta - (phi + theta_0) = theta - theta_0 - phi

Therefore:

F(w, phi + theta_0)
=
∫∫ f(r,theta)
    exp[-j 2pi w r cos((theta - theta_0) - phi)]
    r dr dtheta


Now make a change of variable:

theta' = theta - theta_0
Therefore: theta = theta' + theta_0

and: dtheta = dtheta'


So:

F(w, phi + theta_0)
=
∫∫ f(r, theta' + theta_0)
    exp[-j 2pi w r cos(theta' - phi)]
    r dr dtheta'


Now define the rotated image:

g(r,theta') = f(r, theta' + theta_0)


Therefore:

F(w, phi + theta_0)
=
∫∫ g(r,theta')
    exp[-j 2pi w r cos(theta' - phi)]
    r dr dtheta'

But this integral is exactly the Fourier transform of g:
G(w,phi)

Therefore:

G(w,phi)= F(w, phi + theta_0)


So:

g(r,theta) = f(r,theta + theta_0)
corresponds to:
G(w,phi) = F(w,phi + theta_0)


In words:

A rotation by -theta_0 in the spatial domain
produces the same rotation by -theta_0
in the frequency domain.

Equivalently:

g(r,theta)
=
f(r,theta - theta_0)

gives:

G(w,phi)
=
F(w,phi - theta_0)

which represents a counterclockwise rotation
by theta_0 in both domains.



---
5. WHAT DOES THIS MEAN?

We defined the rotated image as:

g(r,theta) = f(r,theta-theta0)

This represents rotating the image
counterclockwise by theta0.

The Fourier transform becomes:

G(w,phi) = F(w,phi-theta0)

Therefore the Fourier transform is rotated
by the SAME angle.

---
6. WHY DOES THE SAME ANGLE APPEAR?

The important expression in the Fourier transform is:
cos(theta - phi)
Notice that it depends only on the ANGULAR DIFFERENCE:
theta - phi
If we rotate the image by theta0:
theta becomes: theta' + theta0

To keep the same angular difference, 
the frequency angle must effectively 
change by the same amount.
That is why: theta  -> theta + theta0
is accompanied by: phi -> phi + theta0


Therefore:

f(r,theta+theta0) <-> F(w,phi+theta0)

---
7. MATCHING THE BOOK'S FORM

Some books write the property approximately as:

f(r, theta + theta0) <-> F(w, phi + theta0)

The difference is simply the sign convention
used to describe the rotation.


The important relationship is:

SPATIAL ROTATION ANGLE
= FREQUENCY-DOMAIN ROTATION ANGLE

--- 
SUMMARY

Rotate the image:

f(r,theta) -> f(r,theta-theta0)

and the Fourier transform rotates by the same angle:

F(w,phi) -> F(w,phi-theta0)

"""