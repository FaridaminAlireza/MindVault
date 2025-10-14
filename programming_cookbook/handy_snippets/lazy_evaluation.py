# Lazy evaluation is a programming concept where an expression is not evaluated
# until its value is actually needed. This helps improve performance by avoiding
# unnecessary computations and saving memory — especially when dealing with large
# datasets or potentially infinite sequences.

# In Python, lazy evaluation is often seen in:
# Generators
# Iterators
# Some built-in functions 
# (like map(), filter(), range() in Python 3)


# Eager evaluation (normal behavior)
data = [x * 2 for x in range(5)]
print(data)

# Lazy evaluation
data = (x * 2 for x in range(5))
print(data)
# Output: <generator object <genexpr> at 0x...>
# No computation happens yet — values are produced only
# when needed, e.g., in a loop.


# Ex 
def squares(n):
    for i in range(n):
        print(f"Computing square of {i}")
        yield i * i  # Lazily yield one result at a time

gen = squares(5)
print("Generator created!")

print(next(gen))  # Computes only the first square
print(next(gen))  # Computes the next one
# Only one value is computed at a time — this is lazy evaluation.

# Ex
def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1

nums = natural_numbers()

# Print the first 5 natural numbers (the generator is infinite!)
for _ in range(5):
    print(next(nums))



#In Python 3, map() and filter() are lazy iterators:
nums = [1, 2, 3, 4, 5]
squares = map(lambda x: x*x, nums)

print(squares)        # <map object ...>
print(list(squares))  # Forces evaluation → [1, 4, 9, 16, 25]


# Real world example:
# Eager Evaluation (Memory Killer)
# Imagine this reads a huge file into memory all at once

with open("system.log", "r") as f:
    lines = f.readlines()  # loads the ENTIRE file into memory

error_lines = [line for line in lines if "ERROR" in line]
print("Number of errors:", len(error_lines))
# if the log file is 10GB, it could easily consume tens of gigabytes of RAM.
# If your system doesn’t have that much memory, it might crash or swap heavily.

# Lazy Evaluation (Memory Efficient)
def error_lines_from_log(filepath):
    with open(filepath, "r") as f:
        for line in f:  # 👈 iterates lazily, one line at a time
            if "ERROR" in line:
                yield line  # yield makes this function lazy

# Use the generator without ever loading all lines
count = sum(1 for _ in error_lines_from_log("system.log"))
print("Number of errors:", count)

# for line in f: reads one line at a time from the file.
# The generator yields each "ERROR" line on demand.
# Only one line is in memory at a time —
# constant memory usage, even for terabytes of data.

# The file is read sequentially, directly from disk.
# Only a tiny rolling window of memory is used.
# You can process massive files (GBs or TBs) 
# in constant RAM (e.g., <10 MB).


# Demonstration Example 
import psutil, os

# check how much RAM your current Python process is using
def memory_usage_mb():
    return psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024

print(f"Memory before: {memory_usage_mb():.2f} MB")

with open("huge_file.txt") as f:
    for i, line in enumerate(f):
        if i % 1_000_000 == 0:
            print(f"Line {i}, memory: {memory_usage_mb():.2f} MB")

print(f"Memory after: {memory_usage_mb():.2f} MB")


# once the lazy iterator moves to the next item, 
# the previous one’s memory is released and can be 
# reused by Python or the OS.
# That’s the core power of lazy evaluation:
# processing streams of data without ever needing
# to hold the whole dataset in memo