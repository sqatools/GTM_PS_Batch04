#Python program to get a string made of the first and
# the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.

Str_1 = "Programming"

Str_2 = Str_1[:2]
Str_3 = Str_1[-2:]

if len(Str_1)<2:
    print(True)
else:
    print(Str_2 + Str_3);

print("-"*50)