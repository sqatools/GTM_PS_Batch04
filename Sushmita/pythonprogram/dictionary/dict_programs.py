#Python program to iterate over a dictionary.
D1={'a':1,'b':2}
for val in D1:
    print(val,':',D1[val])

print('_'*50)
#Python program to create a dictionary in the given form.
n=4
D2={}

for i in range(1,4+1):
    D2.update({i:i**3})
print(D2)

#Write a python program to create below output dictionary with given string.
#str1 = "India is best cricket teams"
#output = {5: "IndiA", 2: "IS", 4: "BesT", 7:"CrickeT", 5: "TeamS"}

str1='India is best cricket teams'
str2=str1.split(" ")
dict1=dict()

for val in str2:
    count=0
    count=count+1
    dict1[val]=count

print(dict1)

#Write a python python program to calculate sum of all the numbers in the string.
#str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
#output = 89

str
