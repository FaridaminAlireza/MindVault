
# Recursive version
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

#Time Complexity: O(log(n))
#Space Complexity: O(log(n))



#Iterative version
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # not found

#Time Complexity: O(log(n))
#Space Complexity: O(1)


# Example usage
nums = [1, 3, 5, 7, 9, 11]
print(binary_search(nums, 7))   # 3
print(binary_search(nums, 4))   # -1

