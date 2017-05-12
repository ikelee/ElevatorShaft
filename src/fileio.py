import json


# Returns int, int, list of objects. This function is called from outside.
def get_data():
    data = read_file("test_cases/elevator_practice1.json")
    return data["elevators"], data["floors"], data["events"]


# Read as json. This is a helper function.
def read_file(filename):
    with open(filename) as data:
        return json.load(data)
