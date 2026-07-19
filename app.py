import ast
import os
import pandas as pd
import plotly.express as px
import streamlit as st

from src.variable_extractor import extract_variables
from src.function_extractor import extract_functions
from src.class_extractor import extract_classes
from src.import_extractor import extract_imports
from src.loop_extractor import extract_loops
from src.condition_extractor import extract_conditions
from src.call_extractor import extract_function_calls

from src.quality_score import calculate_quality_score
from src.suggestion_engine import generate_suggestions
from src.chart_generator import generate_chart
from src.pdf_report import generate_pdf_report

from src.database_manager import (
    create_database,
    save_analysis,
    get_analysis_history,
    get_latest_two_records
)

st.set_page_config(
    page_title="PyChronicle",
    page_icon="📘",
    layout="wide"
)

LOGO_PATH = "assets/logo.png"

# -----------------------------
# Custom Styling (dark-blue sidebar)
# -----------------------------

st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0D47A1 0%, #1565C0 55%, #0B3C8A 100%);
    }
    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    section[data-testid="stSidebar"] .stAlert {
        background-color: rgba(255, 255, 255, 0.10);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 10px;
    }
    section[data-testid="stSidebar"] hr {
        border-color: rgba(255, 255, 255, 0.25);
    }
    .pc-header-title {
        font-size: 34px;
        font-weight: 800;
        color: #0D47A1;
        margin-bottom: 0px;
    }
    .pc-header-sub {
        font-size: 16px;
        color: #555555;
        margin-top: 0px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------

if os.path.exists(LOGO_PATH):
    st.sidebar.image(LOGO_PATH, use_container_width=True)
else:
    st.sidebar.title("📘 PyChronicle")

st.sidebar.caption("Version 1.0")

st.sidebar.markdown("---")

st.sidebar.info("""
👨‍💻 **Developer**

Siva Sundar Rajan

**Technology**
- Python
- AST
- Streamlit
- SQLite
- ReportLab
- Plotly
""")

st.sidebar.markdown("---")
st.sidebar.success("Python Code Evolution & Analysis Tool")

# -----------------------------
# Main Title (logo top-left + title)
# -----------------------------

logo_col, title_col = st.columns([1, 6])

with logo_col:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=80)
    else:
        st.write("📘")

with title_col:
    st.markdown('<p class="pc-header-title">PyChronicle</p>', unsafe_allow_html=True)
    st.markdown('<p class="pc-header-sub">Python Code Evolution &amp; Analysis Tool</p>', unsafe_allow_html=True)

st.markdown("---")

uploaded_file = st.file_uploader(
    "📂 Upload a Python (.py) file",
    type=["py"]
)

if uploaded_file is not None:

    code = uploaded_file.read().decode("utf-8")

    # ----------------------------------------
    # SAFE PARSE (handles broken/invalid .py files)
    # ----------------------------------------

    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        st.error(
            f"❌ Could not parse '{uploaded_file.name}'. "
            f"It has a Python syntax error: {e}"
        )
        st.stop()

    variables = extract_variables(tree)
    functions = extract_functions(tree)
    classes = extract_classes(tree)
    imports = extract_imports(tree)
    loops = extract_loops(tree)
    conditions = extract_conditions(tree)
    calls = extract_function_calls(tree)

    create_database()

    save_analysis(
        uploaded_file.name,
        variables,
        functions,
        classes,
        imports,
        loops["for"],
        loops["while"],
        conditions,
        calls
    )

    st.success(f"✅ Uploaded Successfully : {uploaded_file.name}")

    # ----------------------------------------
    # ANALYSIS SUMMARY
    # ----------------------------------------

    st.header("📊 Analysis Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric("Variables", len(variables))
    c2.metric("Functions", len(functions))
    c3.metric("Classes", len(classes))

    c4, c5, c6 = st.columns(3)

    c4.metric("Imports", len(imports))
    c5.metric("For Loops", loops["for"])
    c6.metric("While Loops", loops["while"])

    st.metric("If Statements", conditions)

    # ----------------------------------------
    # QUALITY SCORE
    # ----------------------------------------

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

    st.markdown("---")
    st.header("⭐ PyChronicle Quality Score")

    q1, q2 = st.columns(2)

    q1.metric("Overall Score", f"{score}/100")
    q2.metric("Grade", grade)

    # ----------------------------------------
    # SMART SUGGESTIONS
    # ----------------------------------------

    st.markdown("---")
    st.header("💡 Smart Suggestions")

    suggestions = generate_suggestions(
        variables,
        functions,
        classes,
        imports,
        loops,
        conditions,
        calls
    )

    if suggestions:
        for suggestion in suggestions:
            st.success(suggestion)
    else:
        st.info("No suggestions available.")

    # ----------------------------------------
    # ANALYSIS CHART
    # ----------------------------------------

    st.markdown("---")
    st.header("📊 Analysis Chart")

    generate_chart(
        variables,
        functions,
        classes,
        imports
    )

    if os.path.exists("reports/analysis_chart.png"):
        st.image(
            "reports/analysis_chart.png",
            caption="PyChronicle Analysis Chart",
            use_container_width=True
        )
    else:
        st.warning("Chart not found.")

    # ----------------------------------------
    # PIE / BAR COMPARISON CHART
    # ----------------------------------------

    st.markdown("---")
    st.header("🥧 Code Composition Comparison")

    composition_df = pd.DataFrame({
        "Element": ["Variables", "Functions", "Classes", "Imports"],
        "Count": [len(variables), len(functions), len(classes), len(imports)]
    })

    activity_df = pd.DataFrame({
        "Element": ["For Loops", "While Loops", "If Statements", "Function Calls"],
        "Count": [loops["for"], loops["while"], conditions, len(calls)]
    })

    pie_col, bar_col = st.columns(2)

    with pie_col:
        fig_pie = px.pie(
            composition_df,
            names="Element",
            values="Count",
            title="Code Composition",
            color_discrete_sequence=px.colors.sequential.Blues_r,
            hole=0.35
        )
        fig_pie.update_traces(textinfo="percent+label")
        st.plotly_chart(fig_pie, use_container_width=True)

    with bar_col:
        fig_bar = px.bar(
            activity_df,
            x="Element",
            y="Count",
            title="Loops, Conditions & Calls",
            color="Element",
            color_discrete_sequence=px.colors.sequential.Blues_r[::-1],
            text="Count"
        )
        fig_bar.update_layout(showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)

    # ----------------------------------------
    # DETAILED ANALYSIS
    # ----------------------------------------

    st.markdown("---")
    st.header("📄 Detailed Analysis")

    with st.expander("Variables"):
        st.write(variables)

    with st.expander("Functions"):
        st.write(functions)

    with st.expander("Classes"):
        st.write(classes)

    with st.expander("Imports"):
        st.write(imports)

    with st.expander("Function Calls"):
        st.write(calls)

    # ----------------------------------------
    # GENERATE PDF REPORT
    # ----------------------------------------

    pdf_path = generate_pdf_report(
        uploaded_file.name,
        variables,
        functions,
        classes,
        imports,
        loops,
        conditions,
        calls,
        suggestions,
        score,
        grade
    )

    # ----------------------------------------
    # ANALYSIS HISTORY
    # ----------------------------------------

    st.markdown("---")
    st.header("📜 Analysis History")

    history = get_analysis_history()

    if history:

        df = pd.DataFrame(
            history,
            columns=[
                "ID",
                "File",
                "Variables",
                "Functions",
                "Classes",
                "Imports",
                "Time"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        csv_bytes = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📤 Export History to CSV",
            data=csv_bytes,
            file_name="pychronicle_analysis_history.csv",
            mime="text/csv"
        )

    else:
        st.info("No analysis history found.")

    # ----------------------------------------
    # PROJECT EVOLUTION
    # ----------------------------------------

    st.markdown("---")
    st.header("📈 Project Evolution")

    if history and len(history) >= 2:

        evolution_df = pd.DataFrame(
            history,
            columns=[
                "ID",
                "File",
                "Variables",
                "Functions",
                "Classes",
                "Imports",
                "Time"
            ]
        ).sort_values("Time")

        fig_evolution = px.line(
            evolution_df,
            x="Time",
            y=["Variables", "Functions", "Classes", "Imports"],
            markers=True,
            title="Metric Trends Across Analyses",
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        fig_evolution.update_layout(
            legend_title_text="Metric",
            xaxis_title="Analysis Time",
            yaxis_title="Count"
        )
        st.plotly_chart(fig_evolution, use_container_width=True)

    else:
        st.info("Need at least two saved analyses to plot an evolution chart.")

    records = get_latest_two_records()

    if len(records) >= 2:

        latest = records[0]
        previous = records[1]

        e1, e2 = st.columns(2)

        e1.metric(
            "Variables",
            latest[0],
            latest[0] - previous[0]
        )

        e2.metric(
            "Functions",
            latest[1],
            latest[1] - previous[1]
        )

        e3, e4 = st.columns(2)

        e3.metric(
            "Classes",
            latest[2],
            latest[2] - previous[2]
        )

        e4.metric(
            "Imports",
            latest[3],
            latest[3] - previous[3]
        )

    else:
        st.info("Need at least two analyses to compare.")

    # ----------------------------------------
    # DOWNLOAD PDF REPORT
    # ----------------------------------------

    st.markdown("---")
    st.header("📄 Download Report")

    # NOTE: use the actual path returned by generate_pdf_report(),
    # NOT a hardcoded filename — the report filename is dynamic
    # (based on the uploaded file's name).

    if pdf_path and os.path.exists(pdf_path):

        with open(pdf_path, "rb") as pdf_file:

            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_file,
                file_name="PyChronicle_Report.pdf",
                mime="application/pdf"
            )

    else:
        st.warning("PDF report not found.")

# ----------------------------------------
# NO FILE UPLOADED
# ----------------------------------------

else:

    st.info("👆 Upload a Python (.py) file to start analysis.")

# ----------------------------------------
# FOOTER
# ----------------------------------------

st.markdown("---")
st.caption("© 2026 PyChronicle | Developed by Siva Sundar Rajan & Sivaraman")
