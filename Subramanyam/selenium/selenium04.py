# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://automationbysqatools.blogspot.com/p/home.html")
# driver.find_element(By.LINK_TEXT,"Dummy Website").click()
# driver.find_element(By.XPATH,"//a[text()='Python Selenium']").click()
# print(driver.title)
# print(driver.current_url)
# driver.find_element(By.XPATH,"//a[text()='Code Practice']//preceding::a[text()='Home']").click()
# driver.find_element(By.XPATH,"//div[text()=' Dummy Website ']").click()
# element_lst=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
#
# for element in range(len(element_lst)):
#     #print("Element is selected1: ",element.is_selected())
#     element_box=element_lst[element]
#     element_box.click()
#     #print("Element is selected2: ", element.is_selected())
#     city_name=driver.find_element(By.XPATH,f"//table[@id='cities']/tbody//tr[{element+2}]//td[3]")
#     print(city_name.text)
# time.sleep(10)
# driver.close()



# List = [(1,6),(2,4),(9,7),(5,3)]
# list1=[]
#
# # Requirement:: [(9,7),(5,3),(1,6),(2,4)]
# order_map = {tuple_item: index for index, tuple_item in enumerate(list1)}
#
# # Sort the original list based on the indices from the order_map
# reordered_list = sorted(List, key=lambda x: order_map[x])
#
# print(reordered_list)

# Original list
# original_list = [(1,6),(2,4),(9,7),(5,3)]
#
# # Desired order
# desired_order = [(9,7),(5,3),(1,6),(2,4)]
#
# # Create the reordered list based on desired order
# reordered_list = [item for item in desired_order if item in original_list]
#
# print(reordered_list)

# Original list
list1 = [(1,6),(2,4),(9,7),(5,3)]

# Sort the list based on the sum of each tuple, in descending order
sorted_list = sorted(list1, key=lambda x: sum(x), reverse=True)

print(sorted_list)
