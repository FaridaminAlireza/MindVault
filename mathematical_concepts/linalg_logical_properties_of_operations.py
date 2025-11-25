"""
Here’s a list of common mathematical properties
each describing how an operation behaves:

1. Commutative – The order of operands doesn’t matter.
Example: a + b = b + a

2. Associative – The grouping of operands doesn’t matter.
Example: (a + b) + c = a + (b + c)

3. Distributive – One operation distributes over another.
Example: a × (b + c) = a×b + a×c

4. Identity – There exists an element that leaves others unchanged under an operation.
Example: a + 0 = a

5. Inverse – For every element, there’s another that “undoes” it.
Example: a + (−a) = 0

6. Idempotent – Applying the operation multiple times has the same effect as once.
Example: a ∪ a = a (in set theory)

7. Absorptive (or Absorption law) – One operation absorbs another.
Example: a ∪ (a ∩ b) = a

8. Disjoint – Elements or sets that have nothing in common.
Example: A ∩ B = ∅

9. Reflexive – A relation that relates every element to itself.
Example: a = a

10. Symmetric – A relation that holds both ways.
Example: If a = b, then b = a

11. Transitive – A relation that passes through.
Example: If a = b and b = c, then a = c

These properties are used across algebra,
logic, and set theory to describe how 
operations or relations behave.

---
Categorizes list of properties:


# Comprehensive List of Mathematical Properties
---
1. Properties of Binary Operations

These describe how two operands interact under an operation
 (like addition, multiplication, union, etc.).

# Basic Algebraic Properties

* Commutative — a ⋅ b = b ⋅ a
* Associative — (a ⋅ b) ⋅ c = a ⋅ (b ⋅ c)
* Distributive — a ⋅ (b + c) = a⋅b + a⋅c
* Left distributive — a ⋅ (b + c) = a⋅b + a⋅c
* Right distributive — (a + b) ⋅ c = a⋅c + b⋅c

# Identity and Inverses

* Identity element — ∃ e such that a ⋅ e = e ⋅ a = a
* Left identity — e ⋅ a = a
* Right identity — a ⋅ e = a
* Inverse element — ∃ a⁻¹ such that a ⋅ a⁻¹ = e
* Left inverse — a⁻¹ ⋅ a = e
* Right inverse — a ⋅ a⁻¹ = e

# Other Operational Properties

* Idempotent — a ⋅ a = a
* Absorptive — a ⋅ (a + b) = a
* Annihilating (zero) element — a ⋅ 0 = 0 ⋅ a = 0
* Cancellative — a ⋅ b = a ⋅ c ⇒ b = c
* Distributive over itself — (a + b) + c = a + (b + c) 
(when both operations are the same)
* Closure — a ⋅ b ∈ S for all a, b ∈ S

# Order-Specific

* Non-commutative — a ⋅ b ≠ b ⋅ a
* Non-associative — (a ⋅ b) ⋅ c ≠ a ⋅ (b ⋅ c)

---
2. Properties of Relations

Describe how pairs of elements relate to one another 
(used for =, <, ≤, ∈, etc.).

* Reflexive — a R a
* Irreflexive — ¬(a R a)
* Symmetric — a R b ⇒ b R a
* Asymmetric — a R b ⇒ ¬(b R a)
* Antisymmetric — a R b ∧ b R a ⇒ a = b
* Transitive — a R b ∧ b R c ⇒ a R c
* Trichotomous — exactly one of (a R b), (a = b), or (b R a) holds
* Connex (Total) — for any a, b, a R b ∨ b R a
* Equivalence relation — reflexive, symmetric, transitive
* Partial order — reflexive, antisymmetric, transitive
* Total order — partial order + connex
* Well-order — total order where every non-empty subset has a least element

---
3. Logical and Boolean Properties
Used in propositional logic and Boolean algebra.

* Commutative laws — A ∧ B = B ∧ A; A ∨ B = B ∨ A
* Associative laws — (A ∧ B) ∧ C = A ∧ (B ∧ C)
* Distributive laws — A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C)
* Identity laws — A ∨ false = A; A ∧ true = A
* Domination laws — A ∨ true = true; A ∧ false = false
* Idempotent laws — A ∨ A = A; A ∧ A = A
* Negation laws — ¬(¬A) = A
* Complement laws — A ∨ ¬A = true; A ∧ ¬A = false
* De Morgan’s laws — ¬(A ∧ B) = ¬A ∨ ¬B; ¬(A ∨ B) = ¬A ∧ ¬B
* Absorption laws — A ∨ (A ∧ B) = A; A ∧ (A ∨ B) = A
* Double negation — ¬(¬A) = A
* Contrapositive — (A ⇒ B) ≡ (¬B ⇒ ¬A)
* Implication identity — A ⇒ B ≡ ¬A ∨ B

---
4. Set-Theoretic Properties
Used for union (∪), intersection (∩), and complement (′).

* Commutative — A ∪ B = B ∪ A; A ∩ B = B ∩ A
* Associative — (A ∪ B) ∪ C = A ∪ (B ∪ C)
* Distributive — A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
* Identity — A ∪ ∅ = A; A ∩ U = A
* Domination — A ∪ U = U; A ∩ ∅ = ∅
* Idempotent — A ∪ A = A; A ∩ A = A
* Complement laws — A ∪ A′ = U; A ∩ A′ = ∅
* Absorption — A ∪ (A ∩ B) = A
* De Morgan’s laws — (A ∪ B)′ = A′ ∩ B′
* Difference — A − B = A ∩ B′
* Symmetric difference — A Δ B = (A ∪ B) − (A ∩ B)

---
5. Function Properties
Used in calculus, linear algebra, and abstract algebra.

* Injective (one-to-one) — f(a) = f(b) ⇒ a = b
* Surjective (onto) — ∀ y ∈ Y, ∃ x ∈ X: f(x) = y
* Bijective — injective + surjective
* Even function — f(−x) = f(x)
* Odd function — f(−x) = −f(x)
* Monotonic — increasing or decreasing
* Periodic — f(x + T) = f(x)
* Continuous — no breaks or jumps
* Differentiable — derivative exists everywhere
* Linear — f(a + b) = f(a) + f(b); f(ka) = kf(a)
* Homogeneous — f(ka) = kⁿf(a) (degree n)

---
6. Structural (Algebraic) Properties
Used in abstract algebra to define structures.

* Closure
* Associativity
* Commutativity
* Existence of identity
* Existence of inverses
* Distributivity

# Based on these, we define:

* Semigroup — closure + associativity
* Monoid — semigroup + identity
* Group — monoid + inverses
* Abelian group — group + commutativity
* Ring — two operations (addition, multiplication) with distributivity
* Field — ring where every nonzero element has a multiplicative inverse
* Vector space — field + vector addition + scalar multiplication
* Module / Algebra — generalizations of vector spaces


1. Closure
* Definition: Performing the operation on elements of the set stays within the set.
* Example: Integers under addition: for any a, b ∈ ℤ, a + b ∈ ℤ.
* Used in: Semigroup, group, ring, field.

2. Associativity
* Definition: Grouping of elements does not affect the result.
* Example: (2 + 3) + 4 = 2 + (3 + 4) under addition of integers.
* Used in: Semigroup, group, ring, field.

3. Commutativity
* Definition: Order of elements does not affect the result.
* Example: 2 + 3 = 3 + 2 in integers under addition.
* Used in: Abelian group, commutative ring, field.

4. Existence of Identity
* Definition: There exists an element e such that a ⋅ e = e ⋅ a = a.
* Example: 0 is the additive identity in integers: a + 0 = a. 1 
is the multiplicative identity in nonzero real numbers: a × 1 = a.
* Used in: Monoid, group, ring, field.

5. Existence of Inverses
* Definition: For each element, there exists an element that
 “undoes” it under the operation.
* Example: For integers under addition, the additive inverse of 5 
is −5: 5 + (−5) = 0. For nonzero real numbers under multiplication, 
the multiplicative inverse of 2 is 1/2: 2 × 1/2 = 1.
* Used in: Group, Abelian group, field.

6. Distributivity
* Definition: One operation distributes over another operation.
* Example: Multiplication distributes over addition: 2 × (3 + 4) = 2×3 + 2×4.
* Used in: Ring, field.


* Semigroup: closure + associativity
* Example: (ℕ, +) — natural numbers under addition.

* Monoid: semigroup + identity
* Example: (ℕ₀, +) — natural numbers including 0 under addition.

* Group: monoid + inverses
* Example: (ℤ, +) — integers under addition.

* Abelian (commutative) group: group + commutativity
* Example: (ℤ, +) — integers under addition.

* Ring: two operations (addition and multiplication) with distributivity
* Example: (ℤ, +, ×) — integers with addition and multiplication.

* Field: ring + multiplicative inverses for nonzero elements
* Example: (ℝ, +, ×) — real numbers with standard addition and multiplication.

---
7. Miscellaneous and Specialized Properties

* Orthogonal — A ⊥ B ⇒ A · B = 0
* Symmetric matrix — Aᵀ = A
* Skew-symmetric matrix — Aᵀ = −A
* Hermitian — A† = A (complex analog)
* Unitary — A†A = I
* Orthogonal matrix — AᵀA = I
* Idempotent matrix — A² = A
* Nilpotent — Aⁿ = 0 for some n
* Diagonalizable — A = P D P⁻¹
* Normal matrix — A†A = AA†



"""