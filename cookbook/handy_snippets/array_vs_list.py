import array

# ---- Python Array
# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

print(arr)           # array('i', [1, 2, 3, 4, 5])
print(arr[0])        # 1

arr.append(6)
print(arr)           # array('i', [1, 2, 3, 4, 5, 6])


# Pros
# More memory-efficient than lists for large homogeneous data
# Enforces type consistency (via type code like 'i' for int, 'f' for float)

# Cons:
# Limited operations compared to list
# No element-wise math (unlike NumPy)

# ---- Python List
# List can hold mixed data types
lst = [1, 3.5, "hello", True]

print(lst)           # [1, 3.5, 'hello', True]
print(lst[0])        # 1
lst.append(42)
print(lst)           # [1, 3.5, 'hello', True, 42]


# Pros:
# Flexible (can hold any type)
# Built-in and easy to use

# Cons:
# Less memory-efficient for large numeric data
# Arithmetic operations require loops


# ---- Python Numpy Array

import numpy as np

# Create a NumPy array
arr_np = np.array([1, 2, 3, 4, 5])
print(arr_np)            # [1 2 3 4 5]

# Vectorized math operations
print(arr_np * 2)        # [ 2  4  6  8 10]
print(arr_np + 10)       # [11 12 13 14 15]

# Pros:
# Fast and efficient for numerical data
# Supports advanced operations (matrix multiplication, broadcasting, etc.)
# Widely used in data science and machine learning

# Cons:
# Requires numpy library
# Fixed data type