# write a python to find out the vowels in the given string.

str1 = "Code Learning is Fun"
#output = "oeeaiiu"
vowels = "aieou"
output = ""
count = 0



"""
1. iterate though each character using loop "for char in str1"
2. check the char is available in vowels list or not
3. if char is vowels then add in output else continue if not available in output
4. print the output


"""

for var1 in str1:
    print("char :", var1, "output:", output)
    if var1 in vowels and var1 not in output:
        output = output + var1
        count += 1
    else:


        continue

print("output :", output, count)


print("_"*50)
####################
# program : write a python program to find out the longest word from given string.
str2 = "We Are Learning Python Programming and Its Very Easy"

max_len = 0
longest_word = ""

# get word list
word_list = str2.split(" ")
print(word_list)

# iterate though each word
for word in word_list:
    # get word length
    word_len = len(word)
    #print(word, word_len)
    # compare word length with max_lne
    if word_len > max_len:
        # interchange the max_len with word_len
        max_len = word_len
        # assign longest word
        longest_word = word
    else:
        continue
    print(longest_word, max_len)


# print longest word and max length
print(longest_word, max_len)


print("_"*50)
# Program: find out the count of each char without using count method, store in a dictionary
str3 = "Python Programming"
#output = {'P' : 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}

#dict1['P'] = 1
#dict1['P'] += 1
dict1 = {}
for char in str3:
    print(char)
    if char not in dict1:
        dict1[char] = 1
    else:
        dict1[char] += 1

    print(dict1)
