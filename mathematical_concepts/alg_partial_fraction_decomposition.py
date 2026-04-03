"""
1)  Rational Expression

A rational expression is a fraction 
where both numerator and denominator
are polynomials:

    P(x) / Q(x),   where Q(x) ≠ 0

Example: (2x + 3) / (x^2 - 1)

2)  When Can You Decompose into Partial Fractions?
(Partial Fractions: 
splitting a complex fraction into simpler fractions
to make algebra or calculus easier.)

Step 1: The fraction must be proper. 
The degree of the numerator must be
strictly less than the degree of the denominator.

If it is not proper, 
perform polynomial long division first.

Step 2: Factor the denominator completely.

Factor over real numbers 
(or complex numbers if required).

Example: x^2 - 1 = (x - 1)(x + 1)

3)  General Forms of Partial Fraction Decomposition

Case 1: Distinct Linear Factors

If: P(x) / [(x - a)(x - b)]

Then: A/(x - a) + B/(x - b)

Each linear factor gets a constant numerator.

Case 2: Repeated Linear Factors

If: P(x) / (x - a)^n

Then: A1/(x - a) + A2/(x - a)^2 + … + An/(x - a)^n

You must include one term for each power.

Case 3: Irreducible Quadratic Factor

If the denominator contains a quadratic that cannot be factored over the
real numbers (e.g., x^2 + 1),

Then: (Ax + B)/(x^2 + 1)

The numerator must be linear.

Case 4: Repeated Irreducible Quadratic

If: P(x) / (x^2 + 1)^n

Then: 
(A1 x + B1)/(x^2 + 1) + 
(A2 x + B2)/(x^2 + 1)^2 +
 … + 
(An x + Bn)/(x^2 + 1)^n

4)  General Template

If: P(x) / Q(x)

and Q(x) factors as:

    Q(x) = (x - a1)^n1 * (x - a2)^n2 * ... * (x - ak)^nk
       * (quadratic1)^m1 * (quadratic2)^m2 * ... * (quadratic_l)^ml

Then the decomposition is:

  sum over all linear factors of constants / powers of (x - ai) +
  sum over all quadratic factors of (linear numerator) / powers of quadratic

    A1 / (x - a1) + A2 / (x - a1)^2 + ... + Ani / (x - a1)^ni
    plus
    (B1 x + C1) / (quadratic_j) + 
    (B2 x + C2) / (quadratic_j)^2 +
    ... +
    (Bmj x + Cmj) / (quadratic_j)^mj


5)  Procedure to Solve

1.  Make sure the fraction is proper.
2.  Factor the denominator completely.
3.  Write the correct general decomposition form.
4.  Multiply both sides by the common denominator.
5.  Expand all expressions.
6.  Equate coefficients (or substitute convenient x-values).
7.  Solve the resulting system of equations.

6)  Examples

Example 1, Decompose:

    (3x + 5) / [(x - 1)(x + 2)]

Step 1: Write the general form:

    A/(x - 1) + B/(x + 2)

Step 2: Multiply by the denominator:

    3x + 5 = A(x + 2) + B(x - 1)

Step 3: Expand:

    3x + 5 = Ax + 2A + Bx - B
           = (A + B)x + (2A - B)

Step 4: Match coefficients:

    A + B = 3
    2A - B = 5

Step 5: Solve:

    A = 8/3
    B = 1/3


Example 2: Decompose (x^3 + 1) / (x^2 - 1)

Degree numerator = 3
Degree denominator = 2
Since 3 >= 2, it is improper → 
perform polynomial long division

Step 1: Polynomial long division:

Divide x^3 by x^2 → x
Multiply: x * (x^2 - 1) = x^3 - x
Subtract: (x^3 + 1) - (x^3 - x) = x + 1
Remainder = x + 1 (degree 1 < degree 2)

Step 2: Rewrite as polynomial + proper fraction
(x^3 + 1) / (x^2 - 1) = x + (x + 1) / (x^2 - 1)

Step 3: Factor denominator for partial fractions

x^2 - 1 = (x - 1)(x + 1)
(x + 1) / (x^2 - 1) = (x + 1) / [(x - 1)(x + 1)]

Step 4: Set up partial fractions
(x + 1) / [(x - 1)(x + 1)] = A / (x - 1) + B / (x + 1)

Multiply both sides by (x - 1)(x + 1):
x + 1 = A(x + 1) + B(x - 1)

Step 5: Solve for constants
Let x = 1: 2 = 2A + 0 → A = 1
Let x = -1: 0 = 0 + (-2)B → B = 0

Step 6: Write final result
(x^3 + 1) / (x^2 - 1) = x + 1 / (x - 1)


Main Uses of Partial Fractions:

-   Integration
-   Inverse Laplace transforms
-   Differential equations
-   Control systems

"""