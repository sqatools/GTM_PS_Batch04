#Get all the digits from the string

string1=""""
Sinak’s 1112 aim is to 1773 create a new generation of people who understand 444 that an organization’s
        5324 success or failure is based on 555 leadership excellence and not managerial acumen

"""
list1=string1.split()
list2=[ ]
for char in list1:
    if char.isdigit():
        list2.append(char)

print(list2)
