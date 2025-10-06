def is_prime(n):
    if n < 2:
        return False  # numbers less than 2 are not prime
    for i in range(2, int(n ** 0.5) + 1):  # check divisors up to sqrt(n)
        if n % i == 0:
            return False  # divisible by i → not prime
    return True

# Test
print(is_prime(7))   # True
print(is_prime(10))  # False