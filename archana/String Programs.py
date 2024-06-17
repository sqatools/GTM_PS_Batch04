str1= "Its Online Learning"
if len(str1) <2:
    print("True")
else:
    print(str1[:2]+str1[-2:])

print("-"*50)

str2=["hello",'hiiiityiu',"python","archana"]
#hello-5, hi-2, python-6, archana- 7
temp=0
for word in str2:
    a= len(word)
    if a>temp:
        temp =a
print(temp)

print("-"*50)

str3="Its Online Learning"
last_char= str3[-2:]
remaining_char= str3[0:-2]
output= f"{remaining_char}{last_char*4}"
print(output)

print("-"*50)
str4="sqltools"
print(str4[-2:]*4)

print("-"*50)

str5="archana"
a=len(str5)
if a%4==0:
    print(str5[::-1])
else:
    print("not a multiple")

print("-"*50)
str6="sqltoolsqltoolsql"
print(str6.count("s"))

print("-"*50)
letter= "z"
str7=['a','e','i','o','u']
if letter in str7:
    print("it is a vowel")
else:
    print("consonant")

print("-"*50)
str8="python programming"
a= str8.split(" ")
b= max(a)
c= min(a)
print(b)
print(c)

##################################
str9="i am learning"
count=0
for i in str9:
    count+=1
print(count)

str10="sqltooly"
print(str10[-1]+str10[1:-1]+str10[0])

str1="sqa Tools Learning"
result=" "
vowels=[ 'a','e','i','o','u','A','E','I','O','U']
for char in str1:
    if char in vowels:
        result= result+char*3
    else:
        result= result+char*2
print(result)

str= "cricket plays virat"
list= str.split(" ")
list.reverse()
print(list)

str1= """Sinak’s 1112 aim is to 1773 create a new generation of people who understand 444 that an organization’s
        5324 success or failure is based on 555 leadership excellence and no"""

list1= str1.split(" ")
list2=[]
for val in list1:
    if val.isdigit():
        list2.append(val)
print(list2)

print("-"*50)

list2= "JAVA is the JAVA Programming Language in the Market"
output= list2.replace("JAVA","PYTHON")
print(output)

list1= list2.split(" ")
for word in list1:
    if word=="JAVA":
        index= list1.index(word)
        list1[index]="PYTHON"
print(list1)

print("-"*50)
string= "Python efe language aakaa hellolleh"
list= string.split()
new_list=[]

for val in list:
    if val== val[::-1]:
        new_list.append(val)
print(new_list)

string= ["There", "are", "Many", "Programming", "Language"]
print(" ".join(string))

str= "John jany sabi row John sabi"
list1= str.split()
list2=[]
for val in list1:
    if val not in list2:
        list2.append(val)
print(" ".join(list2))
