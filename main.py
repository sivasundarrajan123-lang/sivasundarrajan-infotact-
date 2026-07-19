from src.file_reader import read_python_file
from src.ast_parser import parse_python_code
from src.variable_extractor import extract_variables
from src.function_extractor import extract_functions
from src.class_extractor import extract_classes
from src.import_extractor import extract_imports
from src.loop_extractor import extract_loops
from src.condition_extractor import extract_conditions
from src.call_extractor import extract_function_calls
from src.report_generator import generate_report
from src.database_manager import create_database, save_analysis
from src.history_viewer import show_history 
from src.evolution import compare_latest_analysis
from src.suggestion_engine import generate_suggestions
from src.evolution import compare_latest_analysis
from src.quality_score import calculate_quality_score

from src.chart_generator import generate_chart

from src.pdf_report import generate_pdf_report


file_name = "tests/sample.py"

code = read_python_file(file_name)

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

print("\n" + "=" * 30)
print("Conditions Found")
print("=" * 30)

conditions = extract_conditions(tree)
print(f"If Statements : {conditions}")

print("\n" + "=" * 30)
print("Function Calls")
print("=" * 30)

calls = extract_function_calls(tree)

if calls:
    for call in calls:
        print(call)
else:
    print("No function calls found.")   

    print("\n" + "=" * 30)


# Generate Analysis Report
generate_report(
    "sample.py",
    variables,
    functions,
    classes,
    imports,
    loops,
    conditions,
    calls
)

save_analysis(
    file_name,
    variables,
    functions,
    classes,
    imports,
    loops["for"],
    loops["while"],
    conditions,
    calls
)

show_history()

compare_latest_analysis()





print("\n" + "=" * 30)
print("SMART SUGGESTIONS")
print("=" * 30)

suggestions = generate_suggestions(
    variables,
    functions,
    classes,
    imports,
    loops,
    conditions,
    calls
)

for suggestion in suggestions:
    print("•", suggestion)


generate_pdf_report(
    file_name,
    variables,
    functions,
    classes,
    imports,
    loops,
    conditions,
    calls,
    suggestions
)


score = calculate_quality_score(
    variables,
    functions,
    classes,
    imports,
    loops,
    conditions,
    calls
)

if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"

print("\n" + "=" * 40)
print("PYCHRONICLE QUALITY SCORE")
print("=" * 40)
print(f"Overall Score : {score}/100")
print(f"Grade         : {grade}")
print("=" * 40)


generate_chart(
    variables,
    functions,
    classes,
    imports
)