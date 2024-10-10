# # def addition():
# #     num1=39
# #     num2=69
# #     num3=num1+num2
# #     print("Addition :",num3)
# #
# # addition()
# #
# # def addition_values(numa=69,numb=70):
# #     numc=numa+numb
# #     print("Additiona",numc)
# # addition_values()
# #
# # x=109
# # y=901
# # addition_values(x,y)
# #
# #
# # a=int(input("Enter the number"))
# # b=int(input("Enter the number"))
# #
# # addition_values(a,b)
# #
# # def addition1():
# #     num_a=int(input("Enter the number"))
# #     num_b= int(input("Enter the number"))
# #
# #     num_c=num_a+num_b
# #
# #     print(num_c)
# #
# # addition1()
#
# a1=10
# b1=20
# # c1=a1
# # a1=b1
# # b1=c1
#
# a1,b1=b1,a1
# print(a1)
# print(b1)
#
#
# str1 = "India is best cricket teams"
# #utput = {5: "IndiA", 2: "IS", 4: "BesT", 7:"CrickeT", 5: "TeamS"}
# str2=str1.split()
# print(str2)
# output = {}
# for char in str2:
#     output[len(char)] = char[0].upper()+char[1:-1]+char[-1].upper()
# print(output)
#
# list1 = [13, 56, 77, 23, 29, 11]
# list2=[]
# for num in list1:
#     count=0
#     for i in range(1,num):
#         if num%i==0:
#             count+=1
#     if count==1:
#         list2.append(num)
# print(list2)
#
# a1,b1=b1,a1
#
# # def addition_2(var1=int(input("number")),var2=int(input("number"))):
# #     print("Sum of var3: ",var1+var2)
# # #addition_2()
# # addition_2(50,70)
#
# def multiply_v(v1,v2,v3):
#     add=v1+v3
#     multi=add*v2
#     return add,multi
#
# output= multiply_v(2,3,4 )
# print(output[0])
#
# def function_a():
#     val1=20
#     val2=40
#     val3=val1+val2
#     print(val3)
#
# function_a()

# def string_f(str1=input("data: ")):
#     list1=str1.split(" ")
#     for word in list1:
#         output=word[-1].upper()+word[1:-1]+word[0].upper()
#         return output
#
# out=string_f()
# print("out",out)
# def string_r():
#     output1=string_f()
#     print("output", output1[-1].lower()+output1[1:-1].upper()+output1[0].lower())
#     print(output1.swapcase())
#     #print("output",f"{output1[-1]}{output1[1:-1]}{output1[0]}")
#
# string_r()

def function_c(a,b,c,d,e):
    print(a*b*c*d*e)
function_c(2,3,5,6,4,)

function_c(1,2,3,4,5,)

def args_f(*args):
    print("args: ",sum(args))
    print()

args_f(2,2,3,6,6,8)

def subbu_m(*args):
    count=1
    for num in args:
        count=count-num
    print(count)

subbu_m(5,2,3,2,4)

def user_details(**kwargs):
    print(kwargs)
    for key,val in kwargs.items():
        print(key,":",val)
user_details(username='Rahul', email='rahul@gmail.com', phone=534543543, address="Mumbai")


def get_user_details(*args,**kwargs):
    print("kwargs",kwargs)
    for key,val in kwargs.items():
        print(key, ":", val)

    print(args)
get_user_details(5, 6, 22, 77, 12, name="Chetan", lastname="karu", phone=3543534534, email='chetan@gmail.com')
get_user_details(2,5,6,9,8)

def add(k1,k2):
    return k1+k2
output=add(5,6)
print(output)

def multipication(v1,v2,v3):
    add=v1+v2
    return add*v3
output1=multipication(1,2,3)
print(output1)
def divied(n1,n2):
    return n1//n2
result=divied(10,2)
print(result)