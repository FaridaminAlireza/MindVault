"""
Hyperplane and dot product - it gets at the heart of geometry,
  linear algebra, and how we represent spaces mathematically.
---
1. What a hyperplane is
   A **hyperplane** is a flat, (n-1)-dimensional subspace in an n-dimensional space.
   For example:

* In 2D → a hyperplane is a **line**.
* In 3D → a hyperplane is a **plane**.
* In nD → it’s a “flat slice” of one dimension less than the space.
---

2. The algebraic definition
   A hyperplane is typically written as:

w · x + b = 0

where:

* w is a **normal vector** (a vector perpendicular to the hyperplane),
* x is any point on the plane,
* b is a **bias** (or offset) controlling how far the hyperplane is from the origin.

---

3. Why the dot product
   The dot product captures **orthogonality** and **projection** —
   both are exactly what we need to describe a flat surface.

Let’s see why:

a) The dot product defines perpendicularity
The dot product w · x measures how much of x lies **in the direction of** w.
If two vectors are perpendicular, their dot product is **zero**.

So when we say:

w · x + b = 0

w is the normal vector to the hyperplane, which means it gives
the direction perpendicular to the hyperplane.Its length is arbitrary 
— only the direction matters for defining the orientation of the hyperplane.

If b = 0 → the hyperplane passes through the origin.

If b ≠ 0 → the hyperplane is shifted along w, so the
closest point on the hyperplane to the origin is
in the direction of w at distance |b|/||w||.

w never has to “start” on the hyperplane; it’s just a direction vector.

∥w∥ (the norm of w) is the length (magnitude) of the vector.
Distance from origin to hyperplane:

distance = |b|/||w||

we are saying:
"All points x whose projection onto w equals -b" form the hyperplane.


That’s a clean, algebraic way of defining 
“all points orthogonal to a given direction.”

---
b) The dot product gives a linear condition
The expression w · x + b is **linear** in x.
So it divides the space into two **half-spaces**:

w · x + b > 0 → one side
w · x + b < 0 → other side

That’s why it’s perfect for:

* Geometry (defining planes)
* Machine learning (linear classifiers, SVMs)
* Optimization (linear constraints)

---

4. Intuitive geometric picture
   You can think of the dot product w · x as 
   a **height function** — it measures how “far”
   along direction w a point x is. Then the hyperplane
   is just the set of all points with the **same height**
   (i.e., where this projection equals some constant).

---
5. Example in 2D
   Let’s take w = [2, 1] and b = -3.

Equation:
2x1 + x2 - 3 = 0

This defines a line.
The vector [2,1] is **perpendicular** to that line,
because all points on the line have the same projection
onto [2,1].

---
Summary
We use a **dot product** to define a hyperplane because it:

* Measures projection along a normal vector,
* Expresses perpendicularity compactly,
* Defines a **linear constraint** dividing space into two regions.

It’s the most natural, coordinate-free way to describe a
flat surface in any number of dimensions.

Intuitively:
We use a **dot product** to define a hyperplane 
because it’s the **simplest mathematical way to
express perpendicularity** in any number of dimensions.

* The **dot product** w · x measures how much of x lies
in the direction of w.
* When that value equals a constant (-b), it means
**all those points have the same projection** on w.
* The set of all such points forms a flat surface 
— a **hyperplane** — that’s perpendicular to w.

So the dot product gives us: 
* The notion of “flatness” (linear constraint),
* A clean geometric separation into two half-spaces,
* A direction of normal (w) and a position (b).

Without the dot product, we’d have no simple way to describe
“all points orthogonal to a given direction” in higher dimensions.

"""


"""
How to calculate the distance from a point to a hyperplane.

### **Problem Setup**
We have:
* Hyperplane: `w · x + b = 0`

  * `w` is a vector normal to the hyperplane (`w = [w1, w2, ..., wn]`)
  * `b` is the bias / intercept

* Point: `x0 = [x01, x02, ..., x0n]`

We want: **distance `d` from `x0` to the hyperplane**.

---
### **Step 1: Vector Form of Distance**

The distance from a point to a plane (or hyperplane) is
along the direction of the normal vector `w`.

* Let `p` be the projection of `x0` onto the hyperplane.
* The vector from `x0` to the hyperplane is:

x0  (your point)
p   (its projection on the plane)
The line connecting them — (x0 → p) — is the shortest path to the plane.

  ```
  v = x0 - p
  ```
* This vector is parallel to `w` (the normal vector).

So, `v = λ * w` for some scalar `λ`.


The hyperplane’s normal vector w points perpendicular
to the surface of the plane. So the shortest path 
(the perpendicular drop from x0 to the plane) must
go along the direction of w.

That means: x0 - p  is parallel to w

And in vector math, “is parallel to” means:

x0 - p = λ * w     (for some scalar λ)
λ can be positive or negative depending on
which side of the plane x0 lies.

---
### **Step 2: Hyperplane Equation at the Projection**

* Since `p` lies on the hyperplane, it satisfies:

  ```
  w · p + b = 0
  ```

* Substitute `p = x0 - λ * w`:

  ```
  w · (x0 - λ * w) + b = 0
  ```

* Expand the dot product:

  ```
  w · x0 - λ * (w · w) + b = 0
  ```

* Solve for λ:

  ```
  λ = (w · x0 + b) / (w · w)
  ```

---

### **Step 3: Distance Formula**

* The distance `d` is the magnitude of `v = λ * w`:

  ```
  d = ||v|| = ||λ * w|| = |λ| * ||w||
  ```

* Substitute `λ` from Step 2:

  ```
  d = |(w · x0 + b) / (w · w)| * ||w||
  ```

* Note that `||w||^2 = w · w`, so simplify:

  ```
  d = |w · x0 + b| / ||w||
  ```

This is the **final formula**:

```
Distance from point x0 to 
hyperplane w·x + b = 0:

d = |w · x0 + b| / ||w||
```

---
"""