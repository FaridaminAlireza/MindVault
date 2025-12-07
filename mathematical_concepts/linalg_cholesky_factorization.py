"""
Introduction:

Cholesky factorization (or Cholesky decomposition) is
a way to write a real symmetric positive-definite matrix A as
A = L L^T
where L is a real lower-triangular matrix 
with positive diagonal entries. 
Equivalently one may use an upper-triangular factor U 
and write A = U^T U; 
here I will use the lower-triangular L convention. 

Cholesky is a constructive and numerically stable method
to solve linear systems, compute determinants, and perform other 
matrix computations for symmetric positive-definite matrices.

Step-by-step constructive algorithm (n×n case)
Let A = (a_{ij}) be real, symmetric, and positive-definite.
We compute L = (ℓ_{ij}) lower-triangular (ℓ_{ij} = 0 for j>i)
by the following formulas, 
proceeding column by column (or row by row):

For k from 1 to n:

1. Compute the diagonal entry
   ℓ_{kk} = sqrt( a_{kk} − sum_{j=1}^{k-1} ℓ_{kj}^2 ).
   (Note: the expression under the square root
     must be positive for positive-definite A.)
2. For each row i = k+1, ..., n compute
   the subdiagonal entries in column k:
   ℓ_{ik} = ( a_{ik} − sum_{j=1}^{k-1} ℓ_{ij} ℓ_{kj} ) / ℓ_{kk}.

All other ℓ_{ij} with j>i remain zero; 
after finishing k=n we have L.

Comments on the formulas:
• The formulas come from equating 
  A = L L^T and comparing entries.

  Entry (i,k) of L L^T is 
  sum_{j=1}^{min(i,k)} ℓ_{ij} ℓ_{kj}; 

  for i=k that gives a_{kk} = sum_{j=1}^{k} ℓ_{kj}^2,
  hence ℓ_{kk}^2 = a_{kk} − sum_{j=1}^{k-1} ℓ_{kj}^2.

  For i>k the same comparison gives 
  a_{ik} = sum_{j=1}^{k} ℓ_{ij} ℓ_{kj}, 
  which rearranges to the formula for ℓ_{ik}.

Concrete insightful example (3×3, classic)
Let
A = [  4   12  −16
       12   37  −43
      −16  −43   98 ].

A is symmetric. We will compute L.

k = 1:
a_{11} = 4.
ℓ_{11} = sqrt(4) = 2.

For i = 2,3:
ℓ_{21} = a_{21} / ℓ_{11} = 12 / 2 = 6.
ℓ_{31} = a_{31} / ℓ_{11} = (−16) / 2 = −8.

So first column of L: [2, 6, −8]^T.

k = 2:
Compute ℓ_{22} from
ℓ_{22}^2 = a_{22} − ℓ_{21}^2 = 37 − 6^2 = 37 − 36 = 1,
so ℓ_{22} = 1 (we take positive root).

For i = 3:
ℓ_{32} = ( a_{32} − ℓ_{31} ℓ_{21} ) / ℓ_{22}
= (−43 − (−8)*6) / 1
= (−43 + 48) = 5.

k = 3:
ℓ_{33}^2 = a_{33} − (ℓ_{31}^2 + ℓ_{32}^2)
= 98 − ((−8)^2 + 5^2)
= 98 − (64 + 25) = 98 − 89 = 9,
so ℓ_{33} = 3.

Thus
L = [  2   0   0
       6   1   0
      −8   5   3 ].

Check quickly: L L^T reproduces A. 

Determinant of A equals product of
ℓ_{ii}^2 = 2^2 * 1^2 * 3^2 = 36; 
indeed det(A)=36.

"""

"""
## VISUAL / GEOMETRIC INTERPRETATION (intuition)

Think of a symmetric positive-definite matrix (A)
as encoding **inner products** between some list of
vectors (v_1,...,v_n) in Euclidean space. 
Concretely, there exist vectors (not unique) so that

```
a_{ij} = <v_i, v_j>
```

where `<·,·>` is the usual dot product. 
We call A a *Gram matrix* of these vectors.

Cholesky factorization (A = L L^T) 
can be seen as producing a new list of vectors
(u_1, u_2,..., u_n) (the columns of (L)) that
are **lower-triangular coordinates** relative 
to some orthonormal basis built step-by-step.

Geometrically each step does:

1. Start with the original vector (v_1). 
Its length squared is (a_{11} = |v_1|^2). 
Set (u_1) to be the vector along the first 
axis with length (\sqrt{a_{11}}). 
(So (u_1) encodes the norm of (v_1).)

   ASCII sketch (1D along first axis):

  
   v1  --->  length sqrt(a11)
   u1  --->  same length placed on axis 1
  

2. Now take (v_2). Decompose (v_2) into a part parallel to
 (u_1) and a part orthogonal to (u_1):

  
   v2 = (projection onto u1) + (remainder orthogonal to u1)
  

   The projection length onto (u_1) is encoded by
   the off-diagonal entry (a_{21}) relative to (\ell_{11}); 
   the orthogonal remainder has length squared equal 
   to (a_{22} - (\text{proj length})^2). 
   That remainder’s length is (\ell_{22}). 
   In coordinates: the column 2 of (L) contains the
   projection coefficients onto previous axes and the 
   new diagonal entry is the norm of the perpendicular remainder.

   ASCII sketch (2D):

  
   axis1 --->  u1
   axis2
      |
      |    remainder (perpendicular part)
      |   /
      |  /  v2 (original)
      | /
      |/ projection on u1
  

3. Continue: for (v_3), remove components along both 
(u_1) and (u_2); the leftover perpendicular 
component’s length is (\ell_{33}). 
The entries (\ell_{31}, \ell_{32}) store the projection
coefficients of (v_3) onto (u_1) and (u_2).

So each diagonal (\ell_{kk}) is the length (norm) of
the component of (v_k) orthogonal to the span of the
previous (u_1,\dots,u_{k-1}). 
Each subdiagonal (\ell_{ik}) (for (i>k)) 
is the coordinate (projection coefficient) 
of (v_i) onto the newly created axis (u_k). 
That’s exactly the Gram–Schmidt viewpoint: 
Cholesky is Gram–Schmidt applied to the (hypothetical)
vectors whose Gram matrix is (A), 
but keeping coordinates in a lower-triangular form.

Key geometric takeaways:

* Cholesky = build orthogonal axes step-by-step;
 diagonal entries are norms of 
 successive orthogonal remainders.
* The formula
 
  l_kk = sqrt( a_kk − sum_{j<k} l_kj^2 )
 
  says: “take the squared length of v_k, 
  subtract squared lengths of its projections onto
  previously built axes — what's left is
  squared length of the orthogonal remainder.”
* Positive-definiteness ensures at each step
 the remaining length is strictly positive 
 (so square root is real and nonzero).

---
## PROOF — PART 1: OVERVIEW + BASE CASE + IDEA FOR INDUCTION

**Goal.** Show that for any real symmetric positive-definite (A)
there exists a unique lower-triangular (L)
with strictly positive diagonal entries such that

```
A = L L^T.
```

I’ll prove this in two logical parts 
(uniqueness and existence). For now I’ll do:

* a short *intuition* for uniqueness,
* the *constructive existence* approach, and
* the detailed **base case** of the construction.

(We’ll do the full induction step and
 the rigorous uniqueness finish next.)

**Uniqueness — intuitive remark (preview)**
If two lower-triangular matrices with positive diagonals
produced the same (A), their ratio would be a 
lower-triangular orthogonal matrix. A lower-triangular 
orthogonal matrix with positive diagonal must be the identity,
so the two factors are equal. (I’ll give the explicit algebraic
short argument in the next chunk.)

**Existence — constructive plan (Gram–Schmidt picture)**
We will construct (L) column by column. 
Denote (L = (\ell_{ij})), with (\ell_{ij}=0) for (j>i).
For each k from 1 to n we will set:

1. For diagonal:
  
   l_kk = sqrt( a_kk − sum_{j=1}^{k-1} l_kj^2 )
  
   (this is the length of the orthogonal remainder 
   after removing projections onto columns 1..k-1.)

2. For rows below diagonal (i > k):
  
   l_ik = ( a_ik − sum_{j=1}^{k-1} l_ij * l_kj ) / l_kk
  
   (these are projection coefficients of 
   row i onto the new axis k).

Two things must be shown for this plan to succeed:

* (A) the quantity inside each square root is positive,
so l_kk is real and nonzero;
* (B) after computing column k the top-left k×k block of
L L^T matches that of A.

**Base case (k = 1) — fully explicit**

* Because (A) is positive-definite,
for the first standard basis vector (e_1) we have
 
  e1^T A e1 = a_11 > 0.
 
* Set
 
  l_11 = sqrt(a_11)    (positive)
 
* For i = 2..n set

 
  l_i1 = a_i1 / l_11.
 
* Now compute the first column of (L L^T):

  * Entry (1,1): (l_{11}^2 = a_{11}).
  * Entry (i,1): sum_{j=1}^{1} l_{ij} l_{1j} =
  l_{i1} l_{11} = (a_{i1}/l_{11}) * l_{11} = a_{i1}.
* So after this step the first row and
column of (L L^T) match those of (A).

This completes the base case. 
Everything is explicit and correct; 
note the diagonal entry is positive
 because A is positive-definite.

"""