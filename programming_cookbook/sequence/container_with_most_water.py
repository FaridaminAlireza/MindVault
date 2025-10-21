# You are given an array of non-negative integers height[],
# where each element represents the height of a vertical line 
# drawn at that index. You want to find two lines that together with 
# the x-axis form a container, such that the container holds the maximum water.

# Formally: max area = max of (min(height[i],height[j])⋅(j−i)) for index i<j
# min(height[i], height[j]) → because water cannot exceed the shorter line.
# (j - i) → the width of the container.

# First approach: brute force 
# time complexity O(n^2) 
# Space complexity O(1)

# Second approach: Using two pointers:
# Steps:
    # Start with two pointers, left at index 0, right at last index.
    # Compute area with height[left] and height[right].
    # Move the pointer pointing to the shorter line, 
    # because moving the taller line cannot increase the area.
    # Repeat until left < right.


def max_area(height):

    ptr_1_idx = 0
    ptr_2_idx = len(height) - 1

    max_capacity = 0
    while ptr_1_idx < ptr_2_idx:
        capacity = (min(height[ptr_1_idx], height[ptr_2_idx])
                     * (ptr_2_idx - ptr_1_idx))
        max_capacity = max(capacity, max_capacity)
        if height[ptr_1_idx] <= height[ptr_2_idx]:
            ptr_1_idx += 1
        else:
            ptr_2_idx -= 1
        
    return max_capacity


# In every iteration one of the two cases can occur:

# Case 1: The new height is taller than the previous shorter line
# This is good, because now the limiting height (min(left, right)) might increase.
# Even though the width is smaller, the taller height can compensate
# or even increase the area.

# Case 2: The new height is shorter than the previous shorter line
# The area will definitely be smaller than the previous area.
# That’s okay; we just continue moving pointers to explore all possibilities.

# Time complexity O(n)
# Space complexity O(1)
