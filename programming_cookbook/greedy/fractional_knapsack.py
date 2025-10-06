# Problem:
# Items have weight and value. Knapsack has capacity W.
# Goal: Maximize total value; you can take fractions of items.

# Greedy strategy:
# Compute value/weight ratio for each item.
# Sort items by ratio in descending order.
# Take items in order:
# If the whole item fits → take it.
# Else → take the fraction to fill remaining capacity.


def fractional_knapsack(weights, values, capacity):
    n = len(values)
    items = [(values[i]/weights[i], weights[i], values[i]) for i in range(n)]
    items.sort(reverse=True)
    total_value = 0
    for ratio, w, v in items:
        if capacity >= w:
            capacity -= w
            total_value += v
        else:
            total_value += ratio * capacity
            capacity = 0
            break
    return total_value

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_val = fractional_knapsack(weights, values, capacity)
print("Maximum value (fractional knapsack):", max_val)

# time complexity: O(n)
# space complexity: O(n)
