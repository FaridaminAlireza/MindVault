"""
# Matrix Definiteness and Quadratic Forms

1. Quadratic Form

For a square matrix A and vector x (x ≠ 0), the quadratic form is:

    Q(x) = x^T A x

- x is a point/vector in space.
- Q(x) can be thought of as the "height" of a surface defined by A at point x.
- This is why definiteness of A is linked to "bowl up", "bowl down", or "saddle" shapes.

---
2. Intuition: Why Q(x) is like height

- Think of x as a vector from the origin.
- Q(x) = x^T A x measures a "curvature along x".
- If Q(x) > 0 for all x ≠ 0 → surface always goes "up" (bowl up).
- If Q(x) < 0 → surface always goes "down" (bowl down).
- If Q(x) > 0 in some directions and < 0 in others → saddle (indefinite).

Example 1: Identity matrix (simple bowl)

    A = [[1, 0],
         [0, 1]]
    Q(x) = x1^2 + x2^2
    - At (1,0) → Q = 1
    - At (0,2) → Q = 4
    Surface: symmetric bowl, height increases with distance from origin.

Example 2: Stretch/Compression

    A = [[2, 0],
         [0, 3]]
    Q(x) = 2*x1^2 + 3*x2^2
    - Along x1 axis, height increases twice as fast.
    - Along x2 axis, height increases three times as fast.
    Surface: stretched bowl.

Example 3: Rotation

    A = [[2, 1],
         [1, 2]]
    - Eigenvalues = 3, 1 → positive definite
    - Q(x) = 2*x1^2 + 2*x2^2 + 2*x1*x2
    - The principal axes are rotated → "bowl" rotated in the plane.

---
3. Types of Definiteness

| Type                        | Condition on Q(x)    | Eigenvalues       | Intuition / Shape        
|-----------------------------|----------------------|-------------------|--------------------------
| Positive Definite (PD)      | Q(x) > 0 ∀ x ≠ 0     | all > 0           | Bowl up                  
| Positive Semi-Definite (PSD)| Q(x) ≥ 0 ∀ x         | all ≥ 0           | Bowl up, flat directions 
| Negative Definite (ND)      | Q(x) < 0 ∀ x ≠ 0     | all < 0           | Bowl down                
| Negative Semi-Definite (NSD)| Q(x) ≤ 0 ∀ x         | all ≤ 0           | Bowl down, flat directions 
| Indefinite   | Q(x) > 0 for some x, < 0 for some x | mixed signs       | Saddle                    

---

4. Examples with intuition

Positive Definite  

    A = [[2,0],[0,3]]
    Q([1,1]) = 2*1^2 + 3*1^2 = 5 > 0
    - "Bowl up", stable minimum.
    - Application: optimization (minimization of quadratic form).

Positive Semi-Definite  

    A = [[1,0],[0,0]]
    Q([0,1]) = 0
    - Flat along y-axis, curved along x-axis.
    - Application: covariance matrices in statistics (spread ≥ 0).

Negative Definite  

    A = [[-2,0],[0,-3]]
    Q([1,1]) = -2 - 3 = -5 < 0
    - "Bowl down", single maximum.
    - Application: maximization problems.

Negative Semi-Definite  

    A = [[-1,0],[0,0]]
    Q([0,1]) = 0
    - Flat along y-axis, downward along x-axis.

Indefinite  

    A = [[1,0],[0,-1]]
    Q([1,0]) = 1 > 0
    Q([0,1]) = -1 < 0
    - Saddle shape: up in some directions, down in others.
    - Application: saddle-point problems, game theory, optimization.
---
5. Eigenvalues and definiteness

- Positive definite → all eigenvalues > 0  
- Positive semi-definite → all eigenvalues ≥ 0  
- Negative definite → all eigenvalues < 0  
- Negative semi-definite → all eigenvalues ≤ 0  
- Indefinite → mixed positive and negative eigenvalues  

Eigenvalues tell you curvature along principal axes:  
- Big eigenvalue → steep direction  
- Zero eigenvalue → flat direction  
- Negative → downward curvature

---
6. Geometric Summary

- Positive → “uphill”  
- Negative → “downhill”  
- Semi-definite → some flat directions  
- Indefinite → saddle, mixed curvature  

- Quadratic form Q(x) = x^T A x encodes the
height of the surface along vector x.
- Stretching / compression → different scaling along axes
(controlled by eigenvalues)
- Rotation → principal axes of the surface rotated 
(off-diagonal elements in A)

---
7. Applications

1. Optimization:  
   - PD → unique minimum, ND → unique maximum, Indefinite → saddle point.  
2. Physics / Mechanics:  
   - Potential energy surfaces near equilibrium are quadratic;
     definiteness → stability.  
3. Statistics / ML:  
   - Covariance matrices PSD → measure spread, variance ≥ 0.  
4. Economics / Game Theory:  
   - Saddle points in payoff matrices → indefinite Hessians.

---
8. Visual intuition (2D surface analogy)

- PD: bowl up  
- PSD: bowl up, flat along some axes  
- ND: bowl down  
- NSD: bowl down, flat along some axes  
- Indefinite: saddle  

Stretching/compression → different steepness along axes  
Rotation → principal axes of surface rotated in space

---
9. Summary

| Type | Q(x) | Eigenvalues | Shape | Example |
|------|------|-------------|-------|---------|
| PD | >0 | all >0 | Bowl up | [[2,0],[0,3]] |
| PSD | ≥0 | all ≥0 | Bowl up, flat | [[1,0],[0,0]] |
| ND | <0 | all <0 | Bowl down | [[-2,0],[0,-3]] |
| NSD | ≤0 | all ≤0 | Bowl down, flat | [[-1,0],[0,0]] |
| Indefinite | mixed | ± | Saddle | [[1,0],[0,-1]] |

"""