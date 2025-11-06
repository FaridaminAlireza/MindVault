"""
Why the 2D Determinant Gives the Parallelogram Area
====================================================

Consider two 2D vectors:

u = (u_x, u_y),   v = (v_x, v_y)

We want the area of the parallelogram spanned by u and v.

---
Step 1: Area formula for a parallelogram

The area of a parallelogram is:

Area = base × height

- Choose u as the base vector.
- Height = perpendicular distance from the tip of v to the line along u.

Let θ = angle between u and v. Then:

Height = |v| sin(θ)

So:

Area = |u| × Height = |u| × |v| sin(θ)

---
Step 2: Express |u|, |v|, and sin(θ) in components

The magnitude of u: |u| = sqrt(u_x^2 + u_y^2)  
The magnitude of v: |v| = sqrt(v_x^2 + v_y^2)

From the dot product formula:

u · v = |u||v| cos(θ) → cos(θ) = (u_x v_x + u_y v_y) / (|u||v|)

Then sin^2(θ) = 1 − cos^2(θ):

sin^2(θ) = 1 − [(u_x v_x + u_y v_y)^2 / (|u|^2 |v|^2)]  
sin(θ) = sqrt(|u|^2 |v|^2 − (u_x v_x + u_y v_y)^2) / (|u||v|)

---
Step 3: Area = |u||v| sin(θ)

Substitute sin(θ) in the area formula:

Area = |u| |v| sin(θ)  
     = |u| |v| × [ sqrt(|u|^2 |v|^2 − (u_x v_x + u_y v_y)^2) / (|u||v|) ] 
     = sqrt(|u|^2 |v|^2 − (u_x v_x + u_y v_y)^2)

---
Step 4: Expand |u|^2 |v|^2 − (u · v)^2

Compute:

|u|^2 |v|^2 = (u_x^2 + u_y^2)(v_x^2 + v_y^2)  
            = u_x^2 v_x^2 + u_x^2 v_y^2 + u_y^2 v_x^2 + u_y^2 v_y^2

(u · v)^2 = (u_x v_x + u_y v_y)^2 = u_x^2 v_x^2 + 2 u_x u_y v_x v_y + u_y^2 v_y^2

Subtract:

|u|^2 |v|^2 − (u · v)^2 = (u_x^2 v_y^2 + u_y^2 v_x^2) − 2 u_x u_y v_x v_y  
                         = (u_x v_y − u_y v_x)^2

---
Step 5: Take the square root

Area = sqrt((u_x v_y − u_y v_x)^2) = |u_x v_y − u_y v_x|

This is exactly the **determinant of the 2×2 matrix**:

| u_x  v_x |
| u_y  v_y | = u_x v_y − u_y v_x

---
Step 6: Sign of the determinant

- Positive determinant → v is counterclockwise from u (right-hand orientation in 2D)  
- Negative determinant → v is clockwise from u  

Thus, the determinant encodes both area (magnitude) and orientation (sign).
The formula Area = |u_x v_y − u_y v_x| comes naturally from projecting v
 perpendicular to u and using base × height.
It also explains why the determinant gives the signed area of the
 parallelogram spanned by two 2D vectors.

"""