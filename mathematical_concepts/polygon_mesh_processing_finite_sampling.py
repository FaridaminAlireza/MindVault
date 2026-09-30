"""
Finite sampling is the process of replacing a continuous geometric 
object by a finite set of samples that can be stored and processed 
on a computer. 

Since a surface contains infinitely many points, 
we approximate it using discrete elements 
whose density determines the accuracy of the representation.

For a parametric surface S(u,v) = (x(u,v), y(u,v), z(u,v))
defined over a parameter domain D, finite sampling selects a finite 
set of parameter values (u_i, v_j). Evaluating the surface 
at these samples produces vertices P_ij = S(u_i, v_j).

Neighboring samples are connected to form triangles, 
producing a triangular mesh approximation. 
If the parameter spacing is
Δu = u_(i+1) - u_i,
Δv = v_(j+1) - v_j,
then each small parameter rectangle is divided 
into two triangles. As Δu and Δv approach zero, 
the mesh converges to the original surface 
because continuity implies

lim_(Δu,Δv→0) ||S(u,v) - S_h(u,v)|| = 0,

where S_h denotes the piecewise-linear mesh approximation.

The error is controlled by the local curvature: 
flatter regions can be represented accurately 
with fewer triangles, while highly curved regions 
require denser sampling.

---
For an implicit surface f(x,y,z) = 0,
the geometry is not given explicitly by points 
but by the zero level set of a scalar field. 

Finite sampling therefore discretizes space 
rather than the surface itself. 

A regular grid is created with spacing h, 
and the function is evaluated at grid points
f(ih, jh, kh).

This produces a voxel representation 
of the scalar field. The surface is 
then reconstructed from the sampled values 
by locating where sign changes occur: f(p₁)f(p₂) < 0.

A sign change indicates that the surface crosses 
the edge connecting p₁ and p₂. 

By the Intermediate Value Theorem, if f is continuous 
and the values at two endpoints have opposite signs,
there exists a point between them where f = 0. 
This provides the mathematical justification 
for surface extraction methods such as Marching Cubes.

In a uniform grid, the spacing h is constant everywhere.
The number of samples grows as O(n³), where n is the resolution 
along one axis. Uniform sampling is simple but inefficient 
because flat regions receive the same number of samples 
as detailed regions.

Adaptive grids solve this problem by varying the sampling density.
Space is recursively subdivided only where the scalar field changes
rapidly or where the surface passes through a cell.
If a cell satisfies an error criterion E(cell) > ε,
it is subdivided into smaller cells; 
otherwise it is kept unchanged. 
This creates a hierarchy of cells with different sizes. 
The approximation error decreases as cell size decreases,
while the total number of samples becomes concentrated 
near geometrically important regions. 
Mathematically, if h(x) denotes the local cell size,
then regions with larger curvature or larger variation of f 
receive smaller h(x), yielding higher accuracy for the same 
memory cost.

Thus, finite sampling in the parametric case discretizes 
the parameter domain and approximates the surface with 
triangular meshes, 

while finite sampling in the implicit case discretizes 
the surrounding volume using uniform or adaptive grids 
and reconstructs the surface from sampled scalar values.

Both approaches replace an infinite geometric object by 
a finite set of samples whose approximation 
error decreases as the sampling density increases.
"""