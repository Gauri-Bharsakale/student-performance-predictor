def clean_data(df):
    """
    Clean dataset:
    - Handle missing values
    - Basic sanity checks
    """

    # Check missing values
    missing = df.isnull().sum()

    # Drop rows if any missing (dataset is usually clean)
    df = df.dropna()

    return df, missing
