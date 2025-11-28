"""
Compound Angles in Trigonometry

1. Introduction
   A compound angle is an angle formed by
   combining two angles, usually represented as:
   (A + B) or (A − B)

Trigonometric functions such as 
sine, cosine, and tangent have 
**compound angle formulas** that 
allow us to calculate values for 
combined angles using known values
of individual angles.

These identities are very important in
geometry, physics, and 
simplifying trigonometric expressions.

---

2. Important Rules (Formulas) for Compound Angles

Sine:
sin(A + B) = sinA cosB + cosA sinB
sin(A − B) = sinA cosB − cosA sinB

Cosine:
cos(A + B) = cosA cosB − sinA sinB
cos(A − B) = cosA cosB + sinA sinB

Tangent:
tan(A + B) = (tanA + tanB) / (1 − tanA tanB)
tan(A − B) = (tanA − tanB) / (1 + tanA tanB)

---

3. Proof of Cosine Compound Rule
   We prove:
   cos(A + B) = cosA cosB − sinA sinB

Proof using unit circle and geometry:
Consider two points on the unit circle:
P at angle A → (cosA, sinA)
Q at angle B → (cosB, sinB)

Now rotate point Q by angle A to 
get the point representing angle (A + B):

Rotation formula:
x' = x cosA − y sinA
y' = x sinA + y cosA

Substitute Q = (cosB, sinB):
New x-coordinate = cosB cosA − sinB sinA

But this x-coordinate equals cos(A + B)

Thus:
cos(A + B) = cosA cosB − sinA sinB
Q.E.D.

---

4. Proof of Sine Compound Rule
   Using the same rotation:

New y-coordinate = cosB sinA + sinB cosA
This y-value equals sin(A + B)

Thus:
sin(A + B) = sinA cosB + cosA sinB
Q.E.D.

---

5. Example Calculations

Example 1:
Find sin(75°)

Break 75° into known angles:
75° = 45° + 30°

Apply formula:
sin(75°) = sin(45° + 30°)
= sin45° cos30° + cos45° sin30°
= (√2/2)(√3/2) + (√2/2)(1/2)
= (√6/4) + (√2/4)
= (√6 + √2) / 4

Example 2:
Find cos(15°)

15° = 45° − 30°

cos(15°) = cos(45° − 30°)
= cos45° cos30° + sin45° sin30°
= (√2/2)(√3/2) + (√2/2)(1/2)
= (√6/4) + (√2/4)
= (√6 + √2) / 4

Example 3:
Find tan(75°)

tan(75°) = tan(45° + 30°)
= (tan45° + tan30°) / (1 − tan45°tan30°)
= (1 + 1/√3) / (1 − (1)(1/√3))
= ( (√3 + 1)/√3 ) / ( (√3 − 1)/√3 )
Cancel √3 in denominator:
= (√3 + 1) / (√3 − 1)

(Optionally rationalize denominator)

---

6. Summary
   Compound angle rules help calculate trigonometric
   values of angles not on standard charts.
   They are essential for:
   • Simplifying trigonometric expressions
   • Analytical geometry and vectors
   • Complex numbers and wave addition problems

"""

"""
A different proof for restricted angles,
where angles A and B are both between
0 and 90.

Proof for sin(A+B) and sin(A-B)

Let's assume △ QPR,
where angle Q = A + B
QN is drawn prependicular to the opposite side,
dividing the opposite side to y and x. 
So we have the angles P, R, Q(A+B),
and the correponding sides p,r, and (x+y)

The strategy is that to say that that
area of △ QPR = △ QPN + △ QNR

based on the formula for the area of 
traingle: 1/2 a b since C

-> 1/2 r p sin(A+B) = 1/2 r h sinA + 1/2 p h sinB

Dividing both sides by 1/2 r p gives:

-> sin(A+B) = h/p sinA + h/r sinB

h/p = cosB and h/r = cosA

Therefore:
-> sin(A+B) = cosA sinA + cosA sinB

(this is proved for acute angles A and B, but
the result is true for all angles A and B)

For sin(A-B), a similar method can be used
based on the difference of two areas of triangles
to derive the formula for sin(A-B)

You will get sin(A-B) = sinA cosB - cosA sinB.

---
Proof for cos(A+B) and cos(A-B)
(Where angles A and B are both between
0 and 90.)

Let's assume △ QPR,
where angle Q = A + B
QN is drawn prependicular to the opposite side,
dividing the opposite side to y and x. 
So we have the angles P, R, Q(A+B),
and the correponding sides p,r, and (x+y)


The strategy is to sue the cosine formula to
derive an expression for cos(A+B)
(In a triangle abc: a^2 = b^2 + c^2 - 2 b c cos A)

In triangle PQR: 

(x+y)^2 =  r^2 + p^2 - 2rp cos(A+B)
2rp cos(A+B) = r^2 + p^2 - (x+y)^2 
2rp cos(A+B) = r^2 + p^2 - x^2 - y^2 - 2 x y
2rp cos(A+B) = (r^2 - x^2) + (p^2 - y^2) - 2 x y
2rp cos(A+B) = h^2 + h^2 - 2 x y
2rp cos(A+B) = 2 h^2 - 2 x y

Dividing both side by 2rp gives: 

cos(A+B) =  (h^2 - x y) / 2rp
cos(A+B) =  h^2/rp  -  x y/rp = 

Since 
h/r = cos A
h/p = cos B
x/r = sin A
y/p = sin B

Then the expression becomes:
-> cos(A+B) =  cos A cos B - sin A sin B

A similar method can be used to derive 
the expression for cos (A-B).
The formula will be:
cos(A-B) = cos A cos B + sin A sin B

---
Formula for tan(A+B) and tan(A-B)

we can you the above equations to 
derive the formulas
for tan(A+B) and tan(A-B)

tan (A+B) = sin(A+B)/ cos(A+B)
= (sinA cosB + cosA sinB) / (cosA cosB - sinA sinB)

Dividing the numerator and denominnator of this fraction
by cosA cosB gives:


tan(A+B) = 
 (sinA cosB / cosA cosB + cosA sinB /  cosA cosB) /
 (cosA cosB/  cosA cosB - sinA sinB/  cosA cosB)

=  tanA + tanB / 1 - tanA tanB

Therefore:
tan(A+B) = (tanA + tanB) / (1 - tanA tanB)

The formula for tan(A-B) can be derived similarly.
The formula is 
tan(A-B) = (tanA - tanB) / 1 + tanA tanB

"""

"""
Multiple Angle Forumla:

From the formula 
sin(A+B) = sinA cosB + cosA sinB,
if put B=A,
then sin(A+A) = sinA cosA + cosA sinA

-> sin(2A) = 2 sinA cosA

if θ = 2A
Then 
-> sin(θ) = 2 sin=(1/2 θ) cos(1/2 θ)

--
if we put B=A in 
cos(A+B) = cosA cosB - sinA sinB
we get:
cos(A+A) = cosA cosA - sinA sinA

-> cos(2A) = cos^2 A - sin^2 A

Using pythagoras's theorem,
sin^2 A + cos^2 A = 1

Sin2^ A = 1 - cos^2 A

Replacing the term in 
cos(2A) = cos^2 A - sin^2 A

results in 
cos(2A) = cos^2 A - 1 + cos^2 A

therefore
-> cos(2A) = 2 cos^2 A - 1

If replace cos^2 A with
1 - sin^2 A in the equation,
it will result to:

cos(2A) = cos^2 A - sin^2 A
cos(2A) = 1 - sin^2 A - sin^2 A
-> cos(2A) = 1 - 2 sin^2 A

We can write the result in other forms:

cos(2A) = 2 cos^2 A - 1
->1 + cos(2A) = 2 cos^2 A

cos(2A) = 1 - 2 sin^2 A
-> 1- cos(2A) =  2 sin^2 A

If put 2A = θ: 

-> cos(2A) = cos^2 A - sin^2 A
-> cos(θ) = cos^2 (1/2 θ) - sin^2 (1/2 θ)

-> cos(2A) = 2 cos^2 A - 1
-> cos(θ) = 2 cos^2 θ - 1

-> cos(2A) = 1 - 2 sin^2 A
-> cos(θ) = 1 - 2 sin^2 (1/2 θ)

----
In tan(A+B) formula, if we put B=A,
it will result to:

tan(A+B) =  (tan A + tan B)/ (1 - tanA tanB)
tan(2A) = (tanA + tanA) / (1- tanA tanA)
-> tan(2A) = 2 tanA / ( 1- tan^2 A )

and when θ = 2A
-> tan(θ) = 2 tan (1/2 θ) / ( 1- tan^2 (1/2 θ) )

"""