import ast

code = """
x = 10
y = 20
z = x + y
print(z)
"""

tree = ast.parse(code)

print("Variables Found:")

variables = set()

for node in ast.walk(tree):
    if isinstance(node, ast.Name):
        variables.add(node.id)

for variable in sorted(variables):
    print(variable)