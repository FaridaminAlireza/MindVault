# Decorators are functions that wrap another function to extend or
#  modify its behavior without changing its code. They’re a very Pythonic way
#  to separate concerns like logging, timing, or access control.

# Example 1, a decorator that caches the results of a function (memoization)
#  but also prints the number of cache hits.


from functools import wraps

def cache_with_hits(func):
    cache = {}
    hits = 0

    @wraps(func)
    def wrapper(*args):
        nonlocal hits
        if args in cache:
            hits += 1
            print(f"Cache hit! Total hits: {hits}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

# Example usage: Fibonacci numbers
@cache_with_hits
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))


# Example 2, without using wraps

def my_decorator(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Say hello"""
    print("Hello!")

print(greet.__name__)  # Output: wrapper
print(greet.__doc__)   # Output: None


# Example 2, with using wraps

from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Say hello"""
    print("Hello!")

print(greet.__name__)  # Output: greet
print(greet.__doc__)   # Output: Say hello


# Exmaple 3
from functools import wraps

def debug_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug_decorator
def add(a, b):
    """Adds two numbers"""
    return a + b

print(add.__name__)   # Output: add
print(add.__doc__)    # Output: Adds two numbers
help(add)             # Shows correct info



# Preserving metadata is important for debugging, introspection,
#  and libraries like Flask or FastAPI that rely on function signatures.

# Without @wraps, tools that inspect your functions (like help(),
#  doc generators, or type checkers) will see only the wrapper,
#  not the original function.


# Alternative way (old way) of calling decorators 

def double_result(func):
    def wrapper(*args, **kwargs):
        return 2 * func(*args, **kwargs)
    return wrapper

def increment_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 1
    return wrapper

def my_func(x):
    return x

# Old-fashioned manual stacking
my_func = double_result(increment_result(my_func))
print(my_func(5))  # (5+1)*2 = 12
 

#  So @decorator is just a shortcut for: 
# function = decorator(function)


# Example 2
from functools import wraps

def repeat(n):  # Decorator takes extra argument 'n'
    def decorator(func):  # This will receive the actual function
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Run {i+1}/{n}:")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# Example 2, Old fashion way
def greet(name):
    print(f"Hello, {name}!")

# Outer function returns decorator, decorator wraps greet
greet = repeat(3)(greet)  

greet("Alice")


# repeat(n) --> decorator(func) --> wrapper(*args, **kwargs)

# Outer layer → decorator arguments
# Middle layer → function to decorate
# Inner layer → function call arguments


# A flat version, but doesn't work with @

def repeat_flat(func, n):
    def wrapper(*args, **kwargs):
        for i in range(n):
            func(*args, **kwargs)
    return wrapper

def greet(name):
    print(f"Hello, {name}!")

greet = repeat_flat(greet, 3)  # Manual decoration
greet("Alice")
