
# Function : Inverse Function : Example : Python
# ---------------------------------------------------------------
# Exponential function: exp(x)       : ln(x)           : exp(2) = 7.389  => ln(7.389) = 2      : math.exp(x), math.log(x)
# Natural logarithm: ln(x)            : exp(x)          : ln(e^3) = 3      => exp(3) = 20.085  : math.log(x), math.exp(x)
# Common logarithm: log10(x)          : 10^x            : log10(1000)=3    => 10^3 = 1000      : math.log10(x), 10**x
# Binary logarithm: log2(x)           : 2^x             : log2(8)=3        => 2^3 = 8          : math.log2(x), 2**x
# Square function: x^2                : sqrt(x)         : 4^2 = 16         => sqrt(16) = 4     : x**2, math.sqrt(x)
# Cube function: x^3                  : cbrt(x)         : 3^3 = 27         => cbrt(27) = 3     : x**3, pow(x,1/3)
# Sine function: sin(x)               : arcsin(x)       : sin(pi/2)=1      => arcsin(1)=pi/2   : math.sin(x), math.asin(x)
# Cosine function: cos(x)             : arccos(x)       : cos(0)=1         => arccos(1)=0      : math.cos(x), math.acos(x)
# Tangent function: tan(x)            : arctan(x)       : tan(pi/4)=1      => arctan(1)=pi/4   : math.tan(x), math.atan(x)
# Cotangent function: cot(x)          : arccot(x)       : cot(pi/4)=1      => arccot(1)=pi/4   : 1/math.tan(x), math.atan(1/x)
# Secant function: sec(x)             : arcsec(x)       : sec(pi/3)=2      => arcsec(2)=pi/3   : 1/math.cos(x), math.acos(1/x)
# Cosecant function: csc(x)           : arccsc(x)       : csc(pi/2)=1      => arccsc(1)=pi/2   : 1/math.sin(x), math.asin(1/x)
# Hyperbolic sine: sinh(x)            : arsinh(x)       : sinh(1)=1.175    => arsinh(1.175)=1  : math.sinh(x), math.asinh(x)
# Hyperbolic cosine: cosh(x)          : arcosh(x)       : cosh(1)=1.543    => arcosh(1.543)=1  : math.cosh(x), math.acosh(x)
# Hyperbolic tangent: tanh(x)         : artanh(x)       : tanh(0.5)=0.462  => artanh(0.462)=0.5: math.tanh(x), math.atanh(x)
# Power function: x^a                  : x^(1/a)        : 8^(1/3)=2        => 2^3=8           : x**a, x**(1/a)
# Reciprocal function: 1/x            : 1/x             : 1/5=0.2          => 1/0.2=5         : 1/x



import math

print("Function Demonstrations with Inverses\n")

# Exponential and logarithms
x = 2
print(f"exp({x}) = {math.exp(x)}")
print(f"ln({math.exp(x)}) = {math.log(math.exp(x))}\n")

# Common and binary logarithms
x = 1000
print(f"log10({x}) = {math.log10(x)}")
print(f"10**3 = {10**3}\n")

x = 8
print(f"log2({x}) = {math.log2(x)}")
print(f"2**3 = {2**3}\n")

# Powers and roots
x = 4
print(f"{x}^2 = {x**2}")
print(f"sqrt({x**2}) = {math.sqrt(x**2)}\n")

x = 27
print(f"{x}^3 = {x**3}")
print(f"cbrt({x}) = {x**(1/3)}\n")

# Trigonometric functions
pi = math.pi
print(f"sin(pi/2) = {math.sin(pi/2)}")
print(f"arcsin(1) = {math.asin(1)}\n")

print(f"cos(0) = {math.cos(0)}")
print(f"arccos(1) = {math.acos(1)}\n")

print(f"tan(pi/4) = {math.tan(pi/4)}")
print(f"arctan(1) = {math.atan(1)}\n")

# Cotangent, secant, cosecant
print(f"cot(pi/4) = {1/math.tan(pi/4)}")
print(f"arccot(1) = {math.atan(1/1)}\n")

print(f"sec(pi/3) = {1/math.cos(pi/3)}")
print(f"arcsec(2) = {math.acos(1/2)}\n")

print(f"csc(pi/2) = {1/math.sin(pi/2)}")
print(f"arccsc(1) = {math.asin(1/1)}\n")

# Hyperbolic functions
x = 1
print(f"sinh({x}) = {math.sinh(x)}")
print(f"arsinh({math.sinh(x)}) = {math.asinh(math.sinh(x))}\n")

print(f"cosh({x}) = {math.cosh(x)}")
print(f"arcosh({math.cosh(x)}) = {math.acosh(math.cosh(x))}\n")

x = 0.5
print(f"tanh({x}) = {math.tanh(x)}")
print(f"artanh({math.tanh(x)}) = {math.atanh(math.tanh(x))}\n")

# Power function
x = 8
a = 3
print(f"{x}^(1/{a}) = {x**(1/a)}")
print(f"{(x**(1/a))**a} = { (x**(1/a))**a }\n")

# Reciprocal
x = 5
print(f"1/{x} = {1/x}")
print(f"1/{1/x} = {1/(1/x)}\n")
