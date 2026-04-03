"""
MULTINOMIAL AND BINOMIAL THEOREM

1. BINOMIAL THEOREM

Statement:

For any non-negative integer n and numbers a, b:

    (a + b)^n = Σ_{k=0}^{n} C(n,k) * a^k * b^(n-k)

Where:
- C(n,k) = n! / (k!(n-k)!)  (binomial coefficient)

Explanation:

- Each term arises from picking either a or b 
from each of the n factors.  
- To get a^k b^(n-k), choose a from k of the
n factors, b from the rest.  
- Number of ways = C(n,k).  

Example: (x + y)^4

- Terms:
    k=0: y^4
    k=1: 4xy^3
    k=2: 6x^2y^2
    k=3: 4x^3y
    k=4: x^4
- Expansion: x^4 + 4x^3y + 6x^2y^2 + 4xy^3 + y^4

Intuition for coefficient 4 of x^3y:

- Pick 3 x's and 1 y from 4 factors  
- Number of ways = C(4,3) = 4  
- Matches all sequences: 
(x,x,x,y), (x,x,y,x), (x,y,x,x), (y,x,x,x)

- Choosing positions for x automatically determines
positions for y.
For ex, in (x + y)^5,​ C(5,3) and C(5,2) actually count the same thing.


---
2. MULTINOMIAL THEOREM

Statement:

For m variables x1, x2, ..., xm and integer n ≥ 0:

(x1 + x2 + ... + xm)^n =
 Σ_{k1+k2+...+km=n} [ n! / (k1! k2! ... km!) * x1^k1 x2^k2 ... xm^km ]

Where:
- The sum is over all non-negative integers k1,...,km with sum n  
- n! / (k1! k2! ... km!) = multinomial coefficient  
- Each tuple (k1,...,km) corresponds to a distinct term

Explanation:

- Expansion: pick one variable from each factor  
- Term x1^k1 x2^k2 ... xm^km occurs when:
    - x1 chosen k1 times  
    - x2 chosen k2 times  
    - ...
    - xm chosen km times  
- Total ways (coefficient) = n! / (k1! k2! ... km!)  
- Denominator removes overcounting of repeated variables

Example: (x + y + z)^2
- Tuples: 
(2,0,0), (1,1,0), (1,0,1), (0,2,0), (0,1,1), (0,0,2)  
- Terms: x^2, 2xy, 2xz, y^2, 2yz, z^2  
- Expansion: x^2 + y^2 + z^2 + 2xy + 2xz + 2yz

---
3. MULTINOMIAL COEFFICIENT FORMULA

General formula:

 Coefficient of x1^k1 x2^k2 ... xm^km = n! / (k1! k2! ... km!)

Method 1:
Derivation of the formula by Sequential Choosing:

We want to count the number of ways to form the term
x1^k1 x2^k2 ... xm^km

Step 1: Choose positions for x1
Number of ways = C(n, k1)

Step 2: Choose positions for x2
Number of ways = C(n − k1, k2)

Step 3: Choose positions for a3
Number of ways = C(n − k1 − k2, k3)

Continue this process 
until all variables are assigned.

Final count (multiply all steps):
C(n, k1) × C(n − k1, k2) × 
C(n − k1 − k2, k3) × ... × C(k_m, k_m)

Simplified result:
n! / (n1! n2! ... nk!)


Method 2: Instead of sequential choosing, 
think of the arrangements of the terms:

For example for (a+b+c)^5
for taking 2 a , 2 b and 1 c:

a a b b c → total permutations = 5!

But:

swapping a’s doesn’t change anything → divide by 2!
swapping b’s → divide by 2!
c is single → divide by 1!

So 5!/2!

​This automatically includes all possible “orders” of picking

The resulted enumeration: 
Take positions 1 2 3 4 5. 
Two a’s, two b’s, one c. 
Let’s enumerate all distinct sequences 
(not labeling a’s and b’s individually):

a a b b c
a a b c b
a a c b b
a b a b c
a b a c b
a b b a c
a b b c a
a b c a b
a b c b a
a c a b b
a c b a b
a c b b a
b a a b c
b a a c b
b a b a c
b a b c a
b a c a b
b a c b a
b b a a c
b b a c a
b b c a a
b c a a b
b c a b a
b c b a a
c a a b b
c a b a b
c a b b a
c b a a b
c b a b a
c b b a a

There are exactly 30 distinct sequences, 
matching the multinomial formula.
Notice how swapping the a’s in any of these sequences 
does not create a new one, and similarly for b’s.


Intuition:

- Total factors = n  
- Choose k1 slots for x1, k2 slots for x2, ...  
- Multiply possibilities for each choice (rule of product)  
- Denominator corrects for identical objects

Comparison with binomial coefficient:

- Binomial: (x+y)^n, coefficient of x^k y^(n-k) = n! / (k!(n-k)!)  
- Multinomial = generalization with more variables

Example: (x + y + z + w)^4, term x^2 y z

- k1=2, k2=1, k3=1, k4=0  
- Coefficient = 4! / (2!1!1!0!) = 24 / 2 = 12  
- There are 12 sequences (x,x,y,z), (x,x,z,y), ..., (z,y,x,x)  

---
4. COUNTING NUMBER OF REPETITIONS

- Coefficient counts how many times a term appears in the expansion  
- Binomial case: (x+y)^n, term x^k y^(n-k) → choose k positions for x → C(n,k)  
- Multinomial: choose k1 positions for x1, k2 for x2, ..., 
last variable determined by remaining slots → multiply choices

Rule of Product:

- If there are multiple sequential independent choices,
multiply the number of ways for each choice:

- Example: x^2 y z in (x+y+z)^4:
    - Choose 2 slots for x → 6 ways  
    - Choose 1 slot for y → 2 ways  
    - Remaining 1 slot → 1 way  
    - Total = 6 * 2 * 1 = 12

---
5. SYSTEMATIC GENERATION OF TERMS

To generate all exponent tuples (k1,...,km) with sum n:

1. Loop for first variable: k1 = 0 to n  
2. Loop for second variable: k2 = 0 to n - k1  
3. Loop for third variable: k3 = 0 to n - k1 - k2  
4. ... Continue until k_{m-1}  
5. Last variable: k_m = n - (k1 + ... + k_{m-1})  
6. Each tuple → term x1^k1 x2^k2 ... xm^km, 
coefficient = n! / (k1! k2! ... km!)

Example: (x + y + z)^3, n=3, m=3

- k1=0 → k2=0→k3=3 → (0,0,3)  
- k1=0 → k2=1→k3=2 → (0,1,2)  
- k1=0 → k2=2→k3=1 → (0,2,1)  
- k1=0 → k2=3→k3=0 → (0,3,0)  
- k1=1 → k2=0→k3=2 → (1,0,2)  
- k1=1 → k2=1→k3=1 → (1,1,1)  
- k1=1 → k2=2→k3=0 → (1,2,0)  
- k1=2 → k2=0→k3=1 → (2,0,1)  
- k1=2 → k2=1→k3=0 → (2,1,0)  
- k1=3 → k2=0→k3=0 → (3,0,0)

- Each tuple → term with coefficient n! / (k1! k2! k3!)  

---
6. KEY INSIGHTS

- Multinomial coefficient = number of sequences producing a term  
- Rule of product = multiply sequential independent choices  
- Systematic generation = enumerate all non-negative integer
 solutions to k1+...+km=n  
- Binomial theorem is a special case of multinomial theorem (m=2)  
- Visualizing “slots” for each variable helps understand 
coefficients and terms  

"""