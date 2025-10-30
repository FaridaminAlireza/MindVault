# Monte Carlo simulation is a computational technique that uses
# randomness to solve problems that might be deterministic in principle.

# Key ideas:
# Use random sampling to estimate quantities.
# Repeat experiments many times to get an average or distribution.
# Useful for problems that are hard to solve analytically.

# Example applications:
    # Estimating areas or integrals
    # Financial modeling (option pricing)
    # Risk analysis
    # Physics simulations


# The Basic Concept:
# Define a domain of possible inputs.
# Generate random inputs from that domain.
# Perform a computation for each input.
# Aggregate results to estimate the desired quantity.


# Classic Example: Estimating the Area of a Circle

# Imagine a circle of radius r=1 inside a square of side 2.
# Area of square = 2×2=4
# Area of circle = = 2πr = π

# Monte Carlo idea:
# Randomly throw points in the square.
# Count how many fall inside the circle.
# The fraction inside × area of square ≈ area of circle.


import random

def monte_carlo_circle(num_samples):
    inside_circle = 0
    
    for _ in range(num_samples):
        x = random.uniform(-1, 1)  # random x between -1 and 1
        y = random.uniform(-1, 1)  # random y between -1 and 1
        
        if x**2 + y**2 <= 1:  # check if point is inside the circle
            inside_circle += 1
    
    area_square = 4  # side=2, area=2*2
    estimated_area = (inside_circle / num_samples) * area_square
    return estimated_area

# Run simulation
num_samples = 100000
area_estimate = monte_carlo_circle(num_samples)
print(f"Estimated area of the circle: {area_estimate}")


import numpy as np

def monte_carlo_circle_vectorized(num_samples):
    # Generate random points for x and y
    x = np.random.uniform(-1, 1, num_samples)
    y = np.random.uniform(-1, 1, num_samples)
    
    # Check which points are inside the circle
    inside_circle = x**2 + y**2 <= 1
    
    # Estimate area
    area_square = 4  # side=2, so area=2*2
    estimated_area = np.sum(inside_circle) / num_samples * area_square
    return estimated_area

# Run simulation
num_samples = 1_000_000  # 1 million points
area_estimate = monte_carlo_circle_vectorized(num_samples)
print(f"Estimated area of the circle: {area_estimate}")
