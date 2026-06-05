import pandas as pd

def prepare_features(df):

    if "id" in df.columns:
        df = df.drop("id", axis=1)

    X = df.drop("G3", axis=1)
    y = df["G3"]

    X = pd.get_dummies(
        X,
        drop_first=True
    )

    return X, y
