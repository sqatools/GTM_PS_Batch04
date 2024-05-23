vowel=['a' , 'e','i','o' ,'u']
string =str(input("enter a string"))
count=0
for char in string :
    if char  in vowel :
       count +=1
print (count)
