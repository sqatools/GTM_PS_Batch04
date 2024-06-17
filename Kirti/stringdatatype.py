# # """String is a sequantial data
# # it follows the posotive and negative index
# # anything declared in singl double and triple cotes is known as string"""
# #
# # s1 = 'Hello'
# # s2 = "Hi"
# # s3 = "Hyfy"
# #
# # print("s1",type(s1))
# # print("s2",type(s2))
# # print("s3",type(s3))
# #
# # Str1 ="PROGRAMMING"
# #
# # print(Str1[2])
# # print(Str1[-9])
# #
# # for v in Str1:
# #     print(v)
# #
# # #Sting formatting
# #
# #
# # name = "Rahul"
# # age = 25
# # city = "Mumbai"
# #
# # #1. String concatination (We can add two string using + operator)
# #
# # v1 = 'hello'
# # v2 = 'Good morning'
# # v3 = v1 + " " + v2
# # print(v3)
# #
# # result = "My name is "+name+" and age is "+str(age)+" and i live in"+city
# # print(result)
# #
# # # here we converted the integer data type into sring by str(age)
# #
# # #2. Format method by using {}
# # result1 = "My name is {} and age is {} and i live in {}".format(name, age, city)
# # print(result1)
# #
# # # 3. f string formatting:
# # result2 = f"My name is {name} and age is {age} and i live in {city}"
# # print(result2)
# #
# # city_list = ['Mumbai', "pune","Delhi"]
# # result3 = f"My name is {name} and age is {age} and i live in {city_list[0]}"
# # print(result3)
# #
# #
# # # String slicing
# # #Rule1 : str1[strtingindex : ending indes]
# # #last index will always be trimmed
# #
# # Str1 = "Python Programminng"
# # result4 = Str1[0:6]
# # print("result4:",result4)
# #
# # #positive and negative index
# #
# # output1 = Str1[1 :-1]
# # print(output1)
# #
# #
# # output2 = Str1[-6 :-1]
# # print(output2)
# #
# #
#
#
# print("Practice for string data tyeps ")
#
# # . Write a  Python program to get a string made of the first and the last 2 chars from a given string.
# # If the string length is less than 2, return instead of the empty string.
#
# # is this correct ?
#
# # a = "My name is kirti"
# #
# # print("String : ",a)
# #
# # if len(a) == 2 :
# #     print("True")
# # else :
# #     print(a[:2]+a[-2:])
#
#
# #     a in range (0,-1)
# #     x1 = (a[0],a[1])
# #     x2 = (a[-1],a[-2])
# #     print(x1+x2)
#
#
# #  Python string program that takes a list of strings and returns the length of the longest string.
#
#
# a = ["Kirti","Ram","Shyam","Sita","Hakhkhkjnuman"]
#
#
# temp = 0
#
# for i in a:
#     #print(i)
#     n = len(i)
#     #print(n)
#     if n > temp:
#         temp = n
#         print(temp)


#In this program, we will take a string as input and get a string made of 4 copies of last 2 characters
# a="Python"
#
# print("Last two char :",a[4:6]*4)
# print(a[-2:]*4)

#In this program, we will take a string and substring as input and count occurrences of a substring in a string.

# a = "python programming, pro"
# sub = "pro"
#
# # count =0
# #
# # for i in a :
#     #print(i(a))
#
# print("count", sub.count("pro"))


#

String = "Hello every one"

repete_count =""
repete_chara = ""

for i in range (len(String)-1) :
    if String[i] == String[i]:
        repete_count=+1


#4). Python string program to reverse a string if it’s length is a multiple of 4. Output issue

# a = "Programming"
#
# print(len(a))
# X = len(a)
#
# if X % 4 == 0:
#     print(a[::-1])
# else :
#     print("Exit")

#5). Python string program to count occurrences of a substring in a string. Getting blank out put
#
# string = "My name is kirti, i am learing python"
# substring = "My"
#
# #substring in string  how to do this using range
#
# output = string.count("kirti")  # print statement will refer to what ?
# print(output)

#7). Find the longest and smallest word in the input string. # how min max function work in solution?

# string = "python programming is easy to lear and understand"
#
# length_of_word = ""
# maxlength = 0
# minlength  to try with
#
# #print("count",a.count(a)) # for this out put is 1
# wordslist = string.split(" ")
# print(wordslist)
#
# for word in wordslist:
#    # print(word)
#     length_of_word = len(word)
#     #print(length_of_word)
#     if length_of_word > maxlength:
#         maxlength = length_of_word
#         length_of_word = word
#     else:
#         continue
#     print(length_of_word,maxlength) # back sapce issue


# Smallest word
#
# a = "python programming is easy to lear and understand"
#
# minlenth = 50
# minword = " "
#
# allwords = a.split(" ")
#
# print(allwords)
#
# for words in allwords:
#     #print(words)
#     lengthofword = len(words)
#     #print(lengthofword)
#     if lengthofword <= minlenth:
#         minlenth = lengthofword
#         minword = words
# print(minlenth,minword)



#10). Write a Python program to replace the second occurrence of any char with the special character $.

# str1 ="Programming"
# empstr =" "
# for i in str1 :
#     if i in empstr:
#         empstr = empstr + "$"
#     else:
#         empstr = empstr + i
# print(empstr)


# 11). Write a  python program to get to swap the last character of a given string. # have swapped last two words of string

# q = "Kirti Kaur is my name"
#
# print(q)
#
# a = q.split(" ")
# first_word = a[0]
# last_word = a[-1]
#
# a[0]= last_word
# a[-1] = first_word
#
# print(a)
# print(" ".join(a))
# print("Last character : ", a[-1])
# print("second last char : ",a[-2])
#
# print(a[0],a[1],a[2],a[-1],a[-2])
# print(a[-1],a[1:4],a[0])

# 14). Write a python to repeat vowels 3 times and consonants 2 times

# a = "programming"
#
# vowels = "aeiou"
# conso = " "
#
# for char in a:
#     if char in vowels:
#         print(char*3)
#
#     else :
#         conso = char
#         print(conso*2)
