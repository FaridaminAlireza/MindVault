# A closure in Python is a function object that remembers variables from
# its enclosing lexical scope, even if the outer function has finished executing.
# It allows to “capture” and use data from a surrounding context without using 
# global variables or classes.

# Advantages
# 1. Encapsulation without classes
# You can keep related logic and data together privately inside a function.
# 2. State retention between calls
# The closure “remembers” data between calls without global state.
# 3. Factory functions
# You can create functions dynamically with different behaviors.
# 4. Functional programming style
# Useful in decorators, callbacks, or higher-order functions.


def outer_function(x):
    def inner_function(y):
        return x + y 
    return inner_function

add_five = outer_function(5)
print(add_five(10))  # Output: 15

# Every function in Python has a __closure__ attribute 
# that stores references to the captured variables.

print(add_five.__closure__[0].cell_contents)  # Output: 5

# Ex for Decorators 
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Ex for data hiding 
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
print(c())  # 1
print(c())  # 2


# Ex for customizing functions (Factory Patterns)
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15



#Ex closure vs class 

def make_adder(x):
    def adder(y):
        return x + y
    return adder

add10 = make_adder(10)
print(add10(5))  # Output: 15

class Adder:
    def __init__(self, x):
        self.x = x
    def __call__(self, y):
        return self.x + y

add10 = Adder(10)
print(add10(5))  # Output: 15


# Closure advantage: short and simple for small use-cases.
# Class advantage: more scalable and extensible


