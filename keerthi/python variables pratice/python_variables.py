#Adding of two numbers
var1=10
var2=20
var=var1+var2
print("adding of two:",(var))
print("addin of two:",id(var))

#subtract of two integers
a=40
b=50
c=b-a
print(c)

#Multiply of two numbers
mul1=10
mul2=20
mul=mul1*mul2
print("multiply of two no's is:",(mul))
print("_"*20)

a=10
b=5
c="keerthi"
print("multiply of two no:",(a*b))
print("multiply string:",c*b)

print("-"*30)
#Multiply the string
str1="HELLOWORLD"
print(str1*5)

print("-"*40)

#Average of given numbers
a=10
b=20
c=30
print("Average:",(a+b+c)/3)
print("Average:",(a+b)/2)

print("_"*40)

#Median of given numbers
list=[20,30,40,90,70,80,10]
list.sort()
a=(len(list))/2
print("median:",list[int(a)])

#square cube of a given number
num1=12
#print(num1*num1)
print("square:", int(num1*num1))

print("_"*50)
#Interchange of number
p=20
q=30
# p=q
#q=p
p,q=q,p
print("interchange:",p)
print("interchange:",q)

#pythogoreous theorem
a=20
b=20
c2=a*2+b*2
print("pythgoreous:",c2)
print("_"*50)
#(a-b)2=a2+b2-2ab
a=60
b=20
LHS=(a-b)**2
print("LHSoutput:", LHS)
RHS=a**2+b**2-2*a*b
print("RHSoutput:",RHS)

#a2 – b2 = (a-b)(a+b)
a=20
b=10
LHS=(int(a**2-b**2))
print("LHS output:", LHS)
RHS=(int((a-b)*(a+b)))
print("RHS output:",RHS)

print("_"*50)
#area of circle
r=6
pi=3.14
area=pi*r*r
print("enter the area:",area)

print("_"*50)
radius = int(input("Enter radius of circle: "))
area = 3.14*radius*radius
print("Area of circle: ",area)

print("_"*50)

r=10
h=20
area=2*3.14*10*20+2*3.14*10
print("Area of cylinder:", area)
