import ast

def parse_python_code(code):
    """
    Parse Python source code into an AST.
    """
    return ast.parse(code)