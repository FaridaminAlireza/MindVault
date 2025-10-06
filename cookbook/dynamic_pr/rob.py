# Find the maximum amount of money you can steal from a row of houses,
# with the constraint that you cannot rob two adjacent houses.
# Each house has a certain amount of money stashed.

# Using list to hold the intermediate suboptimal results
def rob(nums):
    result = [0] * len(nums)
    result [0] = nums[0]
    if len(nums) > 1:
        result[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        result[i] = max(nums[i]+ result[i-2], nums[i-1])
    
    return result[-1]

nums = [2, 7, 9, 3, 1]
print(rob(nums))  # Output: 12



# Using dictionary to hold the intermediate suboptimal results
def rob(nums):
    memo = {}
    
    def dp(i):
        if i < 0:
            return 0
        if i in memo:
            return memo[i]
        memo[i] = max(dp(i-1), nums[i] + dp(i-2))
        return memo[i]
    
    return dp(len(nums)-1)

nums = [2, 7, 9, 3, 1]
print(rob(nums))  # Output: 12


# Top-Down (Memoization) – Recursion Tree
#  Suppose nums = [2, 7, 9, 3, 1]. The recursive calls look like this:
# rob(4)
# ├─ rob(3) → max money if we skip house 4
# │  ├─ rob(2)
# │  │  ├─ rob(1)
# │  │  │  ├─ rob(0)
# │  │  │  └─ rob(-1)
# │  │  └─ rob(0)
# │  └─ rob(1)
# └─ rob(2) → max money if we rob house 4
#    ├─ rob(1)
#    └─ rob(0)




