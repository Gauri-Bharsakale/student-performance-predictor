import pandas as pd

def encode_features(X):
    """
    Convert categorical variables into numerical
    """
    X_encoded = pd.get_dummies(X, drop_first=True)
    return X_encoded
