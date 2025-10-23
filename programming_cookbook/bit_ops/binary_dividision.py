# Binary division works similarly to long division in decimal,
#  but with only two digits: 0 and 1.

# Steps:
# - Start from the leftmost bits (most significant bits).
# - Check if the divisor can fit into the current bits of the dividend.
# - If yes:
#     - Subtract divisor from that portion of the dividend.
#     - Write '1' in the quotient.
# - If not:
#     - Write '0' in the quotient.
# - Bring down the next bit and repeat until all bits are processed.

# Example:
# ---------
# Divide 1011 (11 decimal) by 11 (3 decimal):

#    11 ) 1011
# Step 1: 10 < 11 → quotient bit = 0
# Step 2: 101 >= 11 → 101 - 11 = 10 → quotient bit = 1
# Step 3: Bring down next bit → 101 again → subtract → remainder = 10
# Result:
# Quotient = 11 (3 decimal)
# Remainder = 10 (2 decimal)


def binary_divide(dividend: str, divisor: str):
    """Perform binary division using shift-subtract method."""
    # Convert to integers
    dividend_int = int(dividend, 2)
    divisor_int = int(divisor, 2)

    if divisor_int == 0:
        raise ValueError("Division by zero is not allowed.")

    quotient = 0
    remainder = 0
    n = len(dividend)

    # Align divisor with dividend bits (start from MSB)
    for i in range(n - 1, -1, -1):
        # Shift remainder left and bring down the next bit
        remainder = (remainder << 1) | ((dividend_int >> i) & 1)

        if remainder >= divisor_int:
            remainder -= divisor_int
            quotient = (quotient << 1) | 1
        else:
            quotient = (quotient << 1)

    return bin(quotient)[2:], bin(remainder)[2:]


q, r = binary_divide("1011", "11")
print(f"Quotient: {q}, Remainder: {r}") # Quotient: 11, Remainder: 10


# - The code simulates a hardware-style shift-subtract algorithm.
# - Each step checks if the current remainder can "fit" the divisor.
# - The quotient accumulates bits from left to right.
# - This is the same method used internally in CPUs (integer ALUs) for division.


# Each time:
# You try to divide the current remainder (plus any new bit) by the divisor.
# If it doesn’t fit, you record 0 and bring down the next bit to make the number larger.
# If it fits, you record 1, subtract, and then bring down the next bit.
# This “bringing down” is what’s called adding the next most significant digit (or bit) to the remainder.



# In decimal long division, when we “bring down” the next digit,
#  we’re effectively multiplying the remainder by 10 and then adding the next digit.

# new_remainder = remainder * 10 + next_digit

# In binary, when we bring down the next bit, 
# we’re doing the exact same thing — 
# except we multiply by 2 and add 0 or 1.

# So even though a leading zero doesn’t numerically change
#  the value (e.g., 01 = 1), it does change the position in
#  the algorithm because that “shift” represents multiplying
#  by the base.

# new_remainder = remainder * 2 + next_bit


# Binary division including fraction: 

# Binary Division of 3 (011) by 5 (101)
# We want: 3 / 5 in binary, including fractional points.

# Step-by-step long division:

# Quotient: 0.100110011... (repeating)
#       0.100110011...
#     ----------------
# 101 | 011.00000000
#        000        <- 101 does not fit in 011 (quotient bit 0)
#        ----
#        0110       <- bring down 0
#        101        <- 101 fits once in 110
#        ----
#        0010       <- remainder 2, bring down 0
#        00100      <- 101 does not fit in 0100 (quotient bit 0)
#        ----
#        01000      <- bring down 0
#        101        <- 101 fits once in 1000
#        ----
#        00110      <- remainder 6, bring down 0
#        101        <- 101 fits once in 0110
#        ----
#        00010      <- remainder 2, pattern repeats

# Explanation:
# 1. Since 3 < 5, the integer part is 0.
# 2. Add binary point and zeros to perform fractional division.
# 3. Shift and subtract as in decimal long division.
# 4. Each quotient bit is determined by whether 101 fits into the current remainder.
# 5. Continue bringing down zeros to get further fractional bits.
# 6. The repeating remainder leads to repeating binary fraction: 0.10011 0011 0011 ...

# Decimal equivalent: 0.6



# Binary Division of 8 by 2.3 (approximation)

# We want: 8 / 2.3 in binary, including fractional points.

# Step 0: Represent numbers in binary
# * 8 in binary: 1000
# * 2.3 in binary (approx): 2 = 10, 0.3 ≈ 0.01001 → 2.3 ≈ 10.01001_2

# Step 1: Eliminate fractional in divisor
# * Multiply numerator and divisor by 2^5 (32) to shift fractional part:
#   * Numerator: 8 * 32 = 256 → 100000000_2
#   * Divisor: 2.3 * 32 ≈ 73.6 → 1001001.1_2 ≈ 74

# Step 2: Integer division
# * 256 / 74 ≈ 3 (decimal) → integer part of quotient = 3
# * Remainder: 256 - 3*74 = 34

# Step 3: Fractional part
# * Bring down zeros for binary long division
# * 34 / 74 ≈ 0.459 (decimal) → binary fraction ≈ .0111...

# Step 4: Approximate binary quotient
# * Quotient ≈ 11.0111..._2
#   * Integer part: 11_2 = 3
#   * Fractional part: .0111... gives remaining fraction

# Decimal check: 3.47826 ≈ 8 / 2.3

# Visual long division (approximate):
# ```
#   11.0111...
# ----------------
# ```

# 10.01001 | 1000.000000
# 10.01001  <- fits once, subtract
# --------
# 0011...  <- remainder, continue with fractional zeros
# ...      <- repeating division to get fraction



