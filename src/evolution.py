import sqlite3


def compare_latest_analysis():
    conn = sqlite3.connect("database/analysis.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT variables,
               functions,
               classes,
               imports
        FROM analysis_history
        ORDER BY id DESC
        LIMIT 2
    """)

    rows = cursor.fetchall()
    conn.close()

    if len(rows) < 2:
        print("\nNot enough history for comparison.")
        return

    current = rows[0]
    previous = rows[1]

    print("\n" + "=" * 50)
    print("PROJECT EVOLUTION")
    print("=" * 50)

    labels = [
        "Variables",
        "Functions",
        "Classes",
        "Imports"
    ]

    for i, label in enumerate(labels):
        change = current[i] - previous[i]

        if change > 0:
            status = f"+{change}"
        elif change < 0:
            status = str(change)
        else:
            status = "No Change"

        print(
            f"{label:<12}: {previous[i]}  →  {current[i]}   ({status})"
        )

    print("=" * 50)