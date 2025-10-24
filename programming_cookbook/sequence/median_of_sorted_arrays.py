# Given two sorted arrays nums1 and nums2 of sizes m and n,
#  find the median of the combined sorted array without merging them directly.
#  The overall run time complexity should be O(log(min(m, n))).

import math


def get_median(arr_1, arr_2):

    combined_length = (len(arr_1) + len(arr_2))
    if combined_length == 0:
        return None
 
    median_index = []
    if (combined_length // 2) * 2  == combined_length:
        median_index = [ ((combined_length // 2) -1),
                         (combined_length // 2) ]       
    else:      
        median_index = [ ((combined_length + 1) // 2)  - 1]


    if not arr_1:
        median = sum([arr_2[i] for i in median_index]) / len(median_index)
        return median
    elif not arr_2:
        median = sum([arr_1[i] for i in median_index]) / len(median_index)
        return median


    indx_1 = indx_2 = merge_position = 0
    median_values = []
    
    # while indx_1 + indx_2 <= median_index[-1]:
    while merge_position <= median_index[-1]:
        
        val = None 
        if indx_1 == len(arr_1):
            val = arr_2[indx_2]
            indx_2 += 1  
        
        elif indx_2 == len(arr_2):
            val = arr_1[indx_1]
            indx_1 += 1    

        elif arr_1[indx_1] < arr_2[indx_2]:
            val = arr_1[indx_1]
            indx_1 += 1
        else:
            val = arr_2[indx_2]
            indx_2 +=1

        if merge_position in median_index:
            median_values.append(val)
        
        merge_position += 1

    median =  sum(median_values) / len(median_values)

    return median

# Time compleixty O(n+m)
# Space complexity O(n+m) if we store half of the combined array

# Space complexity O(1) if we store only the required median values.



nums1 = [1, 3]
nums2 = [2]
print(get_median(nums1, nums2)) # outputs 2

nums1 = [1, 2]
nums2 = [3, 4]
print(get_median(nums1, nums2)) # outputs 2.5


nums1 = [1, 3, 5, 7]
nums2 = [2, 4]
print(get_median(nums1, nums2)) # outputs 3.5


nums1 = [1]
nums2 = [2]
print(get_median(nums1, nums2)) # outputs 1.5


nums1 = [1]
nums2 = []
print(get_median(nums1, nums2)) # outputs 1


print(get_median([1, 3], [2]))          # 2.0
print(get_median([1, 2], [3, 4]))       # 2.5
print(get_median([1, 3, 5, 7], [2, 4])) # 3.5
print(get_median([], [5, 10, 15]))      # 10.0
print(get_median([1], []))              # 1.0
print(get_median([], []))               # None