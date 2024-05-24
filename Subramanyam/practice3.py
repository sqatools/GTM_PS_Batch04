# Python program to check for the anagram. print the iteration
word = input("Enter the words :")
combination = 0
character = len(word)

while character>0:
    combination+=character
    print(combination)
    character -=1

print("Total combination without repetaation: ",combination)
#  Python program to generate random numbers. sum of random value ---0.00###
import random
sum_val = 0
for i in range(5):
    val = random.random()
    print(val)
    sum_val += val

print("sum value  :", sum_val)

#  Python program to generate random numbers. sum of random value ---10,12,14 ###

import random
sum_val = 0
for i in range(5):
    val = random.randint(30, 50)
    print(val)
    sum_val += val

print("sum value  :", sum_val)