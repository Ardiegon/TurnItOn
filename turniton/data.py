import pandas as pd

def load_data(path:str)->pd.DataFrame:
    csv = pd.read_csv(path)

def preprocess_data(csv: pd.DataFrame)->pd.DataFrame:
    pass
