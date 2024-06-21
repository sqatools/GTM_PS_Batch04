# # # a= "Python Programming"
# # # output1= a[1:8]
# # # print(output1)
# # #
# # # o2= a[1:-1]
# # # print(o2)
# # #
# # # o3= a[-1:1]
# # # print(o3)
# # #
# # # o4=a[-6:-5]
# # # print(o4)
# # #
# # # o5= a[-6:-10]
# # # print(o5)
# # #
# # # o6= a[1:-10:1]
# # # print(o6)
# # #
# # # o7= a[1:-10:-1]
# # # print(o7)
# # #
# # # #1). Write a  Python program to get a string made of the first and the last 2 chars from a given string.
# # # #If the string length is less than 2, return instead of the empty string
# # #
# # # str="python"
# # # if len(str)<2:
# # #     print("true")
# # # else:
# # #     print(str[0:2]+str[-2:])
# # #
# # # #2). Python string program that takes
# # # #a list of strings and returns the length of the longest string.
# # #
# # # str=['i','archana','sachin','anirudh','shravya']
# # # count=0
# # # for i in str:                       #doubt- print longest str
# # #     a= len(i)
# # #     if a>count:
# # #         count= a
# # # print(count)
# # # '''
# # # print("-"*50)
# # # str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
# # # list1 = str1.split()
# # # print(list1)
# # # for i in list1:
# # #     if i!=
# # # '''
# # #
# # # print("-"*50)
# # # '''
# # # str2= "python programming is very easy to learn"
# # # str3= str2.title()
# # # print(str3)
# # # str4= str3.split()
# # # print(str4)
# # # for i in str4:
# # #     if str4[i]== str4[::-1]:
# # #         str4.split()
# # # print(str4)
# # # '''
# # #
# # # print("-"*50)
# # # str5 = "India is best cricket teams"
# # # str6={}
# # # output= str5.split()
# # # print("output")
# # # for word in output:
# # #     word_len=len(word)
# # #     str6[word]= word_len
# # # print(str6)
# # #
# # # '''
# # # print("-"*50)
# # # list1 = [13, 56, 77, 23, 29, 11]
# # # prime= True
# # # for i in list1:
# # #     if list1[i]%i ==0:
# # #         prime= False
# # #         break
# # #     else:
# # #         continue
# # #     if prime:
# # #         print("prime")
# # #     else:
# # #         print("not prime")
# # #
# # # '''
# # str1= "Good 12 Morning 45, Hope 2 you are 30 doing good"
# # str2= str1.split()
# # list1=[]
# # sum=0
# # for val in str2:
# #     if val.isdigit():
# #         list1.append(val)
# # print(list1)
# # total= sum(list1)
# # print(total)
#
# str1= "python programming is very easy to learn"
# str2= str1.title()
# str3=str2.split()
# list1=[]
# for char in str3:
#     list1.append(char[0:-1]+char[-1].upper())
# print(list1)


str5 = "India is best cricket teams"
str6={}
str7={}
output= str5.split()
print("output")
for word in output:
    word_len=len(word)
    str6[word]= word_len
    str7.update(str6)
for k,v in str7.items():
    str7[v]=k
print(str7)
