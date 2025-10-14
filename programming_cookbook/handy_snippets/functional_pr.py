# Functional Programming Charactristics:

# 1. Pure functions:	No side effects, deterministic
# - Always return the same output for the same input.
# - Do not produce side effects (no modifying globals, printing, or I/O inside).
def square(x):
    return x * x  # Always same output, no side effects


# 2. Immutability:	Return new lists/dicts/tuples instead of modifying
# Do not modify data after creation.
# Use new lists, tuples, or dicts instead of changing in place.
lst = [1,2,3]
lst.append(4) # Not functional
lst2 = lst + [4] # Functional

# 3. Recursion:	Use recursion instead of loops
# Replace for/while loops with recursive functions.
# Be careful of Python recursion limits.
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


# 4. Higher-order functions: map, filter, reduce, sorted(key=…)
# Functions that take other functions as arguments or return functions.
# - Examples: map, filter, reduce, sorted(key=...)
nums = [1,2,3,4]
squared = list(map(lambda x: x*x, nums))

# 5. Expression-oriented: Avoid assignments; compute values as expressions
# - Prefer expressions over statements.
# - Avoid assignments, loops, or side-effects inside functional logic.
result = []
for x in lst: # not functional
    result.append(x*2)
result = list(map(lambda x: x*2, lst)) # Functional


# 6. First-class functions: Pass functions as arguments, return functions
# Functions can be passed, returned, and stored in variables.
def apply_twice(f, x):
    return f(f(x))
apply_twice(lambda x: x+2, 5) 

# 7. Avoid side effects: No printing, modifying globals, or I/O inside logic
# - Do not change external state.
# - Keep functions referentially transparent.
# - No printing, file writes, or modifying inputs inside functions.

# 8. Use immutable data structures when possible
# - Tuples instead of lists
# - frozenset instead of set
# - Return new copies instead of modifying in place
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4,)  # create new tuple, 


# Some practical examples:

# Ex 1. Fibonacci (memoized recursive, practical for large n)
from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# First 50 Fibonacci numbers
print([fibonacci(i) for i in range(50)])


# Ex 2. Factorial using recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print([factorial(i) for i in range(10)])


# Ex 3. Flatten a nested list (recursive)
def flatten(lst):
    return [] if not lst else (flatten(lst[0]) 
     if isinstance(lst[0], list) else [lst[0]]) + flatten(lst[1:])

nested = [1, [2, [3, 4], 5], 6]
print(flatten(nested))


# Ex 4. Map, Filter, Reduce with a dataset
from functools import reduce

data = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 22},
]
# Extract ages
ages = list(map(lambda x: x["age"], data))
# Filter adults (age >= 30)
adults = list(filter(lambda x: x["age"] >= 30, data))
# Sum of ages
total_age = reduce(lambda x, y: x + y, ages)

print("Ages:", ages)
print("Adults:", adults)
print("Total age:", total_age)


#Ex 5. Prime numbers (recursive check)
def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

primes = list(filter(is_prime, range(2, 30)))
print(primes)


#Ex 6. Generate combinations of a list (functional style)
from functools import reduce

def combinations(lst, r):
    if r == 0:
        return [[]]
    if not lst:
        return []
    return combinations(lst[1:], r) + [
        [lst[0]] + c for c in combinations(lst[1:], r-1)]

print(combinations([1,2,3,4], 2))


# Ex 7. Functional quicksort (immutable)
def quicksort(lst):
    if not lst:
        return []
    pivot = lst[0]
    less = list(filter(lambda x: x < pivot, lst[1:]))
    greater = list(filter(lambda x: x >= pivot, lst[1:]))
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([5,3,8,1,2,7,4,6]))


# tail call optimization (TCO)

# A tail recursive function is a function where the
# last operation is the recursive call. That means nothing
# needs to be done after the call returns, so the current
# stack frame can be reused.

# Tail call optimization (TCO) is when the language runtime reuses
# the current stack frame for a tail call instead of creating a new one.
# This allows recursion to run in constant stack space, even for very deep recursion.
# - Not all languages implement it.
# - Functional languages like Haskell, Scheme, OCaml, and Scala usually implement TCO.
# - Python does NOT implement TCO, so tail recursion still consumes stack frames and 
# may hit RecursionError.


#Ex 8

# Not tail-recursive
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)  # multiplication happens AFTER recursion


# Not tail-recursive
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)  # multiplication happens AFTER recursion
    
#  tail-recursive
def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial_tail(n-1, n*acc)  # recursive call is LAST operation

# Tail recursion in Python (trick using a loop)
# Since Python doesn’t do TCO, we can manually convert tail recursion
# to iteration to avoid stack overflow:
def factorial_iter(n):
    acc = 1
    while n > 0:
        acc *= n
        n -= 1
    return acc

print(factorial_iter(10000))


# Ex 9. An example of stream processors
def naturals():
    n = 0
    while True:
        yield n
        n += 1

def take(n, it):
    for i, x in enumerate(it):
        if i >= n:
            break
        yield x

def square(it):
    for x in it:
        yield x * x

result = take(5, square(naturals()))
# Nothing is computed yet — 
# all you’ve done is create a chain of generators:
# naturals() → infinite generator of integers
# square() → wraps that generator, squaring values lazily
# take(5, …) → wraps again, limiting to 5 results
# It’s a lazy pipeline — like in functional languages 
# (Haskell, Scala, etc.).
#Useful for Streaming data transformations (ETL, ML pipelines)


print(list(result))
# When we iterate over result, at that moment, 
# Python starts pulling values through the chain — on demand.


# Ex 10. linked list implementation with functional programing
# we can represent a list as nested tuples or dataclasses — like Lisp-style lists
#  A linked list can be either:
# - None (empty list)
# - (head, tail) where tail is another linked list

def cons(head, tail):
    return (head, tail)

def head(lst):
    return lst[0]

def tail(lst):
    return lst[1]

def is_empty(lst):
    return lst is None

def to_pylist(lst):
    return [] if is_empty(lst) else [head(lst)] + to_pylist(tail(lst))

def prepend(x, lst): # This never mutates — it just returns a new list.
    return cons(x, lst)


# Example
lst = cons(1, cons(2, cons(3, None)))
print(to_pylist(lst))  # [1, 2, 3]



# In compilers, interpreters, or analyzers 
# (e.g., Abstract syntax tree(AST) transformations in ast or lib2to3),
# immutable trees are practical — 
# each transformation returns a new AST, not modifying the original.
from dataclasses import dataclass

# @dataclass(frozen=True) makes the tree immutable,
# perfect for a functional approach.

@dataclass(frozen=True)
class Expr:
    op: str
    left: int
    right: int

def eval_expr(e: Expr):
    return e.left + e.right if e.op == '+' else e.left * e.right

# Transform the AST without mutation
expr = Expr('+', 2, 3)
new_expr = Expr('*', expr.left, expr.right)

print(eval_expr(expr))     # 5
print(eval_expr(new_expr)) # 6


