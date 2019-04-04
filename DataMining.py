from Entity import *
import csv
class RModel:
    def __init__(self, Time, Attr , Value):
        self.Time = Time
        self.Attr = Attr
        self.Value = Value
class UModel:
    def __init__(self, Time, Attr):
        self.Time = Time
        self.Attr = Attr
class Cell:
    def __init__(self, Role, ID, Property):
        self.Role = Role
        self.ID = ID
        self.Property = Property
class Probabilistic:
    def __init__(self, Role, Property):
        self.Role = Role
        self.Property = Property


def extractUpdate2SnapShotsRModel(beforeObj,afterObj,arrayAttributes,typeDataset):
    array = []
    for attr in arrayAttributes:
        attr1 = getattr(beforeObj,attr)
        attr2 = getattr(afterObj,attr)
        if (attr1 != attr2 and attr != "Timestamp"):
            idArttr2 = getattr(afterObj,"ID")
            attrRModel = typeDataset + "_" + idArttr2 + "_" + attr
            timeRModel = getattr(afterObj,"Timestamp")
            entity = RModel(timeRModel,attrRModel,attr2)
            array.append(entity)

    return array

def extractUpdate2SnapShotsUModel(beforeObj,afterObj,arrayAttributes,typeDataset):
    array = []
    for attr in arrayAttributes:
        attr1 = getattr(beforeObj,attr)
        attr2 = getattr(afterObj,attr)
        if (attr1 != attr2 and attr != "Timestamp"):
            idArttr2 = getattr(afterObj,"ID")
            attrRModel = typeDataset + "_" + idArttr2 + "_" + attr
            timeRModel = getattr(afterObj,"Timestamp")
            entity = UModel(timeRModel,attrRModel)
            array.append(entity)

    return array

def getUpdatedRModel(valid_iD, dicts,arrayAttributes,typeDataset):
    array = []
    for id in valid_iD:
        arrayObj = dicts[id]
        for i in range(len(arrayObj) - 1):
            res = extractUpdate2SnapShotsRModel(arrayObj[i],arrayObj[i+1],arrayAttributes,typeDataset)
            array += res
    return array
def getUpdatedUModel(valid_iD, dicts,arrayAttributes,typeDataset):
    array = []
    for id in valid_iD:
        arrayObj = dicts[id]
        for i in range(len(arrayObj) - 1):
            res = extractUpdate2SnapShotsUModel(arrayObj[i],arrayObj[i+1],arrayAttributes,typeDataset)
            array += res
    return array

def lastUpdateRModel(afterObj, beforeObj, arrayAttributes, dictLastUpdate):
    for attr in arrayAttributes:
        attr1 = getattr(afterObj,attr)
        attr2 = getattr(beforeObj,attr)
        if (attr1 != attr2 and attr != "Timestamp"):
           if (attr not in dictLastUpdate):
               timeStamp = getattr(afterObj,"Timestamp")
               id = getattr(afterObj,"ID")
               tempObj = {}
               tempObj["value"] = attr1
               tempObj["timestamp"] = timeStamp
               tempObj["id"] = id
               dictLastUpdate[attr] = tempObj


    return dictLastUpdate

def fillUnUpdateValue(dictLastUpdate, arrayAttributes,arrayObj):
    for attr in arrayAttributes:
        if (attr not in dictLastUpdate and attr != "ID" and attr != "Timestamp"):
            obj = arrayObj[len(arrayObj)-1]
            timeStamp = getattr(obj, "Timestamp")
            id = getattr(obj, "ID")
            tempObj = {}
            tempObj["value"] = getattr(obj,attr)
            tempObj["timestamp"] = timeStamp
            tempObj["id"] = id

            dictLastUpdate[attr] = tempObj

    return dictLastUpdate

def writeToFileRModel(array,nameFile):
    with open(nameFile, 'w') as f:
        for item in array:
            f.write(str(item.Time))
            f.write(",")
            f.write(item.Attr)
            f.write(",")
            f.write(str(item.Value))
            f.write("\n")
def writeToFileUModel(array,nameFile):
    # with open(nameFile, 'w') as f:
    #     for item in array:
    #         f.write(str(item.Time))
    #         f.write(",")
    #         f.write(item.Attr)
    #         f.write("\n")
    with open(nameFile, 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        for item in array:
            tsv_writer.writerow([item.Attr, str(item.Time)])

def writeToFileCell(array,nameFile):
    with open(nameFile, 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        for item in array:
            rolePropAndID = item.Role + "_" + item.ID + "_" + item.Property
            roleAndID = item.Role + "_" + item.ID
            roleAndProp = item.Role + "_" + item.Property
            tsv_writer.writerow([rolePropAndID, roleAndID, roleAndProp])

def writeToFileProbabilistic(array,nameFile):
    with open(nameFile, 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        for item in array:
            roleAndProp = item.Role + "_" + item.Property
            tsv_writer.writerow([roleAndProp])

def writeToFileNormalObj(array,nameFile):
    with open(nameFile, 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        for item in array:
            tsv_writer.writerow([item])

def getArrayBasedOnDictLastUpdate(dictLastUpdate, arrayAttributes, typeModel,typeDataset):
    arr = []
    for attr in arrayAttributes:
        if (attr != "ID" and attr != "Timestamp"):
            value = dictLastUpdate[attr]["value"]
            timestamp = dictLastUpdate[attr]["timestamp"]
            id = dictLastUpdate[attr]["id"]
            attribute = typeDataset + "_" + id + "_" + attr
            if (typeModel == "RModel"):
                entity = RModel(timestamp, attribute, value)
            else:
                entity = UModel(timestamp, attribute)

            arr.append(entity)
    return arr

def getArrayLastUpdateAllEntity(valid_iD, dicts, arrayAttributes,typeModel, typeDataset):
    res = []
    for entity in valid_iD:
        tempArray = dicts[entity]
        dictLastUpdate = {}
        for i in range(len(tempArray) - 1, -1, -1):
            if (i > 0):
                dictLastUpdate = lastUpdateRModel(dicts[entity][i], dicts[entity][i - 1],
                                                  arrayAttributes,
                                                  dictLastUpdate)
        dictLastUpdate = fillUnUpdateValue(dictLastUpdate, arrayAttributes, tempArray)
        arr = getArrayBasedOnDictLastUpdate(dictLastUpdate, arrayAttributes,typeModel,typeDataset)
        res += arr

    return res

def getCells(valid_ID, arrayAttributes):
    arr = []

    for ID in valid_iD:
        for attr in arrayAttributes:
            if (attr != "ID" and attr != "Timestamp"):
                cell = Cell("player", ID, attr)
                arr.append(cell)

    return arr

def getProbabilistic(role,arrayAttributes):
    arr = []
    for attr in arrayAttributes:
        if (attr != "ID" and attr != "Timestamp"):
            obj = Probabilistic("player",attr)
            arr.append(obj)

    return arr





#create UMOdel based on Cohorts

arrayAttributes, valid_iD,df,valid_Time, dicts = creatDict("MLS_Data_Small.csv")
resUpdatedUModel = getUpdatedUModel(valid_iD,dicts,arrayAttributes,"player")
resLastUpdateUModel = getArrayLastUpdateAllEntity(valid_iD,dicts,arrayAttributes,"UModel","player")
writeToFileUModel(resUpdatedUModel,"./DataMiningResultCohorts/fiveEntities/updated.tsv")
writeToFileUModel(resLastUpdateUModel,"./DataMiningResultCohorts/fiveEntities/lastupd.tsv")
arr = getCells(df,arrayAttributes)
writeToFileCell(arr, "./DataMiningResultCohorts/fiveEntities/cell.tsv")
arrProbabilistic = getProbabilistic("player",arrayAttributes)
writeToFileProbabilistic(arrProbabilistic,"./DataMiningResultCohorts/fiveEntities/probabilistic.tsv")
writeToFileNormalObj(valid_Time,"./DataMiningResultCohorts/fiveEntities/time.tsv")
print("a")


# arrayAttributes, valid_iD,df,valid_Time, dicts = creatDict("MLS_Data_Small.csv")
# resUpdatedRModel = getUpdatedRModel(valid_iD,dicts,arrayAttributes,"player")
# resUpdatedUModel = getUpdatedUModel(valid_iD,dicts,arrayAttributes,"player")
#
# writeToFileRModel(resUpdatedRModel,"./DataMiningResult/updated_RModel.txt")
# writeToFileUModel(resUpdatedUModel,"./DataMiningResult/updated_UModel.tsv")
#
# resLastUpdateRModel = getArrayLastUpdateAllEntity(valid_iD,dicts,arrayAttributes,"RModel","player")
# resLastUpdateUModel = getArrayLastUpdateAllEntity(valid_iD,dicts,arrayAttributes,"UModel","player")
#
# writeToFileRModel(resLastUpdateRModel,"./DataMiningResult/lastUpdate_RModel.txt")
# writeToFileUModel(resLastUpdateUModel,"./DataMiningResult/lastUpdate_UModel.tsv")
#
# arr = getCells(df,arrayAttributes)
# writeToFileCell(arr,"./DataMiningResult/cell_MLS.tsv")
#
# arrProbabilistic = getProbabilistic("player",arrayAttributes)
# writeToFileProbabilistic(arrProbabilistic,"./DataMiningResult/probabilistic_MLS.tsv")
#
# writeToFileNormalObj(valid_Time,"./DataMiningResult/time_MLS.tsv")
# print(arr)



# For Shervin's Sensor Dataset
# arrayAttributesSensor, valid_iD_Sensor, dicts_Sensor = creatDict("./sensor datasets/clean_intelsensordata.csv")
# resUpdatedRModel = getUpdatedRModel(valid_iD_Sensor,dicts_Sensor,arrayAttributesSensor,"sensor")
# resUpdatedUModel = getUpdatedUModel(valid_iD_Sensor,dicts_Sensor,arrayAttributesSensor,"sensor")
# writeToFileRModel(resUpdatedRModel,"./DataMiningResult/updated_RModel_sensor.txt")
# writeToFileUModel(resUpdatedUModel,"./DataMiningResult/updated_UModel_sensor.txt")
#
# resLastUpdateRModelSensor = getArrayLastUpdateAllEntity(valid_iD_Sensor,dicts_Sensor,arrayAttributesSensor,"RModel","sensor")
# resLastUpdateUModelSenor = getArrayLastUpdateAllEntity(valid_iD_Sensor,dicts_Sensor,arrayAttributesSensor,"UModel", "sensor")
#
# writeToFileRModel(resLastUpdateRModelSensor,"./DataMiningResult/lastUpdate_RModel_Sensor.txt")
# writeToFileUModel(resLastUpdateUModelSenor,"./DataMiningResult/lastUpdate_UModel_Sensor.txt")

#
# #For Zheng's Sensor Dataset
# arrayAttributesSensor, valid_iD_Sensor, dicts_Sensor = creatDict("Sensor.csv")
# resUpdatedRModel = getUpdatedRModel(valid_iD_Sensor,dicts_Sensor,arrayAttributesSensor,"sensor")
# resUpdatedUModel = getUpdatedUModel(valid_iD_Sensor,dicts_Sensor,arrayAttributesSensor,"sensor")
# writeToFileRModel(resUpdatedRModel,"./DataMiningResult/updated_RModel_sensorZheng.txt")
# writeToFileUModel(resUpdatedUModel,"./DataMiningResult/updated_UModel_sensorZheng.txt")
# print(arrayAttributesSensor)
