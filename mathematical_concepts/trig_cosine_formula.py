"""
The cosine formula for a triangle

We consider the two case of
acute-angled triangle and
obtuse_angled tirangle.

Case 1, acute-angled triangle

let's △ ABC, 
angles A,B,C
and opposite side of angles a,b,c

From vertx A draw a vertical line
that intercepts the base a 
call the interception point as D 
and AD as h
and CD as x.

Using Pythagoras's theorem in △ ACD:

b^2 = h^2 + x^2
eq1) h^2 = b^2 -x^2

Using Pythagoras's theorem in △ ADB:

c^2 = h^2 + (a -x)^2 = h^2 + a^2+ x^2 - 2 a*x

eq2) h^2 = c^2 - a^2 - x^2 + 2 a*x

equating h^2 for the two equations gives:

-> b^2 -x^2 = c^2 - a^2 - x^2 + 2 a*x

-> c^2 = a^2 + b^2 - 2 a*x

cos C = x/b
x = b * cos C

-> c^2 = a^2 + b^2 - 2 a b cos C
 

Case 2, obtuse-angled triangle

let's △ ABC, 
angles A,B,C (where C>90 degrees)
and opposite side of angles a,b,c

From vertx A draw a vertical line
that intercepts the continuation of
base a. 
Call the interception point as D 
and AD as h
and CD as x.

From Pythagoras's theorem in △ ADC:

h^2 + x^2 = b^2
eq1) h^2 = b^2 - x^2

From Pythagoras's theorem in △ ADB:

h^2 + (x+a)^2 = c^2
h^2 + x^2 +a^2 + 2 ax = c^2
eq2) h^2 = c^2 - x^2 - a^2 - 2 a x

Equating the two expressions gives:

-> b^2 - x^2 = c^2 - x^2 - a^2 - 2 a x
-> c^2 = a^2 + b^2 + 2 a x

cos (180 - C) = x / b
x = b cos (180 - c) 

And we know that 
cos (180 - c) = - cos C

-> c^2 = a^2 + b^2 - 2 a b cos C
This is called the cosine formula.

This can be written similarly for the 
other two vertices.

a^2 = b^2 + c^2 - 2 b c cos A
b^2 = a^2 + c^2 - 2 a c cos B
c^2 = a^2 + b^2 - 2 a b cos C


"""