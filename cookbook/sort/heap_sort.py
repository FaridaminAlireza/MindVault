def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

# Example usage:
numbers = [9, 5, 1, 4, 3]
insertion_sort(numbers)
print(numbers)  # Output: [1, 3, 4, 5, 9]




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


def heapify(arr, n, i):
    """
    Ensure the subtree rooted at index i is a max heap.
    :param arr: list of elements
    :param n: size of heap
    :param i: index of root
    """
    largest = i        # Initialize largest as root
    left = 2 * i + 1   # left child index
    right = 2 * i + 2  # right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)




# Counting sort does not use comparisons,
#  so it can be faster than comparison-based algorithms for small ranges.
# If you want to make it in-place and stable, it requires a bit 
# more work using cumulative counts.

def counting_sort(arr):
    if not arr:
        return []

    # Step 1: Find the maximum value
    max_val = max(arr)

    # Step 2: Create and populate count array
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1

    # Step 3: Reconstruct the sorted array
    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i] * freq)

    return sorted_arr

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)


# With Cumulative Sum
def counting_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Step 1: Count occurrences
    for num in arr:
        count[num] += 1

    # Step 2: Cumulative sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 3: Build output array (stable)
    output = [0] * len(arr)
    for num in reversed(arr):  # iterate in reverse for stability
        output[count[num] - 1] = num
        count[num] -= 1

    return output

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
#  This is stable (preserves relative order of duplicates). 
# Uses cumulative sum to directly find positions. 
# Time Complexity: O(n + k), Space Complexity: O(n + k).

# The cumulative sum converts “how many times a number occurs”
# into exact positions in the output array, which is why Counting Sort
# can sort elements efficiently and stably.





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


# Quick Sort
# Quick Sort is a divide-and-conquer, comparison-based sorting algorithm.
# How it works:
# Choose a pivot element from the array.
# Partition the array into two sub-arrays:
# Elements less than or equal to the pivot
# Elements greater than the pivot
# Recursively apply quick sort to the two sub-arrays.
# Combine the sorted sub-arrays with the pivot in the middle.

# Key Points
# Time Complexity:
# Average: O(n log n)
# Worst-case: O(n²) (occurs if pivot is always the smallest or largest element)


def quick_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]       # Elements less than pivot
    middle = [x for x in arr if x == pivot]   # Elements equal to pivot
    right = [x for x in arr if x > pivot]     # Elements greater than pivot

    # Recursively sort left and right, then combine
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

# In place version
def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
quick_sort_inplace(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

