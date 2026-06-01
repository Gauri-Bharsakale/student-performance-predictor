def preprocess_data(df):
    # Remove G1 and G2 (to avoid cheating model)
    df = df.drop(['G1', 'G2'], axis=1)

    # Target
    y = df['G3']

    # Features
    X = df.drop(['G3'], axis=1)

    return X, y
