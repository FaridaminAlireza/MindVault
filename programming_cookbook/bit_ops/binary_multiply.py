# Binary multiplication works the same as decimal multiplication, 
# but simpler because multiplying by 0 or 1 is trivial.

# Steps:
    # 1. Multiply each bit of one number by each bit of the other (bitwise AND).
    # 2. Shift left according to the position (like adding zeros in decimal multiplication).
    # 3. Add all the shifted results.

# Example:
#    101   (5 in decimal)
# ×   11   (3 in decimal)
# ---------
#    101   (101 × 1, shift 0)
# + 1010   (101 × 1, shift 1)
# ---------
#   1111   (15 in decimal)


def binary_multiply(a, b):
    # Convert binary strings to integers
    multiplicand = a
    multiplier = b
    
    result = 0
    shift = 0

    while multiplier > 0:
        # Check if the least significant bit is 1
        if multiplier & 1:
            result += multiplicand << shift
        shift += 1
        multiplier >>= 1  # Shift multiplier right by 1 bit

    # Convert result back to binary string
    return bin(result)[2:]

# Example
a = "101"  # 5 in decimal
b = "11"   # 3 in decimal

print(f"{a} * {b} = {binary_multiply(a, b)}")  # Output should be "1111" (15 in decimal)






# How CPUs Do It
# CPUs don’t usually multiply bit by bit manually. There are a few common approaches:

# Shift-and-Add Method (like manual binary multiplication)
# Each bit of the multiplier is checked.
# If bit is 1 → add the multiplicand shifted by that bit’s position.
# If bit is 0 → add 0.
# This is exactly like the example above.

# Booth’s Algorithm (for signed numbers)
# Handles negative numbers efficiently.
# Reduces the number of additions/subtractions.

# Hardware Multipliers / Combinational Circuits
# Modern CPUs often have dedicated multiplier circuits
# that compute the result in parallel using array multipliers
# or Wallace trees.
# This allows multiplication in a single CPU cycle or a few cycles,
# unlike shift-and-add which is slower.



