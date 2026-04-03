"""
Numerical differentiation is the process of estimating the derivative of a function
using discrete data points rather than an explicit function.

This is necessary when the function is unknown or
too complex to differentiate analytically.

The primary approach involves using finite differences, 
which approximate the derivative by 
calculating the slope of a secant line between points.

list of methods:
 Finite difference methods
 Polynomial interpolation
 Richardson extrapolation
 Fourier transforms (spectral differentiation)
 Complex-step differentiation

 -- Finite difference methods --
 These are derived from Taylor series expansions and
form the basis of many numerical techniques 
for solving differential equations.

Forward Difference

 Method: This is a first-order, one-sided approximation.
 It uses the function's value at the current point and a point
 one step forward. 
 Formula: f'(x) = (f(x+h) - f(x)) / h
 Accuracy: The error is proportional to the step size h,
  denoted as O(h)

def forward_diff(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


 Backward Difference

 Method: A first-order, one-sided approximation that uses
 the current point and a point one step backward.

 Formula: f'(x) = (f(x) - f(x-h)) / h

 Accuracy: The error is proportional to the step size h,
 denoted as O(h)

Proof using taylor expansion: 
f(x-h) = f(x) - hf'(x) + h^2/2! f''(x) - h^3/3! f'''(x) + h^4/4! f(4)(x) - ...

f'(x) = (f(x) - f(x-h)) / h + h^2/2 f''(x) / h  + ...

f'(x) = (f(x) - f(x-h)) / h + h/2 f''(ξ)

Example: Finding the mystery point ξ for f(x) = x^3
    1. Setup 
        Function: f(x) = x^3
        Point of interest: x = 2
        Step size: h = 1
        Interval: (x-h, x) = (1, 2)
    2. True Calculus Value
        f'(x) = 3x^2
        At x = 2: f'(2) = 3(2)^2 = 12
    3. Numerical Approximation (Backward Difference)
        Approx = [f(x) - f(x-h)] / h
        Approx = [2^3 - 1^3] / 1
        Approx = [8 - 1] / 1 = 7
    4. The Error
        True Value - Approx Value = 12 - 7 = 5
    5. Solving for ξ using the Error Formula
        Error Formula: E = (h/2) * f''(ξ)
        Plug in knowns: 5 = (1/2) * f''(ξ)
        Multiply by 2: 10 = f''(ξ)
        Since f(x) = x^3, then f'(x) = 3x^2 and f''(x) = 6x.
        10 = 6 * ξ
        ξ = 10 / 6
        ξ ≈ 1.667
    6. Conclusion
        The mystery point ξ ≈ 1.667 lies exactly within our interval (1, 2).
        This confirms that the error in our approximation is perfectly 
        accounted for by the second derivative evaluated at this specific point
        inside the interval.

    Think of as the point that represents the "average" behavior of
    the function's curvature (second derivative) over the interval

    When you use a finite difference like  you are using a straight line
    to approximate a curve. The error you get is the sum of all the "missed"
    curvature. Mathematically, this error is the integral (the sum) of the 
    second derivative over that interval. The Mean Value Theorem for Integrals
    says that for any integral, there is a single point where the function value 
    equals the average value of the function over that whole stretch.

def backward_diff(f, x, h=1e-5):
    return (f(x) - f(x - h)) / h

 Central Difference
 Method: This is a more accurate, second-order approximation
 that uses points on both sides of the target point.

 Formula: f'(x) = (f(x+h) - f(x-h)) / 2h
 Accuracy: The error is proportional to the square of step size h^2,
 denoted as O(h^2)

def central_diff(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


 Higher-order finite difference methods
 For higher accuracy, more data points can be incorporated.
 For instance, the second derivative can be approximated using
  a three-point central difference formula


 Formula: f''(x) = (f(x-h) - 2f(x) + f(x-h)) / h^2

 Proof using taylor expansion
 We begin with the Taylor series expansions of a function f(x) 
 around a central point x, for points x+h and x-h. 
 Here, h is the step size.

 f(x+h) = f(x) + hf'(x) + h^2/2! f''(x) + h^3/3! f'''(x) + h^4/4! f(4)(x) + ...
 f(x-h) = f(x) - hf'(x) + h^2/2! f''(x) - h^3/3! f'''(x) + h^4/4! f(4)(x) - ...

 To eliminate the terms with the first derivative, f'(x),
 we add the two expansions together.
 f(x+h) + f(x-h)
 The terms with odd powers of h 
 (the first derivative, third derivative, etc.) cancel each other out

 f(x+h) + f(x-h) = 2f(x) + 2 h^2/2! f''(x) + 2 h^4/4! f(4)(x) + ...

Next we rearrange the equation to solve for the second derivative, f''(x):

 f''(x) =  f(x+h) - 2 f(x) + f(x-h)  /h^2

 Truncation Error: 
 The discarded higher-order terms from the
 Taylor series determine the truncation error.

 The error term is approximately h^4/12 f(4)(ξ) in the the interval (x - h, x + h).
 
 Accuracy: The error is therefore proportional to h^2, 
 making this a second-order accurate method, 
 denoted as O(h^2). Because  - h^4/12 f(4)(ξ) / h^2 =  - h^2/12 f(4)(ξ)

def second_diff(f, x, h=1e-5):
    return (f(x + h) - 2*f(x) + f(x - h)) / h**2

-----
What ξ Means Exactly:
    An Intermediate Value: 
    When you approximate a function with a Taylor polynomial,
    the "remainder" (error) term is exactly equal to 
    the next derivative evaluated at some point 
    that lies strictly between your base point 
    and the point.

    Based on Mean Value Theorem:  f(a) - f(b) / b- a  = f'(c)

    f(x)=f(a)+f′(ξ)(x−a)

    The "Perfect" Correction: The Mean Value Theorem guarantees
    that there is at least one value in the interval that makes
    the error formula exact. If you knew the exact value of, 
    your "approximation" would actually be the perfect, true value of
    the function. 

    A Tool for Bounds: Since we rarely know the exact value of,
    we use it to find the worst-case scenario. 
    By finding the maximum possible value of the derivative
    across the entire interval, we can calculate the 
    "upper bound" of the error.
"""