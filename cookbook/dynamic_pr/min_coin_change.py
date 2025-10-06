# Coin Change Problem (Minimum Coins)
# Problem:
# - Given coins = [1,3,4] and target sum = 6
# - Find minimum number of coins to make the sum

# Solution:
# dp[x] = min(dp[x], 1 + dp[x - coin]) for all coins where coin <= x
# Base case: dp[0] = 0
# dp[x] represents minimum coins to make sum x

import math
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


coins = [1, 3, 4]
target = 6
print("Minimum coins required =", coinChange(coins, target))


# Visual Step-by-Step example for
# # coins = [1, 3, 4]
# target = 6

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


# Solution2, requires sorting of coins
def coinChange(unsorted_coins, target):
    
    coins = sorted(unsorted_coins)
    min_coin_nums = math.inf
    result = [[math.inf] * (target+1) for i in range(len(coins)+1)]

    for i in range(len(coins)+1):
        result[i][0] = 0  # Base case: 0 coins needed to make value 0
    
    for coin_index in range(1,len(coins)+1):
        for val in range(1, target+1):
          
            coin_nums = val // coins[coin_index-1] 
            remaining_val = val - (coin_nums * coins[coin_index-1])    

            if coins[coin_index-1] > val:
                result[coin_index][val] = result[coin_index-1][val]

            else:

                result[coin_index][val] = min (
                result[coin_index-1][val], 
                result[coin_index-1][remaining_val] + coin_nums
                )

        min_coin_nums = min (result[coin_index][-1], min_coin_nums)
    
    return min_coin_nums if min_coin_nums != math.inf else -1

# That version is a hybrid DP + greedy algorithm —
# it assumes that for each coin, you can take the maximum number
# of that coin (val // coin) without harming the optimality.

# That assumption is only true for canonical coin systems 
# (like real currencies, e.g. [1, 2, 5, 10, 20, 50]) — 
# but it fails for arbitrary denominations.


print(coinChange([1, 3, 4], 6))
print(coinChange([4,3,1], 6))
print(coinChange([1,2,5,10], 11))
print(coinChange([1, 2, 5], 11))  # 3  (5 + 5 + 1)
print(coinChange([2], 3))         # -1 (impossible)
print(coinChange([1], 2))         # 2  (1 + 1)
print(coinChange([9, 6, 5, 1], 11))  # 2 (6 + 5)
print(coinChange(sorted([9, 6, 5, 1]), 11))  # 2 (6 + 5)
print(coinChange(sorted([1,3,4]), 6))  # 2
print(coinChange(sorted([1,7,10]), 14))  # 2
