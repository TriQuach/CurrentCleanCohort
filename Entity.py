from ReadFile import *
import numpy as np

class Entity(object):
    pass

def getValidID(array):
    res = []
    for i in array:
        if (" " in i):
            i = i.replace(" ", "-")
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
        dicts[ID].append(obj)

    return dicts

def creatDict(fileName):
    df = readFile(fileName)
    if isinstance(df["ID"][0], np.int64):
        df["ID"] = np.char.mod('%d', df["ID"].tolist())
    arrayAttributes = list(df)
    init_dict = initDict(arrayAttributes)
    valid_iD = getValidID(df["ID"])

    dictsDefaultValue = hashTable(arrayAttributes,valid_iD,init_dict)
    dictAfterRemoveDefaul = removeDefaultValue(dictsDefaultValue,valid_iD)
    dicts = inputDataToDicts(dictAfterRemoveDefaul,arrayAttributes,df)
    return arrayAttributes,valid_iD, dicts


