#Let's add our car info
def run(state, data):
    #answers = state["answers"]
    #Here we would call our whatever to define how to filter/sort based on the questions
    #I'll just run a capacity filter
    for agg in data["avAgg"]:
        del agg["car_data"]

    return(state,data)
