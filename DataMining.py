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

def getUpdatedRModel(valid_iD, dicts,arrayAttributes):
    array = []
    for id in valid_iD:
        arrayObj = dicts[id]
        for i in range(len(arrayObj) - 1):
            res = extractUpdate2SnapShotsRModel(arrayObj[i],arrayObj[i+1],arrayAttributes)
            array += res
    return array

def writeToFile(array,nameFile):
    with open(nameFile, 'w') as f:
        for item in array:
            f.write(str(item.Time))
            f.write(",")
            f.write(item.Attr)
            f.write(",")
            f.write(str(item.Value))
            f.write("\n")

arrayAttributes, valid_iD, dicts = creatDict("MLS_Data.csv")
resUpdatedRModel = getUpdatedRModel(valid_iD,dicts,arrayAttributes)
writeToFile(resUpdatedRModel,"updated_RModel.txt")
print(resUpdatedRModel)
