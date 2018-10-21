

class BaseFilter:
    def __init__(self):
        self.filterName   = self.initFilterName()
        self.isOr   = self.initIsOr()
        self.objectPath = self.initObjectPath()
        self.filterValues = self.initFilterValues()
    def initIsOr(self):
        return False
    def initFilterName(self):
        return ""
    def initObjectPath(self):
        return []
    def initFilterValues(self):
        return []
    #some classes would be private if using java or c++
    def isMatch(self, obj, fitlerValue):
        return True
    
    def processFilter(self, obj, filters, removalMap):
        #going to skip some validations
        filterArgs = filters[self.filterName]
        matches = 0
        filterableObj = obj
        matchMap = {}
        for path in self.objectPath:
            filterableObj = filterableObj[path]
        for filterArg in self.filterValues:
            if self.isMatch(filterableObj, filterArg):
                if filterArg in filterArgs:
                    matches += 1
                matchMap[filterArg] = 1
            else:
                matchMap[filterArg] = 0
        keep = matches >= len(filterArgs) if self.isOr else matches == len(filterArg)
        removalMap[id(obj)]["filters"][self.filterName] = {'remove' : not keep, 'map' : matchMap}
        removalMap[id(obj)]["remove"] = removalMap[id(obj)]["remove"] or not keep
    
    def processAgg(self, obj, removalMap, aggMap):
        def removedOnlyBySelf(objRmData, filterName):
            for k,v in objRmData.items():
                if v["remove"] and k != filterName:
                    return False
            return True
        _id = id(obj)
        objRmData = removalMap[_id]
        thisRemoved = objRmData["filters"][self.filterName]['remove']
        thisMatchMap = objRmData["filters"][self.filterName]["map"]
        if self.filterName not in aggMap:
            aggMap[self.filterName] = {}
        filterAggs = aggMap[self.filterName]
        if not thisRemoved:
            for k,v in thisMatchMap.items():
                if k in filterAggs:
                    filterAggs[k] += v
                else:
                    filterAggs[k] = v
        else:
            thisRm = removedOnlyBySelf(objRmData["filters"], self.filterName)
            if thisRm and not self.isOr:
                for k,v in thisMatchMap.items():
                    if k not in filterAggs:
                        filterAggs[k] = 0
            else:
                for k,v in thisMatchMap.items():
                    if k in filterAggs:
                        filterAggs[k] += v
                    else:
                        filterAggs[k] = v
        
