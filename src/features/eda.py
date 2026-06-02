import matplotlib.pyplot as plt

def basic_eda(df):
    """
    Perform basic EDA and save plots
    """

    # Study time vs final grade
    plt.figure()
    plt.scatter(df['studytime'], df['G3'])
    plt.xlabel("Study Time")
    plt.ylabel("Final Grade (G3)")
    plt.title("Study Time vs Final Grade")
    plt.savefig("studytime_vs_grade.png")

    # Absences vs final grade
    plt.figure()
    plt.scatter(df['absences'], df['G3'])
    plt.xlabel("Absences")
    plt.ylabel("Final Grade (G3)")
    plt.title("Absences vs Final Grade")
    plt.savefig("absences_vs_grade.png")

    print("EDA plots saved!")
