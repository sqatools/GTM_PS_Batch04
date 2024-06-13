"""
  *  *  *
* *  *  * *
______________________
* *     * *
* *     * *
* *     * *
* *     * *
_____________________
* *  *  * *
  *  *  *
"""

for i in range(2):# i = 0, i = 1
    for j in range(5):  # j = 0, 1, 2, 3, 4
        if i == 0:
            if j == 0 or j == 4:
                print(" ", end="  ")
            else:
                print("*", end="  ")
        else:
            print("*", end="  ")
    print()


for i in range(4):# i = 0, i = 1
    for j in range(5):  # j = 0, 1, 2, 3, 4
        if j == 2:
            print(" ", end="  ")
        else:
            print("*", end="  ")
    print()


for i in range(2):# i = 0, i = 1
    for j in range(5):  # j = 0, 1, 2, 3, 4
        if i == 1:
            if j == 0 or j == 4:
                print(" ", end="  ")
            else:
                print("*", end="  ")
        else:
            print("*", end="  ")
    print()
