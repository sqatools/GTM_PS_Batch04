# 106). Write a program to get a list of all the mobile numbers from the given string using  python.
# Input str = “”” We have 2233 some employee 8988858683 whos 3455 mobile numbers are randomly distributed 2312245566 we want 453452 to get 4532892234 all the mobile numbers 9999234355  from this given string.”””
# Output = [‘8988858683’, ‘2312245566’, ‘4532892234’, ‘9999234355’]
#
# str1 = """"We have 2233 some employee 8988858683 whos 3455 mobile numbers
#         are randomly distributed 2312245566 we want 453452 to get 4532892234
#         all the mobile numbers 9999234355  from this given string"""
#
# str = str1.split(" ")
# str_new = [ ]
#
# for val in str:
#     if len(val) == 10 and val.isnumeric():
#         str_new.append(val)
# print(str_new)
# ----------------------------------------------------------------------------------------------
#
# 105). Write a program to get all the email id’s from given string using python.
# Input str = “”” We have some employee whos john@gmail.com email id’s are randomly distributed jay@lic.com we want to get hari@facebook.com all the email mery@hotmail.com id’s from this given string.”””
# Output = [‘john@gmail.com’, ‘ jay@lic.com’, ‘hari@facebook.com’, ‘mery@hotmail.com’ ]

# str1 = """We have some employee whos john@gmail.com email id’s are
#         randomly distributed jay@lic.com we want to get hari@facebook.com
#         all the email mery@hotmail.com id’s from this given string"""
#
# str_a = str1.split(" ")
# new_str = [ ]
# for word in str_a:
#     for char in word:
#         if char == "@":
#             new_str.append(word)
# print(new_str)

