from app.pipeline import Pipeline
from app.stages import loadAggregateData
from app.stages import loadCarData
from app.stages import questionFiltering
from app.stages import removeCarData


class QuestionsData(Pipeline):
    def __init__(self, state = {}, data ={}):
        super().__init__(state=state, data=data)
    def addStages(self):
        #Load data from our aggregation service
        self.stages.append(loadAggregateData.run)
        #Load car data, to allow us to filter
        self.stages.append(loadCarData.run)
        #Apply our question filter stage
        self.stages.append(questionFiltering.run)
        #Remove car data to reduce the amount of data we have to pass around
        self.stages.append(removeCarData.run)