# Using tuple unpacking (Pythonic way)

a = 5
b = 10

# Swap
a, b = b, a

print(a, b)  # Output: 10 5


# Python evaluates the right-hand side first (b, a) → creates a temporary tuple (10, 5).
# Then it unpacks it into a and b.
# This is the most common and recommended way in Python.