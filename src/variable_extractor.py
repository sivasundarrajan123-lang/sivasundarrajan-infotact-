import ast

def extract_variables(tree):
    variables = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            variables.add(node.id)

    return sorted(variables)