# Given an array height[] representing the height of bars,
# compute how much water can be trapped after raining.
# Each bar has width 1.
# Water is trapped between bars.

# Intuition for the solution:
# At any point: The amount of trapped water depends
#  on the smaller of the two maxes seen from left and right.

def trap_rain_water(height):
    arr_L = [0] * len(height)
    max_so_far = 0
    for i in range(1, len(height)):
        max_so_far = max(height[i-1], max_so_far)
        arr_L[i] = max_so_far

    arr_R = [0] * len(height)
    max_so_far = 0
    for i in range(len(height)-2, -1, -1):
        max_so_far = max(height[i+1], max_so_far)
        arr_R[i] = max_so_far

    total_water = 0 
    for i in range(len(height)):
        total_water +=  max(0, min(arr_L[i], arr_R[i]) - height[i])

    return total_water

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap_rain_water(heights))

# Time complexity: O(n)
# Space complexity: O(n)


