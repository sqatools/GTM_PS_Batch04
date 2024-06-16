#Write a python to repeat vowels 3 times and consonants 2 times.
str1='sql tool'

vowel='a','e','i','o','u'

result=" "
for char in str1:
    if char in vowel:
        result=result+char*3
    else:
        result=result+char*2
print(result)

