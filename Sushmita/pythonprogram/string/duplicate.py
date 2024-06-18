#Write a Python program to remove duplicate words from the string.

string ='John jany sabi row john sabi'

list1=string.split( )
str1=[]

for word in list1:
    if word not in str1:
        str1.append(word)

print(" ".join(str1))

#Remove unwanted characters from the given string
string1="Prog^ra*m#ming"

str2=string1.split()
result=[ ]
for char in str2:
    if char.isalnum():
        result.append(char)


print(result)

#Get common words from strings
string1 = "Very Good Morning, How are You"
string2 = "You are a Good student, keep it up"

list_a=[]
for word in string1.split(" "):
    if word in string2.split(" "):
       list_a.append(word)
print(" ".join(list_a))
