from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(
    file_name,
    variables,
    functions,
    classes,
    imports,
    loops,
    conditions,
    calls,
    suggestions
):
    doc = SimpleDocTemplate("reports/analysis_report.pdf")
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>PyChronicle Analysis Report</b>", styles["Heading1"]))
    elements.append(Paragraph(f"<b>File:</b> {file_name}", styles["Normal"]))
    elements.append(Paragraph("<br/>", styles["Normal"]))

    elements.append(Paragraph("<b>Summary</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Variables: {len(variables)}", styles["Normal"]))
    elements.append(Paragraph(f"Functions: {len(functions)}", styles["Normal"]))
    elements.append(Paragraph(f"Classes: {len(classes)}", styles["Normal"]))
    elements.append(Paragraph(f"Imports: {len(imports)}", styles["Normal"]))
    elements.append(Paragraph(f"For Loops: {loops['for']}", styles["Normal"]))
    elements.append(Paragraph(f"While Loops: {loops['while']}", styles["Normal"]))
    elements.append(Paragraph(f"If Statements: {conditions}", styles["Normal"]))
    elements.append(Paragraph(f"Function Calls: {len(calls)}", styles["Normal"]))

    elements.append(Paragraph("<br/>", styles["Normal"]))
    elements.append(Paragraph("<b>Smart Suggestions</b>", styles["Heading2"]))

    for suggestion in suggestions:
        elements.append(Paragraph(f"• {suggestion}", styles["Normal"]))

    doc.build(elements)

    print("✅ PDF Report Generated Successfully!")