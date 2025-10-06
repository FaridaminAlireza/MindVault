# Given two strings:
# S1 of length n
# S2 of length m
# Find the longest substring that appears in both S1 and S2.

def LCS(str1, str2):
    dp = [[0] * (len(str2) + 1 )  for _ in range(1+len(str1))] 
    max_length = 0
    max_index = ()
    for row in range(len(str1)):
        for col in range(len(str2)):
            if str1[row] == str2[col]:
                dp[row][col] = 1 +  dp[row-1][col-1]

                if dp[row][col] > max_length:
                    max_length =  dp[row][col]
                    max_index = (row,col)

    return max_length, str1[max_index[0] - max_length +1: max_index[0]+1]

s1 = "abcdf"
s2 = "zbcdf"
print(LCS(s1,s2))


# Time complexity: O(n × m)
# We must compare every pair of positions from s1 and s2.

# Space complexity: O(min(n, m))
# Only two rows are stored at a time 
# (current + previous), instead of the full DP table.

# Approach:
# Track the length of the longest common substring ending at s1[i] and s2[j]:
# If characters match, extend from the stored result at (i-1,j-1) + 1.
# If characters don’t match, reset to 0 (because substring must be contiguous).
# Keep a global maximum and remember the ending index in s1 (or s2).
# After filling the table, slice the substring from s1 using
#  the ending index and maximum length.



