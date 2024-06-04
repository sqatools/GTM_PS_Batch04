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


