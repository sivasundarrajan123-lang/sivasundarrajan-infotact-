import ast

def extract_loops(tree):
    loops = {
        "for": 0,
        "while": 0
    }

    for node in ast.walk(tree):
        if isinstance(node, ast.For):
            loops["for"] += 1
        elif isinstance(node, ast.While):
            loops["while"] += 1

    return loops