#  Abstract Syntax Tree (AST)
# a tree representation of your code’s structure,
# where each node represents a syntactic construct — 
# like a function, loop, variable, or expression.

# Python provides a built-in ast module.

# Ex1
import ast
source = "x = 1 + 2 * 3"
tree = ast.parse(source)
print(ast.dump(tree, indent=4))

# Ex2. Detect function definitions
import ast

code = """
def foo():
    return 42

x = lambda y: y*2
"""

tree = ast.parse(code)
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        print(f"Found function: {node.name}")
    if isinstance(node, ast.Lambda):
        print(f"Found lambda function: {node}")
