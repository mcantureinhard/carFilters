from app.filters.carPropertiesFilters.carPropertiesFilter import CarPropertiesFilter

class CarCapacityFilter(CarPropertiesFilter):
    def initIsOr(self):
        return True
    def initFilterName(self):
        return "capacity"
    def initFilterValues(self):
        return [2,3,4,5,6,7,8]
    def isMatch(self, obj, filterValue):
        return obj[self.filterName] >= filterValue