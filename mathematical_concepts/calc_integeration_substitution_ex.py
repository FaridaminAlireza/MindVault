"""

SUBSTITUTION EXAMPLE FOR INTEGRALS WITH sqrt(a^2 - x^2)

1. Recognizing the pattern

When an integral contains:

sqrt(a^2 - x^2)

this matches the trigonometric identity:

sin^2(theta) + cos^2(theta) = 1

Rewriting:
1 - sin^2(theta) = cos^2(theta)

So we choose the substitution:

x = a * sin(theta)

---

2. Example integral

Compute:

∫ sqrt(a^2 - x^2) dx

---

3. Perform the substitution

Step 1: Substitute x

x = a * sin(theta)

Step 2: Differentiate x

dx = a * cos(theta) dtheta

Step 3: Substitute inside the square root

sqrt(a^2 - x^2)
= sqrt(a^2 - a^2 * sin^2(theta))
= sqrt(a^2 * (1 - sin^2(theta)))
= sqrt(a^2 * cos^2(theta))
= a * cos(theta)

---

4. Rewrite the integral

∫ sqrt(a^2 - x^2) dx
= ∫ (a * cos(theta)) * (a * cos(theta) dtheta)
= ∫ a^2 * cos^2(theta) dtheta

---

5. Simplify the integral

Use the identity:

cos^2(theta) = (1 + cos(2theta)) / 2

So:

∫ a^2 * cos^2(theta) dtheta
= (a^2 / 2) ∫ (1 + cos(2theta)) dtheta
= (a^2 / 2) * (theta + sin(2theta)/2) + C

---

6. Convert back to x

From the substitution:

x = a * sin(theta)
theta = arcsin(x / a)

Also:

sin(2theta) = 2 * sin(theta) * cos(theta)

sin(theta) = x / a
cos(theta) = sqrt(a^2 - x^2) / a

So:

sin(2theta) = 2x * sqrt(a^2 - x^2) / a^2

---

7. Final answer

∫ sqrt(a^2 - x^2) dx
= (x/2) * sqrt(a^2 - x^2)

* (a^2/2) * arcsin(x / a)
* C

---

8. Useful substitution rules

sqrt(a^2 - x^2)  ->  x = a * sin(theta)
sqrt(a^2 + x^2)  ->  x = a * tan(theta)
sqrt(x^2 - a^2)  ->  x = a * sec(theta)

"""

"""

HYPERBOLIC SUBSTITUTION — STEP BY STEP EXAMPLE

Hyperbolic substitution is useful for integrals
involving expressions like:

sqrt(x^2 + a^2)
sqrt(x^2 - a^2)

It works because hyperbolic functions have identities
very similar to trigonometric ones.

---

1. Key hyperbolic identities

cosh^2(t) - sinh^2(t) = 1

From this we get:

1 + sinh^2(t) = cosh^2(t)
cosh^2(t) - 1 = sinh^2(t)

---

2. When to use each substitution

If the integrand contains:

sqrt(x^2 + a^2)  ->  x = a * sinh(t)
sqrt(x^2 - a^2)  ->  x = a * cosh(t)

---

3. Example integral

Compute:

∫ sqrt(x^2 + a^2) dx

---

4. Choose the substitution

Because we have sqrt(x^2 + a^2), use:

x = a * sinh(t)

---

5. Compute dx

dx = a * cosh(t) dt

---

6. Substitute into the square root

sqrt(x^2 + a^2)
= sqrt(a^2 * sinh^2(t) + a^2)
= sqrt(a^2 * (sinh^2(t) + 1))
= sqrt(a^2 * cosh^2(t))
= a * cosh(t)

---

7. Rewrite the integral

∫ sqrt(x^2 + a^2) dx
= ∫ (a * cosh(t)) * (a * cosh(t) dt)
= ∫ a^2 * cosh^2(t) dt

---

8. Simplify the integrand

Use the identity:

cosh^2(t) = (1 + cosh(2t)) / 2

So:

∫ a^2 * cosh^2(t) dt
= (a^2 / 2) ∫ (1 + cosh(2t)) dt
= (a^2 / 2) * (t + sinh(2t)/2) + C

---

9. Convert back to x

From the substitution:

x = a * sinh(t)
t = arcsinh(x / a)

Also:

sinh(2t) = 2 * sinh(t) * cosh(t)

sinh(t) = x / a
cosh(t) = sqrt(x^2 + a^2) / a

So:

sinh(2t) = 2x * sqrt(x^2 + a^2) / a^2

---

10. Final answer

∫ sqrt(x^2 + a^2) dx
= (x/2) * sqrt(x^2 + a^2)

* (a^2/2) * arcsinh(x / a)
* C

---

11. Second quick example (sqrt(x^2 - a^2))

Integral:

∫ sqrt(x^2 - a^2) dx

Substitution:

x = a * cosh(t)
dx = a * sinh(t) dt

Then:

sqrt(x^2 - a^2)
= sqrt(a^2 * cosh^2(t) - a^2)
= a * sinh(t)

Integral becomes:

∫ a^2 * sinh^2(t) dt

Using:

sinh^2(t) = (cosh(2t) - 1) / 2

This leads to:

∫ sqrt(x^2 - a^2) dx
= (x/2) * sqrt(x^2 - a^2)

* (a^2/2) * arccosh(x / a)

- C

---

12. Summary table

## Expression              Substitution

sqrt(a^2 - x^2)         x = a * sin(t)
sqrt(x^2 + a^2)         x = a * sinh(t)
sqrt(x^2 - a^2)         x = a * cosh(t)


"""