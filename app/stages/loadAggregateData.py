import requests

def run(state, data):
    rstr = 'http://0.0.0.0:5001/rest/cars_agg?start=11/11/2018&end=13/11/2018&location=[lat,lon]'
    r = requests.get(rstr)
    json_data = r.json()
    if "data" in json_data:
        data["avAgg"] = json_data["data"]
    return(state,data)
