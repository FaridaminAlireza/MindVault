# Approach: 
# Index Sort is a technique where instead of moving the actual 
# elements of an array, we create an index array that stores
# the positions of the elements in sorted order.

# Algorithm Steps:
# Find the maximum value max_val in the input array.
# Create an index array of size max_val + 1, initialized with 0.
# For each element in the input array, increment the value 
# at index equal to the element.
# Reconstruct the sorted array by reading the index array from start to end.

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

# Suitable for Arrays where max(arr) is not huge compared to n
# Not suitable for Arrays with very large max(arr). For ex, If max_val is
#  much larger than n (e.g., n=10^3 and max_val=10^9), this algorithm
#  becomes inefficient in both time and memory

# Not stable (stability requires using cumulative sums, like in counting sort)
