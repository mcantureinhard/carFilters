from app.filters.carPropertiesFilters.carCapacityFIlter import CarCapacityFilter

class CarFilter:
    def __init__(self):
        self.removalMap = {}
        self.aggMap = {}
        self.outputList = []
        self.filters = self.filtersList()
    def filtersList(self):
        filters = []
        filters.append(CarCapacityFilter())
        return filters
    def process(self, objList, filters):
        for obj in objList:
            self.removalMap[id(obj)] = {"remove" : 0, 'filters' : {}}

            for _filter in self.filters:
                _filter.processFilter(obj, filters, self.removalMap)
            if self.removalMap[id(obj)]["remove"] == 0:
                self.outputList.append(obj)
            for filter in filters:
                _filter.processAgg(obj, self.removalMap, self.aggMap)
        return {"list" : self.outputList, "aggs" : self.aggMap}
            
