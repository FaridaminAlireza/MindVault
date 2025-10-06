def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Time complexity: O(n log n)
# Divide step: splits array into two halves → O(1) work per split

#Merge step: merging two sorted halves → O(n) per level
#Number of levels: log₂(n) (keep halving until size 1)
# Total time = O(n)×O(logn)=O(nlogn)

# Space Complexity:
# Recursive stack+temporary arrays=O(logn)+O(n)=O(n) (the dominant term is O(n))
