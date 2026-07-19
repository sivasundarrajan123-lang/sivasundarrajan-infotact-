import os
import matplotlib.pyplot as plt


def generate_chart(variables, functions, classes, imports):
    labels = ["Variables", "Functions", "Classes", "Imports"]
    values = [
        len(variables),
        len(functions),
        len(classes),
        len(imports)
    ]

    os.makedirs("reports", exist_ok=True)

    plt.figure(figsize=(7, 5))
    plt.bar(labels, values)

    plt.title("PyChronicle Analysis Summary")
    plt.xlabel("Metrics")
    plt.ylabel("Count")

    plt.savefig("reports/analysis_chart.png")
    plt.close()

    print("📊 Chart generated successfully!")