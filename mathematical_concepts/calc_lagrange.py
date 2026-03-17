"""
### Lagrange Interpolation Notes

---

## Lagrange Interpolation

### Definition

Given points (x0, y0), (x1, y1), ..., (xn, yn),
find polynomial P(x) of degree ≤ n that passes through all points.

### Formula

P(x) = sum of (yi * Li(x)) for i from 0 to n

where Li(x) = product of (x - xj)/(xi - xj) for all j != i

* Li(xj) = 1 if i=j, 0 if i != j

### Step-by-Step Construction (Example with 3 points)

Points: (1,2), (2,3), (4,1)

* L0(x) = ((x-2)*(x-4))/3
* L1(x) = -((x-1)*(x-4))/2
* L2(x) = ((x-1)*(x-2))/6

Polynomial:
P(x) = 2*L0(x) + 3*L1(x) + 1*L2(x)
= 2*((x-2)*(x-4))/3 - 3*((x-1)*(x-4))/2 + ((x-1)*(x-2))/6

Check: P(1)=2, P(2)=3, P(4)=1

### Example with 2 points

Points: (1,5), (3,9)

* L0(x) = (x-3)/(1-3) = -(x-3)/2
* L1(x) = (x-1)/(3-1) = (x-1)/2

Polynomial:
P(x) = 5*L0(x) + 9*L1(x)
= 5*(-(x-3)/2) + 9*((x-1)/2)
= -(5*(x-3))/2 + (9*(x-1))/2
= (-(5x-15) + (9x-9))/2 = (4x+6)/2 = 2x+3

Check: P(1)=5, P(3)=9

### Trick to Make Li(xi) = 1

* Numerator: product of (x - xj) for j != i → zero at all points except xi

* Denominator: numerator evaluated at xi → normalizes to 1

* At x=xi, numerator = denominator → Li(xi)=1

* At x=xj, j != i, numerator contains (xj-xj)=0 → Li(xj)=0

### Summary Points

1. Each Li(x) peaks at 1 for its own x and 0 for others.
2. No need to solve systems of equations.
3. Degree = number of points - 1.
4. Works for any number of distinct points.
5. Numerator/denominator trick ensures correct scaling.

"""