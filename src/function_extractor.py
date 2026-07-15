import ast

def extract_functions(tree):
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

    return sorted(functions)