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


#Write a python to count vowels from each word in the given string show as dictionary output.
#Input = “We are Learning Python Codding”
#output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}


str_d = "We are Learning Python Codding"
str = str_d.split(" ")
vowels = "aeiou"
new_str= {}
count = 0

for word in str:
    for char in word:
        if char in vowels:
            count = count+1
            new_str[word] = count
        else:
            continue
print(new_str)

#Write a python to repeat vowels 3 times and consonants 2 times.
#Input = “Sqa Tools Learning”
#Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”

str_e = "Sqa Tools Learning"
vowels = ["a","e","i","o","u",
          "A","E","I","O","U"]
result = ""

for word in str_e:
    if word in vowels:
        result = result + word*3
    else:
        result = result + word*2
print(result)


#Write a  python program to re-arrange the string.
#Input = “Cricket Plays Virat”
#Output = “Virat Plays Cricket”

str_e = "Cricket Plays Virat"
str = str_e.split(" ")
str.reverse()

print(" ".join(str))

#Write a  python program to get all the digits from the given string.
#Input = “””
#Sinak’s 1112 aim is to 1773 create a new generation of people who
#understand 444 that an organization’s 5324 success or failure is
#based on 555 leadership excellence and not managerial
#acumen
#“””
#Output = [1112, 5324, 1773, 5324, 555]

#str_f =  """#Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen"""
"""
output = [ ]
str = str_f.split(" ")
print(str)

for word in str:
    if word.isnumeric():
        output.append(word)
print(output)


#Write a python program to replace the words “Java” with “Python” in the given string.
#Input = “JAVA is the Best Programming Language in the Market”
#Output = “Python is the Best Programming Language in the Market”

str_g = "JAVA is the Best Programming Language in the Market"
str = str_g.split(" ")
print(str)
new_str = " "

for word in str:
    if word == "JAVA":
        index = str.index(word)
        str[index] = "Python"

new_str = " ".join(str)
print(new_str)


#Write a  Python program to get all the palindrome words from the string.
#Input = “Python efe language aakaa hellolleh”
#output = [“efe”, “aakaa”, “hellolleh”]

str_z = "Python efe language aakaa hellolleh"
str = str_z.split(" ")
new_str = [ ]
for val in str:
    if val == val[::-1]:
        new_str.append(val)
    else:
        continue
print(new_str)

#Write a  Python program to create a string with a given list of words.

#Input = [“There”, “are”, “Many”, “Programming”, “Language”]
#Output = There are many programming languages.

list1 = ["There", "are", "Many", "Programming", "Language"]

#Printing output
print(" ".join(list1))

#Write a Python program to remove duplicate words from the string.
#Input = “John jany sabi row john sabi”
#output = “John jany sabi row”

str_c = "john jany sabi row john sabi"
str = str_c.split(" ")
new_str= [ ]

for val in str:
    if val not in new_str:
        new_str.append(val)
    else:
        continue
print(" ".join(new_str))

"""
#Write a Python to remove unwanted characters from the given string.
#Input = “Prog^ra*m#ming”
#Output = “Programming”

#Input = “Py(th)#@&on Pro$*#gram”
#Output = “PythonProgram”

list = "Py(th)#@&on Pro$*#gram"
list_2 = list.split(" ")
list_1 = []

for letter in list:
    if letter.isalnum():
        list_1.append(letter)
print(" ".join(list_1))



