# # # # # # # # # # # '''
# # # # # # # # # # # #1). Write a  Python loops program to find those numbers which are divisible
# # # # # # # # # # # #by 7 and multiple of 5, between 1500 and 2700 (both included).
# # # # # # # # # # #
# # # # # # # # # # # for i in range(1500,2701):
# # # # # # # # # # #     if i%7==0 and i%5==0:
# # # # # # # # # # #         print(i,end =' ')
# # # # # # # # # # #
# # # # # # # # # # # '''
# # # # # # # # # # # #2). Python Loops program to construct the following pattern, using a nested for loops.
# # # # # # # # # # # '''
# # # # # # # # # # # *
# # # # # # # # # # # * *
# # # # # # # # # # # * * *
# # # # # # # # # # # * * * *
# # # # # # # # # # # * * * * *
# # # # # # # # # # # * * * *
# # # # # # # # # # # * * *
# # # # # # # # # # # * *
# # # # # # # # # # # *
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # #  (doubt))
# # # # # # # # # # # for i in range(6):
# # # # # # # # # # #     print(i*"*")
# # # # # # # # # # # for i in range(4,-1,-1):
# # # # # # # # # # #     print(i*"*")
# # # # # # # # # # # '''
# # # # # # # # # # # #3). Python Loops program that will add the word from the user to
# # # # # # # # # # # #the empty string using python
# # # # # # # # # # # '''a = input("enter the string")
# # # # # # # # # # # for i in range(a, end=' '):
# # # # # # # # # # #     print(i)
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #4). Python Loops program to count the number of even and odd
# # # # # # # # # # # #numbers from a series of numbers using  python.
# # # # # # # # # # # '''
# # # # # # # # # # # numbers = (1,2,3,4,5,6,7,8,9)
# # # # # # # # # # # even = 0
# # # # # # # # # # # odd =0
# # # # # # # # # # # for i in numbers:
# # # # # # # # # # #     if i%2==0:
# # # # # # # # # # #         even +=1
# # # # # # # # # # #     else:
# # # # # # # # # # #         odd +=1
# # # # # # # # # # # print("number of even numbers :",even)
# # # # # # # # # # # print("number of odd numbers:",odd)
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
# # # # # # # # # # # for i in range(0,11):
# # # # # # # # # # #     if i! =3 or i ! =6:
# # # # # # # # # # #         print(i,end =" ")
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #6). Write a program to get the Fibonacci series between 0 to 20 using python.
# # # # # # # # # # # num1=0
# # # # # # # # # # # num2=1
# # # # # # # # # # # count=0
# # # # # # # # # # #
# # # # # # # # # # # while count< 20:
# # # # # # # # # # #     print(num1,end=' ')
# # # # # # # # # # #     n2= num1+num2
# # # # # # # # # # #     num1= num2
# # # # # # # # # # #     num2=n2
# # # # # # # # # # #     count=count+1
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #7). Write a program that iterates the integers from 1 to 30 using
# # # # # # # # # # # #python. For multiples of three print “Fizz” instead of the number and
# # # # # # # # # # # #for multiples of five print “Buzz”.
# # # # # # # # # # # #For numbers that are multiples of both three and five print “FizzBuzz”.
# # # # # # # # # # # for i in range(1,31):
# # # # # # # # # # #     if i % 3 == 0:
# # # # # # # # # # #         print("Fizz")
# # # # # # # # # # #     elif i % 5 == 0:
# # # # # # # # # # #         print("Buzz")
# # # # # # # # # # #     elif i % 3==0 and i % 5==0:
# # # # # # # # # # #         print("FizzBuzz")
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #11). Python Loops program to print all natural numbers from
# # # # # # # # # # # #1 to n using a while loop in  python.
# # # # # # # # # # # #1,2,3,4,5,6,...
# # # # # # # # # # #
# # # # # # # # # # # n = int(input("enter the number"))
# # # # # # # # # # # count= 1
# # # # # # # # # # # while count<=n:
# # # # # # # # # # #     print(count,end=" ")
# # # # # # # # # # #     count+=1
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #12). Write a program to
# # # # # # # # # # # #print all natural numbers in reverse (from n to 1) using a while loop in  python.
# # # # # # # # # # # #n............6.5.4.3.2.1
# # # # # # # # # # #
# # # # # # # # # # # n= int(input("enter the value"))
# # # # # # # # # # # count = n
# # # # # # # # # # # while (count != 0):
# # # # # # # # # # #     print(count,end=" ")
# # # # # # # # # # #     count-=1
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #14)Python Loops program to print all even numbers between 1 to 100 in python.
# # # # # # # # # # # #2,4,6,8,..100
# # # # # # # # # # #
# # # # # # # # # # # for i in range(1,101):
# # # # # # # # # # #     if i%2==0:
# # # # # # # # # # #         print(i)
# # # # # # # # # # #     else:
# # # # # # # # # # #         pass
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #15)Python Loops program to print all odd numbers between 1 to 100 using python.
# # # # # # # # # # # #1,3,5,7,.......99
# # # # # # # # # # #
# # # # # # # # # # # for i in range(1,101):
# # # # # # # # # # #     if i%2!=0:
# # # # # # # # # # #         print(i,end=' ')
# # # # # # # # # # #    '''
# # # # # # # # # # # '''
# # # # # # # # # # # #16). Python Loops program to find the sum of all natural numbers between 1 to n using python.
# # # # # # # # # # # #1,2,3,4,...n
# # # # # # # # # # #
# # # # # # # # # # # n= int(input("enter the value"))
# # # # # # # # # # # count =0
# # # # # # # # # # # for i in range(1,n+1):
# # # # # # # # # # #     count= count+i
# # # # # # # # # # # print(count)
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #17). Python program to find the sum of all even numbers between 1 to n using  python.
# # # # # # # # # # # #2,4,6,8.......n
# # # # # # # # # # #
# # # # # # # # # # # n= int(input("enter the value "))
# # # # # # # # # # # count = 0
# # # # # # # # # # # for i in range(1,n+1):
# # # # # # # # # # #     if i%2==0:
# # # # # # # # # # #         count=count+i
# # # # # # # # # # # print(count)
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #18). Python Loops program to find the sum of all odd numbers between 1 to n using python.
# # # # # # # # # # # n= int(input("enter the value "))
# # # # # # # # # # # count = 0
# # # # # # # # # # # for i in range(1,n+1):
# # # # # # # # # # #     if i%2 != 0:
# # # # # # # # # # #         count=count+i
# # # # # # # # # # # print(count)
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #19)Write a program to count the number of digits in a number using python.
# # # # # # # # # # # #1 2 3 4 5
# # # # # # # # # # # count = 0
# # # # # # # # # # # n =int(input("enter the value"))
# # # # # # # # # # # for i in range(1,n+1):
# # # # # # # # # # #     count= count+i
# # # # # # # # # # # print(count)
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #length of string
# # # # # # # # # # # num= '123456789sddddddsdddddsds////........'
# # # # # # # # # # # print(len(num))
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #20)Write a program to find the first and last digits of a number using python.
# # # # # # # # # # #
# # # # # # # # # # # n = 12345
# # # # # # # # # # # b= str(n)
# # # # # # # # # # # for i in range(len(b)):
# # # # # # # # # # #     if i == 0:
# # # # # # # # # # #         print("first digit",b[i])
# # # # # # # # # # #     elif i == len(b)-1:
# # # # # # # # # # #         print("last digit",b[i])
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # n = 12347
# # # # # # # # # # # b= str(n)
# # # # # # # # # # # c= len(b)
# # # # # # # # # # # for i in range(c):
# # # # # # # # # # #     if i == 0:
# # # # # # # # # # #         print("first digit",b[i])
# # # # # # # # # # #     elif i == c-1:
# # # # # # # # # # #         print("last digit",b[i])
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #21). Write a program to find the sum of the first and last digits of a number using python.
# # # # # # # # # # #
# # # # # # # # # # # n= 123456
# # # # # # # # # # # a = str(n)  doubt
# # # # # # # # # # # b = len(a)
# # # # # # # # # # # total = 0
# # # # # # # # # # # for i in range(b):
# # # # # # # # # # #     if i==0:
# # # # # # # # # # #         total += int(a[i])  doubt
# # # # # # # # # # #     elif i==b-1:
# # # # # # # # # # #         total+=int(a[i])
# # # # # # # # # # #
# # # # # # # # # # # print("sum of first and last digits",total)
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # n= "abcde"
# # # # # # # # # # # a = str(n)
# # # # # # # # # # # b = len(a)
# # # # # # # # # # # total = 0
# # # # # # # # # # # for i in range(b):
# # # # # # # # # # #     if i==0:
# # # # # # # # # # #         total += a[i]
# # # # # # # # # # #     elif i==b-1:
# # # # # # # # # # #         total+= a[i]
# # # # # # # # # # #
# # # # # # # # # # # print("sum of first and last digits",total)
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # #22). Write a program to calculate the sum of digits of a number using  python.
# # # # # # # # # # #
# # # # # # # # # # # n= 12345
# # # # # # # # # # # a= str(n)
# # # # # # # # # # # total =0
# # # # # # # # # # # '''
# # # # # # # # # # # #24). Python loops program to enter a number and print its reverse using python.
# # # # # # # # # # # '''
# # # # # # # # # # # n = 12345
# # # # # # # # # # # a = str(12345)
# # # # # # # # # # # for i in range(len(a),-1,1):
# # # # # # # # # # #     print(a[i])
# # # # # # # # # # #     '''
# # # # # # # # # # # '''
# # # # # # # # # # # *
# # # # # # # # # # # * *
# # # # # # # # # # # * * *
# # # # # # # # # # # * * * *
# # # # # # # # # # # * * * * *
# # # # # # # # # # #
# # # # # # # # # # # * * * * *
# # # # # # # # # # # * * * *
# # # # # # # # # # # * * *
# # # # # # # # # # # * *
# # # # # # # # # # # *
# # # # # # # # # # #
# # # # # # # # # # # """
# # # # # # # # # # #
# # # # # # # # # # # for i in range(1, 6):
# # # # # # # # # # #     for j in range(i):
# # # # # # # # # # #         print(j, end=" ")
# # # # # # # # # # #     print()
# # # # # # # # # # #
# # # # # # # # # # # for i in range(6, 0, -1):
# # # # # # # # # # #     for j in range(i):
# # # # # # # # # # #         print(j, end=" ")
# # # # # # # # # # #     print()
# # # # # # # # # # #
# # # # # # # # # # # 1
# # # # # # # # # # # 2 3
# # # # # # # # # # # 4 5 6
# # # # # # # # # # # 7 8 9 10
# # # # # # # # # # # 11 12 13 14 15
# # # # # # # # # # # 16 17 18 19 20 21
# # # # # # # # # # # 22 23 24 25 26
# # # # # # # # # # # 27 28 29 30
# # # # # # # # # # # 31 32 33
# # # # # # # # # # # 34 35
# # # # # # # # # # # 36
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # """
# # # # # # # # # # # '''
# # # # # # # # # # # '''
# # # # # # # # # # # temp = 1
# # # # # # # # # # # for i in range(1, 6):
# # # # # # # # # # #     for j in range(i):
# # # # # # # # # # #         print(temp, end=" ")
# # # # # # # # # # #         temp += 1
# # # # # # # # # # #     print()
# # # # # # # # # # #
# # # # # # # # # # # for i in range(6, 0, -1):
# # # # # # # # # # #     for j in range(i):
# # # # # # # # # # #         print(temp, end=" ")
# # # # # # # # # # #         temp += 1
# # # # # # # # # # #     print()
# # # # # # # # # # #     '''
# # # # # # # # # # # '''
# # # # # # # # # # # A
# # # # # # # # # # # B C
# # # # # # # # # # # D E F
# # # # # # # # # # # G H I J
# # # # # # # # # # # K L M N O
# # # # # # # # # # # P Q R S T U
# # # # # # # # # # # V W X Y Z
# # # # # # # # # # # [ \ ] ^
# # # # # # # # # # # _ ` a
# # # # # # # # # # # b c
# # # # # # # # # # # d
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # """
# # # # # # # # # # #
# # # # # # # # # # # ascii_value = 65
# # # # # # # # # # # for i in range(1, 6):
# # # # # # # # # # #     for j in range(i):
# # # # # # # # # # #         print(chr(ascii_value), end=" ")
# # # # # # # # # # #         ascii_value += 1
# # # # # # # # # # #     print()
# # # # # # # # # # #
# # # # # # # # # # # for i in range(6, 0, -1):
# # # # # # # # # # #     for j in range(i):
# # # # # # # # # # #         print(chr(ascii_value), end=" ")
# # # # # # # # # # #         ascii_value += 1
# # # # # # # # # # #     print()
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # print(ord("C")) # 67
# # # # # # # # # # # print(ord("c")) # 99
# # # # # # # # # # # '''
# # # # # # # # # # #
# # # # # # # # # # # for i in range(1,5):
# # # # # # # # # # #     for j in range(i):
# # # # # # # # # # #         print(j, end=' ')
# # # # # # # # # # #     print()
# # # # # # # # # # #
# # # # # # # # # # # for i in range(6,0,-1):
# # # # # # # # # # #     for j in range(i):
# # # # # # # # # # #         print(j,end=' ')
# # # # # # # # # # #     print()
# # # # # # # # # # #
# # # # # # # # # # # word=input("enter the value")
# # # # # # # # # # # str1=" "
# # # # # # # # # # # for i in range(len(word)):
# # # # # # # # # # #     str1+=word[i]
# # # # # # # # # # # print(str1)
# # # # # # # # # #
# # # # # # # # # # input1="SqaTOOLS"
# # # # # # # # # # result=" "
# # # # # # # # # # for char in input1:
# # # # # # # # # #     if char.isupper():
# # # # # # # # # #         print(char.lower(),end="")
# # # # # # # # # #     else:
# # # # # # # # # #         print(char,end="")
# # # # # # # # #
# # # # # # # # # word= "python1234"
# # # # # # # # # digit=0
# # # # # # # # # character=0
# # # # # # # # # for i in word:
# # # # # # # # #      if i.isalpha():
# # # # # # # # #          character+=1
# # # # # # # # #      elif i.isnumeric():
# # # # # # # # #          digit+=1
# # # # # # # # # print(digit)
# # # # # # # # # print(character)
# # # # # # # #
# # # # # # # # for row in range(0,7):
# # # # # # # #     for column in range(0,7):
# # # # # # # #         if (row==0 or row==6) and (1<column<5):
# # # # # # # #             print("*",end="")
# # # # # # # #         elif(0<row<=5) and (column==1 or column==5):
# # # # # # # #             print("*",end="")
# # # # # # # #         else:
# # # # # # # #             print(" ",end=" ")
# # # # # # # # #     print()
# # # # # # # #
# # # # # # # # n=int(input("enter the value"))
# # # # # # # # count=n
# # # # # # # # while count!=0:
# # # # # # # #     print(count,end=" ")
# # # # # # # #     count-=1
# # # # # # #
# # # # # # # for i in range(1,101):
# # # # # # #     if i%2==0 :
# # # # # # #         print(i,end=" ")
# # # # # # #
# # # # # #
# # # # # # for i in range(1,101):
# # # # # #     if i%2 !=0:
# # # # # #         print(i,end=" ")
# # # # # n=11
# # # # # sum=0
# # # # # for i in range(1,n+1):
# # # # #     sum=sum+i
# # # # # print(sum)
# # # # #
# # # # #
# # # # num="1234567"
# # # # count=0
# # # # for i in num:
# # # #     count+=1
# # # # print(count)
# # #
# # #
# # # num=2665
# # # str1=str(num)
# # # sum=0
# # # for i in range(len(str1)):
# # #     if i==0:
# # #         sum+=int(str1[i])
# # #     elif i==len(str1)-1:
# # #         sum+=int(str1[i])
# # # print(sum)
# # #
# # # num=int(input("enter the number"))
# # # sum=0
# # # while num>0:
# # #     rem= num%10
# # #     sum=sum+rem
# # #     num=num//10
# # # print(sum)
# # #
# #
# # str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
# # output=[]
# # str2= str1.split(" ")
# # print(str1)
# #
# # for word in str2:
# #     if word.isdigit():
# #         output.append(word)
# # print (output)
# # total= sum(output)
# # print(total)
#
#
# list1 = [13, 56, 77, 23, 29, 11]
# list2=[]
#
# for value in list1:
#     count=0
#     for i in range(2,value):
#         if value%i==0:
#             count+=1
#     if count==0:
#         list2.append(value)
# print(list2)
#
# def my_function():
#   print("Hello from a function")
#
# my_function()

# def my_function(fname):
#     print( fname+" refsnes")
#
# my_function("email")
# my_function("archana")
# my_function("sachin")

# def my_function(fname,lname):
#     print(fname + " "+ lname)
# my_function("archana")

#
# n=121
# rev =0
# while n>0:
#     r= n%10
#     rev= (rev*10)+r
#     n=n//10
# print(rev)
#
# if n == rev:
#     print("palindrome")
# else:
#     print("not palindrome")
# num=n=int(input("Enter a number: "))
# rev = 0
#
# while n>0:
#     r = n%10
#     rev = (rev*10) + r
#     n = n//10
# print("Reverse number: ",rev)
#
# if num == rev:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

# num=12323
# str1= str(num)
# dict1={}
# for val in str1:
#     if val in dict1:
#         dict1[val]+=1
#     else:
#         dict1[val]=1
# print(dict1)

# num= int(input("enter the value"))
# str1=" "
# for i in str(num):
#     if i == '1':
#         str1+="one"
#     elif i==2:
#         str1+="Two"
#     elif i == "3":
#         str1 += "Three"
#     elif i == "4":
#         str1 += "Four"
#     elif i == "5":
#         str1 += "Five"
#     elif i == "6":
#         str1 += "Six"
#     elif i == "7":
#         str1 += "Seven"
#     elif i == "8":
#         str1 += "Eight"
#     elif i == "9":
#         str1 += "Nine"
#
# print(str1)

# num= int(input("enter the value"))
# pw= int(input("enter the value"))
# result= 1
# for n in range(pw):
#     result= result*num
# print(result)

# num= int(input("enter the value"))
# for i in range(1,num+1):
#     if num%i ==0:
#         print(i,end=" ")



# num= int(input("enter the value"))
# result= 1
# for i in range(1,num):
#     if num>0:
#         result= result* num
#         num= num-1
#
# print(result)

# num=int(input("enter the value"))
# count=1
# for i in range(2,num//2):
#     if num%i==0:
#         count+=1
# if count> 1:
#     print("not prime")
# else:
#     print("prime")

# total=0
# for num in range(2,10):
#     count=0
#     for i in range(2,num):
#         if num%i ==0:
#             count+=1
#     if count==0:
#         total= total+num
# print(total, end=" ")

# str1= "Good 12 Morning 45, Hope 2 you are 30 doing good"
# str1= str1.replace(","," ")
# str2= str1.split()
# print(str2)
# print(type(str2))
#
# list1=[]
# sum=0
# for val in str2:
#     if val.isdigit():
#         list1.append(int(val))
#         sum =sum+int(val)
#
# print(list1)
# print(sum)
list1 = [13, 56, 77, 23, 29, 11]
list2=[]

for num in list1:
    count=0
    for i in range(2,num):
        if num % i==0:
            count+=1
    if count==0:
        list2.append(num)
print(list2)