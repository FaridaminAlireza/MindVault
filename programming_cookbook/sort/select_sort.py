# Selection sort is a simple comparison-based sorting algorithm.
# It works by repeatedly selecting the smallest 
# (or largest, depending on the order you want) element from the 
# unsorted portion of the list and moving it to its correct position
# in the sorted portion.

# step-by-step explanation:
# 1. Start with the whole list as unsorted.
# 2. Find the smallest element in the unsorted part.
# 3. Swap that smallest element with the first element of the unsorted part.
# 4. Move the boundary between the sorted and unsorted portions one element forward.
# Repeat steps 2–4 until the entire list is sorted.


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current position i is the minimum
        min_index = i
        # Find the actual minimum in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)


# Time Complexity: O(n²) in all cases (best, average, worst)
# Space Complexity: O(1) (in-place sorting)
# Stable: No (unless implemented carefully)
# Usage: Mostly educational; 
# rarely used for large datasets because of inefficiency