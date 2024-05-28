"""
# range function accept three parameter start_value and end_value and dofference.
then output for loop will always exclude the last_value

for i in range(start_value, end_value, difference)
    print(i)

"""

for i in range(1, 11, 2):
    print(i)

# range with two parameter, the default different value will be 1
print("_"*50)

for j in range(2, 20):
    print(j)

# range with one parameter, then the default initial value will be zero and difference is One
print("_"*50)
for k in range(5):
    print(k, end=" ")

print()
print("Hello world")
print("Python")


##### Print reverse numbers ###

for i in range(10, 0, -1):
    print(i)


########## print table of any given number ####
print("_"*50)
n = 6

for i in range(1, 11):
    print(n, "*", i, ":",i*n)


###### get all the even numbers from 1 to 20 ####
print("_"*50)

for j in range(1, 20):
    if j%2 ==0:
        print(j)
