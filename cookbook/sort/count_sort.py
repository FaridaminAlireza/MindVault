# Uses Cumulative Sum
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
        # count[i] tells us the last index where
        #  i should go in the sorted array.

    # Step 3: Build output array (stable)
    output = [0] * len(arr)
    # Iterate through the input array from right to left (to maintain stability)
    # and place elements in the correct positions using the count array.
    for num in reversed(arr): 

        output[count[num] - 1] = num
        count[num] -= 1

    return output

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)

#  This is stable (preserves relative order of duplicates). 
# Uses cumulative sum to directly find positions. 
# Time Complexity: O(n + k)
# Space Complexity: O(n + k)

# The cumulative sum converts “how many times a number occurs”
# into exact positions in the output array, which is why Counting Sort
# can sort elements efficiently and stably.