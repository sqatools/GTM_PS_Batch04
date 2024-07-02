def addition(var1,var2):
    return var1 + var2

def subtraction(var1,var2):
    return var1 - var2

def multiply(var1,var2):
    return var1 * var2

def division(var1, var2):
    return var1/var2

def calculator():
    print('1.addition:\n'
          '2.subtraction:\n'
          '3.multiply:\n'
          '4.division:\n'
          '5.Exit'
          )
    option=int(input('Enter your choice:'))
    if option!=5:
        var1 = int(input('enter variable1:'))
        var2 = int(input('enter variable2:'))
    if option==1 :
        print('addition:',addition(var1,var2))
    elif option==2:
        print('subtraction:',subtraction(var1,var2))
    elif option==3:
        print('multiply:',multiply(var1,var2))
    elif option==4:
        print('division:',division(var1,var2))

calculator()
