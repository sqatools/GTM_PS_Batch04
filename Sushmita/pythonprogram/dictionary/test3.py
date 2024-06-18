#Write a Python Program to find out prime number from give list of values
#list1 = [13, 56, 77, 23, 29, 11]
#output = [13, 23, 29, 11]

list1 = [13, 56, 77, 23, 29, 11]
prime=[]
for i in list1:
     count=0
     for j in range (1,i):
        if i%j==0:
             count+=1
     if count==1:
          prime.append(i)

print(prime)
