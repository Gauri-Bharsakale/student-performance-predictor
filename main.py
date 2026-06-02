from src.data.load_data import load_data
from src.data.clean_data import clean_data
from src.data.preprocess import preprocess_data
from src.features.encode_features import encode_features
from src.features.eda import basic_eda

def main():
    print("🔹 Starting Pipeline...\n")

    # Load data
    df = load_data("data/student-mat.csv")
    print("✅ Dataset Loaded:", df.shape)

    # Clean data
    df, missing = clean_data(df)
    print("\n✅ Data Cleaned")
    print("Missing values:\n", missing)

    # EDA
    basic_eda(df)

    # Preprocess
    X, y = preprocess_data(df)

    # Encode
    X = encode_features(X)

    print("\n✅ Encoding Done")
    print("Final Features Shape:", X.shape)
    print("Target Shape:", y.shape)

if __name__ == "__main__":
    main()
