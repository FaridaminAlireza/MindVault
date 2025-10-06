def coinChange(coins, target):
    # Initialize DP array with infinity
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # 0 coins to make sum 0

    # Build up solutions for each sum
    for x in range(1, target + 1):
        for coin in coins:
            if x - coin >= 0:
                dp[x] = min(dp[x], 1 + dp[x - coin])

    return dp[target] if dp[target] != float('inf') else -1


# Example usage
coins = [1, 3, 4]
target = 6
print("Minimum coins required =", coinChange(coins, target))



# Coin Change Problem (Minimum Coins) - Visual Explanation
# Problem:
# - Given coins = [1,3,4] and target sum = 6
# - Find minimum number of coins to make the sum

# DP Formula:
# dp[x] = min(dp[x], 1 + dp[x - coin]) for all coins where coin <= x
# Base case: dp[0] = 0
# dp[x] represents minimum coins to make sum x

# Visual Step-by-Step:

# Initial DP array (target=6):
# dp = [0, ∞, ∞, ∞, ∞, ∞, ∞]

# Step 1: Compute dp[1]
# - Use coin 1: dp[1] = min(∞, 1 + dp[0]) = 1
# - Coins 3,4 too big
# DP now: [0, 1, ∞, ∞, ∞, ∞, ∞]

# Step 2: Compute dp[2]
# - Coin 1: dp[2] = min(∞, 1 + dp[1]) = 2
# - Coins 3,4 too big
# DP now: [0, 1, 2, ∞, ∞, ∞, ∞]

# Step 3: Compute dp[3]
# - Coin 1: dp[3] = min(∞, 1 + dp[2]) = 3
# - Coin 3: dp[3] = min(3, 1 + dp[0]) = 1 (better)
# - Coin 4 too big
# DP now: [0, 1, 2, 1, ∞, ∞, ∞]

# Step 4: Compute dp[4]
# - Coin 1: dp[4] = 1 + dp[3] = 2
# - Coin 3: dp[4] = 1 + dp[1] = 2
# - Coin 4: dp[4] = 1 + dp[0] = 1 (best)
# DP now: [0, 1, 2, 1, 1, ∞, ∞]

# Step 5: Compute dp[5]
# - Coin 1: 1 + dp[4] = 2 (best)
# - Coin 3: 1 + dp[2] = 3
# - Coin 4: 1 + dp[1] = 2
# DP now: [0, 1, 2, 1, 1, 2, ∞]

# Step 6: Compute dp[6]
# - Coin 1: 1 + dp[5] = 3
# - Coin 3: 1 + dp[3] = 2 (best)
# - Coin 4: 1 + dp[2] = 3
# DP now: [0, 1, 2, 1, 1, 2, 2]

# Final Answer:
# dp[6] = 2 (minimum coins to make 6)
