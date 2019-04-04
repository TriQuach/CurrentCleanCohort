from Entity import *


class RModel:
    def __init__(self, Time, Attr , Value):
        self.Time = Time
        self.Attr = Attr
        self.Value = Value
def extractNotUpdate2SnapShotsRModel(beforeObj,afterObj,arrayAttributes,typeDataset):
    array = []
    for attr in arrayAttributes:
        attr1 = getattr(beforeObj,attr)
        attr2 = getattr(afterObj,attr)
        club = getattr(afterObj,"Club")
        if (attr1 == attr2 and attr != "Timestamp" and attr != "POS" and attr != "Club" and attr != "ID" and attr == "GP" and club == "KC"):

            idArttr2 = getattr(afterObj,"ID")
            attrRModel = typeDataset + "_" + idArttr2 + "_" + attr
            timeRModel = getattr(afterObj,"Timestamp")
            entity = RModel(timeRModel,attrRModel,attr2)
            array.append(entity)

    return array

def getNotUpdate(valid_iD, dicts,arrayAttributes,typeDataset):
    array = []
    for id in valid_iD:
        arrayObj = dicts[id]
        for i in range(len(arrayObj) - 1):
            res = extractNotUpdate2SnapShotsRModel(arrayObj[i],arrayObj[i+1],arrayAttributes,typeDataset)
            array += res
    return array


#
# arrayAttributes, valid_iD,df,valid_Time, dicts = creatDict("./Cohorts/east_coast_att_nonstarsubs.csv")
# arr = getNotUpdate(valid_iD,dicts,arrayAttributes,"player")
# print("asd")