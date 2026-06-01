import pandas as pd

def load_data(path: str):
    """
    Load dataset with correct separator
    """
    df = pd.read_csv(path, sep=',')  # ✅ FIXED
    return df

if __name__ == "__main__":
    df = load_data("data/student-mat.csv")
    print(df.head())
