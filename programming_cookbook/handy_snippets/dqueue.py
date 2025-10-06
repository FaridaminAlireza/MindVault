from collections import deque

dq = deque()
dq.append(1)      # add to right
dq.appendleft(0)  # add to left
print(dq.pop())   # remove from right -> 1
print(dq.popleft())  # remove from left -> 0

# collections.deque

# Great for single-threaded queues, stacks, sliding windows.
# Very fast → implemented in C, optimized for appending and popping from both ends.
# Not thread-safe by default (though append/pop operations are atomic).
