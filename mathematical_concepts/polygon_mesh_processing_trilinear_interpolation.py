"""
Trilinear Interpolation

1. Motivation
Suppose we know values of a function only at the 
eight corners of a rectangular box (a voxel in 3D space).

For example:
* Temperature at the corners of a cube
* Density values in a CT scan
* Color values inside a 3D texture
* Signed distance values in a volumetric grid

We want to estimate the function value at
an arbitrary point inside the box.

The simplest method is **trilinear interpolation**.

The name comes from:

* Linear in x
* Linear in y
* Linear in z

It is the 3D extension of:
* Linear interpolation (1D)
* Bilinear interpolation (2D)

---
2. Geometry

Consider a box (x₀,y₀,z₀) → (x₁,y₁,z₁)
with function values known at all eight corners.

Corner notation:
f₀₀₀ = f(x₀,y₀,z₀)
f₁₀₀ = f(x₁,y₀,z₀)
f₀₁₀ = f(x₀,y₁,z₀)
f₁₁₀ = f(x₁,y₁,z₀)
f₀₀₁ = f(x₀,y₀,z₁)
f₁₀₁ = f(x₁,y₀,z₁)
f₀₁₁ = f(x₀,y₁,z₁)
f₁₁₁ = f(x₁,y₁,z₁)

We want f(x,y,z) for a point inside the box.

---
3. Normalized Coordinates

Define local coordinates:

u = (x - x₀)/(x₁ - x₀)

v = (y - y₀)/(y₁ - y₀)

w = (z - z₀)/(z₁ - z₀)

Then 0 ≤ u,v,w ≤ 1

Interpretation:
u = relative position in x direction
v = relative position in y direction
w = relative position in z direction

For example:

u = 0.3 means 30% from x₀ toward x₁.

---
4. Reminder: 1D Linear Interpolation

Suppose we know 
f₀ and f₁ at the ends of an interval.

Then f(u) = (1-u)f₀ + uf₁

Check: 
u = 0 gives f₀
u = 1 gives f₁
This is a weighted average.
The weights: (1-u), u sum to 1.
---
5. Step 1: Interpolate Along x

At z=z₀ and y=y₀:
c₀₀ = (1-u)f₀₀₀ + uf₁₀₀

At z=z₀ and y=y₁:
c₁₀ = (1-u)f₀₁₀ + uf₁₁₀

At z=z₁ and y=y₀:
c₀₁ = (1-u)f₀₀₁ + uf₁₀₁

At z=z₁ and y=y₁:

c₁₁ = (1-u)f₀₁₁ + uf₁₁₁

We now have four interpolated values.

---
6. Step 2: Interpolate Along y

Interpolate between c₀₀ and c₁₀:
d₀ = (1-v)c₀₀ + vc₁₀

Interpolate between c₀₁ and c₁₁:
d₁ = (1-v)c₀₁ + vc₁₁

Now only two values remain.
---
7. Step 3: Interpolate Along z

Finally: f(u,v,w) = (1-w)d₀ + wd₁

This is the trilinear interpolated value.

---
8. Expanding the Formula

Substitute d₀ and d₁.

Then substitute c-values.

After expansion:

f(u,v,w)

= (1-u)(1-v)(1-w)f₀₀₀

* u(1-v)(1-w)f₁₀₀

* (1-u)v(1-w)f₀₁₀

* uv(1-w)f₁₁₀

* (1-u)(1-v)w f₀₀₁

* u(1-v)w f₁₀₁

* (1-u)vw f₀₁₁

* uvw f₁₁₁

This is the standard trilinear interpolation formula.

---
9. Basis Functions

The eight weights are:

N₀₀₀=(1-u)(1-v)(1-w)

N₁₀₀=u(1-v)(1-w)

N₀₁₀=(1-u)v(1-w)

N₁₁₀=uv(1-w)

N₀₀₁=(1-u)(1-v)w

N₁₀₁=u(1-v)w

N₀₁₁=(1-u)vw

N₁₁₁=uvw

Thus f(u,v,w)=Σ Nᵢⱼₖ fᵢⱼₖ

These are called the trilinear basis functions.
---
10. Why Do the Weights Sum to One?

Add all eight basis functions:
[(1-u)+u]
[(1-v)+v]
[(1-w)+w]
= 1·1·1

= 1

Therefore

ΣNᵢⱼₖ = 1

This property is called the **partition of unity**.

Consequences:
* weighted average
* no artificial scaling
* constant functions reproduced exactly

---
11. Proof of Exact Corner Reproduction

Consider corner (u,v,w)=(0,0,0).

Then

N₀₀₀=1
all other basis functions = 0
Therefore
f(0,0,0)=f₀₀₀

Similarly:

f(1,0,0)=f₁₀₀
f(0,1,0)=f₀₁₀
f(1,1,0)=f₁₁₀
f(0,0,1)=f₀₀₁
f(1,0,1)=f₁₀₁
f(0,1,1)=f₀₁₁
f(1,1,1)=f₁₁₁

Thus every corner value is reproduced exactly.
This is the interpolation property.
---
12. Why Is It Called "Trilinear"?

Fix y and z.
Then v and w become constants.

The formula becomes
f(u)=A+Bu
which is linear in u.

Similarly:
* fixing x and z gives a linear function in v
* fixing x and y gives a linear function in w

Hence the function is linear in each variable separately.

Therefore it is called trilinear.
---

13. Polynomial Form

After collecting terms:

f(u,v,w)
= a₀
* a₁u
* a₂v
* a₃w
* a₄uv
* a₅uw
* a₆vw
* a₇uvw

Notice:

u², v², w²
do not appear.

The highest-order term is uvw.

---
14. Numerical Example

Consider a unit cube.

Corner values:
f₀₀₀ = 0
f₁₀₀ = 10
f₀₁₀ = 20
f₁₁₀ = 30
f₀₀₁ = 40
f₁₀₁ = 50
f₀₁₁ = 60
f₁₁₁ = 70
Find the value at
(u,v,w)=(0.5,0.5,0.5)
Center of the cube.

Every basis function equals
(0.5)(0.5)(0.5) = 0.125

Therefore
f = 0.125(0+10+20+30+40+50+60+70)
= 0.125(280) = 35

The interpolated value at the center is f = 35

which is simply the average of the eight corners.
---
15. Geometric Interpretation

Each corner pulls the result 
according to its distance.

A corner near the query point 
receives a larger weight.

A corner far away receives 
a smaller weight.

For example:
N₀₀₀=(1-u)(1-v)(1-w)
becomes large when the point is close to corner (0,0,0).

Thus trilinear interpolation computes a distance-based 
weighted average of the eight corner values.

---
16. Error Behavior

Trilinear interpolation exactly reproduces:
* constant functions
* linear functions
* functions of the form
a₀+a₁x+a₂y+a₃z+a₄xy+a₅xz+a₆yz+a₇xyz

Errors arise when the true function contains:
x², y², z² 
or higher-order terms.

Therefore accuracy improves as 
the grid cells become smaller.

---
17. Applications

Computer graphics:
* volume rendering
* voxel grids
* 3D textures

Medical imaging:
* CT volumes
* MRI volumes

Scientific computing:
* scalar fields
* finite-volume data

Geometry processing:
* signed distance fields
* level-set methods
* volumetric meshes

Machine learning:
* neural field sampling
* 3D feature grids
"""