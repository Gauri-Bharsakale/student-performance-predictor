
from src.data.load_data import load_data
from src.data.clean_data import clean_data

from src.data.database import (
    create_table,
    insert_data,
    fetch_data
)

from src.models.train_model import train_model
from src.models.evaluate_model import evaluate_model


def main():

    print("Starting Day 4 Pipeline...\n")

    # Load Data
    df = load_data(
        "data/student-mat.csv"
    )

    # Clean Data
    df, _ = clean_data(df)

    # Prepare DB Data
    df_db = df[
        [
            "studytime",
            "failures",
            "absences",
            "G3"
        ]
    ]

    # Create DB
    create_table()

    # Store Data
    insert_data(df_db)

    # Read Data Back
    df_sql = fetch_data()

    print(
        "Records Loaded From SQL:",
        len(df_sql)
    )

    # Train Model
    model, X_test, y_test = train_model(
        df_sql
    )

    print(
        "\nModel Trained Successfully"
    )

    # Evaluate
    mae, r2 = evaluate_model(
        model,
        X_test,
        y_test
    )

    print(
        f"\nMAE: {mae:.2f}"
    )

    print(
        f"R² Score: {r2:.2f}"
    )

    print(
        "\nModel Saved Successfully"
    )


if __name__ == "__main__":
    main()
