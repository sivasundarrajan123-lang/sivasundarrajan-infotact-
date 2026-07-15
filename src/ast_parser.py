import ast

code = """
x = 10
y = 20
z = x + y
print(z)
"""

tree = ast.parse(code)

print(ast.dump(tree, indent=4))