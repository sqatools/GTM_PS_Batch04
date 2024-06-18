v1= 'python'
v2='programming'
v3 = v1+ " " +v2
print(v3)

print("-"*50)

name= 'archana'
age= 33
city='bellary'
#result= "my name is "+name+" and age is "+str(age)+" and i live in "+city

#result= "my name is {} and age is {} and i live in {}".format(name,age,city)

result= f"my name is {name} and age is {age} and i live in {city}"
print(result)

str1="Its Online Learning"
last_char= str1[-1]
first_char= str1[0]
remaining_char= str1[1:-1]
result= f"{last_char}{remaining_char}{first_char}"
print(result)

output2= f"{first_char*3}{remaining_char}{last_char*3}"
print(output2)

str_a="Hello"
print("uppercase:", str_a.upper())

str_b="HelLo"
print("swapcase:",str_b.swapcase())

str_c="Python hello program"
print("titlecase:",str_c.title())

str_d="Python case"
print(str_d.istitle())

str_f="heeeeeeeeeeeelo"
print("count is:", str_f.count("e"))

str ="pythhon"
temp=" "
for char in str:
    if char not in temp:
        print("char:",str.count(char))
        temp= temp+char
    else:
        continue
print("temp")


str_y="hello,we are learning python"
output= str_y.replace("python","java").replace("are","were")
print(output)

output1= str_y.split(",")
print(output1)



