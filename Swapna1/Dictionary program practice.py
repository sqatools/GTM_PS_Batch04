"""Python program to add elements to the dictionary"""
dic = {}
dic["Name"]="Swapna"
dic["Age"]="30"
dic["Location"]="Blore"
print(dic)
print("_" *50)
"""Print the square of all values in a dictionary."""

dic1={'a':2, 'b':3,'c':5}
for i in dic1:
    print(i,":",dic1[i]**2)
print("_" *50)


"""Move items from one dictionary to another."""

dic3={'Name':'Swapna', 'Location':'Blore','Working at':'TCS'}
dic4={}
for a in dic3:
    dic4[a]=dic3[a]
print(dic4)
print("_" *50)

"""Program to concatenate two dictionaries"""
