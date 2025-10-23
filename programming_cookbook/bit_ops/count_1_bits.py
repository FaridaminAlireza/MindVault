# Given an integer n, return an array ans of length n + 1 such that:
# ans[i] is the number of 1’s in the binary representation of i.

# Example

# Input: n = 5
# Output: [0, 1, 1, 2, 1, 2]
# Explanation:
# 0 -> 0 (0 ones)
# 1 -> 1 (1 one)
# 2 -> 10 (1 one)
# 3 -> 11 (2 ones)
# 4 -> 100 (1 one)
# 5 -> 101 (2 ones)

# Approach 1: 
# counting the number of 1s for each number.
def count_ones(n):
    result = [0] * (n+1)
    for i in range(1, n+1):
        num = i 
        total_ones = 0
        remainder = 0
        quotient = 0
        while(num):
            quotient = num//2
            remainder = num - (quotient * 2) 
            if remainder == 1:
                total_ones += 1
            num = quotient 
        # quotient becomes 1 or 0 
        total_ones += quotient
        
        result[i] = total_ones
    
    return result

print(count_ones(5))


# Approach 2: Using dynamic programming and bit operations i >> 1 and i & 1

# i >> 1 — right shift by 1: it drops the least-significant bit (LSB).
# Example: 1011₂ (11) >> 1 → 0101₂ (5).
# Intuitively: i >> 1 ≈ floor(i / 2).

# i & 1 — masking with 1: extracts the LSB (0 or 1).
# Example: 1011₂ & 0001₂ = 0001₂ → LSB is 1.
# If LSB is 0, i & 1 = 0; if LSB is 1, i & 1 = 1.

# So i >> 1 gives the number with the last bit removed;
# i & 1 tells you whether that removed bit was 1.


def count_ones_dp(n):
    result = [0] * (n+1)
    for i in range(1, n+1):
        result[i] = result[i>>1] + (i & 1)
    
    return result

print(count_ones_dp(5))


#Approach 3. By looking at the pattern of repeatition

# look at how the pattern restarts every time we hit a power of two:

# [0..1]    1 + bits[i−1]	[0, 1]
# [2..3]    1 + bits[i−2]	[1, 2]
# [4..7]    1 + bits[i−4]	[1, 2, 2, 3]
# [8..15]   1 + bits[i−8]	[1, 2, 2, 3, 2, 3, 3, 4]
# [16..31]  1 + bits[i−16]	[1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5]
# Notice:
# When you reach a new power of two (like 2, 4, 8...),
#  the bit count pattern repeats — but with an extra leading 1
#  in front of each binary number.

# Example: between 4 and 7
# At i = 4, binary = 100 — that’s a new power of two (2²).

# From 4 to 7:
# 4 (100)  = 1 + bits[4-4] = 1 + bits[0]
# 5 (101)  = 1 + bits[5-4] = 1 + bits[1]
# 6 (110)  = 1 + bits[6-4] = 1 + bits[2]
# 7 (111)  = 1 + bits[7-4] = 1 + bits[3]

# → In each case, bits[i] = 1 + bits[i - 4].

def count_ones_offset(n):
    bits = [0] * (n + 1)
    offset = 1
    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        bits[i] = 1 + bits[i - offset]
    return bits

print(count_ones_offset(5))


# count ones for a given number
# called as Hamming Weight / Popcount
def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += n & 1  # Add 1 if last bit is 1
        n >>= 1         # Shift right
    return count

