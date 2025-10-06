# You are given 3 rods (or pegs) and n disks of different sizes.
# All disks start stacked on the first rod, largest at the bottom, smallest on top.

# Goal:
# Move all disks to the third rod (destination), following these rules:
# You can move only one disk at a time.
# You can only move the top disk of any rod.
# No larger disk may be placed on top of a smaller disk.


def tower_of_hanoi(n, S1,S2,S3):
    global stack_counter
    
    if n == 0:
        return 
    else:
        tower_of_hanoi(n-1, S1,S3,S2)
        x = S1.pop()
        S3.append(x)
        stack_counter +=1
        print('stack', stack_counter, S1, S2,S3)
        tower_of_hanoi(n-1, S2,S1,S3)
    
n = 4
S1 = [4,3,2,1]
S2 = []
S3 = []

stack_counter = 0
tower_of_hanoi(n, S1,S2,S3)

# Time Complexity: O(2^n)

# Space complexity: O(n), 
# it is determined by the maximum depth of the recursion stack.
# At any moment, the maximum number of active function calls
# (stack depth) is n.

# Recurrence relation:
# The recurrence relation for Tower of Hanoi is: T(n) = 2 * T(n - 1) + 1.
# where +1 represents the current function call itself.
# Solving this recurrence: T(n) = 2^n - 1, therefore the time Complexity of O(2^n).
# Each recursive call generates two more calls (except the base case), 
# forming a complete binary recursion tree with n levels. Hence, the number of
# operations (moves) grows exponentially with the number of disks.


# Number of Stack Calls:
# If we only count actual moves (disk transfers),
# the number of moves is: 2^n - 1

# If we count each call to the function (including those that hit the base case), 
# the total number of function calls C(n) follows:
#  C(n) = 2 * C(n - 1) + 1, with C(0) = 1, 
# Solving this recurrence gives: C(n) = 2^(n + 1) - 1
# So the total number of function calls (stack activations) = 2^(n + 1) - 1.


# By expanding (unrolling) the recurrence T(n) = 2 * T(n - 1) + 1 for different n values, 
# we notice emerging the pattern T(n) = 2^n - 1
# Recursive reasoning proof by mathematical induction 

# Base Case (n = 1):
#     - Only one disk: move it directly.
#     => Requires 1 move = 2^1 - 1

# Inductive Hypothesis:
#     Assume that for n - 1 disks,
#     the minimum number of moves is 2^(n - 1) - 1.

# Inductive Step:
#     For n disks:
#         - Move (n - 1) disks to auxiliary rod → 2^(n - 1) - 1 moves
#         - Move the largest disk → 1 move
#         - Move (n - 1) disks from auxiliary to destination → 2^(n - 1) - 1 moves

#     Total moves = (2^(n - 1) - 1) + 1 + (2^(n - 1) - 1)
#                 = 2 * 2^(n - 1) - 1
#                 = 2^n - 1


