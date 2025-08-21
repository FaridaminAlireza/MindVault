
# Computes (a^b) % m efficiently
print(pow(7, 256, 13))  # Output: 9

def mod_exp(base, exp, mod):
    result = 1
    print('base',base)
    base = base % mod  # Reduce base initially
    print('base',base)

    counter = 0
    while exp > 0:
        counter +=1
        print('---------------\nindex:',counter)
        if exp % 2 == 1:  # If exponent is odd
            result = (result * base) % mod
            print('result',result)
        exp //= 2
        base = (base * base) % mod
        print('exp', exp)
        print('base', base)

    print('result',result)
    return result

# Example
# print(mod_exp(7, 256, 13))  # Output: 9

mod_exp(3, 1001, 7)



# We want to show:
# a^(2x) mod y = (a^x mod y) \* (a^x mod y) mod y

# ---

# Step 1: Expand the left side
# a^(2x) = (a^x) \* (a^x)

# So,
# a^(2x) mod y = (a^x \* a^x) mod y

# ---

# Step 2: Use the modular property
# For any numbers p, q:
# (p \* q) mod y = ((p mod y) \* (q mod y)) mod y

# ---

# Step 3: Apply it with p = a^x, q = a^x
# (a^x \* a^x) mod y
# \= ((a^x mod y) \* (a^x mod y)) mod y

# ---

# Therefore:
# a^(2x) mod y = (a^x mod y) \* (a^x mod y) mod y

# ---

# Example:
# Let a = 7, x = 4, y = 13

# Left side:
# 7^(8) mod 13 = 5764801 mod 13 = 9

# Right side:
# (7^4 mod 13) = 2401 mod 13 = 9
# (9 \* 9) mod 13 = 81 mod 13 = 9

# Both sides = 9 ✅

# ---

# Do you want me to also write a similar copy-paste proof for the **more general case**:
# a^(m+n) mod y = (a^m mod y) \* (a^n mod y) mod y ?
