def knapsack(values, weights, W):
    n = len(values)
    # DP table with (n+1) rows and (W+1) columns
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i-1] <= w:
                # Either take the item or leave it
                dp[i][w] = max(dp[i-1][w],
                               values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                # Can't take the item
                dp[i][w] = dp[i-1][w]

    return dp[n][W]


# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
print("Maximum value in Knapsack =", knapsack(values, weights, W))



# Dynamic Programming Mindset for 0/1 Knapsack Problem
# ----------------------------------------------------

# 1. Identify Overlapping Subproblems
#    - Brute force explores all subsets: O(2^n).
#    - Subproblems repeat: "What’s the best value using items [0...i] with capacity c?"

# 2. Define State
#    - Let:
#      dp[i][w] = maximum value achievable with first i items and capacity w

# 3. State Transition (Recurrence Relation)
#    - For item i (weight = wt[i], value = val[i]):

#      If we don’t take item i:
#         dp[i][w] = dp[i-1][w]

#      If we take item i (only if wt[i] <= w):
#         dp[i][w] = max(dp[i-1][w], val[i] + dp[i-1][w - wt[i]])

#      Otherwise:
#         dp[i][w] = dp[i-1][w]

# 4. Base Cases
#    - dp[0][w] = 0 for all w (if no items, max value = 0)
#    - dp[i][0] = 0 for all i (if capacity = 0, no value possible)

# 5. Answer
#    - After filling the table:
#      Answer = dp[n][W]

# Key Idea:
# - Each row represents "considering one more item".
# - Each column represents "increasing capacity".
# - Each cell represents "best I can do at this stage".
# - Final cell dp[n][W] gives the maximum achievable value.


