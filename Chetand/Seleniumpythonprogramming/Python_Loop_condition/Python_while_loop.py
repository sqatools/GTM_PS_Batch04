# While Loop

num1 = 1

while num1 <= 20:
    print(num1)
    num1 += 1

    print("*"*50)

# Program to check if a number is prime or not

num = 29

# To take input from the user
# num = int(input("Enter a number: "))

# define a flag variable
prime = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            prime = True
            # break out of loop
            break

    # check if flag is True
    if prime:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

