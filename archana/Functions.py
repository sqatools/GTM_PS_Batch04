# def my_function(fname, lname):
#   print(fname + " " + lname)
#
# my_function("Emil")


# def my_function(*args):
#     print("the youngest child is "+args[2])
# my_function("archana","sachin","shravya")

# def my_function(child3,child2,child1):
#     print("the youngest chils is "+child3)
# my_function(child3= "email",child2 = "password",child1= "linus")

# def my_function(**kid):
#     print("his last name is ", kid['lname'])
# my_function(fname="archana",lname="sachin")

# def my_function(country="India"):
#     print("my country is ",country)
# my_function("sweden")
# my_function()

# def my_function(food):
#     for x in food:
#         print(x)
#
# fruits=['apple','banana','Grapes']
# my_function(fruits)


# def my_function(x):
#     return 5*x
#
# a= my_function(3)
# print(a)

# def my_function(x):
#     print(x)
# a= my_function(x= 3)
# print(a)

# def math_operation(v1,v2,v3):
#     add= v1+v2
#     sub=v1-v2
#     mul=v1* v2
#     return add,sub,mul
# v1,v2,v3= math_operation(20,30,40)
# print(v2)

# def function(*args):
#     for val in args:
#         print(args)
#
# function(4,5)

def getuserdetails(*args,**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,":",value)
getuserdetails(username="rahul",email="archana@gmai.com",phone="9886976894")
