import math
import random

cities = {
    'A': (0, 0),
    'B': (2, 6),
    'C': (5, 2),
    'D': (6, 6),
    'E': (8, 3)
}


def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def total_distance(route):
    dist = 0
    for i in range(len(route)):
        dist += distance(route[i], route[(i + 1) % len(route)])
    return dist

# Generate new route by swapping two cities
def neighbor(route):
    new_route = route[:]
    i, j = random.sample(range(len(route)), 2)
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route

def simulated_annealing(initial_route, T=1000, alpha=0.995, stopping_T=1e-8):
    current_route = initial_route
    best_route = list(current_route)
    current_distance = total_distance(current_route)
    best_distance = current_distance

    while T > stopping_T:
        new_route = neighbor(current_route)
        new_distance = total_distance(new_route)
        delta = new_distance - current_distance

        # Accept new solution if better or with probability e^(-delta/T)
        if delta < 0 or random.random() < math.exp(-delta / T):
            current_route = new_route
            current_distance = new_distance

        # Update best solution
        if current_distance < best_distance:
            best_route = list(current_route)
            best_distance = current_distance

        T *= alpha  # Cool down

    return best_route, best_distance


initial_route = list(cities.keys())
best_route, best_distance = simulated_annealing(initial_route)

print("Best route:", best_route)
print("Total distance:", best_distance)

# TSP is NP-hard, so exact polynomial-time algorithms do not exist
# (unless P=NP).
# Heuristics & metaheuristics like SA: gives polynomial time per iteration; 
# can handle hundreds or thousands of cities but only approximate
# the solution.

#Time complexity: O(iter × n²), depends on iterations and cooling schedule

# Early in Simulation Annealing: exploratory (not greedy)
# Late Simulation Annealing = almost greedy (accepts only improvements)
# So Simulation Annealing(SA) generalizes greedy search,
# but it is much more flexible and powerful for combinatorial optimization
# problems like TSP.



import numpy as np
import matplotlib.pyplot as plt

# Δ values (worse costs)
deltas = [1, 5, 10, 20]

# Temperature range
 # start from small T to avoid division by zero
T = np.linspace(0.01, 100, 1000) 

plt.figure(figsize=(8,5))

for delta in deltas:
    P = np.exp(-delta / T)
    plt.plot(T, P, label=f"Δ = {delta}")

plt.xlabel("Temperature T")
plt.ylabel("Acceptance Probability P = e^(-Δ/T)")
plt.title("Simulated Annealing Acceptance Probability vs Temperature")
plt.legend()
plt.grid(True)
plt.show()
