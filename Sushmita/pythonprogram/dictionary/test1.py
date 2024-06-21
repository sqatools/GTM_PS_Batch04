#Write a python python program to calculate sum of all the numbers in the string.
#str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
#output = 89

# str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
# str2=str1.split()
# list1=[]
#
# for val in str2:
#     if val.isnumeric():
#         list1.append(val)
# print((list1))
# print(sum(list1))
#
# #print(list1)

str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
output = []
word_list = str1.split(" ")
print(word_list)
sum=0
for word in word_list:
    if word.isnumeric():
        output.append(word)
        sum=sum+int(word)
print(output)
print(sum)
