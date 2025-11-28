"""
Principle Angles in Trigonometry

1. Introduction
A principal angle 
is the smallest positive angle 
measured from the positive x-axis 
to a given ray in standard position.
In standard trigonometry,
angles can have infinitely many 
equivalent rotations because 
adding or subtracting multiples of 360°
(or 2π radians) produces the same terminal side.
Therefore, every angle has a unique principal angle
inside a fixed interval.

For degrees: Principal angle range is 0° ≤ θ < 360°
For radians: Principal angle range is 0 ≤ θ < 2π

Examples:
The angle 390° has a principal angle:
390° − 360° = 30°
The angle −45° has a principal angle:
−45° + 360° = 315°
The angle 17π/6 (≈510°) has a principal angle:
17π/6 − 2π = 17π/6 − 12π/6 = 5π/6

2. Coterminal Angles
Angles with the same terminal side 
but different rotations are called
coterminal angles.
General rule:
θ_coterminal = θ + 360° × k  (where k is any integer)
θ_coterminal = θ + 2π × k   (in radians)

Proof:
Rotating a full circle brings you back
to the same direction → 
the sine and cosine values repeat
every 360° or 2π.
cos(θ + 2π) = cosθ and 
sin(θ + 2π) = sinθ 
(periodicity of sine and cosine)

Thus, adding multiples of a full rotation
does not change the position of
the terminal side.
Example:
Coterminal angles of 45°:
..., -675°, -315°, 45°, 405°, 765°, ...

3. Periodicity Rules

3.1 Sine and Cosine
sin(θ + 2π) = sinθ
cos(θ + 2π) = cosθ

Proof:
Using unit circle definition:
Coordinates of a point on 
unit circle at θ are (cosθ, sinθ).
A full rotation (2π) returns the point
to the same location →
coordinates unchanged.

3.2 Tangent
tan(θ + π) = tanθ

Proof:
tanθ = sinθ / cosθ
tan(θ + π) = 
sin(θ + π) / cos(θ + π)
= (-sinθ) / (-cosθ)
= sinθ / cosθ = tanθ

So tangent repeats 
every π radians (180°).

3.3 Even-Odd Identities
cos(-θ) = cosθ (even function)
sin(-θ) = -sinθ (odd function)
tan(-θ) = -tanθ (odd function)

Proof:
Using symmetry of unit circle:
Cosine is x-coordinate 
(symmetric about y-axis)
Sine is y-coordinate 
(symmetric about x-axis)

4. Quadrant Rules for Signs
Quadrant I (0° to 90°): sin +, cos +, tan +
Quadrant II (90° to 180°): sin +, cos -, tan -
Quadrant III (180° to 270°): sin -, cos -, tan +
Quadrant IV (270° to 360°): sin -, cos +, tan -


Right Angle, Acute Angle, and Obtuse Angle:

Right Angle:
A right angle is an angle that measures
exactly 90°, which is equal to π/2 radians.
It represents a perfect quarter turn and
is formed when two lines are perpendicular
to each other. A small square symbol is 
often used to mark a right angle in diagrams.

Acute Angle:
An acute angle is any angle that
measures greater than 0° 
and less than 90° (0 < θ < 90°).
In radians, this means 0 < θ < π/2.
Acute angles are always sharp and appear narrow.
Example: 30°, 45°, 60° are acute angles.

Obtuse Angle:
An obtuse angle is any angle that
measures greater than 90° and 
less than 180° (90° < θ < 180°).
In radians, this means π/2 < θ < π.
Obtuse angles are wider than a 
right angle but less than a straight line.
Example: 120°, 135° are obtuse angles.


5. Reference Angle
Reference angle is the acute angle 
formed by the terminal side of θ
and the x-axis. It helps to compute 
trigonometric values using 
the nearest first-quadrant angle.

Example:
θ = 210° (Quadrant III)
Reference angle = 210° − 180° = 30°
So, sin(210°) = -sin(30°) = -1/2

--
Example:
Find the principal angle of -840°.
    Add multiples of 360°:
    -840 + 360 = -480
    -480 + 360 = -120
    -120 + 360 = 240°
    Answer: 240°

Example:
Convert 25π/4 to its principal angle.
    25π/4 − 2π = 25π/4 − 8π/4 = 17π/4
    17π/4 − 2π = 17π/4 − 8π/4 = 9π/4
    9π/4 − 2π = 9π/4 − 8π/4 = π/4
    Answer: π/4

6. Sine and Cosine Symmetry Rules
 (Based on Unit Circle Geometry)

We use the unit circle to analyze 
how coordinates change when 
angles move around the quadrants.
Recall: On the unit circle,
any angle θ has coordinates:
(cosθ, sinθ)

A. Rules Involving π/2 (90°)

Rule 1: sin(π/2 − θ) = cosθ

Proof:
Angle (π/2 − θ) corresponds to
rotating down from the y-axis.
On the unit circle:
Coordinates of (π/2 − θ) = (sinθ, cosθ)
Thus y-value = cosθ
So sin(π/2 − θ) = cosθ.

Example: 
sin(π/2 − 30°) = sin(60°) 
= √3/2 = cos30°

Rule 2: sin(π/2 + θ) = cosθ
Proof:
Angle (π/2 + θ) puts the angle in Quadrant II.
Coordinates: 
(cos(π/2 + θ), sin(π/2 + θ)) = (−sinθ, cosθ)
So sin(π/2 + θ) = cosθ.

But note sign check:
In Quadrant II, cosine is negative and sine positive.
Thus, we keep: sin(π/2 + θ) = cosθ 
(cosθ here will inherently have correct quadrant sign)

Example: sin(π/2 + 30°) = sin120° 
= √3/2 = cos30° = √3/2

Rule 3: cos(π/2 − θ) = sinθ
Proof:
From unit circle reflection:
Coordinates of (π/2 − θ) = (sinθ, cosθ)
Thus cos(π/2 − θ) = sinθ

Rule 4: cos(π/2 + θ) = −sinθ
Proof:
Coordinates of (π/2 + θ): (−sinθ, cosθ)
So x-value = −sinθ
Thus cos(π/2 + θ) = −sinθ.

---
B. Rules Involving π (180°)

Rule 5: sin(π − θ) = sinθ
Proof:
Angle is in Quadrant II: 
same vertical height as θ in Quadrant I
Coordinates of (π − θ) = (−cosθ, sinθ)
y-value = sinθ
So sin(π − θ) = sinθ

Rule 6: sin(π + θ) = −sinθ
Proof:
Angle is in Quadrant III: 
both x and y negative
Coordinates: (−cosθ, −sinθ)
So sin(π + θ) = −sinθ

Rule 7: cos(π − θ) = −cosθ
Proof:
Coordinates of (π − θ) = (−cosθ, sinθ)
So cos(π − θ) = −cosθ

Rule 8: cos(π + θ) = −cosθ
Proof:
Coordinates of (π + θ): (−cosθ, −sinθ)
x-value remains −cosθ
Thus cos(π + θ) = −cosθ

---
Summary of the Symmetry Rules

Sine:
sin(π/2 − θ) = cosθ
sin(π/2 + θ) = cosθ
sin(π − θ) = sinθ
sin(π + θ) = −sinθ

Cosine:
cos(π/2 − θ) = sinθ
cos(π/2 + θ) = −sinθ
cos(π − θ) = −cosθ
cos(π + θ) = −cosθ

---

Examples
1. Evaluate sin(π − 40°)
sin(π − θ) = sinθ → sin(180° − 40°) = sin40°

2. Evaluate cos(π/2 + 55°)
cos(π/2 + θ) = −sinθ → cos(145°) = −sin55°

3. Evaluate sin(π + 20°)
sin(π + θ) = −sinθ → sin200° = −sin20°

4. Evaluate cos(π − 30°)
cos(180° − 30°) = −cos30° = −√3/2


---
When θ > 90° in the expression sin(π/2 + θ):
• π/2 + θ becomes greater than 180°
• That means the resulting angle lies 
  in **Quadrant III or Quadrant IV**, 
  depending on the exact value of θ
• In Quadrant III and Quadrant IV, 
  **sine is negative**
• So sin(π/2 + θ) gives a **negative value**
  when θ > 90°

This still follows the identity:
sin(π/2 + θ) = cosθ
But since θ > 90° often puts cosθ
in a negative region, 
the result becomes negative.

Example 1:
Let θ = 100°
π/2 + 100° = 
90° + 100° = 190° (Quadrant III)
sin(190°) = cos(100°)
cos(100°) is negative
So sin(190°) is negative.

Numerical values:
cos(100°) ≈ -0.1736
sin(190°) ≈ -0.1736
→ They match.

Example 2:
θ = 120°
π/2 + 120° = 210° (Quadrant III again)
sin(210°) = cos(120°)
both are negative

So the key idea: When θ > 90°,
cosθ becomes negative → therefore 
sin(π/2 + θ) becomes negative too.

"""
