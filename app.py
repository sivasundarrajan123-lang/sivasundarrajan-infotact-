import ast
import os
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

# ----------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------

st.set_page_config(
    page_title="PyChronicle",
    page_icon="📘",
    layout="wide"
)

st.title("📘 PyChronicle")
st.subheader("Python Code Evolution & Analysis Tool")

st.markdown("---")

# ----------------------------------------
# FILE UPLOAD
# ----------------------------------------

uploaded_file = st.file_uploader(
    "📂 Upload a Python (.py) file",
    type=["py"]
)

# ----------------------------------------
# ANALYSIS
# ----------------------------------------

if uploaded_file is not None:

    code = uploaded_file.read().decode("utf-8")

    st.success(f"✅ Uploaded Successfully : {uploaded_file.name}")

    tree = ast.parse(code)

    # -------------------------
    # Extract Information
    # -------------------------

    variables = extract_variables(tree)
    functions = extract_functions(tree)
    classes = extract_classes(tree)
    imports = extract_imports(tree)
    loops = extract_loops(tree)
    conditions = extract_conditions(tree)
    calls = extract_function_calls(tree)

    # -------------------------
    # SUMMARY
    # -------------------------

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

    # -------------------------
    # QUALITY SCORE
    # -------------------------

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

    # -------------------------
    # SMART SUGGESTIONS
    # -------------------------

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
        st.info("No suggestions.")

    # -------------------------
    # CHART
    # -------------------------

    generate_chart(
        variables,
        functions,
        classes,
        imports
    )

    st.markdown("---")

    st.header("📊 Analysis Chart")

    if os.path.exists("reports/analysis_chart.png"):
        st.image(
            "reports/analysis_chart.png",
            caption="PyChronicle Analysis Chart",
            use_container_width=True
        )

    # -------------------------
    # DETAILED ANALYSIS
    # -------------------------

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

else:
    st.info("👆 Upload a Python (.py) file to start analysis.")