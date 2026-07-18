import ast
import builtins

def extract_variables(tree):
    variables = set()

    builtin_names = set(dir(builtins))

    function_names = {
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    }

    imported_names = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_names.add(alias.asname or alias.name)

        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                imported_names.add(alias.asname or alias.name)

    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if (
                node.id not in builtin_names
                and node.id not in function_names
                and node.id not in imported_names
                and node.id != "self"
            ):
                variables.add(node.id)

    return sorted(variables)