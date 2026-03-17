"""
Projectile Motion in Vertex Form

We are given the parametric equations of motion:

x = u * t
y = 0
z = v * t - (1/2) * g * t^2

Step 1: Solve for t from the x-equation:

t = x / u

Step 2: Substitute t into the z-equation:

z = v * (x / u) - (1/2) * g * (x / u)^2

Simplify:

z = (v / u) * x - (g / (2 * u^2)) * x^2

Step 3: Rewrite z in vertex form by completing the square:

z = - (g / (2 * u^2)) * (x^2 - (2 * u * v / g) * x)

Complete the square:

x^2 - (2 * u * v / g) * x = (x - (u * v / g))^2 - (u * v / g)^2

Substitute back:

z = - (g / (2 * u^2)) * (x - (u * v / g))^2 + (g / (2 * u^2)) * (u * v / g)^2

Simplify the constant term:

(g / (2 * u^2)) * (u * v / g)^2 = v^2 / (2 * g)

Step 4: Final form of the trajectory in terms of x:

y = 0
z = (v^2 / (2 * g)) - (g / (2 * u^2)) * (x - (u * v / g))^2

Vertex Explanation:

* The vertex of the parabola is at x = uv/g, y = 0, z = v^2 / (2g).
* This corresponds to the **maximum height** of the projectile.
* In general, the vertex form z = A - B * (x - h)^2 makes
the **maximum point** immediately visible, which is why it is useful
in projectile motion problems.

Summary:

* Standard form: z = (v / u) * x - (g / (2 * u^2)) * x^2
* Vertex form: z = (v^2 / (2 * g)) - (g / (2 * u^2)) * (x - (uv/g))^2
* Vertex coordinates: (x, y, z) = (uv/g, 0, v^2 / 2g)

"""