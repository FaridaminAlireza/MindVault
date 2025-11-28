"""
Key terms:
Chord:	A straight line joining any two points on the circle.
Arc:	The curved part of the circle between two points.
Inscribed Angle:	An angle with its vertex on the circle,
 and its sides (rays) passing through points on the circle.
Central Angle:	An angle with its vertex at the center of the circle
Subtend: A chord or arc subtends an angle if the endpoints of 
the chord/arc lie on the sides (rays) of the angle.


THEOREM

The central angle subtending a given chord equals
twice any inscribed angle that subtends the same chord.

In the usual notation 
(circle center O,
 chord BC, 
 point A on the circle),
the appropriate central angle BOC = 2 * angle BAC.

Proof:

Case1, 
The diameter is one of the chords of the inscribed angle.

Let the point A, make the incsibe angle
with chords AC (passing from center O),
and another chord (AB).

Let's call
∠BAC = θ_1 
∠ABO = θ_2 
∠BOC =  β
∠AOB =  α 


AO = OB = r (radius) -> θ_1 = θ_2

1) α + β = 180 (The degree of flat line)

2) θ_1 + θ_2 + α = 180 (The sum of triangle angels)
2) 2θ_1 + α = 180 

3, deducting eq 2 from eq1 gives:
  2θ_1 - β = 0
   2θ_1 = β 
   (2 * angle BAC = BOC)


Case 2,
The central angel is in the interior 
of the inscribed angle

Let's draw the radius OA,

In △ ABO, AO = BO = r
-> ∠OAB = OBA = θ
∠AOB = 180 - 2 θ


In △ AOC, AO = CO = r
-> ∠OAC = OCA = γ  
∠AOC = 180 - 2 γ 

Let's call ∠BOC = β

∠AOB  + ∠AOC + ∠BOC = 360
∠BOC = 360 - ∠AOB  - ∠AOC 
β = 360 - (180 - 2 θ) - (180 - 2 γ )
β = 360 - 180 + 2 θ - 180 + 2 γ 
β =  2 θ + 2 γ 
β =  2 (θ + γ) 
(2 * angle BAC = BOC)

Case 3, 
the central angel is in the exterior
of the inscribed angle.

Let's create a diameter by
extending OA, calling the 
intercepting point D.

Let's call 
∠OAC = α_1
∠BAC = α_2

Based on Case 1 and 2 proofs:

eq1) ∠CAD = 2 ∠COD  
eq2) ∠BAD = 2 ∠BOD 

Deducting eq1 from eq2 gives:

∠BAD - ∠CAD  = 2 ∠BOD  - 2 ∠COD  
<BAC = 2 (∠BOD  - ∠COD) = 2 (∠BOC)
(2 * angle BAC = BOC)
"""