# The idea:
# Track the minimum price seen so far (min_price).
# Track the maximum profit if you sold on each day (max_profit).
# This is actually a 1D DP problem,
# because each day depends only on previous information.

def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]  # minimum price seen so far
    max_profit = 0          # maximum profit so far

    for price in prices[1:]:
        # profit if sold today
        profit = price - min_price
        # update max profit
        max_profit = max(max_profit, profit)
        # update min price
        min_price = min(min_price, price)

    return max_profit

#  Time complexity: O(n)
#  Space complexity: O(1)

