"""
Dictionary is mutable
can hold multiple data types
its defined by curly braces
It stores data in key value pair
Duplicate keys are not allowed
index and slicing is not available in dictionary
it can have duplicate values
only immutable data type can be added as a key : float int boolean string tuple
all types of data type can be value
"""

# clear method : this method clears all the data from dictionary

dict_q = {"Name" :"Jhon", "Age" :35, "Address" : "Pune"}
print(dict_q)
dict_q.clear()
print(dict_q)

#Del method :
dict_r = {"Name" :"Jhon", "Age" :35, "Address" : "Pune"}
print(dict_r)
del dict_r
print(dict_r) # name error


del dict_r  ['Address']
print(dict_r)

# copy method shallow copy

#when you modify the refence list then the changes reflects to the initial list, both the list will have same address


dicta ={"a" :345, "b":485, "c":456}

#Deep coppy

dictp = {"abc" : 556, "pqr" : 456, "xyz" : 4521}

# Set default Key
dict_h ={"a" :345, "b":485, "c":456}
