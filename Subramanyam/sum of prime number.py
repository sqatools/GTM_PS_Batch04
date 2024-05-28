num = int(input("Enter a number up to which you want to find sum: "))
total = 0

for i in range(1,num+1):
    if i%2==0:
        continue
    total += i
    print(i,end=" ")



print(i,"Total: ",total)
'''
num = int(input("Enter a number up to which you want to find sum: "))
total = 0

for i in range(1, num + 1):
    if i % 2 != 0:
        continue
    total += i
    print(i, end=" ")

print(i, "Total1: ", total)
'''