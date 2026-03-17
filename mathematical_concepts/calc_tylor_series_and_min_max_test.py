"""
SUMMARY: Derivatives, Taylor Series, and Min/Max Tests

1) Are higher-order derivatives always smaller than lower-order ones?
No. There is no general rule that the n-th derivative at a point is
larger than or smaller than the (n+1)-th derivative.
- Example: f(x)=e^x -> all derivatives are equal.
- Example: sin(x) -> derivatives oscillate in sign and size.
- Example: polynomials -> derivatives may eventually become zero,
but this is not a general principle.
Conclusion: The size and sign of derivatives depend entirely on the function.

2) Using Taylor series to analyze minima and maxima
Taylor expansion around x:
f(x+h) = f(x) + f'(x)h + (f''(x)/2)h^2 + (f'''(x)/6)h^3 + ...

At a critical point:
f'(x)=0

If f''(x)>0, the point is a candidate for a local minimum.
If f''(x)<0, the point is a candidate for a local maximum.

3) Is the third Taylor term always smaller than the second when f''(x)>0?
No.
- Second term magnitude: (f''(x)/2) h^2
- Third term magnitude: (|f'''(x)|/6) |h|^3
The third term is smaller only when h is sufficiently small.
This is why Taylor-based arguments are local: near the point,
the quadratic term dominates, but not necessarily for larger h.

4) What if the second derivative is zero?
If:
f'(a)=0
f''(a)=0

Then look for the first non-zero derivative of order n >= 3.

Let n be the smallest integer such that f^(n)(a) != 0.

Near a:
f(a+h) - f(a) behaves like h^n multiplied by a constant.

Classification:
- n even and f^(n)(a) > 0 -> local minimum
- n even and f^(n)(a) < 0 -> local maximum
- n odd -> neither minimum nor maximum (inflection/saddle point)

5) Examples
- f(x)=x^4 at x=0: first non-zero derivative is 4th, positive -> minimum
- f(x)=-x^4 at x=0: first non-zero derivative is 4th, negative -> maximum
- f(x)=x^3 at x=0: first non-zero derivative is 3rd (odd) -> no min or max

Key idea:
The first non-zero term in the Taylor expansion dominates all higher-order
terms near the point and determines the local behavior.

"""