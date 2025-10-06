def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)



#  Recursive with memoization
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n == 0: return 0
    if n == 1: return 1
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

#Time complexity: O(n)
#Space complexity: O(n) for memoization + recursion stack



# Iterative (bottom-up)
def fib_iter(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b
# Time complexity: O(n)
# Space complexity: O(1)


############################################

# Recursive Fibonacci Complexity

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


# Each call to fib(n) calls fib(n-1) and fib(n-2).

# This forms a binary recursion tree.

# Let’s count calls:

# fib(n)
# ├─ fib(n-1)
# │  ├─ fib(n-2)
# │  └─ ...
# └─ fib(n-2)
#    ├─ ...

# fib(4)
#  ├── fib(3)
#  │    ├── fib(2)
#  │    │    ├── fib(1)
#  │    │    └── fib(0)
#  │    └── fib(1)
#  └── fib(2)
#       ├── fib(1)
#       └── fib(0)


# Number of calls grows roughly like 2^n.

# So the time complexity is O(2^n), not O(n).

# Space complexity is O(n) due to the recursion stack.
# Since the deepest recursion stack can be n times at any time.
# In the above ex, fib(4) → fib(3) → fib(2) → fib(1)
# total space = O(n * s). Since s is constant per call 
# (stores local vars + return address), we usually drop it and just say O(n).
