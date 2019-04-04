from ReadFile import *
import numpy as np

fiveEntities = ["Marco-Etcheverry","Carlos-Valderrama","Eric-Wynalda","Preki","Robert-Warzycha"]


class Entity(object):
    pass

def getValidID(array):
    res = []
    for i in array:
        if (" " in i):
            i = i.replace(" ", "-")
        if (i not in res ):
            if (i in fiveEntities):
                res.append(i)
    return res
def getValidTime(array):
    res = []
    for i in array:
        if (i not in res):
            res.append(i)
    return res
def hashTable(arrayAttributes,valid_id,dicts):
    obj = Entity()
    for i in range(len(arrayAttributes)):
        setattr(obj,arrayAttributes[i],0)
    for i in valid_id:
        dicts[i] = [obj]
    return dicts
def removeDefaultValue(dicts,valid_id):
    del dicts['999']


    for i in valid_id:
        del dicts[i][0]
    return dicts

def initDict(arrayAttributes):
    temp = Entity()
    for i in range(len(arrayAttributes)):
        setattr(temp, arrayAttributes[i], 0)
    dicts = {
        '999': [temp]
    }

    return dicts


def inputDataToDicts(dicts,arrayAttributes,df):
    for index, row in df.iterrows():
        obj = Entity()
        # setattr(obj,a)
        for attr in arrayAttributes:
            attribute_value = row[attr]
            if (attr == "ID" and " " in attribute_value):
                attribute_value = attribute_value.replace(" ", "-")
            setattr(obj,attr,attribute_value)
        ID = getattr(obj,"ID")
        if (ID in fiveEntities):
           dicts[ID].append(obj)

    return dicts

def isContainSpecialChar(df,arrayAttributes,character):
    for attr in arrayAttributes:
        if (attr != "Timestamp" and attr != "ID"):
            if (character in df[attr][0]):
                return True

    return False

def cleanSpecialCharacter(df, arrayAttributes,character):
    for attr in arrayAttributes:
        if (attr != "Timestamp" and attr != "ID"):
            col = df[attr]
            arr = []
            for str in col.tolist():
                val = str.split(character)[1]
                arr.append(val)
            df[attr] = arr

    return df
def creatDict(fileName):
    df = readFile(fileName)
    arrayAttributes = list(df)
    if isinstance(df["ID"][0], np.int64):
        df["ID"] = np.char.mod('%d', df["ID"].tolist())
    # if (isContainSpecialChar(df,arrayAttributes,":")):
    #     df = cleanSpecialCharacter(df,arrayAttributes,":")
    #     print("asd")
    init_dict = initDict(arrayAttributes)
    valid_iD = getValidID(df["ID"])
    valid_Time = getValidTime(df["Timestamp"])
    dictsDefaultValue = hashTable(arrayAttributes,valid_iD,init_dict)
    dictAfterRemoveDefaul = removeDefaultValue(dictsDefaultValue,valid_iD)
    dicts = inputDataToDicts(dictAfterRemoveDefaul,arrayAttributes,df)
    return arrayAttributes,valid_iD,df,valid_Time, dicts







