import ast

code = "x = 10"
tree = ast.parse(code)

assert isinstance(tree, ast.Module)
print("AST test passed")