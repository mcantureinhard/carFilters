

class Pipeline:
    def __init__(self, state = {}, data ={}):
        self.state = {}
        self.data = {}
        self.stages=[]
        self.addStages()
    def addStages(self):
        return
    def executePipeline(self):
        if len(self.stages) == 0:
            print("Empty pipelines not allowed")
            return
        #I would have implemented this differently without the time contraints
        #I.e. adding stage dependencies
        for stage in self.stages:
            (self.state, self.data) = stage(self.state, self.data)
        return self.data
    def getState(self):
        return self.state
    def getData(self):
        return self.data