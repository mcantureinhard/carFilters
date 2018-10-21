import requests

#Let's add our car info
def run(state, data):
    carsMap = {}
    for agg in data["avAgg"]:
        carsMap[agg["car"]] = {}
    cars = list(carsMap)
    rstr = 'http://0.0.0.0:5002/rest/cars_dict'
    r = requests.post(rstr, json={"ids":cars})
    json_data = r.json()
    print(json_data)
    for car, car_info in json_data.items():
        carsMap[car] = car_info
    #With a real obj this loop probably would have been avoided
    for agg in data["avAgg"]:
        agg["car_data"] = carsMap[agg["car"]]
    return(state,data)