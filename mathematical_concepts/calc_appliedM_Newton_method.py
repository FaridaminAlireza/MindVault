# Newton's Method for Finding Roots

# Newton's Method (also called the Newton-Raphson method) 
# is an iterative technique for finding approximate roots 
# of a real-valued function f(x). 
# It is especially useful when analytical solutions are difficult
# or impossible to obtain.

# Approach
# Given a function f(x) and its derivative f'(x), the Newton-Raphson iteration formula is:

#  x_{n+1} = x_n - f(x_n)/f'(x_n)

# Here:
# - x_n is the current approximation.
# - x_{n+1} is the next, hopefully more accurate, approximation.
# - The process is repeated until |x_{n+1} - x_n| is smaller than a specified tolerance.
# The convergance is proved through Taylor series expansion.


# Ex. 
# f'(x1) = f(x1) - (f(x2) = 0)  / x2-x1
# f'(x1) x2 - f'(x1) x1 = f(x1)
# x2 = (f(x1) - f'(x1) x1) / f'(x1)
# x2 = x1 - f(x1) /f'(x1)


# Derivation
# The idea is to approximate f(x) near x_n using a tangent line:

# The tagnent line to f(x) at x_n has the slope f'(x_n), and
# passes through the point (x_n, f(x_n)).

# The point-slope form of a line is: 
# y−y0 ​= m(x−x0​) where
#  m = f'(x_n),
#  x_0 = x_n ,
#  y_0 = f(x_n),
#  y = f(x)
# f(x) = f(x_n) + f'(x_n) (x - x_n)

# f(x) ≈ f(x_n) + f'(x_n)(x - x_n)
# Setting f(x) = 0 to find the root:

#  0 = f(x_n) + f'(x_n) (x_{n+1} - x_n)
#  - f(x_n) = f'(x_n) (x_{n+1} - x_n)
#  -f(x_n) /f'(x_n) = (x_{n+1} - x_n)

#  x_{n+1} = x_n - f(x_n)/f'(x_n)
# This gives the iterative formula used in Newton's Method.

# Algorithm
# Given f(x), f'(x), initial guess x0, tolerance tol:
# Repeat:
#     x1 = x0 - f(x0)/f'(x0)
#     if |x1 - x0| < tol:
#         break
#     x0 = x1
# Return x1

# Notes
# - Convergence is fast if the initial guess is close to the root.
# - If f'(x_n) is zero or near zero, the method may fail.
# - Multiple roots reduce convergence speed.


# Convergence Proof of Newton's Method

# Let f: R → R be a function with a simple root at x = α,
# meaning f(α) = 0 and f'(α) ≠ 0.

# Newton's iteration formula:
#     x_{n+1} = x_n - f(x_n) / f'(x_n)

# We want to show that x_n → α and find the rate of convergence.

# 1. Taylor Expansion of f(x_n)

# Expand f(x_n) around α using Taylor's theorem:
# f(x_n) = f(α) + f'(α)(x_n - α) + (1/2)f''(ξ_n)(x_n - α)^2
# for some ξ_n between x_n and α.
# Since f(α) = 0, this simplifies to:
# f(x_n) = f'(α)(x_n - α) + (1/2)f''(ξ_n)(x_n - α)^2

# 2. Substitute into Newton Iteration
# The iteration is:
#     x_{n+1} = x_n - f(x_n) / f'(x_n)
# Subtract α from both sides:
#     x_{n+1} - α = x_n - α - f(x_n)/f'(x_n)
# Substitute f(x_n) from the Taylor expansion:
# x_{n+1} - α = x_n - α - [ f'(α)(x_n - α) + (1/2)f''(ξ_n)(x_n - α)^2 ] / f'(x_n)
# Simplify:
# x_{n+1} - α = (x_n - α) [1 - f'(α)/f'(x_n)] - (1/2)[f''(ξ_n)/f'(x_n)](x_n - α)^2

# 3. Approximation near the root
# For x_n close to α, f'(x_n) ≈ f'(α), so:
#     1 - f'(α)/f'(x_n) ≈ 0
# Hence, the dominant term is the quadratic one:
#     x_{n+1} - α ≈ - (1/2)[f''(α)/f'(α)](x_n - α)^2

# 4. Convergence Order
# Taking absolute values:
# |x_{n+1} - α| ≈ C |x_n - α|^2

# where C = |f''(α) / (2f'(α))|.

# Thus, Newton's method converges quadratically to α,
# provided f is twice continuously differentiable and f'(α) ≠ 0.

# 5. Conditions Summary

# Convergence is guaranteed if:
# - f ∈ C² near α
# - f'(α) ≠ 0
# - initial guess x₀ is sufficiently close to α

# In summary, Newton’s method converges 
# quadratically near a simple root.
# That is:
#     |x_{n+1} - α| ≤ C |x_n - α|²ßß
# for some constant C > 0.


def newton_method(f, f_prime, x0, tol=1e-7, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if fpx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x_next = x - fx / fpx
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    raise ValueError("Did not converge within max_iter iterations")

# Ex f(x)=x2−2=0
f = lambda x: x**2 - 2
f_prime = lambda x: 2*x

root = newton_method(f, f_prime, x0=1)
print("Root ≈", root)

# f(x)=x3−x−2=0
f = lambda x: x**3 - x - 2
f_prime = lambda x: 3*x**2 - 1

root = newton_method(f, f_prime, x0=1.5)
print("Root ≈", root)


# f(x)=cos(x)−x=0
import math

f = lambda x: math.cos(x) - x
f_prime = lambda x: -math.sin(x) - 1

root = newton_method(f, f_prime, x0=1)
print("Root ≈", root)



# Newton’s method doesn’t “find all roots” by itself —
# it converges to one root depending on the starting point.

# Different initial guesses converge to different roots.
# This leads to Newton fractals — beautiful visualizations
# showing which starting points lead to which root.


#Ex f(x)=x4−1

# x^4 - 1 = (x^2 - 1)(x^2 + 1)
# x^2 - 1 = (x - 1)(x + 1)
# x^4 - 1 = (x - 1)(x + 1)(x^2 + 1)
# x^2 + 1 = (x - i)(x + i)
# Final factorization: y = (x - 1)(x + 1)(x - i)(x + i)
# Real roots: x=±1,  Complex roots: x=±i

def newton_method_complex(f, f_prime, x0, tol=1e-8, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if abs(fpx) < 1e-12: # scientific notation of 1* 10^{-12}
            break
        x_next = x - fx / fpx
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    return x
#  note: comparing floating-point numbers with == is unsafe 
# — because of tiny precision errors (for fpx)
# e1-12 effectively means “if the derivative is
# effectively zero, stop before dividing

import cmath

f = lambda x: x**4 - 1
f_prime = lambda x: 4*x**3

# Try multiple starting guesses
# j represents the imaginary unit, just like i in mathematics.
# j = sqrt(-1)

guesses = [
    1+0j, -1+0j, 0+1j, 0-1j,
    0.5+0.5j, -0.5+0.5j, 0.5-0.5j, -0.5-0.5j
]

roots = []
for g in guesses:
    root = newton_method_complex(f, f_prime, g)
    roots.append(root)

# Cluster near-identical roots
unique_roots = []
for r in roots:
    if not any(abs(r - u) < 1e-6 for u in unique_roots):
        unique_roots.append(r)

print("Unique roots found:")
for r in unique_roots:
    print(r)


