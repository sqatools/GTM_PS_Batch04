"""1. Write a python python program to calculate sum of all the numbers in the string.
str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
output = 89"""

str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
word_list=str1.split()
output=[]
for word in word_list:
    if word.isnumeric():
        output.append(int(word))
print(output)  #[12, 45, 2, 30]

print(sum(output)) # 89

#print("output: ",sum(str(count)))

# """2. Write a python Program to convert first and last character to upper case.
# str1= "python programming is very easy to learn"
# output = "PythoN ProgramminG IS VerY EasY TO LearN"""
#
str2= "python programming is very easy to learn"
list_word=str2.split(" ")
out=[]

for word1 in list_word:
    out.append(word1[0].upper()+word1[1:-1]+word1[-1].upper())

print(" ".join(out))

# '''
# 3. Write a Python Program to find out prime number from give list of values
# list1 = [13, 56, 77, 23, 29, 11]
# output = [13, 23, 29, 11]

list1 = [13, 56, 77, 23, 29, 11]
output=[]
for i in list1:
    count=0
    for j in range(1,i):
        if i%j ==0:
            count+=1
    if count==1:
        output.append(i)
print(output)

# """4. Write a python program to create below output dictionary with given string.
# str1 = "India is best cricket teams"
# output = {5: "IndiA", 2: "IS", 4: "BesT", 7:"CrickeT", 5: "TeamS"}"""
#

str3 = "India is best cricket teams"
list2=str3.split(" ")
dict1={}
dict2={}


for word in list2:
    word_len=len(word)
    dict1[word_len]=f"{word[0].upper()}{word[1:-1]}{word[-1].upper()}"

print(dict1)

k1=dict1.keys()
val=dict1.values()
final_output=dict(zip(val,k1))
print(final_output)




