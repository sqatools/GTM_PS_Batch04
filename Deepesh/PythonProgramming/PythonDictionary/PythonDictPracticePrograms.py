# write a python program to create a dictionary from given string.

str1= "Hello Good Morning, Hope you are"
# output = {'Hello' : 5, 'Good' : 4, 'Morning,' : 8, 'Hope' : 4, 'you' : 3, 'are' : 3 }

word_list = str1.split(" ")
print(word_list)
result = {}

for word in word_list:
    word_len = len(word)
    result[word] = word_len

print("Result :", result)


#dict1= {'a': 123}
#dict1['b'] = 400

print("_"*50)
################################################
# write a python to store even data with square and odd data with cube in the dict.

list1 = [4, 7, 2, 8, 1, 6, 9]
# output = {4: 16, 7:343, 2: 4, 8: 64, 1:1, 6:36, 9:729}
result = {}
for val in list1:
    if val%2 ==0:
        result[val] = val**2
    else:
        result[val] = val**3

print("result :", result)



