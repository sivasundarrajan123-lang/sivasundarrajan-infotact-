import sqlite3
from datetime import datetime


def create_database():
    conn = sqlite3.connect("database/analysis.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT,
        variables INTEGER,
        functions INTEGER,
        classes INTEGER,
        imports INTEGER,
        for_loops INTEGER,
        while_loops INTEGER,
        if_statements INTEGER,
        function_calls INTEGER,
        analysis_time TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_analysis(
    file_name,
    variables,
    functions,
    classes,
    imports,
    for_loops,
    while_loops,
    if_statements,
    function_calls
):
    conn = sqlite3.connect("database/analysis.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO analysis_history(
            file_name,
            variables,
            functions,
            classes,
            imports,
            for_loops,
            while_loops,
            if_statements,
            function_calls,
            analysis_time
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        file_name,
        len(variables),
        len(functions),
        len(classes),
        len(imports),
        for_loops,
        while_loops,
        if_statements,
        len(function_calls),
        datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    ))

    conn.commit()
    conn.close()

    print("✅ Analysis saved to database.")