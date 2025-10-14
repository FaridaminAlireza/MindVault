# In functional programming, "functor" and "monad" are abstract patterns for
#  working with computations and data transformations in a clean, composable way.
# While Python is not a purely functional language, it supports these concepts
# through objects, methods, and classes that behave similarly.


# A Functor is a container-like structure that can apply a function
#  to the value(s) it holds without changing the structure itself.
# Something that implements `map(function)`
# Think of it as: a box that knows how to apply a function to its contents.


class Box:
    def __init__(self, value):
        self.value = value

    def map(self, func):
        return Box(func(self.value))

    def __repr__(self):
        return f"Box({self.value})"

box = Box(5)
result = box.map(lambda x: x * 2)
print(result)   # Box(10)

# The Box holds a value (5).
# We applied a function (x*2) to that value without unwrapping the box.
# The structure stayed the same (a Box), only the value changed.
# This pattern is useful for consistent function chaining:
#     box.map(f).map(g).map(h)

# Real-world Python examples:
# - The `map()` built-in function acts like a functor over iterables.
# - The `Maybe` or `Option` pattern (in functional libraries like
# `toolz` or `returns` generalizes this idea for safe transformations.


# MONADS
# A Monad is a functor that also supports "chaining" of operations
# where each step might produce another wrapped value.
# It adds a new operation called `bind` (also known as `flatMap` or `>>=`)
# Monad = Functor + bind

# The key rule:
# - Functor applies a function to its contents.
# - Monad chains functions that return wrapped results.

class Box:
    def __init__(self, value):
        self.value = value

    def map(self, func):
        return Box(func(self.value))

    def bind(self, func):
        # func must return another Box
        return func(self.value)

    def __repr__(self):
        return f"Box({self.value})"

def double(x):
    return Box(x * 2)

def increment(x):
    return Box(x + 1)

result = Box(3).bind(double).bind(increment)
print(result)   # Box(7)


# Each function returns a new Box.
# The bind() method unwraps the value, applies the function, and flattens the result.
# This prevents nested Box(Box(...)) structures.


# Functors and Monads are important because they:
# - Enable composition of transformations in a predictable way.
# - Help manage side effects (like errors, missing data, IO) cleanly.
# - Allow declarative pipelines for data and computation.
# - Improve code reuse and testability.


class Maybe:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        if self.value is None:
            return Maybe(None)
        return func(self.value)

    def __repr__(self):
        return f"Maybe({self.value})"

# Example usage:
def safe_reciprocal(x):
    return Maybe(1/x) if x != 0 else Maybe(None)

result = Maybe(4).bind(safe_reciprocal)
print(result)

result = Maybe(0).bind(safe_reciprocal)
print(result)
# This handles the "division by zero" case gracefully
# without throwing exceptions.


# In Python, examples of monad-like patterns:
# - `Optional` handling (`None` vs value)
# - `async`/`await` (asynchronous monads)
# - Generators (`yield`) managing sequences of computations
# - Libraries like `returns` provide formal Functor/Monad implementations