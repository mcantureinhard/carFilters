from app.filters.carFilter import CarFilter

#Let's add our car info
def run(state, data):
    #answers = state["answers"]
    #Here we would call our whatever to define how to filter/sort based on the questions
    #I'll just run a capacity filter
    filters = {"capacity" : [3]}
    objList = data["avAgg"]
    carFilter = CarFilter()
    result = carFilter.process(objList, filters)
    data["avAgg"] = result["list"]
    data["aggs"] = result["aggs"]

    return(state,data)
