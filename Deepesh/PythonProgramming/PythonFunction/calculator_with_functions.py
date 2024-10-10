def addition(v1, v2):
    return v1 + v2


def multiply(v1, v2):
    return v1 * v2


def subtraction(v1, v2):
    return v1 - v2


def divide(v1, v2):
    return v1 / v2


def calculator():
    print("1. addition\n"
          "2. multiply \n"
          "3. subtraction \n"
          "4. divide \n"
          "5. Exit")

    option = int(input("Enter your option :"))
    if option != 5:
        var1 = int(input("Please enter first value :"))
        var2 = int(input("Please enter second value :"))
    if option == 1:
        print("addition :", addition(var1, var2))
    elif option == 2:
        print("Multiplication : ", multiply(var1, var2))
    elif option == 3:
        print("subtraction : ", subtraction(var1, var2))
    elif option == 4:
        print("subtraction : ", divide(var1, var2))
    elif option == 5:
        exit()


while True:
    calculator()
