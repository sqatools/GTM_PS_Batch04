"""
#1vowels in string

str1 = "code learning is fun"
vowels = "aeiou"
output =""
count = 0
for val in str1:
    if val in vowels and val not in output:
        output = output + val
        count = count+1
    else:
        continue
print(output)
print(count)

print("-"*60)
#2 largest word among string

str2 = "We Are Learning Python Programming and Its Very Easy"

max_len = 0
longest_word = ""

word_list = str2.split(" ")
print(word_list)

for word in word_list:
    word_len = len(word)
    if word_len > max_len:
        max_len = word_len
        longest_word = word
    else:
        continue
    print(longest_word, max_len)
print(longest_word, max_len)

print("-"*60)
#3 Count of each character without count method

#findout the count of each word without using count method and store in a dictionary

str3 ="python programming"
#output = { 'p':2,'y':1............)

dict1 ={}
for char in str3:
    print(char)
    if char in dict1:
        dict1[char] +=1
    else:
        dict1[char] = 1
print (dict1)


dict1 ={}
for char in str3:
    if char in dict1:
        dict1[char] += 1
    else:
        dict1[char] = 1
print(dict1)


#4 Python program to get a string made of the first and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string

str4 = "Good luck"

length = len(str4)
if length < 2:
    print(true)
else:
    print(str4[:2] + str4[-2:])

#5 Python string program that takes a list of strings and returns the length of the longest string.

str5 = "better luck on coming sessions"

max_len =0
longest_word =""

str_list = str5.split(" ")
print(str_list)
for str in str_list:
    word_len=len(str)
    if word_len>max_len:
        max_len =word_len
        longest_word = str
    else:
        continue
print(max_len,longest_word)


#6 Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).

str5 = "Good"
#str = str5[-2:]
#print(str)
print(str5[-2:]*4)


#7  Python string program to reverse a string if it’s length is a multiple of 4.

str6 = "Good morning all"   #space will also count


#len = len(str6)
#if len%4==0:
#    print(str6[::-1])


if len(str6) %4==0:
    print(str6[::-1])

# 8Python string program to count occurrences of a substring in a string.

str = "python learning python on laptop"

print(str.count("on"))


#Python string program to test whether a passed letter is a vowel or consonant.
str7 = "learning python"
vowels = "aeiou"

for char in str7:
    if char== 'a' or char =='e' or char == 'i' or char == 'o' or char == 'u':
        print(f"{char}, is vowel")
    else:
        print(f"{char} is consonent")



#9 Find the longest and smallest word in the input string.

str8 = "i am learning python since last month"

str = str8.split(" ")

print("longest word :",max(str, key = len))
print("shortest word : ", min(str, key=len))



#Print most simultaneously repeated characters in the input string.

str9 ="sdsfsfsf sdsdsf gfgfhghgdf dfddruruir"

re_count = {}

for char in str9:
    if char in re_count:
        re_count[char] +=  1
    else:
        re_count[char] = 1
print(re_count)

max_key = max(re_count ,key=re_count.get)
print(max_key, re_count[max_key])



#length of string using loop concept



str = "im am mahila"
count = 0

for char in str:
    count = count+1

print("count of string without len method : ", count)
print("count of string with len method : ", len(str))


#Write a Python program to replace the second occurrence of any char with the special character $.
#Input = “Programming”
#Output = “Prog$am$in$”

str_a = "programming"
occu_char = " "

for char in str_a:
    if char in occu_char:
       occu_char = occu_char + "$"
    else:
       occu_char = occu_char + char

print(occu_char)



#Write a  python program to get to swap the last character of a given string.
#Input = “SqaTool”
#Output = “lqaTooS”

str_b = "SqaTool"
first_char = str_b[0]
last_char = str_b[-1]
rem_str = str_b[1:-1]

output = last_char+rem_str+first_char
print(output)


#Write a  python program to exchange the first and last character of each word from the given string.
#Input = “Its Online Learning”
#Output = “stI enlino gearninL”

str_c = "Its online learning"

list_c = str_c.split(" ")
print(list_c)

for word in list_c:
    new_word = word[-1]+word[1:-1]+word[0]
    index_word =list_c.index(word)
    list_c[index_word]= new_word

output = print(" ".join(list_c))

"""
#Write a python to count vowels from each word in the given string show as dictionary output.
#Input = “We are Learning  Python Codding”
#output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}



