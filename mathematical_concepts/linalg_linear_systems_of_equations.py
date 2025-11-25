"""
1. What makes a system “linear”?
A system is linear if each equation is linear in the unknowns —
meaning every unknown (variable we are solving for) appears only
to the first power, with no products or nonlinear combinations of them.

Example of linear equations in unknowns (a, b, c, d):
a x_1 + b x_2 + c x_3 + d x_4 = y

No (a^2), (ab), (a/c), etc. — just linear combinations.

---
2. What if (x_1 = x^5), (x_2 = x^2), etc.?

That’s totally fine — because (x_1, x_2, x_3, x_4) are not unknowns 
in that context; they are known coefficients (numbers derived from (x)).

For example, suppose your equation comes from:
y = a x^5 + b x^3 + c x^2 + d x

At a specific (x), say (x = 2),
you can rewrite it as:
(32)a + (8)b + (4)c + (2)d = y


This is linear in the unknowns (a,b,c,d), even though it came from powers of (x).
The nonlinearity is in the data (the coefficients), not in the unknowns.

So it doesn’t matter if (x_1 = x^5), (x_2 = x^3), or any other function of (x).
As long as your unknowns (the things you’re solving for — (a, b, c, d))
appear linearly, the system is still linear.

You can always represent it as:

A X = b


where:

* (A) is built from known numbers (like (x^5, x^3, x^2, x))
* X = ([a, b, c, d]^T)
* b = known right-hand sides (like (y) values)

---
3. Application:

That’s exactly how polynomial fitting and interpolation work:
You collect equations like: 

a x_i^5 + b x_i^3 + c x_i^2 + d x_i = y_i

for several points (x_i, y_i),
and then solve the linear system for ([a, b, c, d]).

Libraries like NumPy or SciPy just build that coefficient matrix (A)
 from powers of (x_i) and use LU decomposition (or QR, SVD, etc.) internally.

---
4. Example:


4x4 Example where coefficients are powers of x 
(x1 = x^5, x2 = x^3, x3 = x^2, x4 = x)

We take the model:
    y = a * x^5 + b * x^3 + c * x^2 + d * x

Choose true coefficients (for this example):
    a = 1, b = 2, c = 3, d = 4

Evaluate at x = 1, 2, 3, 4 to build the linear system A [a b c d]^T = b:

For each x_i, the row is [x_i^5, x_i^3, x_i^2, x_i]


Constructed matrix A (rows = [x^5, x^3, x^2, x]):

[[1.000e+00, 1.000e+00, 1.000e+00, 1.000e+00],
 [3.200e+01, 8.000e+00, 4.000e+00, 2.000e+00],
 [2.430e+02, 2.700e+01, 9.000e+00, 3.000e+00],
 [1.024e+03, 6.400e+01, 1.600e+01, 4.000e+00]]


Right-hand side vector b (computed from a=1, b=2, c=3, d=4):

[  10.,   68.,  336., 1216.]


We now perform LU factorization (no pivoting) and record steps:


Step 1, pivot U[0,0] = 1.0

  Eliminate row 1 using row 0: multiplier m = 32.0

    Row 1 before: [32.0, 8.0, 4.0, 2.0]

    Row 1 after : [0.0, -24.0, -28.0, -30.0]

  Eliminate row 2 using row 0: multiplier m = 243.0

    Row 2 before: [243.0, 27.0, 9.0, 3.0]

    Row 2 after : [0.0, -216.0, -234.0, -240.0]

  Eliminate row 3 using row 0: multiplier m = 1024.0

    Row 3 before: [1024.0, 64.0, 16.0, 4.0]

    Row 3 after : [0.0, -960.0, -1008.0, -1020.0]

Step 2, pivot U[1,1] = -24.0

  Eliminate row 2 using row 1: multiplier m = 9.0

    Row 2 before: [0.0, -216.0, -234.0, -240.0]

    Row 2 after : [0.0, 0.0, 18.0, 30.0]

  Eliminate row 3 using row 1: multiplier m = 40.0

    Row 3 before: [0.0, -960.0, -1008.0, -1020.0]

    Row 3 after : [0.0, 0.0, 112.0, 180.0]

Step 3, pivot U[2,2] = 18.0

  Eliminate row 3 using row 2: multiplier m = 6.222222222222222

    Row 3 before: [0.0, 0.0, 112.0, 180.0]

    Row 3 after : [0.0, 0.0, 0.0, -6.666666666666657]


Resulting L:

[[1.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
 [3.20000000e+01, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00],
 [2.43000000e+02, 9.00000000e+00, 1.00000000e+00, 0.00000000e+00],
 [1.02400000e+03, 4.00000000e+01, 6.22222222e+00, 1.00000000e+00]]


Resulting U:

[[  1.        ,   1.        ,   1.        ,   1.        ],
 [  0.        , -24.        , -28.        , -30.        ],
 [  0.        ,   0.        ,  18.        ,  30.        ],
 [  0.        ,   0.        ,   0.        ,  -6.66666667]]


Forward substitution (L y = b) gives y:

[  10.        , -252.        ,  174.        ,  -26.66666667]


Backward substitution (U x = y) gives solution x (coefficients [a,b,c,d]):

[1., 2., 3., 4.]


Check: A @ x = b ? ->

[  10.,   68.,  336., 1216.]

Conclusion: The solved coefficients are a=1, b=2, c=3, d=4 as expected.



----
5. Extra information on LU Decomposition and Role of y, L, U, and b

We start with a system of linear equations:
    A x = b

Where:
- A is a known square matrix (coefficients from equations),
- x is the vector of unknowns (what we want to find),
- b is the known right-hand side (results of the equations).

Example:
    [ [1, 1, 1, 1],
      [32, 8, 4, 2],
      [243, 27, 9, 3],
      [1024, 64, 16, 4] ]
    [a, b, c, d]^T = [10, 120, 1000, 8000]^T

Here A comes from powers of x, b is the target y-values,
 and x = [a, b, c, d]^T are the coefficients we want.


LU Factorization:
We decompose A into two simpler matrices:
    A = L * U
where
- L is lower-triangular (1s on the diagonal, multipliers below)
- U is upper-triangular (zeros below the diagonal)

Now substitute into A x = b:
    (L U) x = b

To simplify, define:
    U x = y
so the system becomes:
    L y = b

That’s the key transformation. It splits the problem 
into two triangular systems:
1. L y = b  (Forward substitution)
2. U x = y  (Backward substitution)


Why introduce y?
Because both L and U are triangular, 
they are easy to solve sequentially.

Forward substitution (solve for y):

    y1 = b1
    y2 = b2 - L21*y1
    y3 = b3 - L31*y1 - L32*y2
    ...

Backward substitution (solve for x):

    x4 = y4 / U44
    x3 = (y3 - U34*x4)/U33
    x2 = (y2 - U23*x3 - U24*x4)/U22
    ...


For the polynomial case, in our 
4x4 example (powers of x):
    A [a, b, c, d]^T = b

The steps are:
1. Perform LU decomposition to get A = L U.
2. Solve L y = b (forward substitution, top to bottom)).
3. Solve U x = y (backward substitution, bottom to top).

So:
- b is the known right-hand side (e.g., polynomial values at given x).
- L stores the multipliers from elimination.
- U is the upper-triangular matrix from Gaussian elimination.
- y is an intermediate variable that links b and x.


"""