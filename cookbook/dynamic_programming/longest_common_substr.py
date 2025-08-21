def longest_common_substring(s1: str, s2: str) -> str:
    n, m = len(s1), len(s2)
    
    # DP table (n+1) x (m+1), initialized with 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    max_len = 0      # length of longest substring found
    end_idx = 0      # end index of substring in s1

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_idx = i
            else:
                dp[i][j] = 0  # mismatch → reset
     
    # Extract substring from s1
    return s1[end_idx - max_len:end_idx]


# Example usage:
s1 = "abcdf"
s2 = "zbcdf"
print(longest_common_substring(s1, s2))  # Output: "bcdf"

# Time complexity: O(n × m)
# We must compare every pair of positions from s1 and s2.

# Space complexity: O(min(n, m))
# Only two rows are stored at a time (current + previous), instead of the full DP table.

# We track the length of the longest common substring ending at s1[i-1] and s2[j-1].
# If characters match, extend from prev[j-1] + 1.
# If characters don’t match, reset to 0 (because substring must be contiguous).
# Keep a global maximum and remember the ending index in s1.
# After filling, slice the substring from s1[end_idx - max_len : end_idx].

