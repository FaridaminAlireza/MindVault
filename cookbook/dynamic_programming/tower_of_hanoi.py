def tower_of_hanoi(n, source, target, auxiliary):
    if n == 0:
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)

def tower_of_hanoi(n, A1, A2, A3):
    if n == 0:
        return
    tower_of_hanoi(n-1, A1, A3, A2)
    print(f"Move disk {n} from {A1} to {A2}")
    tower_of_hanoi(n-1, A3, A2, A1)

# Each time, you move n−1 disks aside,
# move the largest disk, then move the n−1 disks back on top.
# Total moves needed = 2ⁿ − 1.



