# Using the Identity a^b = exp(b * ln(a))

# The exponential and logarithmic functions are inverses of each other.
# That means: ln(exp(x)) = x   and   exp(ln(x)) = x

# We can express exponentiation in terms of 
# exponential and logarithmic functions using this property.

# For any positive real number a > 0 and any real number b:
#     a^b = exp(b * ln(a))

# This works because:
# 1. Taking the natural logarithm of both sides gives:
#        ln(a^b) = b * ln(a)
# 2. Then exponentiating both sides gives:
#        a^b = exp(b * ln(a))

# This identity is useful in:
# - Numerical computation (for better precision)
# - Differentiation or integration involving powers
# - Extending power operations to non-integer 
# or real-valued exponents


# The identity a^b = exp(b * ln(a))
# is not only a mathematical relationship 
# but also the foundation for how computers and calculators compute
# powers efficiently, especially when b is not an integer.

# Computational Insight

# Directly computing a^b for arbitrary real numbers is difficult.
# For example:
# 2^3 can be computed by multiplying 2 * 2 * 2.
# But how do you compute 9^0.5 (the square root of 9) or 2^pi?

# Instead of trying to directly calculate the result,
# computers use the logarithmic–exponential identity:

# 1. Compute the natural logarithm of a: ln(a)
# 2. Multiply it by b: b * ln(a)
# 3. Compute the exponential of that product: exp(b * ln(a))

# This process is mathematically valid and computationally 
# efficient because exp() and ln() are core functions that
# hardware and software math libraries implement with great precision.

# Advantages
# Universality - Works for any real exponent b, including fractional or negative values.
# Efficiency - CPUs and calculators use optimized low-level routines 
# for exp() and ln(), making this faster than other methods.

# Precision - Mathematical libraries use series expansions 
# and iterative refinements to ensure accuracy.
# Simplicity - The approach reduces the problem of 
# computing a power to two well-known functions.
# -> By reducing the operation to a combination of exponential
# and logarithmic functions, it allows fast computation across
# all real numbers using optimized and precise internal algorithms.


import math

def power_via_identity(a, b):
    """Compute a^b using the identity a^b = exp(b * ln(a))"""
    if a <= 0:
        raise ValueError("a must be positive for real logarithm")
    return math.exp(b * math.log(a))

# Example usage
print(power_via_identity(2, 3))    # Expected output: 8.0
print(power_via_identity(9, 0.5))  # Expected output: 3.0

# Explanation:
# - math.log(a) computes the natural logarithm ln(a)
# - math.exp(x) computes e^x
# - Multiplying b * math.log(a) and exponentiating gives the same result as a ** b