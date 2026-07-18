import ast

def extract_conditions(tree):
    count = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            count += 1

    return count