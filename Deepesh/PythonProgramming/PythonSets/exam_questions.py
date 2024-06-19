"""
str1 = "Good 12 Morning 45 , Hope 2 you are 30 doing good"

str2 = str1.split(" ")
print(str2)
Total=0

for val in str2:
    if val.isnumeric():
        print(val)
        print(type(val))
        x1 = int(val) # conversion not possible hence addition not possible
        print(type(val))
        Total += x1

print(Total)
"""

"""
str1 = "India is best cricket teams"
#utput = {5: "IndiA", 2: "IS", 4: "BesT", 7:"CrickeT", 5: "TeamS"}
str2=str1.split()
print(str2)
output = {}
for char in str2:
    output[len(char)] = char[0].upper()+char[1:-1]+char[-1].upper()

print(output)
"""


str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
word_list=str1.split(" ")
output=[]
count=0

for word in word_list:
    if word.isnumeric():
        output.append(word)
        count+=int(word)

print(count)
