import pandas as pd
import datetime
def cleanTimestamp(data):
    arr = []
    for i in data:
        temp = datetime.datetime.strptime(i, "'%Y-%m-%dT%H:%M:%S'")
        arr.append(int(temp.timestamp()))
    return arr
def readFile(fileName):
    df = pd.read_csv(fileName,encoding = "utf-8")
    # arr = cleanTimestamp(df["Timestamp"])
    # df["Timestamp"] = arr

    return df

