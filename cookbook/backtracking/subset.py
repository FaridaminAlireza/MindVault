def subsets(nums):
    result = []
    def backtrack(index=0, path=[]):
        if index == len(nums):
            result.append(path[:])
            return
        backtrack(index+1, path)
        path.append(nums[index])
        backtrack(index+1, path)
        path.pop()

    backtrack()
    return result


# Number of subsets: A set with n elements has 2^n subsets.
# * Any algorithm that generates all subsets must produce 2^n outputs.
# * Each element has 2 choices: include or exclude.
# * Leads to 2^n recursive calls.
# * Each step doubles the number of subsets → final number = 2^n.

# Time Complexity
# * Recursive/backtracking:
#   * Number of recursive calls = 2^n
#   * Each call may copy a subset of size up to n → O(n) per call
# Time Complexity: O(n * 2^n)


# Space Complexity
# * Recursion stack: maximum depth = n → O(n)
# * Output storage: total subsets = 2^n, each of size up to n → O(n * 2^n)

# Summary
# Time Complexity: O(n * 2^n)
# Recursion stack: O(n)
# Storing all subsets: O(n * 2^n)


