import json

def read_json_data(filename):
    with open(filename, "r") as file:
        data = file.read()
        json_data = json.loads(data)
        print(json_data)

data = read_json_data("json_filehandling.json")

import json

def read_json_data(filename):
    with open(filename, "r") as file:
        data = file.read()
        json_data = json.loads(data)
        return json_data

data = read_json_data("json_filehandling.json")

print(data['name'])

test1_data = read_json_data("json_filehandling.json")["test_data"]["test_01"]
print(test1_data)

test2_data = read_json_data("json_filehandling.json")["test_data"]["test_02"]
print(test2_data)

test3_data = read_json_data("json_filehandling.json")["test_data"]["test_03"]
print(test3_data)