def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    used = []
    for coin in coins:
        if amount >= coin:
            num = amount // coin
            count += num
            used.append((coin, num))
            amount -= coin * num
    if amount != 0:
        return -1, []
    return count, used

# Example usage
coins = [25, 10, 5, 1]
amount = 63
count, used_coins = greedy_coin_change(coins, amount)
print("Minimum coins:", count)
print("Coins used:", used_coins)

# Time complexity: O(n)
# Space complexity O(n)

