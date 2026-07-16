import ast

def extract_classes(tree):
    classes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            classes.append(node.name)

    return sorted(classes)