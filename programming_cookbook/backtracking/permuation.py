def perumation_with_result(nums):
    result = []
    counter = [0]
    def permuation(nums,path):
      
        counter[0] = counter[0] + 1
        if  len(nums)==1:
            # print('path', path + nums)
            result.append(path + nums)
            return 

        for i in range(0,len(nums)):
            x = nums[:]
            permuation(x, path +  [x.pop(i)])

    permuation(nums,[])
    print(counter)
    return result
        
for i in perumation_with_result([1,2,3]):
    print(i)

# Start: []
#  ├── Pick 1 → [1]
#  │     ├── Pick 2 → [1, 2]
#  │     │     ├── Pick 3 → [1, 2, 3] 
#  │     │     └── Backtrack
#  │     └── Pick 3 → [1, 3]
#  │           ├── Pick 2 → [1, 3, 2] 
#  │           └── Backtrack
#  │
#  ├── Pick 2 → [2]
#  │     ├── Pick 1 → [2, 1]
#  │     │     ├── Pick 3 → [2, 1, 3] 
#  │     │     └── Backtrack
#  │     └── Pick 3 → [2, 3]
#  │           ├── Pick 1 → [2, 3, 1] 
#  │           └── Backtrack
#  │
#  └── Pick 3 → [3]
#        ├── Pick 1 → [3, 1]
#        │     ├── Pick 2 → [3, 1, 2] 
#        │     └── Backtrack
#        └── Pick 2 → [3, 2]
#              ├── Pick 1 → [3, 2, 1]
#              └── Backtrack


# path contains only primitive values (like integers, strings).
# Primitives are immutable in Python — once created, they don’t change.
# So shallow copy (path[:]) is enough, because the integers themselves
#  can’t be modified in place.

# number of calss formula: calls(n)=1+ n⋅calls(n−1)
# Let calls(n) be the total number of times permute is called when
# the subarray length is n.

# At each call:
#   1. Count 1 for the current call.
#   2. Loop n times (from start to len(nums)-1) making
#  a recursive call each time with a subarray of length n-1.

# So the recurrence is: calls(n) = 1 + n * calls(n-1)
# Base case: calls(0) = 1 or 
# call(0) =0 if call is returned when lenght of subarray is 1.

# Computing examples
# n = 1
# calls(1) = 1 + 1 * calls(0) = 1
# n = 2
# calls(2) = 1 + 2 * calls(1) = 2


# Expanding recursively
# For large n, the +1 in the recurrence is negligible,
# so we can approximate: calls(n) ≈ n * calls(n-1)
# Expanding recursively:
# calls(n) ≈ n * (n-1) * (n-2) * ... * 1 * calls(0) = n!
# This shows why the number of calls grows roughly factorially.


# Time Complexity
# Each call does O(1) work besides recursion.
# Total calls ≈ n! → Total time complexity: O(n * n!)

# Space Complexity
# Recursion stack depth = n → O(n)
# Output storage (if storing all permutations) = n! 
# permutations of length n → O(n * n!)

# Time Complexity: O(n * n!)
# Recursion stack: O(n)
# Storing permutations: O(n * n!)




