from ReadFile import *
from Entity import *
import csv
import pandas as pd
def creatMap(data):
    dicts = {}
    for i in range(len(data)):
        dicts[data[i]] = i
    return dicts
def possibleClub(data):
    array = []
    for i in data:
        if i not in array:
            array.append(i)

    return array

def calculateMedoid(data,arrayAttributes):
    arr = []
    obj = Entity()
    for attr in arrayAttributes:
        if (attr != "ID"):
            for rows in data:
                val = rows[attr]
                arr.append(val)


            valAttr = np.mean(arr)
            setattr(obj,attr,valAttr)
    return obj
def superEntities(df,k,name,arrayAttributes):
    count = 0
    count2 = 0
    arr1 = []
    arr2 = []
    for index, row in df.iterrows():
        count += 1
        arr1.append(row)
        if (count == k):
            count2 += 1
            medoid = calculateMedoid(arr1,arrayAttributes)
            setattr(medoid,"ID",name + str(count2))
            arr1 = []
            arr2.append(medoid)
            count = 0
    return arr2
def writeToCSV(name,data):
    with open(name, 'a') as csvFile:
        writer = csv.writer(csvFile)
        for row in data:
            writer.writerow(row)
            # writer.writerow(row.GS)

    csvFile.close()

def create2DArray(data,rows,cols,arrayAttributes):
    res = [[0 for x in range(cols)] for y in range(rows)]
    for i in range(rows):
        entity = data[i]
        for j in range(cols):
            res[i][j] = getattr(entity,arrayAttributes[j])
    return res

arrayAttributes, valid_iD,df,valid_Time, dicts = creatDict("./Cohorts/west_coast_def_assistor.csv")
res = possibleClub(df["Club"])
dicts = creatMap(res)
df["Club"] = df["Club"].map(dicts)
superEntityArray = superEntities(df,3,"WestCoastDefAssist",arrayAttributes)
#
twoDimesionArray = create2DArray(superEntityArray,len(superEntityArray), len(arrayAttributes),arrayAttributes)
writeToCSV("./SuperEntitiesCSV/SuperEntities.csv",twoDimesionArray)
print("a")