from src.data.load_data import load_data
from src.data.preprocess import preprocess_data

def main():
    print("🔹 Starting Student Performance Pipeline...\n")

    # Step 1: Load dataset
    df = load_data("data/student-mat.csv")
    print("✅ Dataset Loaded Successfully")
    print("Shape:", df.shape)

    # Step 2: Preprocess data
    X, y = preprocess_data(df)
    print("\n✅ Preprocessing Done")
    print("Features shape:", X.shape)
    print("Target shape:", y.shape)

    print("\n📊 Feature Columns:")
    print(list(X.columns))

if __name__ == "__main__":
    main()
