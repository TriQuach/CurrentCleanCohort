from Entity import *

class RModel:
    def __init__(self, Time, Attr , Value):
        self.Time = Time
        self.Attr = Attr
        self.Value = Value
class UModel:
    def __init__(self, Time, Attr):
        self.Time = Time
        self.Attr = Attr

def extractUpdate2SnapShotsRModel(beforeObj,afterObj,arrayAttributes):
    array = []
    for attr in arrayAttributes:
        attr1 = getattr(beforeObj,attr)
        attr2 = getattr(afterObj,attr)
        if (attr1 != attr2 and attr != "Timestamp"):
            idArttr2 = getattr(afterObj,"ID")
            attrRModel = "player" + "_" + idArttr2 + "_" + attr
            timeRModel = getattr(afterObj,"Timestamp")
            entity = RModel(timeRModel,attrRModel,attr2)
            array.append(entity)

    return array

def extractUpdate2SnapShotsUModel(beforeObj,afterObj,arrayAttributes):
    array = []
    for attr in arrayAttributes:
        attr1 = getattr(beforeObj,attr)
        attr2 = getattr(afterObj,attr)
        if (attr1 != attr2 and attr != "Timestamp"):
            idArttr2 = getattr(afterObj,"ID")
            attrRModel = "player" + "_" + idArttr2 + "_" + attr
            timeRModel = getattr(afterObj,"Timestamp")
            entity = UModel(timeRModel,attrRModel)
            array.append(entity)

    return array

def getUpdatedRModel(valid_iD, dicts,arrayAttributes):
    array = []
    for id in valid_iD:
        arrayObj = dicts[id]
        for i in range(len(arrayObj) - 1):
            res = extractUpdate2SnapShotsRModel(arrayObj[i],arrayObj[i+1],arrayAttributes)
            array += res
    return array
def getUpdatedUModel(valid_iD, dicts,arrayAttributes):
    array = []
    for id in valid_iD:
        arrayObj = dicts[id]
        for i in range(len(arrayObj) - 1):
            res = extractUpdate2SnapShotsUModel(arrayObj[i],arrayObj[i+1],arrayAttributes)
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
    with open(nameFile, 'w') as f:
        for item in array:
            f.write(str(item.Time))
            f.write(",")
            f.write(item.Attr)
            f.write("\n")




arrayAttributes, valid_iD, dicts = creatDict("MLS_Data.csv")
resUpdatedRModel = getUpdatedRModel(valid_iD,dicts,arrayAttributes)
resUpdatedUModel = getUpdatedUModel(valid_iD,dicts,arrayAttributes)

writeToFileRModel(resUpdatedRModel,"updated_RModel.txt")
writeToFileUModel(resUpdatedUModel,"updated_UModel.txt")

tempArray = dicts["Marco-Etcheverry"]
dictLastUpdate = {}
for i in range(len(tempArray)-1,-1,-1):
    if (i>0):
        dictLastUpdate = lastUpdateRModel(dicts["Marco-Etcheverry"][i], dicts["Marco-Etcheverry"][i-1], arrayAttributes,
                                      dictLastUpdate)
dictLastUpdate = fillUnUpdateValue(dictLastUpdate,arrayAttributes,tempArray)
print(dictLastUpdate)



print(resUpdatedRModel)
