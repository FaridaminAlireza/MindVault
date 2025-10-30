import math

def taylor_expansion(f, a, x, n):
    """Compute Taylor expansion of function f around point a up to n terms."""
    result = 0
    for i in range(n):
        term = (f(a) if i == 0 else derivative(f, a, i)) * ((x - a)**i) / math.factorial(i)
        result += term
    return result

def derivative(f, x, n, h=1e-5):
    """Approximate nth derivative using central differences."""
    if n == 0:
        return f(x)
    elif n == 1:
        return (f(x + h) - f(x - h)) / (2*h)
    else:
        return (derivative(f, x + h, n - 1, h) - derivative(f, x - h, n - 1, h)) / (2*h)

# Example: e^x
approx = taylor_expansion(math.exp, a=0, x=1, n=6)
print(f"Approximation of e^1 using 6 terms: {approx}")
print(f"Actual value: {math.e}")
