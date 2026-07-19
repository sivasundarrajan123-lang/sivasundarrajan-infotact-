def generate_suggestions(
    variables,
    functions,
    classes,
    imports,
    loops,
    conditions,
    calls
):
    suggestions = []

    # Classes
    if len(classes) == 0:
        suggestions.append("Consider using classes for better code organization.")
    else:
        suggestions.append("Good use of classes.")

    # Functions
    if len(functions) == 0:
        suggestions.append("Consider creating functions to improve modularity.")
    else:
        suggestions.append("Functions are well organized.")

    # Imports
    if len(imports) > 5:
        suggestions.append("Too many imports. Remove unused modules.")

    # Variables
    if len(variables) > 10:
        suggestions.append("Large number of variables. Consider refactoring.")

    # Loops
    total_loops = loops["for"] + loops["while"]

    if total_loops > 5:
        suggestions.append("Too many loops. Check if logic can be simplified.")

    # Conditions
    if conditions == 0:
        suggestions.append("No conditional statements found.")

    # Function Calls
    if len(calls) == 0:
        suggestions.append("No function calls detected.")

    return suggestions