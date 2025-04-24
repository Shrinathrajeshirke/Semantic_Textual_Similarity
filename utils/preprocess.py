import pandas as pd

def load_and_preprocess(filepath):
    df = pd.read_csv(filepath)
    df['text1'] = df['text1'].str.lower().str.strip()
    df['text2'] = df['text2'].str.lower().str.strip()
    return df