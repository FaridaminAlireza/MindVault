# Problem:
# Given activities with start and end times,
# select maximum number of non-overlapping activities.
# Greedy strategy:
# Sort activities by finish time.
# Select first activity (earliest finish).
# For each next activity, select it if its start time ≥ finish time of
# last selected.

def activity_selection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    selected = [activities[0]]
    last_finish = activities[0][1]
    for s, f in activities[1:]:
        if s >= last_finish:
            selected.append((s,f))
            last_finish = f
    return selected

# Example usage
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
selected_activities = activity_selection(start, finish)
print("Selected activities:", selected_activities)

