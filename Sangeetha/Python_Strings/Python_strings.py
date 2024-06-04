# string formating
name ="sangeetha"
age = "26"
city = "chennai"

# my name is sangeetha and age is 26 and i live in chennai
result = "My name is "+name+" and age is "+str(age)+" and I live in "+city
print(result)

result1 ="my name is {} and age is {} and i live in {}".format (name,age,city)
print(result1)

city_list = {'chennai','kakinada','hyderabad'}
result2 = f"my name is {name} and age is {age} and i live in {city_list}"
print(result2)

#String Slicilng

str1= "Python Programming"
result = str1[0:6]
print("result:", result)

result1 =str1[1:5]
print("result:",result1)

output1= str1[0:-1]
print("output1:",output1)

output2=str1[-5:-1]
print("output2:",output2)


