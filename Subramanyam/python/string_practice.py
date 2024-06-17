# str1="python"
# for i in str1:
#     #print(i)
#     print(i,end=" ")

# name="subbu"
# age=30
# city="Tirupathi"
# city1=["chennai","pune","Bengalore"]
# rel="My name is "+name+" and age is "+str(age)+" and my from "+city
# print(rel)
# rel1="My name is {} and age is {} and my from {} ".format(name,age,city)
# print(rel1)
# rel2=f"My name is {name} and age is {age} and live in {city1[2]}"
#
# print(rel2)

# str1="python programming"
# output=str1[0:6]
# print(output)
# print(str1.index(" "))
#
# opu=str1[7::]+" "+str1[:6:]
# print(opu)
#
# last_char=str1[-1]
# first_char=str1[0]
# remaining_char=str1[1:-1]
# result=f'{last_char*3}{remaining_char}{first_char*3}'
# print(result)
#
# last_word=str1[7:]
# first_word=str1[:6]
#
# rel=f"{last_word} {first_word}"
# print(rel)
#
#
# we="we are are are  learning codding"
# print(we.upper())
# print(we.lower())
# print(we.swapcase())
# print(we.title())
# print(we.count("e"))
#
# print(we.count("re"))


# str_g = "9966466046"
# temp = ""
# for char in str_g:
#     if char not in temp:
#         print(char,":", str_g.count(char))
#         temp = temp + char
#         #print(temp)
#     else:
#         continue

#print("string with duplicate :", temp)

# phone=input("Enter phone number: ")
# count=""
# temp=""
# for i in phone:
#     if i not in count:
#         # print(i,":",phone.count(i))
#         count=count+i
#         # count=temp
#     else:
#         continue

# for i in phone:
#     if i in temp:
#         print(temp)

#print(count)

# str1="indian  cricket team"
# print("Index is: ",str1.index("ket"))
# print("Index of team: ",str1.index("team"))
# print(str1[8::-1])
# output=str1.replace("cricket","Cricket")
# op=str1.replace("indian","Indian").replace("team","Team")
#
# print(output)
# print(op)
#
# str_4 = "Pytn%ghon ProngramingAre"
# print("output4 :", str_4.split("%"))
# ['Pyth', 'n Pr', 'graming']

#print("output5 :", str_4.split("ng"))
# ['Pyt', 'hon Pro', 'rami', 'Are']

# str_m = "  Python Programming  "
# print(str_m)
#
# output1 = str_m.strip()
# print(output1)
#
# output2 = str_m.lstrip()
# print(output2)
#
# output3 = str_m.rstrip()
# print(output3)
#
# str2="python"
# ou="&_&".join(str2)
# print(ou)
#
# opt=ou.replace("&_&","")
# print(opt)
#
#
# str_e = "Hello good morning, I hoper you are doing good"
#
# for char in str_e:
#     print(char, ":", char.isspace())
#
#
# for i in range(65,127):
#     print(i,":",chr(i))


# st1="we are learning codding here your"
# vowels="aeiou"
# count=0
# output=""
# for i in st1:
#     #print("char: ",i,"output: ",output)
#     if i in vowels and i not in output:
#         output=output+i
#         count+=1
#     else:
#         continue
# print(output)

# str1="Enjoying to learning python codding"
# for i in range(len(str1)-1,-1,-1):
#     print(str1[i],end="")
# print()
# print("_"*100)
#
#
# count=len(str1)-1
# while count>=0:
#     print(str1[count],end="")
#     count-=1
# print()
# print("-"*100)
#
# out=str1[::-1]
# print(out)
#
# print()
# print("-"*100)
#
# val=list(reversed(str1))
# print(val)
# print("".join(val))
# print("-"*100)
#
# str2=" "
# str3=[]
# for i in str1:
#     str3.append(i)
# print(str3)
# str2="".join(str3)
# print(str2)
# print(dir(str))


# str1="we are learning python programming here in  today session"
# max_len=0
# longest_word=""
# word_list=str1.split()
# for word in word_list:
#     word_len=len(word)
#     if word_len>max_len:
#         max_len=word_len
#         longest_word=word
#     else:
#         continue
# print(longest_word,":",max_len)

# str1="python programming"
# dict1={}
# for char in str1:
#     if char not in dict1:
#         dict1[char]=1
#     else:
#         dict1[char]+=1
#
# print(dict1)

# str1="we are learning python"
# output=str1.split()
# print("maximum length is: ",max(output,key=len))
# print("minimum length is: ",min(output,key=len))
# count=0
# for word in output:
#     if len(word)>long:
#         long=word
#     elif len(word)<short:
#         short=word
#
# print(long)
# print(short)

# def longest_and_smallest_words(input_string):
#     words = input_string.split()  # Split the string into words
#     if not words:
#         return None, None  # Handle case where there are no words
#
#     longest_word = shortest_word = words[0]  # Initialize variables with the first word
#
#     for word in words:
#         if len(word) > len(longest_word):
#             longest_word = word
#         if len(word) < len(shortest_word):
#             shortest_word = word
#
#     return longest_word, shortest_word
#
#
# # Example usage:
# input_str = "Python is an amazing language"
# longest, smallest = longest_and_smallest_words(input_str)
# print("Longest word:", longest)
# print("Smallest word:", smallest)

# str1="heellooo asjhhdjdf kkisjsffhfhhd"
# word_co=0
# word_le=""
# temp=1
# for i in range(len(str1)-1):
#     if str1[i]==str1[i+1]:
#         temp=temp+1
#         if temp>word_co:
#             word_co=temp
#             word_le=str1[i]
#     else:
#         temp=1
#
# print(word_le,word_co)
#
# str1="we are learning"
# count=0
# for i in str1:
#     count=count+1
#
# print(count)
# print(len(str1))

# str1="programming"
# result=""
# for i in str1:
#     if i in result:
#         result=result+"$"
#     else:
#         result=result+i
#
# print(result)
# result1=str1[-1]+str1[1:-1]+str1[0]
# print(result1)

# str1="we are learning python"
# list1=str1.split(" ")
#
# for word in list1:
#     new_word=word[-1]+word[1:-1]+word[0]
#     index=list1.index(word)
#     list1[index]=new_word
# print(' '.join(list1))
# vo='aeiou'
# dict1=dict()
# count=0
# for i in list1:
#     count = 0
#     for j in i:
#         if j in vo:
#             count+=1
#     dict1[i]=count
# print(dict1)

# vowels='aeiou'
# dict1=dict()
# for word in list1:
#     count=0
#     for char in word:
#         if char in vowels:
#             count+=1
#     dict1[word]=count
# print(dict1)

# str1="Sqa Tools is Learning"
# str2=""
# li="aeiouAEIOU"
# for char in str1:
#     if char in li:
#         str2=str2+char*3
#     else:
#         str2 = str2 + char * 2
# print(str2)
#
# list1=str1.split()
# list1.reverse()
# output=" ".join(list1)
# print("Ra-arrangement of a string: ",output)

str1="""Sinak’s 1112 aim is to 1773 create a new generation of people who understand 444 that an organization’s
        5324 success or failure is based on 555 leadership excellence and not managerial acumen"""

list1=str1.split(" ")
list2=[]
for i in list1:
    if i.isdigit():
        list2.append(i)
print(list2)

str2="python is fun,learning python"
#st=str2.replace("python","java")
list3=str2.split(" ")
for word in list3:
    if word=="python":
        index=list3.index(word)
        list3[index]="java"
print(" ".join(list3))


st="aha digital eneterpriecs ala"
li1=st.split(" ")
new_li=[]
for word in li1:
    if word==word[::-1]:
        new_li.append(word)
print(new_li)