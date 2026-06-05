from sklearn.model_selection import train_test_split
import joblib

from src.data.database import fetch_data

from src.features.feature_engineering import (
    prepare_features
)

from src.models.tune_model import (
    tune_model
)

from src.models.feature_importance import (
    show_feature_importance
)


def main():

    print("🚀 Day 6 Pipeline Started\n")

    # Load data from SQL
    df = fetch_data()

    print(
        f"✅ Records Loaded: {len(df)}"
    )

    # Feature Engineering
    X, y = prepare_features(df)

    print(
        f"✅ Features Shape: {X.shape}"
    )

    print(
        f"✅ Target Shape: {y.shape}"
    )

    # Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print(
        "\n✅ Train-Test Split Completed"
    )

    # Hyperparameter Tuning
    best_model = tune_model(
        X_train,
        y_train
    )

    print(
        "\n✅ Best Model Found"
    )

    print(best_model)

    # Feature Importance
    show_feature_importance(
        best_model,
        X_train
    )

    # Save Model
    joblib.dump(
        best_model,
        "models/best_student_model.pkl"
    )

    print(
        "\n✅ Model Saved Successfully"
    )

    print(
        "\n📁 Saved To:"
    )

    print(
        "models/best_student_model.pkl"
    )

    print(
        "\n🎉 Day 6 Completed Successfully"
    )


if __name__ == "__main__":
    main()
