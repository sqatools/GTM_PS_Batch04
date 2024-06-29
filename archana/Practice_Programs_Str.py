#Q : Write a python program to find out the max and min length word

str1 = "Hello Good Morning How are you"

word_list = str1.split(" ")
max_len_word = ''
max_len = 0
min_len_word = word_list[0]
min_len = len(word_list[0])

for word in word_list:
    word_len = len(word)

    if word_len > max_len:
        max_len = word_len
        max_len_word = word

    if word_len < min_len:
        min_len = word_len
        min_len_word = word

print("Max length word :", max_len_word)
print("Min length word :", min_len_word)