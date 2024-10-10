# ####Fibonacci series#########
# n1=0
# n2=1
# count=0
# print("fibonacci series: ",end="")
# while count<10:
#     print(n1,end=" ")
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     count+=1
#
# print()
# ##################prime numbers####################
# for i in range(2,200):
#     prime=True
#     for j in range(2,i):
#         if i%j ==0:
#             prime=False
#             break
#         else:
#             continue
#     if prime:
#         print(i,end=' ')
#     else:
#         pass
# print()
# ########################palinodrome####################
#
# num=n=151
# rev=0
# while n>0:
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
#
# if num==rev:
#     print("given number is palinodrome")
# else:
#     print("not a palinodrome")
#
# ########################Armstrong###################
# num=n=151
# rv=0
# while n>0:
#     rem=n%10
#     rv=rv+rem**3
#     n=n//10
#
# if num==rv:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
#
# ############# factorial#######################
# # num=n=int(input("Enter the number: "))
# # fact=1
# # while n>0:
# #     fact*=n
# #     n-=1
# # print(f'The factorial of {num} is {fact}')
#
#
# ############sum of number###################
# # num=int(input("Enter the number"))
# # total=0
# #
# # for i in range(1,num):
# #     total+=i
# #     if i%2==0:
# #         continue
# #     print(i,end=" ")
# # print("Total: ",total)
#
# num=int(input("number"))
# total=0
# for i in range(1,num+1):
#     count=0
#     for j in range(2,i):
#         if i%j ==0:
#             count+=1
#
#     if count==2:
#         total+=i
# print("sum:",total)
#
