# You are given a set of n items, each with:
# a weight w[i] and a value (or profit) v[i]
# A knapsack (or bag) that can carry at most W weight.
# Each item can either be taken or left — you cannot take fractions.
# (0/1 Knapsack Problem)
# You must choose a subset of these items to maximize the total value,
# without exceeding the knapsack’s weight capacity.


def knapsack_01(values, weights, W):
    dp = [[0] * (W+1) for _ in range(len(values))]

    for row in range(len(weights)):
        for col in range(1,W+1):
     
            choice_1 = dp[row-1][col]
            choice_2 = 0
            if weights[row] <= col:
                choice_2 = dp[row - 1][col - weights[row]] + values[row]
                
            dp[row][col] = max(choice_1, choice_2)


    return dp[-1][-1]

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
print("Maximum value in Knapsack =", knapsack_01(values, weights, W))


# DP solution identifies Overlapping Subproblems
# Subproblems repeat: "the best value using items [0...i] with capacity c"

#  State defintion: 
#  - Let: dp[i][w] = maximum value achievable with first i items and capacity w

# State Transition (Recurrence Relation):
#    - For item i (weight = wt[i], value = val[i]):
#      If we don’t take item i:
#         dp[i][w] = dp[i-1][w]
#      If we take item i (only if wt[i] <= w):
#         dp[i][w] = max(dp[i-1][w], val[i] + dp[i-1][w - wt[i]])
#      Otherwise:
#         dp[i][w] = dp[i-1][w]


# Base Cases:
# dp[0][w] = 0 for all w (if no items, max value = 0)
# dp[i][0] = 0 for all i (if capacity = 0, no value possible)

# Each row represents "considering one more item".
# Each column represents "increasing capacity".
# Each cell represents "best I can do at this stage".
# Final cell dp[n][W] gives the maximum achievable value.

# Brute Force solution: explore all subsets: O(2^n).
