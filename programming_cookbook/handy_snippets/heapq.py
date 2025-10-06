
from collections import Counter
import heapq

nums = [10, 4, 7, 20, 15, 3]
k = 3

# Top-K largest
largest = heapq.nlargest(k, nums)
print(largest)  # [20, 15, 10]

# Top-K smallest
smallest = heapq.nsmallest(k, nums)
print(smallest)  # [3, 4, 7]


nums = [10, 4, 7, 20, 15, 3]
k = 3
# Top-K largest
largest = sorted(nums, reverse=True)[:k]
print(largest)  # [20, 15, 10]

# Top-K smallest
smallest = sorted(nums)[:k]
print(smallest)  # [3, 4, 7]


def top_k_frequent_items(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

print(top_k_frequent_items([1,1,1,2,2,3], 2))  # [1, 2]

