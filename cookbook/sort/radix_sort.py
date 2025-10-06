# Radix sort (also called bucket sort) is a non-comparison-based sorting algorithm that
# sorts numbers (or strings) digit by digit (or character by character),
# starting either from the least significant digit (LSD) or 
# the most significant digit (MSD). It’s especially efficient when sorting
# large lists of numbers with the same number of digits.

# It works best for integers or strings of equal length.
# Unlike QuickSort or MergeSort, it doesn’t compare elements directly;
# it groups them by digits.

# Approach (LSD version):

# 1. Find the maximum number in the list to determine the number of digits, d.
# 2. Starting from the least significant digit (rightmost), 
# sort the numbers based on that digit using a stable sort (usually Counting Sort).
# 3. Move to the next significant digit (one place to the left) and repeat step 2.
# Continue until the most significant digit is sorted.

# In counting sort,
# n = number of elements in the array
# k = range of possible key values
# So, if you’re sorting integers where the keys (digits or values) can take k possible values,
# then the algorithm must maintain a count (or bucket) array of size k.
# For base 10 numbers k = 10

# | Base | Digits (possible values) | `k` value | Typical usage                  |
# | ---- | ------------------------ | --------- | ------------------------------ |
# | 10   | 0–9                      | 10        | Standard decimal integers      |
# | 2    | 0–1                      | 2         | Binary sorting                 |
# | 16   | 0–15 (hexadecimal)       | 16        | Faster radix sort on computers |
# | 256  | 0–255 (bytes)            | 256       | Efficient for strings/bytes    |




def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0–9

    # Count occurrences
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count[i] to contain position info
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (stable)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy output to original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find maximum number to know number of digits
    max_num = max(arr)

    exp = 1  # start with least significant digit
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)  # Output: [2, 24, 45, 66, 75, 90, 170, 802]


# Time Complexity O(n . k)
# Space Complexity O(n . k)


# Radix Sort (not stable version)

def counting_sort_simple(arr, exp):
    # Create 10 buckets for digits 0–9
    buckets = [[] for _ in range(10)]

    # Distribute numbers into buckets based on the current digit
    for num in arr:
        digit = (num // exp) % 10
        buckets[digit].append(num)

    # Collect numbers back into the array
    result = []
    for b in buckets:
        result.extend(b)

    return result


def radix_sort_simple(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        arr = counting_sort_simple(arr, exp)
        exp *= 10
    return arr


# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort_simple(arr)
print(sorted_arr)


# Time Complexity O(n . k) per pass O(d.(n . k))  (here k=10 → O(n))
# Space Complexity O(n . k)

