"""
# 1. Scaling Transformation

Scaling changes the size of a vector along each axis.

Matrix form in 2D:
S = [[sx, 0],
     [0, sy]]
where sx, sy are scaling factors along x and y.

Transformation:
[x']   [sx  0 ]  [x]   [sx*x]
[y'] = [0  sy ]  [y] = [sy*y]

Proof / Reasoning:
* Each coordinate is multiplied by
a constant scaling factor.
* If sx > 1 or sy > 1, 
it stretches along that axis;
if 0 < sx < 1, it shrinks.

Example:
Scale by 2 along x and 0.5 along y:
S = [[2, 0], 
     [0, 0.5]]
Apply to vector [3, 4]:
[2*3, 0.5*4] = [6, 2]

---
# 2. Rotation Transformation

Rotation rotates a vector by an angle theta
counterclockwise about the origin.

Matrix form in 2D:
R(theta) = [[cos(theta), -sin(theta)],
            [sin(theta),  cos(theta)]
            ]

Transformation:
[x']   [cos(theta)  -sin(theta)] [x]   [x*cos(theta) - y*sin(theta)]
[y'] = [sin(theta)   cos(theta)] [y] = [x*sin(theta) + y*cos(theta)]

Proof / Reasoning:

* Express vector in polar coordinates: 
x = r*cos(phi), y = r*sin(phi).
* Rotating by theta:
  x' = r*cos(phi + theta) = x*cos(theta) - y*sin(theta)
  y' = r*sin(phi + theta) = x*sin(theta) + y*cos(theta)

Complete version: 
We start with a 2D point (x, y).
Any point in 2D can be expressed in polar form:

x = r * cos(phi)
y = r * sin(phi)

where
* r is the magnitude (distance from origin)
  r = √(x² + y²)
* phi is the angle the vector makes with the positive x-axis

Now we rotate this vector by an angle theta.
A rotation adds angle theta to phi:

New angle = phi + theta

So after rotation:

x' = r * cos(phi + theta)
y' = r * sin(phi + theta)

Now apply angle sum identities
from trigonometry:

cos(A + B) = cos(A)cos(B) – sin(A)sin(B)
sin(A + B) = sin(A)cos(B) + cos(A)sin(B)

Let A = phi, B = theta:

cos(phi + theta)
= cos(phi)cos(theta) – sin(phi)sin(theta)

sin(phi + theta)
= sin(phi)cos(theta) + cos(phi)sin(theta)

Substitute back x = r*cos(phi) and y = r*sin(phi):

x' = r * [cos(phi)cos(theta) – sin(phi)sin(theta)]
= (r*cos(phi))*cos(theta) – (r*sin(phi))*sin(theta)
= x*cos(theta) – y*sin(theta)

y' = r * [sin(phi)cos(theta) + cos(phi)sin(theta)]
= (r*sin(phi))*cos(theta) + (r*cos(phi))*sin(theta)
= x*sin(theta) + y*cos(theta)

Final result:
x' = x*cos(theta) – y*sin(theta)
y' = x*sin(theta) + y*cos(theta)

Meaning:
A rotation in the plane can be expressed entirely
using x and y without needing r or phi after substitution.
This gives us the rotation matrix:

[x'] = [cos(theta)  -sin(theta)] [x]
[y'] = [sin(theta)   cos(theta)] [y]

Example:
Rotate (1,0) by 90 degrees (pi/2 radians):
R(pi/2) = [[0, -1], 
           [1, 0]]

[0, -1; 1, 0] * [1,0] = [0,1]

---
# 3. Shear Transformation

Shear slants the shape along
one axis while keeping the other fixed.

Horizontal shear (x changes with y):
H = [[1, kx], 
     [0, 1]]
[x'] = x + kx*y
[y'] = y

Vertical shear (y changes with x):
V = [[1, 0], 
     [ky, 1]]

[x'] = x
[y'] = y + ky*x

Proof / Reasoning:
* Shear shifts one coordinate linearly
with respect to the other.
* Determinant of shear matrix is 1,
so area is preserved but angles change.

Example:
Horizontal shear with kx = 2 on (1,2):
[1,2;0,1]*[1,2] = [1+2*2, 2] = [5,2]

---
# 4. Reflection Transformation

Reflection flips vectors across a line or axis.

Matrix forms in 2D:

* About x-axis: 
[[1,0], 
 [0,-1]]
* About y-axis: 
[[-1,0], 
 [0,1]]
* About y=x: 
[[0,1], 
 [1,0]]

Example:
Reflect (3,4) across x-axis:
[1,0;0,-1]*[3,4] = [3,-4]

---
# 5. Combined Transformation

Multiple transformations can be combined by
multiplying matrices. Order matters.

Example: Scale → Rotate → Shear:
T = H * R * S
Apply T to vector v to perform all three in sequence.
---
# 6. Key Insights

1. Determinant of transformation matrix tells area/volume change:

   * |det| > 1 → stretches
   * |det| < 1 → shrinks
   * |det| = 1 → preserves area (rotation, shear, reflection)

2. Eigenvectors and eigenvalues:

   * Directions only scaled, not rotated.
   * Scaling matrix eigenvectors are along axes.

3. Geometric meaning:

   * Scaling → stretch/shrink
   * Rotation → spin around origin
   * Shear → slant shape while preserving area
   * Reflection → mirror image

"""

"""
Rotation in 3D and higher dimensions 
is much richer and a bit trickier than in 2D.

# ROTATION IN 2D (for comparison)

In 2D, rotation is simple:
• There is only one axis of rotation (the origin)
• There is only one angle that determines rotation
→ Any rotation is fully described by a single number: θ

Rotation matrix (2×2):
[ cosθ  -sinθ ]
[ sinθ   cosθ ]

---
# ROTATION IN 3D

In 3D:
• Rotation does not happen around the origin alone
• It happens about an axis (a line through the origin)
• You still have a single angle θ
→ Rotation is determined by:
(a) the axis of rotation (unit vector u)
(b) the angle θ

This leads to multiple valid rotation matrices in 3D.

Example: Rotation around the Z-axis:

[ cosθ  -sinθ   0 ]
[ sinθ   cosθ   0 ]
[  0      0     1 ]

Similarly, around the X or Y axes:

Rotate around X-axis:
[ 1     0        0    ]
[ 0   cosθ   -sinθ ]
[ 0   sinθ    cosθ ]

Rotate around Y-axis:
[ cosθ   0  sinθ ]
[ 0      1   0  ]
[-sinθ   0  cosθ]

More generally, rotation about any axis 
u = (ux, uy, uz) uses 
Rodrigues’ rotation formula (3×3 matrix).

Key idea:
• There is no single universal rotation matrix 
  in 3D like in 2D
• The space of rotations in 3D
is much larger — described by
SO(3) (3 degrees of freedom)

---

# ROTATION IN 4D (and higher dimensions)

Things become even more interesting.

In 4D:
• Rotation does not happen around a line
• It happens inside a plane (2D subspace)
• You must choose which plane to rotate in

Examples of planes:

* x-y plane
* x-z plane
* y-w plane
* etc…

Each plane gets its own independent rotation angle.

Example: Rotation in the x-y plane (4×4 matrix):
[ cosθ  -sinθ   0      0 ]
[ sinθ   cosθ   0      0 ]
[  0      0     1      0 ]
[  0      0     0      1 ]

But we could also rotate in another plane simultaneously,
e.g., z-w plane:

[ 1     0      0       0     ]
[ 0     1      0       0     ]
[ 0     0    cosφ   -sinφ ]
[ 0     0    sinφ    cosφ ]

This means a 4D object can rotate in two planes at once.
Example: It may spin one way in x-y and a different way in z-w.

In n dimensions (n > 2):
• Rotations always occur in planes
• Number of independent rotation planes = n(n−1)/2
→ That’s the number of degrees of freedom for rotation in nD

---

# SUMMARY

| Dimension | What defines rotation?           | Degrees of freedom |
| --------- | -------------------------------- | ------------------ |
| 2D        | Only angle θ                     | 1                  |
| 3D        | Axis + angle                     | 3                  |
| 4D        | Several planes (each with angle) | 6                  |
| nD        | Multiple planes                  | n(n−1)/2           |

---

# KEY INSIGHTS

✔ In 2D → rotation in 1 plane
✔ In 3D → rotation about 1 axis 
(equivalently: rotation in a plane 
 perpendicular to the axis)
✔ In 4D+ → rotation can occur in 
multiple independent planes at once

Example phenomenon in 4D:
A shape can rotate without anything 
that looks like “turning” to a 3D observer —
one part of rotation can cancel another from 3D view.

---
Learn more?
• Rodrigues’ formula derivation
• Why gimbal lock happens in 3D but not in 4D
• Connection to Special Orthogonal Groups SO(n)
"""

"""
Derivation of Rodrigues’ Rotation Formula and
how 3D rotations are constructed from 
the idea of 2D rotations around coordinate axes.

# PART 1 — ROTATION IN 2D (THE SEED IDEA)

In 2D, rotation of a vector (x, y)
by angle θ around the origin:

[x']   [cosθ  -sinθ] [x]
[y'] = [sinθ   cosθ] [y]

This rotates in the x–y plane, 
which is equivalent to 
a 3D rotation around the z-axis.

Extend the 2×2 matrix to 3×3 (preserve z):

[ cosθ  -sinθ   0 ]
[ sinθ   cosθ   0 ]
[  0      0     1 ]

This is the rotation around z-axis.

So:
2D rotation is the blueprint for all 3D rotations.


# PART 2 — ROTATION IN 3D ABOUT A COORDINATE AXIS

We can similarly rotate around 
x or y by rotating the planes:

1. Rotate around x-axis → rotate the y–z plane:

[ 1     0       0     ]
[ 0   cosθ      -sinθ ]
[ 0   sinθ      cosθ  ]

2. Rotate around y-axis → rotate the z–x plane:

[ cosθ   0   sinθ ]
[ 0      1   0    ]
[-sinθ   0   cosθ ]

So we now know:

Any rotation in 3D around a coordinate axis is 
just a 2D rotation in a perpendicular plane.

# BUT THIS IS NOT ENOUGH
We need to rotate around any arbitrary axis,
not just x, y, z.

To do that, we need a formula that works for
any unit vector axis u = (ux, uy, uz).

This leads us to Rodrigues’ Rotation Formula.

# PART 3 — GEOMETRIC DECOMPOSITION OF A VECTOR v

Let:

• u = axis of rotation (unit vector, |u| = 1)
• v = vector we want to rotate
• θ = rotation angle

We decompose v into parts parallel and
 perpendicular to u:

1. Parallel component:
   v_parallel = (u ⋅ v) * u

2. Perpendicular component:
   v_perp = v – v_parallel

3. A third direction perpendicular to both:
   v_cross = u × v

These three vectors are mutually perpendicular.

Important geometric facts:

* Rotating v around u does not change the parallel part.
* Only v_perp rotates in the plane perpendicular to u.
* v_cross gives the 90°-rotated direction inside that plane.

So rotation must look like:

R(u,θ)v =
v_parallel (unchanged)

* (v_perp * cosθ)
* (v_cross * sinθ)

This is the core idea of Rodrigues’ formula.


Only v_perp participates in the rotation,
and this rotation is a 2D rotation 
inside the plane perpendicular to u.

So v_perp is rotated just like a 2D vector:

x' = x cosθ − y sinθ
y' = x sinθ + y cosθ

This same pattern MUST appear in 3D rotations —
because inside the perpendicular plane,
the rotation is literally a 2D rotation.
That’s why cosθ and sinθ appear.


Cross product behaves like 
a 90° rotation inside that plane.

For example, with the z-axis rotation:
z-axis = (0, 0, 1)
v_perp = (x, y, 0)
u × v_perp = (0,0,1) × (x,y,0) = (−y, x, 0)

But (−y, x) is the 90° rotation of
    (x,y) in the xy-plane.

So:
v_perp plays the role of 
“x-axis direction in the plane”

v_cross plays the role of 
“y-axis direction in the plane” (90° shift)

In every plane, for every axis u, 
the cross product u × v_perp produces 
the direction that is exactly 90° ahead 
of v_perp with respect to the rotation direction.

Therefore:
v_perp = “cos basis direction”
v_cross = “sin basis direction” (90° shifted)

Just like in 2D rotations:

x' = x cosθ − y sinθ
y' = x sinθ + y cosθ

We need two perpendicular directions in the plane.
v_perp and v_cross ARE those two directions.


Great — you understand the 2D rotation formula and the idea that
`v_perp` and `v_cross` are two perpendicular directions in the plane.
Now the remaining question is:

**How exactly do these two ideas connect?
How do we replace the 2D basis vectors (i, j)
with the 3D basis vectors (v_perp, v_cross)?**

### 0. RECALL: 2D ROTATION USES TWO PERPENDICULAR DIRECTIONS

In 2D, the standard basis is:
e1 = (1, 0)
e2 = (0, 1)

These are:
* perpendicular
* unit length
* span the xy-plane

Rotate a vector:
v = x * e1 + y * e2

Rotation gives:

R(v) = x*cosθ * e1 + x*sinθ * e2
+ y*(-sinθ) * e1 + y*cosθ * e2

Or grouped:

R(v) = (x*cosθ - y*sinθ)*e1 + (x*sinθ + y*cosθ)*e2


### 1. IN 3D, ROTATION STILL HAPPENS IN A 2D PLANE

When rotating a vector v in 3D around an axis u,
the motion still happens **in a 2D plane** 
— the plane perpendicular to u.

So inside that plane, you again need:

* a first perpendicular direction
* a second perpendicular direction
rotated 90° from the first

In the xy-plane we used (1,0) and (0,1).
But in a general plane, those directions
are not convenient.

Instead we use:

e1' = v_perp (the component of v inside the plane)
e2' = v_cross = u × v_perp (the 90°-rotated version)

These two form an orthogonal basis 
**for the rotation plane**.

So think of them as the new “i and j” inside this plane.

---
### 2. HOW EXACTLY WE CHANGE 
# FROM (e1, e2) → (v_perp, v_cross)

---

Let’s imagine we take the 2D formula:

x' = x cosθ − y sinθ
y' = x sinθ + y cosθ

This works when:

* x is the coordinate along the first direction
* y is the coordinate along the second direction

But in a general 3D plane, the first direction is:

v_perp (the direction currently pointing to v)

and the second direction (90° advanced direction) is:

v_cross = u × v_perp

So we now think:

x = coefficient of v in the v_perp direction
y = coefficient of v in the v_cross direction

But because we constructed:

v_perp = projection of v
v_cross = u × v_perp
and v has **no component 
along v_cross before rotation**,
we only have:

x = |v_perp|
y = 0

This means v looks like:

v = (|v_perp| along e1’) + (0 along e2’)

where
e1’ = unit vector parallel to v_perp
e2’ = unit vector parallel to v_cross

Now, apply the 2D rotation inside that plane:

After rotation:

component along e1' = |v_perp| * cosθ
component along e2' = |v_perp| * sinθ

Now convert back from components to vectors:

component along e1' → v_perp * cosθ
component along e2' → v_cross * sinθ

That’s where these terms come from.

### 3. PUTTING IT ALL TOGETHER

Start with v. Decompose:

v = v_parallel + v_perp

Rotate only the perpendicular part:

You take the perpendicular plane and
treat it like a 2D plane.

In that plane:

* v_perp is your "x direction"
* v_cross is your "y direction"
* original vector has coordinates (|v_perp|, 0)

After 2D rotation by θ:

(new_x, new_y) = (|v_perp| cosθ, |v_perp| sinθ)

Convert back to vectors:

new_v_perp = v_perp * cosθ
new_v_cross = v_cross * sinθ

Add the unchanged parallel part:

R(v) = v_parallel + v_perp*cosθ + v_cross*sinθ



### 4. ANALOGY — ROTATING THE BASIS VECTORS

In 2D:

e1 → e1*cosθ + e2*sinθ
e2 → −e1*sinθ + e2*cosθ

In 3D plane:

e1' → e1'*cosθ + e2'*sinθ
e2' → −e1'*sinθ + e2'*cosθ

Now assign:

e1' = (v_perp / |v_perp|)
e2' = (v_cross / |v_cross|)

Then reconstruct the vector in that plane.

### 5. SUMMARY (VERY SIMPLE VERSION)

1. Rotation in 3D still happens in a 2D plane.
2. That plane has its own “x-axis” = v_perp.
3. It has its own “y-axis” = v_cross = u × v_perp.
4. Inside that plane, we apply the *ordinary* 2D rotation formula.
5. Then we convert back from (x’, y’) to the actual vector:

   new v = v_parallel + x’ * e1' + y’ * e2'

which becomes:

R(v) = v_parallel + v_perp*cosθ + v_cross*sinθ.
---

# PART 4 — CLEANING UP THE FORMULA

We substitute:

v_parallel = (u ⋅ v) u
v_perp = v – (u ⋅ v)u
v_cross = u × v

Plug them into:

R(v) = v_parallel + cosθ * v_perp + sinθ * v_cross

Expand:

R(v) = (u⋅v)u +
cosθ [v – (u⋅v)u] +
sinθ (u×v)

Distribute cosθ:

R(v) = (u⋅v)u + cosθ v – cosθ (u⋅v)u + sinθ (u×v)

Group terms:

R(v) = cosθ v
+ sinθ (u×v)
+ (1 – cosθ)(u⋅v)u

This is the vector form of Rodrigues’ rotation formula.

---

# PART 5 — MATRIX FORM (THE FAMOUS FORMULA)

We now rewrite the vector expression using matrices.

1. Write u = (ux, uy, uz).
2. Define the "cross product matrix":

[u]_x =
[   0   -uz   uy  ]
[  uz    0   -ux  ]
[ -uy   ux    0   ]

Such that:

[u]_x v = u × v

3. Also, define uu^T (outer product):

uu^T =
[ ux*ux   ux*uy   ux*uz ]
[ uy*ux   uy*uy   uy*uz ]
[ uz*ux   uz*uy   uz*uz ]

4. Combine terms from:

R(v) = cosθ I v + sinθ [u]_x v + (1 – cosθ) (uu^T) v

Factor out v:

R = cosθ I + sinθ [u]_x + (1 – cosθ) uu^T

This is the matrix form of Rodrigues’ rotation formula.

---

# PART 6 — INTUITION SUMMARY

Rodrigues’ formula comes from:

1. Breaking v into: parallel, 
perpendicular, cross-product directions
2. Rotating the perpendicular plane using
the 2D rotation formula
3. Reassembling the components
4. Rewriting everything as matrices

So the process generalizes:

2D rotation → rotation around z
→ rotation around any coordinate axis
→ rotation around any unit vector axis u

This is why Rodrigues’ formula is 
the universal 3D rotation formula.

---
# PART 7 — FINAL FORMULAS (RAW TEXT)

Vector form:

R(u,θ)v = v*cosθ + (u×v)*sinθ + u*(u⋅v)*(1 − cosθ)

Matrix form:

R = cosθ*I + sinθ*[u]_x + (1−cosθ)*(u*u^T)
---

Learn more?

• why quaternions encode the
 same rotation
• how to derive rotation matrices 
from quaternion multiplication
• how to combine rotations cleanly
 without gimbal lock

"""


