from src.file_reader import read_python_file
from src.ast_parser import parse_python_code
from src.variable_extractor import extract_variables
from src.function_extractor import extract_functions
from src.class_extractor import extract_classes
from src.import_extractor import extract_imports
from src.loop_extractor import extract_loops

# Read Python source file
code = read_python_file("tests/sample.py")

# Parse source code into AST
tree = parse_python_code(code)

# Display Variables
print("=" * 30)
print("Variables Found")
print("=" * 30)

variables = extract_variables(tree)

if variables:
    for variable in variables:
        print(variable)
else:
    print("No variables found.")

# Display Functions
print("\n" + "=" * 30)
print("Functions Found")
print("=" * 30)

functions = extract_functions(tree)

if functions:
    for function in functions:
        print(function)
else:
    print("No functions found.")

    print("\n" + "=" * 30)
print("Classes Found")
print("=" * 30)

classes = extract_classes(tree)

if classes:
    for cls in classes:
        print(cls)
else:
    print("No classes found.")

    print("\n" + "=" * 30)
print("Imports Found")
print("=" * 30)

imports = extract_imports(tree)

if imports:
    for module in imports:
        print(module)
else:
    print("No imports found.")

    print("\n" + "=" * 30)
print("Loops Found")
print("=" * 30)

loops = extract_loops(tree)

print(f"For Loops   : {loops['for']}")
print(f"While Loops : {loops['while']}")