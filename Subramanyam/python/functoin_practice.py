# def addition():
#     num1=39
#     num2=69
#     num3=num1+num2
#     print("Addition :",num3)
#
# addition()
#
# def addition_values(numa=69,numb=70):
#     numc=numa+numb
#     print("Additiona",numc)
# addition_values()
#
# x=109
# y=901
# addition_values(x,y)
#
#
# a=int(input("Enter the number"))
# b=int(input("Enter the number"))
#
# addition_values(a,b)
#
# def addition1():
#     num_a=int(input("Enter the number"))
#     num_b= int(input("Enter the number"))
#
#     num_c=num_a+num_b
#
#     print(num_c)
#
# addition1()

a1=10
b1=20
# c1=a1
# a1=b1
# b1=c1

a1,b1=b1,a1
print(a1)
print(b1)


str1 = "India is best cricket teams"
#utput = {5: "IndiA", 2: "IS", 4: "BesT", 7:"CrickeT", 5: "TeamS"}
str2=str1.split()
print(str2)
output = {}
for char in str2:
    output[len(char)] = char[0].upper()+char[1:-1]+char[-1].upper()
print(output)

list1 = [13, 56, 77, 23, 29, 11]
list2=[]
for num in list1:
    count=0
    for i in range(1,num):
        if num%i==0:
            count+=1
    if count==1:
        list2.append(num)
print(list2)

a1,b1=b1,a1