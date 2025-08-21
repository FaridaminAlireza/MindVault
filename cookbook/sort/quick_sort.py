def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)



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

