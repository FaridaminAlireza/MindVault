
# How Calculators and Computers Compute Roots and Powers
# using numerical methods, especially the Newton-Raphson method,
# and how they find a good initial guess.

# 1) The Root-Finding Problem

# We want to compute the real n-th root of a number a, that is:
# x = a^(1/n)
# This means finding x such that:
# f(x) = x^n - a = 0
# We can find x by solving this equation iteratively using a root-finding method.


# 2) Newton-Raphson Method

# Newton's method improves an approximate root x_k by using the formula:
# x_{k+1} = x_k - f(x_k) / f'(x_k)

# For our function f(x) = x^n - a, the derivative is:
# f'(x) = n * x^(n-1)

# Substituting these into Newton's update formula gives:
# x_{k+1} = x_k - ( (x_k)^n - a) / (n * (x_k)^(n-1))
# x_{k+1} = x_k - ( (x_k)^n / (n * (x_k)^(n-1)) - (a / (n * (x_k)^(n-1)))
# Simplify the expression:

# Simplify (x_k)^n / (x_k)^(n - 1):
#     (x_k)^n / (x_k)^(n - 1) = x_k

# Now substitute this back:
#     x_{k+1} = x_k - ( x_k / n) +  (a / (n * (x_k)^(n - 1)))

# Combine terms over a common denominator n
# Write everything as a single fraction:
#     x_{k+1} = (n * x_k - x_k + a / (x_k)^(n - 1)) / n

# Simplify the numerator
# Simplify n * x_k - x_k:
# n * x_k - x_k = (n - 1) * x_k

# Therefore:
#  x_{k+1} = ( (n - 1) * x_k  +  a / (x_k)^(n - 1) ) / n



# x_{k+1} = ( (n - 1) * x_k  +  a / (x_k)^(n - 1) ) / n
# This is the formula used in most calculators and math libraries.

# Special case for n = 2 (square root):
# x_{k+1} = (x_k + a / x_k) / 2
# This specific case is also known as the Babylonian method for square roots.


# 3) Why Newton’s Method Works Well

# - It converges quadratically near the root, meaning the number of correct digits
#   roughly doubles at each iteration.
# - Usually, only a few iterations (3 to 6) are needed for double precision.
# - It’s purely arithmetic, so it can run efficiently on binary floating-point hardware.

# 4) Choosing a Good Initial Guess

# Newton’s method converges fast only if the initial guess (x_0) is reasonably close
# to the actual root.
# A bad initial guess may lead to slow convergence or overflow/underflow.

# 4.1) Simple Heuristic Guess

#     if a >= 1:  x_0 = a
#     else:        x_0 = 1
# This works but may take several iterations to converge.


# 4.2) Exponent and Mantissa-Based Guess

# Floating-point numbers are stored as:
#     a = m * 2^e
# where:
# - m is the mantissa in [0.5, 1.0)
# - e is the binary exponent (integer)

# We can extract (m, e) using the function `frexp(a)` in C or Python.

# We know that:

#     a^(1/n) = (m * 2^e)^(1/n)
#              = m^(1/n) * 2^(e/n)

# So, we can approximate:

#     x_0 ≈ 2^(e/n) * m^(1/n)

# This gives a very good initial guess.
# For the 2^(e/n) part, we can split e/n into integer and fractional parts:

#     int_part = floor(e / n)
#     frac_part = e / n - int_part

# Then compute:

#     guess = ldexp(1.0, int_part) * (2.0 ** frac_part) * (m ** (1.0 / n))
# where ldexp(x, i) = x * (2 ** i)

# This is the approach used in high-quality implementations.


# 4.3) Bit-Level Trick (Fast Inverse Square Root)

# For the specific case of 1/sqrt(x), an approximate initial guess can be obtained
# directly from the binary representation of the floating-point number.

# In the famous “Fast Inverse Square Root” (used in Quake III), the steps are:

# 1. Interpret the float’s bits as an integer.
# 2. Subtract half of the exponent bits from a magic constant (0x5f3759df).
# 3. Interpret the bits back as a float.
# 4. Perform one or two Newton refinements for 1/sqrt(x).

# This yields a surprisingly good and fast approximation for single-precision floats.


# 5) Example in Python

#     def nth_root_newton(a, n):
#         x = initial_guess(a, n)
#         for i in range(max_iterations):
#             x = ((n - 1) * x + a / (x ** (n - 1))) / n
#             if converged(x): break
#         return x

#     # Initial guess could be based on exponent and mantissa as shown above.


# 6) Summary

# - The nth root problem is turned into a root-finding problem f(x) = x^n - a.
# - Newton’s method provides a fast iterative way to solve it.
# - A good initial guess ensures fast convergence.
# - Calculations are done in binary (IEEE-754 floats).
# - Hardware sqrt instructions or software Newton loops
#  both rely on this principle.


# Algorithm Overview
# We want to find x such that:
#     f(x) = x^n - a = 0
# Newton's method iterates:
#     x_{k+1} = x_k - f(x_k) / f'(x_k)
# Here, f'(x) = n * x^(n - 1)#
# Substituting, we get:
#     x_{k+1} = ((n - 1) * x_k + a / x_k^(n - 1)) / n
# This is the iterative formula for nth roots.

# Implementation Details
# - Step 1: Handle sign and trivial cases (zero, negative numbers).
# - Step 2: Extract mantissa and exponent using math.frexp().
# - Step 3: Compute an initial guess using exponent scaling.
# - Step 4: Apply Newton iterations until convergence.
# - Step 5: Return the result with proper sign.

import math

def nth_root_newton(a: float, n: int, tol: float = 1e-15, maxiter: int = 100) -> float:
    """Compute the real n-th root of a using Newton-Raphson iteration."""
    if n == 0:
        raise ValueError("n must be non-zero")
    if a == 0.0:
        return 0.0
    if a < 0.0 and (n % 2 == 0):
        raise ValueError("Even root of a negative number is not real.")

    # Determine the sign and use absolute value for iteration
    sign = -1.0 if a < 0 else 1.0
    a_abs = abs(a)

    # Step 1: Extract mantissa and exponent
    # a_abs = m * 2^e  with m in [0.5, 1.0)
    m, e = math.frexp(a_abs)

    # Step 2: Compute a good initial guess
    # a^(1/n) = m^(1/n) * 2^(e/n)
    exponent = e / n
    int_part = int(math.floor(exponent))
    frac_part = exponent - int_part

    # ldexp(x, k) = x * (2 ** k)
    init_guess = math.ldexp(1.0, int_part) * (2.0 ** frac_part) * (m ** (1.0 / n))

    x = init_guess

    # Step 3: Newton-Raphson Iteration
    for i in range(maxiter):
        prev = x
        x = ((n - 1) * x + a_abs / (x ** (n - 1))) / n

        # Check for convergence (relative difference small enough)
        if abs(x - prev) <= tol * max(1.0, abs(prev)):
            break

    return sign * x

if __name__ == "__main__":
    test_values = [
        (2.0, 2),
        (27.0, 3),
        (16.0, 4),
        (0.001, 3),
        (-8.0, 3),
        (1e20, 2),
    ]

    for a, n in test_values:
        result = nth_root_newton(a, n)
        ref = math.copysign(math.pow(abs(a), 1.0 / n), a)
        print(f"a={a:>10}, n={n:>2} | newton={result:.17g} | reference={ref:.17g} | diff={result - ref:+.3e}")
