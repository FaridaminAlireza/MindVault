"""
Newton-Raphson Method and Convergence Analysis

1. Newton-Raphson Iteration:
   x_{n+1} = x_n - f(x_n)/f'(x_n)

2. Fixed-Point Form:
   x_{n+1} = g(x_n), where g(x) = x - f(x)/f'(x)

3. Define Error:
   e_n = x_n - alpha  (alpha is the root where f(alpha)=0)

4. Taylor Expansion of g(x) around root alpha:
   g(x_n) = g(alpha + e_n) = g(alpha) + g'(alpha)*e_n + g''(alpha)/2 * e_n^2 + g'''(alpha)/6 * e_n^3 + ...
   Since g(alpha) = alpha:
   e_{n+1} = x_{n+1} - alpha = g'(alpha)*e_n + g''(alpha)/2 * e_n^2 + g'''(alpha)/6 * e_n^3 + ...

5. First Derivative g'(x):
   g'(x) = 1 - (f'(x)*f'(x) - f(x)*f''(x)) / (f'(x))^2 = f(x)*f''(x) / (f'(x))^2
   At x = alpha: g'(alpha) = 0

6. Implication of g'(alpha) = 0:
   Linear term in error vanishes => quadratic convergence

7. Second Derivative g''(alpha):
   g''(alpha) controls the constant factor in quadratic convergence

8. Third Derivative g'''(alpha):
   g'''(alpha) affects higher-order error terms for precise analysis

9. Error Iteration Summary:
   e_{n+1} = g'(alpha)*e_n + g''(alpha)/2 * e_n^2 + g'''(alpha)/6 * e_n^3 + ...
   For Newton-Raphson, e_{n+1} ~ g''(alpha)/2 * e_n^2 (quadratic)

10. Convergence Insights:

    * g'(alpha) < 1 => linear convergence
    * g'(alpha) = 0 => quadratic convergence
    * g''(alpha) gives proportionality of error shrinkage
    * g'''(alpha) shows higher-order corrections

11. Summary:
    Newton-Raphson is very fast near the root due to quadratic convergence.
    Evaluating g', g'', g''' at the root explains convergence speed and error behavior.
    Choosing a good initial guess ensures convergence.

"""