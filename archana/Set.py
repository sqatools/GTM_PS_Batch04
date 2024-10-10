set_1= {4,6,8,9}
set_2= {'a','b','c','d'}
set_3= set_1.union(set_2)
print(set_3)


set_a={33,2,7,8,12,55,88}
set_b={33,2,14,18,22,15,88}
diff_value=set_a.difference(set_b)
print(diff_value)


set_c={33,2,7,8,12,55,88}
set_d={33,2,14,18,22,15,88}
set_c.difference_update(set_d)
print(set_c)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)

a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}

b.difference(a, c)

print(b)

set_e= {33,2,7,8,12,55}
set_f= {33,2,14,18,12,55}
output= set_e.intersection(set_f)
print(output)
print(set_e)

set_e.intersection_update(set_f)
print(set_e)


set1={33,2,7,8,12,55,88}
set2={33,2,14,18,22,15,88}
result= set1.symmetric_difference(set2)
print(result)
print(set1)
