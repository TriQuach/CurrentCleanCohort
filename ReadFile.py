import pandas as pd
def readFile(fileName):
    df = pd.read_csv(fileName)
    return df


