#methods
# clear,copy,fromkeys,get,items,keys,pop,popitem,setdefault,update,value

#Accessing Values by Key []

dict={"name":"sangeetha","age":"27"}
# print(dict["name"])
# print(dict["age"])

#get method
print(dict.get("name"))
print(dict.get("city"))

#`len()` function: Returns the number of key-value pairs in a dictionary.

print("_"*50)

print(len(dict))

#`keys()` method: Returns a view object that contains all the keys in a dictionary.
print("_"*50)
dictionary = {"name": "Yash", "age": 23, "occupation": "Architect"}
keys=dictionary.keys()
print(keys)

#`values()` method: Returns a view object that contains all the values in a dictionary.
print("_"*50)
dictionary1 = {"name": "Yash", "age": 23, "occupation": "Architect"}
value=dictionary1.values()
print(value)

#items()` method: Returns a view object that contains all the key-value pairs
# as tuples in a dictionary.
print("_"*50)
dictionary2 = {"name": "Yash", "age": 23, "occupation": "Architect"}
items=dictionary2.items()
print(items)

##`pop()` method: Removes and returns the value associated with a given key. It takes the key
# as an argument and removes the corresponding key-value pair from the dictionary.

dictionary = {"name": "Yash", "age": 23, "occupation": "Architect"}
removed_value = dictionary.pop("age")
print(removed_value)
print(dictionary)

#update()` method: Merges the key-value pairs from another dictionary into the currentdictionary.
# If a key already exists, the value is updated; otherwise, a new key-value pair is added.
dictionary = {"name": "sangeetha", "age": 23}
new_dict = {"occupation": "Architect", "city": "Pune"}
dictionary.update(new_dict)
print(dictionary)

#`clear()` method: Removes all key-value pairs from a dictionary, making it empty.
dictionary = {"name": "Yash", "age": 23, "occupation": "Architect"}
dictionary.clear()
print(dictionary)
