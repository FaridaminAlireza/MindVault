# You are given an integer array nums that was originally sorted in ascending order,
#  but then rotated at some pivot index k (0 ≤ k < nums.length).
# [nums[k], nums[k+1], ..., nums[0], nums[1], ..., nums[k-1]]
# You are also given an integer target — and you must return the index of target
#  in nums if it exists, otherwise return -1.

#Example 
# Input: nums = [4,5,6,7,0,1,2], target = 0   Output: 4
# Input: nums = [4,5,6,7,0,1,2], target = 3  Output: -1


# Desired time complexity: O(log n)


#Intuition: Since the array is sorted but rotated, at least one half is still sorted.
# We can use a modified binary search to exploit this property.

def binary_search(nums, start_indx, end_indx, target):
  
    mid_indx = (start_indx + end_indx) //2 
    
    if start_indx > end_indx:
        return -1
    
    if target == nums[mid_indx]:
        return mid_indx
    
    elif target < nums[mid_indx] :
        return binary_search(nums, start_indx, mid_indx -1, target)
    else:
        return binary_search(nums, mid_indx+1, end_indx, target)


def search_sorted_arr(nums, start_indx, end_indx, target):

    if start_indx > end_indx:
        return -1
 

    mid_indx = (start_indx + end_indx) // 2

    if nums[mid_indx] == target:
        return mid_indx

      # The first half is sorted
    if nums[start_indx] <= nums[mid_indx]:
        if nums[start_indx] <= target <= nums[mid_indx]:
            return binary_search(nums, start_indx, mid_indx, target)
        else:
            # search in the second half, which includes the rotation
            return search_sorted_arr(nums, mid_indx+1, end_indx, target)
    
     # The second half is sorted
    
    elif (mid_indx+1 < len(nums)) and nums[mid_indx+1] <=  nums[end_indx]:
        if nums[mid_indx+1] <= target <= nums[end_indx]:
            return binary_search(nums, mid_indx+1, end_indx, target)
        else:
            # search in the first half, which includes the rotation
            return search_sorted_arr(nums, start_indx, mid_indx -1, target)
    
    return -1

# Time complexity O(log n)
# Space complexity O(lon n) (the maximum depth of recursive stack)


nums = [3,4,5,6,7,0,1,2]
print(search_sorted_arr(nums,0, len(nums)-1, 0)) #Output: 5
nums = [4,5,6,7,0,1,2]
print(search_sorted_arr(nums,0, len(nums)-1, 0)) # Output: 4
print(search_sorted_arr(nums,0, len(nums)-1, 3)) # Output: -1

nums = [4,5,6,7,0,1,2]
print(search_sorted_arr(nums, 0, len(nums)-1, 0))  # Output: 4
print(search_sorted_arr(nums, 0, len(nums)-1, 3))  # Output: -1
print(search_sorted_arr([6,7,8,1,2,3,4,5], 0, 7, 3))  # Output: 5
print(search_sorted_arr([1], 0, 0, 1))  # 0

# The verbose version of the four conditons in the implementation:
# if  nums[start_indx] <= nums[mid_indx] and nums[start_indx] <= target <= nums[mid_indx]:
#     # The first half is sorted and target in the interval
#     return binary_search(nums, start_indx, mid_indx, target)
    
# elif nums[mid_indx+1] <=  nums[end_indx] and nums[mid_indx+1] <= target <= nums[end_indx]:
#     # The second half is sorted and target in the interval
#     return binary_search(nums, mid_indx+1, end_indx, target)

# elif nums[start_indx] > nums[mid_indx]:
#     # The first half include the rotation,
#     return search_sorted_arr(nums, start_indx, mid_indx -1, target)

# elif nums[mid_indx+1] >  nums[end_indx]:
#      # The second half include the rotation,
#     return search_sorted_arr(nums, mid_indx+1, end_indx, target)

