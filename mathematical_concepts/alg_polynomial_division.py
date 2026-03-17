"""
POLYNOMIAL DIVISION (LONG DIVISION AND SYNTHETIC DIVISION)


This document summarizes polynomial division, including:
- Polynomial long division
- Synthetic division
- Step-by-step procedures
- Examples
- When each method works or does not work
- Common mistakes
- Related theorems

---
1. OVERVIEW

Polynomial division is similar to integer division.

Dividend ÷ Divisor = Quotient + Remainder

For polynomials:
P(x) / D(x) = Q(x) + R(x)/D(x)

Where:
- Degree of R(x) < Degree of D(x)


2. POLYNOMIAL LONG DIVISION


Used when the divisor is ANY polynomial (linear, quadratic, etc.).

Core idea:
1. Divide leading terms
2. Multiply
3. Subtract
4. Repeat until remainder degree is smaller than divisor degree

---
2.1 Long Division Example (Linear Divisor)


Divide:
(2x^3 + 3x^2 - x + 5) ÷ (x + 1)

Step 1:
2x^3 / x = 2x^2

Step 2:
2x^2(x + 1) = 2x^3 + 2x^2

Step 3:
Subtract:
(2x^3 + 3x^2 - x + 5)
- (2x^3 + 2x^2)
= x^2 - x + 5

Step 4:
x^2 / x = x

Multiply:
x(x + 1) = x^2 + x

Subtract:
(x^2 - x + 5) - (x^2 + x) = -2x + 5

Step 5:
-2x / x = -2

Multiply:
-2(x + 1) = -2x - 2

Subtract:
(-2x + 5) - (-2x - 2) = 7

Final result:
Quotient = 2x^2 + x - 2
Remainder = 7

---
2.2 Long Division Example (Quadratic Divisor)


Divide:
(x^3 - 1) ÷ (x^2 + x + 1)

Step 1:
x^3 / x^2 = x

Multiply:
x(x^2 + x + 1) = x^3 + x^2 + x

Subtract:
(x^3 + 0x^2 + 0x - 1)
- (x^3 + x^2 + x)
= -x^2 - x - 1

Step 2:
-x^2 / x^2 = -1

Multiply:
-(x^2 + x + 1) = -x^2 - x - 1

Subtract:
0

Final result:
Quotient = x - 1
Remainder = 0

---
3. SYNTHETIC DIVISION


Synthetic division is a shortcut for long division.

It works ONLY when the divisor is of the form:
x - a


3.1 Synthetic Division Algorithm


1. Write coefficients of the polynomial (include zeros)
2. Use 'a' from x - a
3. Bring down the first coefficient
4. Multiply by 'a'
5. Add to next coefficient
6. Repeat
7. Last number is the remainder


3.2 Synthetic Division Example


Divide:
(2x^3 - 3x^2 + 5) ÷ (x - 1)

Coefficients:
2  -3  0  5

a = 1

Synthetic table result:
2  -1  -1  4

Quotient:
2x^2 - x - 1

Remainder:
4


3.3 Synthetic Division with Zero Remainder


Divide:
(x^3 - 6x^2 + 11x - 6) ÷ (x - 2)

Coefficients:
1  -6  11  -6

a = 2

Result:
1  -4  3  0

Quotient:
x^2 - 4x + 3

Remainder:
0

---
4. WHEN SYNTHETIC DIVISION DOES NOT WORK


Synthetic division does NOT work when:
- Divisor degree > 1
- Divisor is not linear
- Divisor is not of the form x - a

Example where it fails:
(x^3 + 2x^2 + 3x + 4) ÷ (x^2 + 1)

Correct method: Polynomial long division.

---
5. SPECIAL CASE: NON-MONIC LINEAR DIVISORS


Divisor:
2x - 3

Cannot apply synthetic division directly.

Rewrite:
2x - 3 = 2(x - 3/2)

Then synthetic division can be applied using a = 3/2.

---
6. IMPORTANT THEOREMS


Remainder Theorem:
If P(x) is divided by x - a, the remainder is P(a).

Factor Theorem:
If P(a) = 0, then (x - a) is a factor of P(x).

---
7. COMMON MISTAKES


- Forgetting missing powers (always include zero coefficients)
- Using the wrong sign for 'a'
- Applying synthetic division to non-linear divisors
- Stopping long division too early

---
8. SUMMARY


Polynomial Long Division:
- Works for all polynomials
- More steps, but always valid

Synthetic Division:
- Faster
- Only works for x - a
- Useful for remainders and factor testing

"""