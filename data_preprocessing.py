import pandas as pd

def preprocess_data(path):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    df['loan_status'] = df['loan_status'].map({'Fully Paid': 0, 'Default': 1})
    return df
