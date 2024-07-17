from PythonOOPS_11_July_24 import Car

print("_"*50)
obj = Car(car_name='XUV700', car_price="32 Lac", car_comp="Mahindra")
obj.show_car_details()

print(obj.__module__)  # PythonOOPS_11_July_24

"""
each file default module name is __main__, but we access the file in some other
file then module name will be become filename that we imported.

"""
