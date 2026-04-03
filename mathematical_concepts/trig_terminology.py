"""
TRIGONOMETRIC TERMINOLOGY: 
This document provides a thorough geometric and historical explanation
of the six classical trigonometric functions:

sine, cosine, tangent, cotangent, secant, cosecant

The exposition is primarily inspired by Classical Euclidean geometry,
Unit circle, and right-triangle definitions


1. THE GEOMETRIC SETUP
We begin with a unit circle centered at the origin (0, 0).

Let: - A ray from the origin form an angle θ with the positive x-axis. -
The ray intersects the unit circle at point P = (cos θ, sin θ).

This single construction contains all six trigonometric functions.
Alternatively, consider a right triangle with: 
- Hypotenuse = 1
- Angle θ at the origin

The unit circle and right triangle viewpoints are equivalent.


2. SINE

Historical origin: - The word “sine” comes from the Latin “sinus”,
meaning bay or fold. - This arose from a mistranslation of the Arabic
“jiba”, itself a transliteration of the Sanskrit “jya”,
meaning chord or half-chord.

Geometric meaning: - Sine measures a vertical length.

Definition (unit circle): sin θ = y-coordinate of point P

Definition (right triangle): sin θ = opposite / hypotenuse

Geometric interpretation: - Draw a perpendicular from point P to the
x-axis. - The length of this perpendicular is sin θ.

Example: If θ = 30°, sin 30° = 1/2

Proof (unit circle): 
- The unit circle has radius 1.
- The y-coordinate of point P is the vertical projection. 
- Thus sin²θ + cos²θ = 1 (Pythagorean theorem).


3. COSINE (COMPLEMENTARY SINE)

Name logic: - “co-” means complement. 
- Cosine originally meant “sine of the complementary angle”.

That is: cos θ = sin(90° − θ)    

Geometric meaning: - Cosine measures a horizontal length.

Definition (unit circle): cos θ = x-coordinate of point P

Definition (right triangle): cos θ = adjacent / hypotenuse

Geometric interpretation: - Drop a perpendicular from P to the y-axis. 
The horizontal distance is cos θ.

Example: If θ = 60°, cos 60° = 1/2

Proof: 
- In a right triangle, the adjacent side of θ is the opposite
side of its complement. 
- Thus cosine is a co-function of sine.


4. TANGENT (THE TOUCHING LINE)

Etymology: - From Latin “tangere” = to touch.

Geometric origin: 
- The tangent line touches the unit circle at exactly
one point. 
- It's length is the distance between
the touching point (The point that ray with angle θ
reaches the border of circle) and the intersection of
tangent with the line passing the center and point (1,0))

Definition: tan θ = sin θ / cos θ

Right triangle definition: tan θ = opposite / adjacent

Example: If θ = 45°, tan 45° = 1

Proof: 
- Similar triangles formed between the unit circle and tangent
line yield tan θ = y / x = sin θ / cos θ.


5. SECANT (THE CUTTING LINE)

Etymology: - From Latin “secare” = to cut.

Geometric origin: - A secant line cuts the circle at two points.

Definition: sec θ = 1 / cos θ

Geometric construction:
- Extend the ray from the origin until it
intersects the vertical tangent line 
- The distance from the origin to this point is sec θ.

Example: If θ = 60°, cos 60° = 1/2 sec 60° = 2

Proof: - By similar triangles, 
the hypotenuse-like segment equals 1 /cos θ.



6. COSECANT (COMPLEMENTARY SECANT)

Name logic: - Cosecant means “secant of the complementary angle”.

That is: cosec θ = sec(90° − θ)
Proof: 
    Start with definitions:
    cosec(theta) = 1 / sin(theta)
    sec(x) = 1 / cos(x)

    Now evaluate sec(90° − theta):
    sec(90° − theta) = 1 / cos(90° − theta)

    Use complementary identity:
    cos(90° − theta) = sin(theta)

    Substitute:
    sec(90° − theta) = 1 / sin(theta)
    But: 1 / sin(theta) = cosec(theta)
    Therefore: cosec(theta) = sec(90° − theta)


Algebraic definition: cosec θ = 1 / sin θ

Geometric meaning: - The cosecant corresponds to a vertical secant
segment.

Example: If θ = 30°, sin 30° = 1/2 cosec 30° = 2


7. COTANGENT (COMPLEMENTARY TANGENT)

Name logic: - Cotangent means “tangent of the complementary angle”.

That is: cot θ = tan(90° − θ)
Proof:
    Start with the definitions:

    cot(theta) = cos(theta) / sin(theta)
    tan(x) = sin(x) / cos(x)

    Now evaluate tan(90° − theta):
    tan(90° − theta) = sin(90° − theta) / cos(90° − theta)

    Use complementary angle identities:
    sin(90° − theta) = cos(theta)
    cos(90° − theta) = sin(theta)

    Substitute:
    tan(90° − theta) = cos(theta) / sin(theta)
    But: cos(theta) / sin(theta) = cot(theta)
    Therefore: cot(theta) = tan(90° − theta)


Algebraic definition: cot θ = cos θ / sin θ

Geometric meaning: - Ratio of horizontal to vertical lengths.

Right triangle definition: cot θ = adjacent / opposite

Example: If θ = 45°, cot 45° = 1

Proof: 
- From tan θ = opposite / adjacent,
cot θ is its complementary ratio.


8. FUNDAMENTAL IDENTITIES

Pythagorean identity: 
sin²θ + cos²θ = 1

Derived identities: 
1 + tan²θ = sec²θ 
1 + cot²θ = cosec²θ

Proof: 
- These follow directly from the Pythagorean theorem
applied to the geometric constructions.

9. Derivatives:
(Calculus Applications)

d/dx(sin x) = cos x
d/dx(cos x) = -sin x
d/dx(tan x) = sec^2 x
d/dx(cot x) = -csc^2 x
d/dx(sec x) = sec x tan x
d/dx(csc x) = -csc x cot x


10. Summary:

- sine historical half-chord 
- cosine sine of complement 
- tangent touching line 
- secant cutting line 
- cosecant secant of complement 
- cotangent tangent of complement

Key insight: 
- The “co-” functions are named for complements, not reciprocals. 
- Reciprocal interpretations came later.

sin = opp/hyp, cos = adj/hyp, tan = opp/adj
csc = hyp/opp, sec = hyp/adj, cot = adj/opp

tan θ = sin θ / cos θ
cot θ = cos θ / sin θ

Reciprocal Relationships:
csc θ = 1 / sin θ
sec θ = 1 / cos θ
cot θ = 1 / tan θ

Pythagorean Identities:
sin^2 θ + cos^2 θ = 1
1 + tan^2 θ = sec^2 θ
1 + cot^2 θ = csc^2 θ

"""