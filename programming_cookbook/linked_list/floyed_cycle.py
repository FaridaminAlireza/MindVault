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
#total steps for slow: t
#total steps fast: 2t-l 

# once slow reaches the loop:
#total steps in loop for slow: t-l
#total step in loop for fast: 2t-l 
# They meet when: (t-l) mod k = (2t-l) mod C
# let s = t-l, then: 
# L + s ≡ L + 2s (mod C)
# ⟹ s ≡ 0 (mod C)

# Which means after s steps that are a multiple of the cycle length C, 
# they align again — they meet!

