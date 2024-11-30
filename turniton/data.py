import pandas as pd

def get_data(path:str)->pd.DataFrame:
    csv = pd.read_csv(path)
    data = preprocess_csv(csv)
    return data

def preprocess_csv(csv: pd.DataFrame)->pd.DataFrame:
    return csv

def print_data(data: pd.DataFrame)->None:
    data.info()
    data.describe()