def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print(numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]


# Number of comparisons: n-1 + n-2 + ... + 1 = n(n-1)/2 ≈ O(n^2)
# Number of swaps: Also up to O(n^2)

# Time Complexity: O(n^2)
# Space Complexity: O(1)