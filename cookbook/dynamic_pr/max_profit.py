#You’re given an array prices[] where prices[i] is the price of a stock on day i.
# You must decide when to buy and sell to achieve the maximum profit

# The idea:
# Track the minimum price seen so far (min_price).
# Track the maximum profit if you sold on each day (max_profit).
# This is actually a 1D DP problem,
# because each day depends only on previous information.

def max_profit_v1(prices):
    if not prices:
        return 0

    min_price = prices[0]  
    max_profit = 0         

    for price in prices[1:]:

        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)

    return max_profit

#  Time complexity: O(n)
#  Space complexity: O(1)


def max_profit_v2(nums):

    max_ls = [nums[0]]
    min_ls = [nums[0]]
    diff = [0]
    for i in range(1, len(nums)):
        for j in range(0, len(max_ls)):
            if nums[i] > max_ls[j]:
                max_ls[j] = nums[i]
                diff[j] = max_ls[j] - min_ls[j]
            if nums[i] < min(min_ls):
                max_ls.append(nums[i])
                min_ls.append(nums[i])
                diff.append(0)

    return max(diff)


#  Time complexity: O(n^2)
#  Space complexity: O(n)


prices = [7,1,5,3,6,4]
print(max_profit_v1(prices))
print(max_profit_v2(prices))

prices = [10,11,5,7,4,20,17]
print(max_profit_v1(prices))
print(max_profit_v2(prices))

