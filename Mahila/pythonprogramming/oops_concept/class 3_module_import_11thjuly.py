from class_3_notes_11thjuly import car

obj = car(car_name = "XUV700",car_price = "32Lac", car_comp ="mahindra")
obj.show_car_name()
obj.show_car_price()
obj.show_car_company()

print(obj.__module__)   # module name changed from main to class_3_notes_11thjuly

"""
car name is : XUV700
car price is : 32Lac
car compnay : mahindra
class_3_notes_11thjuly

each file default module name is __main__ but if we access the file in someother file then the 
module name will become filename that we imported.
"""
#so when we import from other file and the otherfile also have the obj called, both will execute at parallely,
#so to print only the obj values in imported file alone then we need to giive the if condition in the file
#from which we are copying. see the class_3_notes_11thjuly.py file

"""
if  __name__ == '__main__':
     obj = car(car_name = "XUV300",car_price = "20Lac", car_comp ="mahindra")
     obj.show_car_name()
     obj.show_car_price()
     obj.show_car_company()
     print(obj.__module__)
     

"""