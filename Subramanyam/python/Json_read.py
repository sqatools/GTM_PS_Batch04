import json

def read_json_file(filename):
    with open(filename,"r") as file:
        data=file.read()
        json_data= json.loads(data)
        return json_data

data=read_json_file("test_file1.json")
print(data['name'])


email=read_json_file("test_file1.json")["email"]
print("the email address: ",email)

test1_data=read_json_file("test_file1.json")["test_data"]["test_01"]["username"]
print(test1_data)

test2_data=read_json_file("test_file1.json")["test_data"]["test_02"]
print(test2_data["password"])

test3_data=read_json_file("test_file1.json")["test_data"]["test_03"]
print(test3_data)