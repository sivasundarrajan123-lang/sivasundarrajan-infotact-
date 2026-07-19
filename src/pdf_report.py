import os
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4


# =====================================================
# STYLES
# =====================================================

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER
title_style.textColor = colors.white
title_style.spaceAfter = 20

heading_style = styles["Heading2"]
heading_style.textColor = colors.HexColor("#0B5ED7")

normal_style = styles["BodyText"]
normal_style.leading = 18

footer_style = styles["Italic"]
footer_style.alignment = TA_CENTER
footer_style.textColor = colors.grey

suggestion_style = styles["BodyText"]
suggestion_style.leading = 16
suggestion_style.leftIndent = 6


# =====================================================
# COLOR PALETTE (blue theme)
# =====================================================

PRIMARY_BLUE = colors.HexColor("#1565C0")
DARK_BLUE = colors.HexColor("#0D47A1")
LIGHT_BLUE = colors.HexColor("#E3F2FD")
ACCENT_BLUE = colors.HexColor("#0B5ED7")

GRADE_COLORS = {
    "A": colors.HexColor("#2E7D32"),
    "B": colors.HexColor("#558B2F"),
    "C": colors.HexColor("#F9A825"),
    "D": colors.HexColor("#EF6C00"),
    "F": colors.HexColor("#C62828"),
}


def _grade_color(grade):
    key = str(grade).strip().upper()[:1]
    return GRADE_COLORS.get(key, PRIMARY_BLUE)


# =====================================================
# MAIN REPORT GENERATOR
# =====================================================

def generate_pdf_report(
    file_name,
    variables,
    functions,
    classes,
    imports,
    loops,
    conditions,
    calls,
    suggestions,
    score,
    grade,
    output_path=None
):
    """
    Generates a professional, blue-themed PyChronicle PDF analysis report.

    Returns the path of the generated PDF.
    """

    os.makedirs("reports", exist_ok=True)

    if output_path is None:
        safe_name = os.path.splitext(os.path.basename(file_name))[0]
        output_path = f"reports/{safe_name}_analysis_report.pdf"

    pdf = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    elements = []

    # -------------------------------------------------
    # TITLE BANNER
    # -------------------------------------------------

    header = Table(
        [[
            Paragraph(
                "<b>📘 PYCHRONICLE</b><br/>"
                "<font size=13>"
                "Python Code Evolution &amp; Analysis Tool"
                "</font>",
                title_style
            )
        ]],
        colWidths=[7.2 * inch]
    )

    header.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PRIMARY_BLUE),
        ("BOX", (0, 0), (-1, -1), 2, DARK_BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
    ]))

    elements.append(header)
    elements.append(Spacer(1, 20))

    # -------------------------------------------------
    # DEVELOPER DETAILS
    # -------------------------------------------------

    info_data = [
        ["👨‍💻 Developer", "Siva Sundar Rajan"],
        ["📅 Analysis Date", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")],
        ["📄 File Name", file_name],
        ["⭐ Quality Grade", grade],
    ]

    info_table = Table(info_data, colWidths=[2.2 * inch, 4.8 * inch])

    info_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), LIGHT_BLUE),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
        ("GRID", (0, 0), (-1, -1), 1, colors.grey),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BACKGROUND", (1, 0), (1, -1), colors.whitesmoke),
    ]))

    elements.append(info_table)
    elements.append(Spacer(1, 25))

    # -------------------------------------------------
    # ANALYSIS SUMMARY
    # -------------------------------------------------

    elements.append(Paragraph("<b>📊 ANALYSIS SUMMARY</b>", heading_style))
    elements.append(Spacer(1, 10))

    summary = [
        ["Metric", "Count"],
        ["Variables", str(len(variables))],
        ["Functions", str(len(functions))],
        ["Classes", str(len(classes))],
        ["Imports", str(len(imports))],
        ["For Loops", str(loops["for"])],
        ["While Loops", str(loops["while"])],
        ["If Statements", str(conditions)],
        ["Function Calls", str(len(calls))],
    ]

    summary_table = Table(summary, colWidths=[4.5 * inch, 1.5 * inch])

    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PRIMARY_BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (1, 1), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 1, colors.grey),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.beige, colors.HexColor("#FDF6E3")]),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("TOPPADDING", (0, 1), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 8),
    ]))

    elements.append(summary_table)
    elements.append(Spacer(1, 25))

    # -------------------------------------------------
    # QUALITY SCORE CARD
    # -------------------------------------------------

    elements.append(Paragraph("<b>⭐ QUALITY SCORE CARD</b>", heading_style))
    elements.append(Spacer(1, 10))

    grade_color = _grade_color(grade)

    score_data = [[
        Paragraph(
            f"<para align='center'><font size=26 color='white'><b>{score}</b></font>"
            f"<br/><font size=10 color='white'>OUT OF 100</font></para>",
            normal_style
        ),
        Paragraph(
            f"<para align='center'><font size=26 color='white'><b>{grade}</b></font>"
            f"<br/><font size=10 color='white'>GRADE</font></para>",
            normal_style
        ),
    ]]

    score_table = Table(score_data, colWidths=[3.6 * inch, 3.6 * inch], rowHeights=[1.0 * inch])

    score_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), PRIMARY_BLUE),
        ("BACKGROUND", (1, 0), (1, 0), grade_color),
        ("BOX", (0, 0), (0, 0), 1.5, DARK_BLUE),
        ("BOX", (1, 0), (1, 0), 1.5, DARK_BLUE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))

    elements.append(score_table)
    elements.append(Spacer(1, 25))

    # -------------------------------------------------
    # SMART SUGGESTIONS
    # -------------------------------------------------

    elements.append(Paragraph("<b>💡 SMART SUGGESTIONS</b>", heading_style))
    elements.append(Spacer(1, 10))

    if suggestions:
        suggestion_rows = [
            [Paragraph(f"• {s}", suggestion_style)] for s in suggestions
        ]
    else:
        suggestion_rows = [
            [Paragraph("✅ No issues found — great job! Your code follows good practices.", suggestion_style)]
        ]

    suggestions_table = Table(suggestion_rows, colWidths=[7.2 * inch])

    suggestions_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F1F8FF")),
        ("BOX", (0, 0), (-1, -1), 1, PRIMARY_BLUE),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, colors.HexColor("#BBDEFB")),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
    ]))

    elements.append(suggestions_table)
    elements.append(Spacer(1, 30))

    # -------------------------------------------------
    # FOOTER
    # -------------------------------------------------

    elements.append(
        Paragraph(
            "Generated by <b>PyChronicle</b> — Python Code Evolution &amp; Analysis Tool",
            footer_style
        )
    )
    elements.append(
        Paragraph(
            f"Report generated on {datetime.now().strftime('%d %B %Y, %I:%M %p')}",
            footer_style
        )
    )

    # -------------------------------------------------
    # BUILD PDF
    # -------------------------------------------------

    pdf.build(elements)

    return output_path


# =====================================================
# DEMO / MANUAL TEST
# =====================================================

if __name__ == "__main__":
    demo_path = generate_pdf_report(
        file_name="example_script.py",
        variables=["x", "y", "z", "total"],
        functions=["main", "helper", "process_data"],
        classes=["DataProcessor"],
        imports=["os", "sys", "datetime"],
        loops={"for": 4, "while": 1},
        conditions=6,
        calls=["print", "len", "range", "open"],
        suggestions=[
            "Consider adding docstrings to all functions.",
            "Avoid using global variables where possible.",
            "Break down 'process_data' into smaller functions.",
        ],
        score=82,
        grade="A"
    )
    print(f"Report generated at: {demo_path}")