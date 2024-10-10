# 88)Write a program to find the maximum number from the list using  Python Loops
# Input : [12,14,45,88,63,97,88]
# Output : Maximum number: 97
#
# var = [12,14,45,88,63,97,88]
# max = 0
#
# for val in var:
#     if val > max:
#         max = val
# print("maximum number :", max)

#---------------------------------------------------------------------------------

# 87). Write a program to add elements from one list to another list and print It in descending order using Python Loops.
# Input :
# A=[2,5,8,0,1,4], B=[]
# Output = [8,5,4,2,1,0]

# l1 = [2,5,8,0,1,4]
# l2 = []
#
# for val in l1:
#     l2.append(val)
#     output = sorted(l2,reverse = True)
# print(output)


def try_except_else_condition(num1, num2):
    try:
        c = num1 + num2
        print("adddition :", c)
    except Exception as e:
        print(e)
        print("Both the variable should have int value")
    else:
        multiplication = num1 * num2
        print(" multiply :", multiplication)


try_except_else_condition(50, "Hello")
#
try_except_else_condition(5, 6)

