"""
Lambda function : Lambda function is anonymous function without any body, left side user has to pass parameter,
                right side will do the code execution.

"""
add=lambda x,y :x+y
print('addition :',add(40,50))

check_even_odd=lambda x :x%2==0
print(check_even_odd(31))
print(check_even_odd(20))

#Map, Filter and Reduce
# map : map function help to mapping of any specific function with list of values

def square(n):
    return n**2

list1=[4,6,8,2,12]

result=list(map(square,list1))
print(result)

result1=list(map(lambda x: x**2 ,list1))
print(result1)

list2 = ['Hello', 'Python', 'Program']
result2=list(map(lambda x:x*2 ,list2))
print(result2)

dict1 = {'a': 123, 'b' : 345, 'c' : 789}
result3=list(map(lambda x : x*2,dict1))
print(result3)

# Filter : Filter function return the output on our favour.
print("_"*50)
list_a = [5, 8, 2, 18, 12, 4, 13, 15, 7]
result5 = list(filter(lambda x:x%2 == 0, list_a))
print("result 5:", result5)

print("_"*50)
# reduce : reduce function return the combine the result from give list of values

from functools import reduce

list_6 = [4, 7, 1, 5, 23, 35, 11]

# addition of values
result_6 = reduce(lambda x,y:x+y, list_6)
print("result 6:", result_6)

# multiplication of values
list_7 = [1, 2, 3, 4]
result_7 = reduce(lambda x,y:x*y, list_7)
print("result 7:", result_7)


