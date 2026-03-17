"""
### 1. RMS (Root Mean Square)

Definition:
The RMS of a function x(t) over a period T is:

x_rms = sqrt((1/T) * integral from 0 to T of x(t)^2 dt)

Example: AC current i(theta) = I * sin(theta), where I is the peak current

1. Square the function: i^2 = I^2 * sin^2(theta)
2. Average over one period (0 to 2*pi):
   i_mean^2 = (1/(2*pi)) * integral from 0 to 2*pi of I^2 * sin^2(theta) dtheta
   = I^2 / 2
3. Take the square root:
   i_rms = I / sqrt(2)

Meaning: RMS value is the effective current that would produce the same heating effect as the AC current.

### 2. Surface Area of Revolution

Formula: For y = f(x) rotated about the x-axis from x = a to x = b:

S = 2 * pi * integral from a to b of y * sqrt(1 + (dy/dx)^2) dx

Explanation:

* ds = sqrt(dx^2 + dy^2) = sqrt(1 + (dy/dx)^2) dx is the slant length of a tiny segment
* 2 * pi * y is the circumference of the circle made by rotating that segment
* Multiplying circumference * slant length gives the area of the tiny ribbon: dS = 2 * pi * y * ds
* Integrate all ribbons over the interval to get total surface area

Example: y = sqrt(x), 0 <= x <= 1

1. Compute dy/dx = 1/(2*sqrt(x))
2. Compute sqrt(1 + (dy/dx)^2) = sqrt(1 + 1/(4x)) = sqrt(4x + 1) / (2 * sqrt(x))
3. Substitute into formula:
   S = 2*pi * integral from 0 to 1 of sqrt(x) * (sqrt(4x + 1) / (2 * sqrt(x))) dx
   = pi * integral from 0 to 1 of sqrt(4x + 1) dx
4. Use substitution u = 4x + 1, du = 4 dx, dx = du/4, limits u = 1 to 5
   S = (pi / 4) * integral from 1 to 5 of u^(1/2) du
   = (pi / 4) * (2/3) * (5^(3/2) - 1)
   = (pi / 6) * (5^(3/2) - 1)

Final Answer: S = (pi / 6) * (5^(3/2) - 1)

"""