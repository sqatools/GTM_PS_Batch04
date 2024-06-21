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

# str1='India is best cricket teams'
# str2=str1.split(" ")
# dict1={}
#
# for val in str2:
#     count=0
#     count=count+1
#     dict1[val]=count
#
# print(dict1)
str3 = "India is best cricket teams"
list2=str3.split(" ")
dict1={}
dict2={}


for word in list2:
    word_len=len(word)
    dict1[word_len]=f"{word[0].upper()}{word[1:-1]}{word[-1].upper()}"

print(dict1)

# k1=dict1.keys()
# val=dict1.values()
# final_output=dict(zip(val,k1))
# print(final_output)

#Write a python python program to calculate sum of all the numbers in the string.
#str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
#output = 89

str
