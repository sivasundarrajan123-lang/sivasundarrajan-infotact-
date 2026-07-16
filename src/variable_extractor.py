import ast
import builtins

def extract_variables(tree):
    variables = set()

    # Built-in function names (print, len, etc.)
    builtin_names = set(dir(builtins))

    # Function names
    function_names = {
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    }

    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if (
                node.id not in builtin_names
                and node.id not in function_names
                and node.id != "self"
            ):
                variables.add(node.id)

    return sorted(variables)