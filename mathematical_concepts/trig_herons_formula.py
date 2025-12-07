"""
Heron's formula

In triangle  △ ABC with sides a, b, and c
let's call s = (a + b + c) / 2

Step1, use cosine formula to calculate cos A:

a^2 = b^2 + c^2 - 2bc CosA 

CosA = (b^2 + c^2 - a^2) / 2 bc

step 2, get te value of sin A from 
pythogras identity sin^2 A + cos^2 = 1

-> sin^2 A = 1 - cos^2 A = (1 + cos A)(1 - cosA)

step3, replace cosA in step2 with the formula from step1:

sin^2 A = 
1 - cos^2 A = 
(1 + (b^2 + c^2 - a^2) / 2 bc)(1 - (b^2 + c^2 - a^2) / 2 bc)

= ( (2bc+ b^2 + c^2 - a^2) / 2 bc)( (2bc + b^2 - c^2 + a^2) / 2 bc)

=  ((2bc+ b^2 + c^2 - a^2) (2bc - b^2 - c^2 + a^2)) / 4 b^2c^2
=  (( (b + c)^2 - a^2) (a^2 - (b-c)^2 )) / 4 b^2c^2

=  ( ( (b + c) + a) ( (b + c) - a)   (a + (b-c) )(a - (b-c) ) 
    ) / 4 b^2c^2

=  ( (b + c + a)(b + c - a)(a + b - c )(a - b - c) ) / 4 b^2c^2

=  ( 2s (2(s-a))(2(s-c))(2(s-b)) ) / 4 b^2c^2

=  ( 4s (s-a)(s-c)(s-b) ) / b^2c^2

Since  △ ABC = 1/2 b c sin A

△ ABC = 1/2 bc sin A 
= 1/2 bc * sqrt(( 4s (s-a)(s-c)(s-b) ) / b^2c^2)
= 1/2 bc * sqrt( 4s (s-a)(s-c)(s-b) ) / bc
=  sqrt( s (s-a)(s-c)(s-b) ) 

-> △ ABC = sqrt( s(s-a)(s-c)(s-b) ) 

This is called as Heron's formula.
"""