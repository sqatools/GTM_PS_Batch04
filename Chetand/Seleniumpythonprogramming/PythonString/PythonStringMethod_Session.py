##################### String Methods #####################
print(dir(str))

"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
  'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
   'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
    'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
     'partition', 'removeprefix', 'removesuffix', 'replace', 
     'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
      'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
      'title', 'translate', 'upper', 'zfill'
"""

# convert the string into upper to lower and lower to upper

########
# upper() and lower() methods:

str_a = "Hello We Learning Python"
print("upper case :", str_a.upper())   # HELLO WE LEARNING PYTHON
print("Lower case :", str_a.lower())   # hello we learning

# swapcase method : This will convert upper to lower and lower to upper
print("swap case output :", str_a.swapcase()) # LLO wE lEARNING pYTHON

# isupper() and islower() method : This method will return the True and False if the string is upper or lower
strb = "Hello"
print("strb:", strb.isupper(), strb.islower()) # False False
strc = "PYTHON"
strd = "programming"
print("strc is upper :", strc.isupper()) #  True
print("strd is lower :", strd.islower()) #  True

print("_"*50)
##########
# title() method : This method will convert the string into title case, it means first character of each word will be capital
str_e = "learning Is fun, python is very easy"
print("title case :", str_e.title())  #  Learning Is Fun, Python Is Very Easy

# istitle() method: This method check the given string is title case or not.
str_f = "Python Programming"
print("str_f is title :", str_f.istitle())  # True
print("str_e is title :", str_e.istitle())  # False


print("_"*50)
##########
# count() method : This method will return the count of any char/substring in given string.
str_g = "learning Is fun, python Is very easy"
print("count of e :", str_g.count("e")) # 3
print("count of Is :", str_g.count("Is")) # 2
print("count of space :", str_g.count(" "))  # 6

temp = ""
for char in str_g:
    if char not in temp:
        print(char,":", str_g.count(char))
        temp = temp + char
        #print(temp)
    else:
        continue

print("string with duplicate :", temp)

########
# index method : this method will return the index position of any char/substring
str_h = "Indian Cricket Team"
print("index of C :", str_h.index("C"))  # 7
print("index of Cricket :", str_h.index("Cricket")) # 7
print("index of Team :", str_h.index("Team")) # 15

# if given string/char is not available then it will throw error
# print("index of W :", str_h.index("W"))  #  ValueError: substring not found


###########
# find method() : This method return the index position of char/substring if
# it is available else it will return -1

str_k = "Learning is Fun"
print("find is :", str_k.find("is"))  # 9
# if the string or char is not available then it will return output as -1
print("find is :", str_k.find("Was")) # -1

####################################

str2 = "Good Morning"
print(str2[:8:-1])

print("_"*50)
###################################
# replace method : this method replace the one word to another

str_a = "Hello We Are Learning Python"
output = str_a.replace("Python", "Java")
print("Replaced output :", output)

Output2 = output.replace("Are", "Were")
print("output2 :", Output2)

output3 = str_a.replace("Python", "Java").replace("Are", "Were")
print("Output3 :", output3)

output4 = output3.replace("Python", "Java")
print("output4 :", output4)

print("-"*50)
####################
# split() method : This method can break the string in list of substring.

str_1 = "Today India is playing good cricket"
str_2 = "India,will,win,the,match"
str_3 = "Learning%is%Fun"

output1 = str_1.split(" ")
print("output 1:", output1)
# ['Today', 'India', 'is', 'playing', 'good', 'cricket']


output2 = str_2.split(",")
print("output 2:", output2)
# ['India', 'will', 'win', 'the', 'match']

output3 = str_3.split("%")
print("output 3:", output3)
# ['Learning', 'is', 'Fun']


str_4 = "Pytnghon ProngramingAre"
print("output4 :", str_4.split("o"))
# ['Pyth', 'n Pr', 'graming']

print("output5 :", str_4.split("ng"))
# ['Pyt', 'hon Pro', 'rami', 'Are']

###################
print("_"*50)
# strip() method : This method remove the training spaces from given string
str_m = "  Python Programming  "
print(str_m)

output1 = str_m.strip()
print(output1)

output2 = str_m.lstrip()
print(output2)

output3 = str_m.rstrip()
print(output3)

########################################
#join() method : This method can join any string with delimeters

str_j = "Learning"

output_j = "-".join(str_j)
print("output j:", output_j)  # L-e-a-r-n-i-n-g

print("output2 :", "&^&".join(str_j))  # L&^&e&^&a&^&r&^&n&^&i&^&n&^&g

var1 = "&^&".join(str_j)
print(var1)

var2 = var1.replace("&^&", "")
print("var2 :", var2)

####################################
print("_"*50)
# isalpha method will return if string only contains alphabates
str_a = "Hello"
print(str_a.isalpha()) # True

# isnumeric : This method return true if string only contains numberic value
str_b = "34567"
print("check is numeric :", str_b.isnumeric()) # True

str_b1 = "34567 Word"
print("check is numeric :", str_b1.isnumeric()) # False

# isalnum: This method check if string only contains number and characters.
str_c = "234Virat"
print("check for string and numeric values :", str_c.isalnum())  # True

str_c1 = "234Virat 112"
print("check for string and numeric values :", str_c1.isalnum()) # False

# isspace: this method check given char is space or not
str_e = "Hello good morning, I hoper you are doing good"

for char in str_e:
    print(char, ":", char.isspace())

str_f = "  "
print("check for space :", str_f.isspace())


# isascii method:
# ASCII characters have code points in the range U+0000-U+007F

str_t = "127"
print("is ascii :", str_t.isascii())
print("is ascii :", "U+0001".isascii())

for i in range(65, 128):
    print(i, ":", chr(i))





