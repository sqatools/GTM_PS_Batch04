list_1 = [4, 6, 8, 3, 7, 11, 14]
output = []

for val in list_1:
    if val % 2 == 0:
        output.append(val ** 2)
    else:
        output.append(val ** 3)
print(output)


str1="Good 12 Morning 45 , Hope 2 you are 30 doing good"
print("Good 12 Morning 45 , Hope 2 you are 30 doing good")
sum=0
x=str1.split()
print(x)
for i in x:
   if x.isnumeric():
       sum+=int(i)
       print(sum)