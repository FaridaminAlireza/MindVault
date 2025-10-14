# Function composition means combining multiple functions into one,
# so that the output of one becomes the input of another: g(f(x))

# Example:
# f(x) = x + 2
# g(x) = x * 3
# g(f(4)) = g(6) = 18

def f(x):
    return x + 2

def g(x):
    return x * 3

result = g(f(4))
print(result)   # 18


# We can create a reusable "compose" function:

def compose(g, f):
    return lambda x: g(f(x))

# or 
def compose(g, f):
    def fnc(x):
        return g(f(x))
    return fnc

# Usage
h = compose(g, f)
print(h(4))   # 18


# To chain multiple functions, we can extend the idea:

from functools import reduce

def compose_many(*funcs):
    return reduce(lambda f, g: lambda x: f(g(x)), funcs)

# Example:
def f(x): return x + 2
def g(x): return x * 3
def h(x): return x - 5

composed = compose_many(f, g, h)
print(composed(4))



# functools provides `partial` and `reduce` but not direct composition.
# However, you can write elegant pipelines with `map`, `filter`, or
# functional libraries like `toolz`.

from toolz import compose

def f(x): return x + 2
def g(x): return x * 3
 
h = compose(g, f)
print(h(4))  # 18

# `toolz.compose` automatically builds the function g(f(x)).


# Python 3.10+ allows more readable chaining with the "pipe" idea.
# You can simulate it:

class Pipe:
    def __init__(self, value):
        self.value = value

    def __or__(self, func):
        return Pipe(func(self.value))

    def __repr__(self):
        return f"Pipe({self.value})"

result = Pipe(4) | (lambda x: x + 2) | (lambda x: x * 3)
print(result)  # Pipe(18)

# This style mimics function composition in reverse order:
# the output of one function flows into the next.
