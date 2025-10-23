# To subtract numbers in binary, the CPU performs addition using the identity:
# A - B = A + (-B)
# where -B is called the two's complement of B.

# In an n-bit system, any negative number is represented
# in such a way that it satisfies: B + X ≡ 0 (mod 2^n)
# From this, we can write:
# X = -B ≡ 2^n - B (mod 2^n)

# This works because in an n-bit system, any value larger than 2^n - 1
# automatically wraps around due to modular arithmetic. A useful trick
# to compute -B is: (2^n - 1) - B

# This is equivalent to reversing all the bits of B,
# since 2^n - 1 is a number with all ones in an n-bit system.
# Adding 1 to this result gives: -B = [(2^n - 1) - B] + 1
# Thus, invert all bits of B and add 1 to obtain -B.

# Once -B is computed, subtraction can be performed
# as a regular binary addition: A - B = A + (-B)
# This approach eliminates the need for the more complex
# subtraction logic that involves borrow bits, allowing the CPU
# to use the same adder circuitry for both addition and 
# subtraction efficiently.


# Example representation
# Computers store negative numbers using this two’s complement system.
# Given an n-bit binary number B:
#     - Invert all bits (called one’s complement)
#     - Add 1
# The result is the binary encoding of -B.
# Example (8-bit system):
#     B = 00001101 (13)
#     Invert bits → 11110010
#     Add 1       → 11110011  (represents -13)
# When added to B:
#     00001101 + 11110011 = 1 00000000  → discard overflow → 00000000 (0)
# The discarded carry is the “wrap-around” of modulo 2^n arithmetic.


# on a current MacBook Pro (with Apple Silicon), 
# integers in the CPU registers for arithmetic operations are 64-bit,
# meaning the CPU naturally works modulo 2^64 
# That is, the largest unsigned integer that fits is: 2 ^ 64 -1
# = 18,446,744,073,709,551,615
# so subtraction via two’s complement works natively in 64-bit registers.
# Example: Representing -14 in 64-bit Two's Complement
# 1. Positive number B = 14
# Decimal: 14
# Binary (64-bit):
# 0000000000000000000000000000000000000000000000000000000000001110
# 2. Step 1: Invert all bits (one's complement)
# 1111111111111111111111111111111111111111111111111111111111110001
# 3. Step 2: Add 1 to get two's complement (-B)
# 1111111111111111111111111111111111111111111111111111111111110010
# Decimal equivalent (unsigned interpretation): 18,446,744,073,709,551,602
# 4. Verification: Add B + (-B) modulo 2^64
# 0000000000000000000000000000000000000000000000000000000000001110  (14)
# +1111111111111111111111111111111111111111111111111111111111110010  (-14)
# ------------------------------------------------
# 1 0000000000000000000000000000000000000000000000000000000000000000  (overflow ignored)
# Result = 0 



def negate_num(a, bit_size):
    num = a 
    negate = ((num &1) ^ 1)
    current_offset = 2
    
    for _ in (range(bit_size-1)):

        num = (num >> 1)
        negate += current_offset * ((num &1) ^ 1)
        current_offset *= 2
    
    mask = (1 << bit_size) - 1   # Create a mask with bit_size 1's
    lsb = (negate + 1 + a) & mask # Extract least significant [bit_size] bits

    # print(bin(a)[2:].zfill(bit_size+1))
    # print(bin(negate)[2:].zfill(bit_size+1))
    # print(bin(negate+1)[2:].zfill(bit_size+1))
    # print(bin(negate+1+a)[2:].zfill(bit_size+1))
    # print(bin(lsb)[2:].zfill(bit_size+1))

    return negate+1

def positive_num(a,bit_size):
    return a & ((1 << bit_size) - 1)

def bitwise_subtract(a,b, bit_size):
    return positive_num(a,bit_size) + negate_num(b, bit_size) & ((1 << bit_size) - 1)


# Example, the bit lenght is 4 (can hold 0-15 values)
nbits = int(2**3).bit_length()
print(nbits) # bit_size = 4
print(bitwise_subtract(10,5,nbits))
print(bitwise_subtract(10, negate_num(5,nbits),nbits))
print(bitwise_subtract(10, negate_num(6,nbits),nbits))



# conceptually, floating-point subtraction (A - B) 
# is handled under the hood in a way very similar to addition,
# but there are subtle details due to floating-point representation.

# -- Floating-point representation
# In IEEE 754 (common floating-point standard), a number is represented as:

# (-1)^s * 1.m * 2^e

# * s = sign bit
# * m = mantissa (or significand)
# * e = exponent


# -- Subtraction as addition of a negative

# subtraction is performed as addition:
# A - B ≡ A + (-B)

# You first flip the sign bit of B to get -B.
# Then perform floating-point addition of A + (-B).

# Steps in floating-point addition/subtraction

# -- Align exponents:

#    * Suppose A = 1.m_1 * 2^e_1 and B = 1.m_2 * 2^e_2.
#    * Shift the mantissa of the smaller exponent so both numbers have the same exponent.

# -- Add or subtract mantissas:
#  Now it’s essentially integer addition/subtraction on the mantissas.
#  If signs are different (for subtraction), you subtract the mantissas.

# 6. Normalize the result:
# Shift the mantissa left/right to ensure it’s in the correct range
# (usually 1.0 ≤ mantissa < 2.0).
# Adjust the exponent accordingly.

# 7. Round the result:
# Round the final mantissa to fit the available bits 
# (e.g., 23 bits for single precision).

# Important caveats
# Precision loss: If A and B are very close, 
# significant digits may cancel, leading to catastrophic cancellation.
# Overflow/underflow: Adding very large or very small numbers 
# may exceed the representable range.


# So, under the hood:
# A - B becomes A + (-B)
# but the actual computation works on aligned exponents
# and integer-like mantissas, not on the floating-point
# numbers as a monolithic entity.

