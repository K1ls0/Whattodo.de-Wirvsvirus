import os
from config import getConfigInstance

logger = logging.getLogger(__name__)
config = getConfigInstance()


def filterExcluding(data, tags):
    retItems = dict()
    for cKey in data.keys():
        dataStg = data[cKey]
        for cTag in tags:
            if (cTag in data[cKey]):
                dataStg = None
                break

        if not (dataStg is None):
            retItems[cKey] = dataStg
    return retItems


def filterIncluding(data, tags):
    retItems = dict()
    for cKey in data.keys():
        dataStg = None
        # print("Tags:")
        # print(tags)
        # print("data[cKey]:")
        # print(data[cKey])
        for cTag in tags:
            if cTag in data[cKey]:
                retItems[cKey] = data[cKey]
                break
        if not (dataStg is None):
            retItems[cKey] = dataStg
    return retItems


class SQLAdapter:
    def __init__(self):
        if not (os.path.exists(config.dataFile) and os.path.isfile(config.dataFile)):
            with open(config.dataFile, 'w') as f:
                f.write('>Test-task\n')
                f.write('Tag1,Tag2,Tag3')

        lines = []
        with open(config.dataFile, 'r+') as f:
            lines = f.readlines()

        # actual Data

        self.data = self.deserialize(lines)

        self.updateClassification()

    def deserialize(self, lines):
        i = 0
        data = dict()
        while i < len(lines):
            if i < (len(lines)-1) and lines[i].startswith('>') and len(lines[i]) > 1:
                idea = lines[i][1:].rstrip()
                i += 1
                while lines[i].strip() == '' or i >= len(lines):
                    i += 1
                tags = lines[i].strip().split(',')
                for cI in range(len(tags)):
                    tags[cI] = tags[cI].strip()

                data[idea] = tags
            i += 1
        return data

    def serialize(self, datadict, mode):
        with open(config.newDataQueryFile, mode) as f:
            for cKey in datadict.keys():
                f.write('>{}\n'.format(cKey))
                for cTagIndex in range(len(datadict[cKey])):
                    f.write(datadict[cKey][cTagIndex])
                    if cTagIndex != len(datadict[cKey]) - 1:
                        f.write(',')
                f.write('\n')




    def updateClassification(self):

        self.allTags = set()

        for i in self.data.keys():
            for c in self.data[i]:
                self.allTags.add(c)

    def getAllTags(self):
        return {'tags': list(self.allTags)}

    def getByTags(self, tags, include):

        filteredTags = []
        # filter to have only tags that acctually exist in data
        for cTag in tags:
            print("allTags:")
            print(self.allTags)
            print("cTag")
            print(cTag)
            if cTag in self.allTags:
                filteredTags.append(cTag)

        if len(filteredTags) == 0:
            return self.data

        if include:
            return filterIncluding(self.data, filteredTags)
        else:
            return filterExcluding(self.data, filteredTags)

    def queryNew(self, data):
        self.serialize(data, 'a')

    def __str__(self):
        retStr = ''
        keys = self.data.keys()
        for i in keys:
            tagsAsStr = "["
            for c in range(len(self.data[i])):
                tagsAsStr += self.data[i][c]

                if c != (len(self.data[i]) - 1):
                    tagsAsStr += ", "
            tagsAsStr += "]"
            retStr += i + ": " + tagsAsStr + "\n"
        return retStr + "\nAll Tags: " + self.allTags.__str__()
