from app.filters.baseFilter import BaseFilter

class CarPropertiesFilter(BaseFilter):
    def initObjectPath(self):
        return ["car_data"]