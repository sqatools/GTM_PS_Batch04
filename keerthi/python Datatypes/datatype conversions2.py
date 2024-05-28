str1  = "44.45"
result = float(str1)
print(result, type(float))


import json
str6='{"name":"kaashu", "class":"4th", "school":"st.Anns", "Place":"Hyderabad"}'
dict3 = json.loads(str6)
print(dict3, dict3["name"])