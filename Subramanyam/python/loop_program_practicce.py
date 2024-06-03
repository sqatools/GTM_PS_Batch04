# even number from to 100

for i in range(1,101):
    if i%2==0:
        print(i,end=" ")

print()

###########################
#odd number from 1 to 100

for i in range(1,101):
    if i%2!=0:
        print(i,end=" ")

print()

############################
# prime number from 1 to 100

for i in range(2,101):
    prime = True
    for j in range(2,i):

        if i%j==0:
            prime=False
            break
        else:
            continue
    if prime:
        print(i, end=" ")
    else:
        pass

print()


#####################################
count =0
while count<=100:
    print(count,end=" ")
    count+=1
print()
n=100
t1=0
for i in range(1,n+1):
    t1+=i
    print(i,end=" ")
print()
print(t1)
###########################################

num =50
total=0
for i in range(1,num+1):
    print(i,end=" ")
    total+=i
print()
print(total)

#############################################
'''num=int(input("Enter the number: "))
T1=0
for i in range(1,num+1):
    if i%2==0:
        T1+=i
print(T1)

num1=int(input("Enter the number: "))
T2=0
for i in range(1,num1+1):
    if i%2!=0:
        T2+=i
print(T2)
'''
###############################################

num="9966466046"
count=0
for i in num:
    count+=1
print(count)

num="python1234"
di=0
cha=0
for i in num:
    if i.isalpha():
        cha+=1

    elif i.isnumeric():
        di+=1

print(di)
print(cha)

#############################
num2=1225630
str1=str(num2)
for i in range(len(str1)):
    if i==1:
        print("First number of given number is: ",str1[i])
    elif i== len(str1)-2:
        print("last number of given number is: ", str1[i])


num3=2775
str2=str(num3)
total=0
for i in range(len(str2)):
    if i==0:
        total+=int(str2[i])
    elif i==len(str2)-1:
        total+=int(str2[i])
print("Total of: ",total)

#########################################################

num =12345
count=0

while num>0:
    rem = num%10
    count+=rem
    num= num // 10

print(f"the sum of: ",count)

#####################################################

nu=56
pu=1

while nu>0:
    rem = nu%10
    pu=pu*rem
    nu = nu//10

print(pu)
#################################################

num=9966466046
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("Reverse of give number is : ",rev)

#######################################################
'''num=n=int(input("Enter the number: "))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if num==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
   '''

'''num=n=int(input("Data"))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)

if num==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
'''
##########################################################################

moblie=9966466046
str1=str(moblie)
dict1={}
for val in str1:
    if val in dict1:
        dict1[val]+=1
    else:
        dict1[val]=1
print(dict1)




def digit_frequency(number):
    # Initialize a dictionary to store digit frequencies
    freq = {str(i): 0 for i in range(10)}

    # Convert number to string for easy iteration
    number_str = str(number)

    # Count the frequency of each digit
    for digit in number_str:
        freq[digit] += 1

    return freq

# Test the function
number = 1234567890
print(digit_frequency(number))




################################################################

u=int(input("Enter the number: "))
str1=" "
for i in str(u):
    if i=="1":
        str1+="one"
    elif i=="2":
        str1+="two"
    elif i=="3":
        str1+="three"
    elif i=="4":
        str1+="four"
    elif i=="5":
        str1+="five"
    elif i=="6":
        str1+="six"
    elif i=="7":
        str1+="seven"

print(str1)
#########################################################
num=9
pw=2
result=1

for n in range(pw):
    result=result*num

print(result)

###############################################################
num =int(input("Enter the number: "))

for i in range(1,num+1):
    if num%i ==0:
        print(i,end=" ")