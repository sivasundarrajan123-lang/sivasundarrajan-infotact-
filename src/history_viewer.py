import sqlite3

def show_history():
    conn = sqlite3.connect("database/analysis.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id,
               file_name,
               variables,
               functions,
               classes,
               imports,
               analysis_time
        FROM analysis_history
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    print("\n" + "=" * 50)
    print("        PYCHRONICLE ANALYSIS HISTORY")
    print("=" * 50)

    if not rows:
        print("No analysis history found.")
    else:
        for row in rows:
            print(f"""
Analysis ID : {row[0]}
File        : {row[1]}
Variables   : {row[2]}
Functions   : {row[3]}
Classes     : {row[4]}
Imports     : {row[5]}
Time        : {row[6]}
----------------------------------------
""")

    conn.close()