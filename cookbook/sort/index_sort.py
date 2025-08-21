# Algorithm (Steps)
#  Find the maximum value max_val in the input array.
# Create an index array of size max_val + 1, initialized with 0.
#  For each element in the input array, increment the value 
#  at index equal to the element.
#  Reconstruct the sorted array by reading the index array from start to end.

def index_sort(arr):
    if not arr:
        return []

    # Step 1: Find the maximum value
    max_val = max(arr)

    # Step 2: Create the index array
    index_arr = [0] * (max_val + 1)

    # Step 3: Count occurrences
    for num in arr:
        index_arr[num] += 1

    # Step 4: Reconstruct the sorted array
    sorted_arr = []
    for i, count in enumerate(index_arr):
        sorted_arr.extend([i] * count)

    return sorted_arr

# Example usage
arr = [4, 2, 2, 3, 1]
sorted_arr = index_sort(arr)
print("Sorted array:", sorted_arr)

# Time Complexity: O(n + k), where n = array size, k = maximum value.
# Space Complexity: O(k) (index array).
# Stable? Not stable in this simple version; 
# stability requires using cumulative sums, like in counting sort.

#Definition of Stability
# A sorting algorithm is stable if it preserves the relative order
#  of elements with equal values.

#In other words:
#If two elements are equal in the input,
#  they will appear in the same order in the sorted output as
#  they were in the original array.

# In short:
# Stable: equal elements keep their original order.
# Unstable: equal elements may be reordered.
