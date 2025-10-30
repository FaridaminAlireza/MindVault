# Numerical differentiation is the process of estimating the derivative of a function
#  using discrete data points rather than an explicit function. This is necessary when
#  the function is unknown or too complex to differentiate analytically.
#  The primary approach involves using finite differences, which approximate
#  the derivative by calculating the slope of a secant line between points.

# list of methods:
# Finite difference methods
# Polynomial interpolation
# Richardson extrapolation
# Fourier transforms (spectral differentiation)
# Complex-step differentiation


# -- Finite difference methods --
# These are derived from Taylor series expansions and
# form the basis of many numerical techniques for solving differential equations.




# Finite Numerical Differentiation Methods
# This note summarizes finite difference methods for numerical differentiation 
# — ways to approximate the derivative of a function \( f(x) \) 
# using values of \( f \) at discrete points.

# Forward Difference

# Method: This is a first-order, one-sided approximation.
# It uses the function's value at the current point and a point
# one step forward. 
# Formula: f'(x) = (f(x+h) - f(x)) / h
# Accuracy: The error is proportional to the step size h,
#  denoted as O(h)

def forward_diff(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


# Backward Difference

# Method: A first-order, one-sided approximation that uses
# the current point and a point one step backward.

# Formula: f'(x) = (f(x) - f(x-h)) / h

# Accuracy: The error is proportional to the step size h,
# denoted as O(h)


def backward_diff(f, x, h=1e-5):
    return (f(x) - f(x - h)) / h

# Central Difference
# Method: This is a more accurate, second-order approximation
# that uses points on both sides of the target point.

# Formula: f'(x) = (f(x+h) - f(x-h)) / 2h
# Accuracy: The error is proportional to the square of step size h^2,
# denoted as O(h^2)

def central_diff(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


# Higher-order finite difference methods
# For higher accuracy, more data points can be incorporated.
# For instance, the second derivative can be approximated using
#  a three-point central difference formula


# Formula: f'(x) = (f(x-h) - 2f(x) + f(x-h)) / h^2

# Accuracy: The error is proportional to the square of step size h^2,
# denoted as O(h^2)

def second_diff(f, x, h=1e-5):
    return (f(x + h) - 2*f(x) + f(x - h)) / h**2


# Proof using taylor expansion
# We begin with the Taylor series expansions of a function f(x) 
# around a central point x, for points x+h and x-h. 
# Here, h is the step size.

# f(x+h) = f(x) + hf'(x) + h^2/2! f''(x) + h^3/3! f'''(x) + h^4/4! f(4)(x) + ...
# f(x-h) = f(x) - hf'(x) + h^2/2! f''(x) - h^3/3! f'''(x) + h^4/4! f(4)(x) - ...

# To eliminate the terms with the first derivative, f'(x), we add the two expansions together.

# f(x+h) + f(x-h)
# The terms with odd powers of h 
# (the first derivative, third derivative, etc.) cancel each other out

# f(x+h) + f(x-h) = 2f(x) + 2 h^2/2! f''(x) + 2 h^4/4! f(4)(x) + ...

# Next we rearrange the equation to solve for the second derivative, f''(x):

# h^2 f''(x) =  f(x+h) - 2 f(x) + f(x-h)  /h^2

# Truncation Error: 
# The discarded higher-order terms from the
#  Taylor series determine the truncation error.
# The error term is approximately h^4/12 f(4)(ξ) in the  the interval (x - h, x + h)
# The error is therefore proportional to h^2, making this a second-order accurate method, 
# denoted as O(h^2)

     
