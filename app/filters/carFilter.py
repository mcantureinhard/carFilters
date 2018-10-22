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
            for _filter in self.filters:
                _filter.processAgg(obj, self.removalMap, self.aggMap)
        filtersList = self.filtersFromAggs(filters)
        return {"list" : self.outputList, "filters" : filtersList}
    def filtersFromAggs(self, filters):
        filtersList = []
        for category, aggs in self.aggMap.items():
            _filter = {'title' : category}
            if category in filters:
                applied = filters[category]
            else:
                applied = {}
            aggregations = []
            for aggName, count in aggs.items():
                aggregation = {'title' : aggName, 'count' : count}
                if aggName in applied:
                    aggregation["selected"] = True
                else:
                    aggregation["selected"] = False
                aggregations.append(aggregation)
            _filter["aggregations"] = aggregations
            filtersList.append(_filter)
        return filtersList
            
