
"""
CIRCLE GEOMETRY

DEFINITIONS
Circle: All points in a plane that are 
the same distance from a fixed point (center).

Center: The single point inside the circle that is 
the same distance from every point on the circle.

Segment:(has two meanings)
1) Line Segment (in general geometry)
A straight part of a line connecting two points
Example: a radius is a line segment
from the center to the circle
2) Circular Segment (Circle Geometry)
A region/area inside a circle bounded 
by a chord and the arc above it

Arc: A continuous part of the circle’s circumference.
Chord: A line segment with both endpoints on the circle.

Sector: A region bounded by two radii (plural radius)
and the connecting arc.

Segment: A region bounded by a chord and its arc.

Radius (r): A line segment from the center to the circle.

Diameter (d): A chord passing through the center (d = 2r).

Circumference: The total distance around the circle.

Tangent: A line touching the circle at exactly one point.

Secant: A line intersecting the circle at exactly two points.

Minor Arc: The shorter arc between two points.

Major Arc: The longer arc between the same two points.

Central Angle: An angle with its vertex at the center,
intercepting an arc.

Inscribed Angle: An angle with its vertex on the circle,
intercepting an arc.

Intercepted Arc: The arc lying between the sides of an angle.

Concentric Circles: Circles with the same center, different radii.

Cyclic Quadrilateral: A quadrilateral with all vertices on a circle.
Opposite angles sum to 180°.
(a four-sided figure whose vertices all lie on a single circle.
The key property is that opposite angles are supplementary,
meaning they add up to 180. All rectangles are cyclic quadrilaterals,
but not all parallelograms are; a trapezoid is only cyclic 
if it is an isosceles trapezoid.)


FORMULAS

Arc Length (when angle is θ in degrees): Arc Length = (θ/360) × 2πr
Arc Length (when angle is θ in radians): Arc Length = θr
Area of Sector (degrees): Sector Area = (θ/360) × πr²
Area of Sector (radians): Sector Area = (1/2)r²θ
Area of Segment: 
Segment Area =  Sector Area − Triangle Area 
(specific triangle formula depends on chord)

Power of a Point (Chord form):
Often known as the Intersecting Chords Theorem,
states that if two chords AB and CD intersect at a point P
inside a circle, the product of the lengths of the segments
of one chord equals the product of the lengths of 
the segments of the other. 
PA × PB = PC × PD

Power of a Point (Tangent–Secant): 
If a tangent (touching the circle at point T) and
a secant (with touching points B and A) 
are drawn from a point P outside a circle,
the square of the tangent’s length equals 
the product of the lengths of the secant’s segments.
(Tangent length)² = (External secant part × Entire secant)
PT^2 = PA × PB

ANGLE RELATIONSHIPS
Inscribed Angle Theorem: 
Inscribed angle = 1/2 × intercepted arc.
The measure of an angle inscribed in a circle is exactly
half the measure of its intercepted arc. 
This means if an angle's vertex lies on the circle 
and its sides are chords, the angle is 1/2
the degree measure of the arc in its interior


Central vs Inscribed: 
Central angle = 
2 × inscribed angle intercepting the same arc.

Angles in the Same Segment: 
Angles standing on the same arc are equal.

Angle in a Semicircle: Always 90°.

Exterior Angle (formed by secants): 
Exterior angle = 1/2 × (difference of intercepted arcs).

CYCLIC QUADRILATERALS
Opposite angles sum to 180°.
Exterior angle equals interior opposite angle.

TANGENTS
Tangent forms a 90° angle with the radius at point of contact.
Two tangents from the same external point are equal in length. This is a
fundamental circle theorem. If a point P outside a circle connects 
to tangent points A and B on the circumference, the lengths PA and PB 
are identical


# PROOF OF AREA OF A CIRCLE USING INTEGRATION

We want to find the area of a circle of radius r.

Step 1: Consider the circle in polar coordinates
* In polar coordinates, 
a point on the circle is given by (r, θ).
* Radius of circle = r (fixed).
* θ varies from 0 to 2π.

Step 2: Concept of “infinitely small triangles

* Imagine slicing the circle into
infinitely small sectors (like thin pizza slices).
* Each small sector has:
  * Radius = r
  * Angle = dθ (in radians)
  * Arc length of small sector = r × dθ
* If we approximate each small sector as a triangle:
  * Height = r (radius)
  * Base = r × dθ (arc length)
  
Step 3: Area of a small triangle (sector approximation)
* dA =1/2 × base × height = 1/2 (r × dθ) × r =
1/2 r² dθ

Step 4: Sum up all triangle (integration)

* θ goes from 0 to 2π
* Total area A = ∫(θ=0 to 2π) 1/2 r² dθ

Step 5: Perform the integration

* 1/2 r² is constant, so:
  A = 1/2 r² ∫(θ=0 to 2π) dθ
  A = 1/2 r² [θ](θ=0 to 2π)
  A = 1/2 r² × (2π − 0)
  A = π r²
"""