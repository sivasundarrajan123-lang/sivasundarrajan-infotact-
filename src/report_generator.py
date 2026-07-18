from datetime import datetime

def generate_report(file_name, variables, functions, classes,
                    imports, loops, conditions, calls):

    report = f"""
==================================================
           PyChronicle Analysis Report
==================================================

Analysis Time : {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
File Name     : {file_name}

SUMMARY
--------------------------------------------------
Variables        : {len(variables)}
Functions        : {len(functions)}
Classes          : {len(classes)}
Imports          : {len(imports)}
For Loops        : {loops['for']}
While Loops      : {loops['while']}
If Statements    : {conditions}
Function Calls   : {len(calls)}

VARIABLES
--------------------------------------------------
"""

    for var in variables:
        report += f"• {var}\n"

    report += "\nFUNCTIONS\n"
    report += "--------------------------------------------------\n"

    for func in functions:
        report += f"• {func}\n"

    report += "\nCLASSES\n"
    report += "--------------------------------------------------\n"

    for cls in classes:
        report += f"• {cls}\n"

    report += "\nIMPORTS\n"
    report += "--------------------------------------------------\n"

    for imp in imports:
        report += f"• {imp}\n"

    report += "\nFUNCTION CALLS\n"
    report += "--------------------------------------------------\n"

    for call in calls:
        report += f"• {call}\n"

    report += "\n==================================================\n"
    report += "Analysis Completed Successfully\n"
    report += "==================================================\n"

    with open("reports/analysis_report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print("\n✅ Report generated successfully!")
    print("📄 Saved as reports/analysis_report.txt")