def calculate_quality_score(
    variables,
    functions,
    classes,
    imports,
    loops,
    conditions,
    calls
):
    score = 0

    # Variables (15)
    if len(variables) >= 3:
        score += 15
    else:
        score += len(variables) * 5

    # Functions (20)
    if len(functions) >= 3:
        score += 20
    else:
        score += len(functions) * 7

    # Classes (15)
    if len(classes) > 0:
        score += 15

    # Imports (10)
    if len(imports) > 0:
        score += 10

    # Code Structure (20)
    if loops["for"] + loops["while"] > 0:
        score += 10

    if conditions > 0:
        score += 10

    # Function Calls (20)
    if len(calls) >= 3:
        score += 20
    else:
        score += len(calls) * 6

    return min(score, 100)