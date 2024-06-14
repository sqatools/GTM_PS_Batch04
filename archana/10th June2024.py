#sort,sorted,reverse,reversed
list1=[3,6,8,12]
list1[1]= 600
print(list1)

print('-'*50)

list2=[3,6,8]
print(list2.index(8))

print('-'*50)
list3=[4,6,2,7,2,7,2,2]
print(list3.count(2))

list4=[4,8,2,1,7]
list4.sort()
print(list4)

list5= [3,4,2,1,75]
list5.sort(reverse=True)
print(list5)

list6=[3,2,5,6,4]
result= sorted(list6)
print(result)

list7=[4,7,3,2,6]
result= sorted(list7,reverse=True)
print(result)

#Reverse a string
list8=[4,6,1,7,1,5,22]
list8.reverse()
print(list8)

list9=[3,2,4,5,72,1,2]
result= list(reversed(list9))
print(result)

#copy
list_a= [1,2,3,4]
list_b= list_a
list_b.append(100)
list_b.insert(2,500)
print(list_a)
print(list_b)

list_p=[ 3,5,2,11]
list_q= list_p.copy()
list_q.append(100)
list_q.insert(2,345)
print(list_p)
print(list_q)


list_m= [3,6,8,33]
print(max(list_m))
print(min(list_m))
print(sum(list_m))

list_c = [3,45,33,11]       #doubt
result2 = [val for val in list_c if val%2==0]
print("all even numbers",result2)

list_z= [4,56,2,2]
result1= [(val,"even") if val%2==0 else (val,"odd") for val in list_z]
print(result1)

output= []
list_a= [4,6,8,3,7,11,14]
for i in list_a:
    if i%2==0:
        print("square of even:", i**2)
    elif i%2!=0:
        print("cube of odd", i**3)
print(output.append(i))   # doubt