class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Time: O(N) — each pointer moves at most N steps before meeting or finishing.
# Space: O(1) — uses only two pointers (constant memory).


# Once both pointers are inside the cycle, 
# the fast pointer closes the gap by one node each time:
# If the cycle length = k, and the fast is d nodes ahead of slow,
# then after each step, the distance decreases by 1 (mod k).
# Eventually, d becomes 0, and they point to the same node.

# Proof
# Let: L = number of nodes before the cycle starts
# C = length of the cycle
# After t steps:
# Slow pointer is at position L + s (mod C)

# Fast pointer is at position L + 2s (mod C)

# They meet when:

# L + s ≡ L + 2s (mod C)
# ⟹ s ≡ 0 (mod C)

# Which means after s steps that are a multiple of the cycle length,
# they align again — they meet!

# Intuition
# Slow moves 1 step, fast moves 2 steps per iteration
# The distance between them decreases by 1 step each iteration modulo C
# After C steps, the distance wraps around to 0 → they meet



