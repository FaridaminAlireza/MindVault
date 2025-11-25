"""
This includes:

1. The explanation of headings (definitions, lemmas, etc.)
2. The sample chapter layout
3. The worked example (differentiability ⇒ continuity)
4. Tips on reading math books
5. The mini-chapter on Graph Theory

---

University-level math books follow a structured 
logical format using headings such as Definition,
Example, Lemma, Proposition, Theorem, Proof, 
Corollary, Remark, and Exercises. 
 
 Here are the meanings:

Definition: Introduces a new concept or notation.
Remark: Optional clarification or intuition.
Example: Demonstrates a definition or concept.
Theorem: Major, central mathematical result.
Proposition: Important but not as central as a theorem.
Lemma: A helper result used to prove a larger theorem.
Corollary: A quick consequence of a theorem.
Proof: Logical argument showing why a statement is true.
Exercise: Problems for the reader to solve.

---
Sample Chapter Layout 
(Example from Real Analysis)

Chapter 4: Continuity

4.1 Definition of Continuity

* Definition: Limit of a function
* Definition: Continuity at a point
* Example: Polynomials are continuous
* Remark: Explanation of epsilon-delta

4.2 Properties of Continuous Functions

* Proposition: Sums/products of continuous functions
* Lemma: Bound differences technical lemma
* Theorem: Composition of continuous functions is continuous
* Corollary: Continuous functions preserve compactness

4.3 Uniform Continuity

* Definition: Uniform continuity
* Theorem (Heine–Cantor): Continuous functions on
compact sets are uniformly continuous
* Corollary: Uniform continuity implies continuity

4.4 Applications

* Example: Lipschitz functions
* Application in numerical analysis

Exercises: Ranging from basic to challenging.

---

Worked Example: Differentiability Implies Continuity

Definition: A function f is differentiable at a if the limit of 
(f(a+h) - f(a)) / h as h -> 0 exists. This is f'(a).

Lemma: If f is differentiable at a, then 
E(h) = f(a+h) - f(a) - f'(a)h approaches 0 as h -> 0.

Proof of Lemma: Rewrite difference quotient; 
the term E(h)/h -> 0, so E(h) -> 0.

Theorem: Differentiability at a implies continuity at a.

Proof: Write f(a+h) - f(a) = f'(a)h + E(h). 
Both terms -> 0. Therefore f(a+h) -> f(a).

Corollary: If f is differentiable everywhere on an interval,
it is continuous on that interval.

Exercises:

1. Show that the limit of |f(a+h) - f(a)| / |h| equals |f'(a)|.
2. Give an example of a continuous but nowhere differentiable function.
3. Prove polynomials are differentiable.

---

Tips for How to Read Math Books Effectively

1. Do not read linearly; skim examples and theorems first.
2. Rewrite definitions in your own words.
3. After each definition, create your own examples.
4. For proofs, track the goal, assumptions, and
how each assumption is used.
5. Break long proofs into smaller internal claims.
6. Do the exercises; they are essential for understanding.
7. When a theorem seems abstract, look for simple concrete cases.
8. Revisit chapters multiple times;
understanding deepens on repeated passes.

---

Mini-Chapter: Introduction to Graph Theory

1. Basic Definitions

Definition: A graph G = (V, E) consists of a set of vertices V
and a set of edges E, where each edge is a 2-element subset of V.

Definition: Two vertices are adjacent if an edge connects them.
Edges are incident to their endpoints.

Definition: The degree of a vertex is the number of
edges incident to it.

Example: For V = {1,2,3,4} and edges {1,2}, {2,3}, {2,4},
vertex 2 has degree 3.

Remark: Graphs model networks of many types.

2. Paths, Cycles, Connectivity

Definition: A path is a sequence of distinct vertices
where consecutive vertices share edges.

Definition: A cycle is a closed path of length at least 3.

Definition: A graph is connected if a path exists between
every pair of vertices.

Lemma: Removing a single edge from a cycle
does not disconnect the graph.

Proof: The remaining edges of the cycle still provide
a path between the endpoints of the removed edge.

3. Trees

Definition: A tree is a connected graph with no cycles.

Theorem (Equivalent characterizations of trees):
For a graph with n vertices, the following are equivalent:

1. It is a tree.
2. It is connected and acyclic.
3. It is connected with n - 1 edges.
4. It is acyclic with n - 1 edges.
5. There is exactly one path between any two vertices.

Proof: Outline showing equivalences via induction and
cycle removal logic.

Corollary: Every tree with n vertices has n - 1 edges.

Example: A linear chain of 5 vertices is a tree with 4 edges.

4. Degree Properties

Theorem (Handshake Lemma): The sum of all vertex degrees
equals 2 times the number of edges.

Proof: Each edge contributes 2 to the total degree count.

Corollary: The number of vertices of odd degree is even.

Proof: Even sums can only arise
from an even number of odd terms.

5. Exercises

6. Is it possible to have exactly three
vertices of odd degree? Explain why or why not.

7. Construct a connected graph with five vertices
containing exactly one cycle.

8. Prove that any tree with at least two vertices
has at least two leaves.

9. Give an example of a connected graph with 7
vertices and 7 edges that is not a tree.

10. Show that a graph is a tree if and only if
adding any edge creates exactly one cycle.

"""