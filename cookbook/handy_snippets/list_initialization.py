# -> Basic list initialization

# Empty list
lst1 = []

# List with elements
lst2 = [1, 2, 3, 4]

# Using list() constructor
lst3 = list()           # empty
lst4 = list([1, 2, 3]) # from iterable


# -> Using repetition * to initialize lists

# Repeating elements
lst5 = [0] * 5  # [0, 0, 0, 0, 0]

# Repeating mutable elements
lst6 = [[]] * 3  # [[], [], []]

# Important Pitfall with * and mutable objects:
# The last example (lst6) creates references to the
#  same inner list, not independent lists:
lst6[0].append(1)
print(lst6)  # [[1], [1], [1]] <-- all sublists updated

# Correct way for independent sublists:
#  (List comprehension is safer for mutable repeated elements.)
lst7 = [[] for _ in range(3)]
lst7[0].append(1)
print(lst7)  # [[1], [], []]


# -> Using list() with iterables
#  list() constructor can convert any iterable to a list.
lst8 = list(range(5))  # [0, 1, 2, 3, 4]
lst9 = list("hello")   # ['h', 'e', 'l', 'l', 'o']


# Using unpacking * (Python 3.5+)
# You can unpack elements from other lists into a new list:
a = [1, 2]
b = [3, 4]
c = [*a, *b]  # [1, 2, 3, 4]
# Works with other iterables
s = "hi"
d = [*s, 1, 2]  # ['h', 'i', 1, 2]


# -> Avoid * with mutable default values in functions:
def add_item(item, lst=[]):  # BAD
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] <-- shared default list

# Safe alternative:
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# Why `add_item(item, lst=[])` Shares the Same List in Python

# 1. Default arguments are evaluated once. 
# The expression `lst=[]` is evaluated once, at the moment the function is defined.
# That empty list is then stored as the default value inside the function object itself.

# You can check this directly:
#     print(add_item.__defaults__)
#     # ([],)
# That tuple contains the same list object that will be reused for all calls
# that don’t explicitly pass a `lst` argument.

# 2. The same list is reused between calls
# Each time you call `add_item()` without passing a list, Python reuses that same
# default list reference.
#     print(add_item(1))  # [1]
#     print(add_item(2))  # [1, 2]  <-- same list reused
# That’s because the list was created once, not freshly each time.

# 3. Why Python does this
# Python does it for performance and design consistency: default arguments are
# evaluated once when the function is defined, not every time it’s called.
# If a mutable object is used as a default and is modified, the modification
# persists across future calls.

# 4. Correct and safe pattern
# To avoid this, use `None` as a sentinel value and create a new list inside.


# In summary
# - Default arguments are evaluated once at definition time.
# - Mutable defaults like `[]` or `{}` persist across calls.
# - Use `None` as a default and create a new object inside the function.
