def string_f(str1=input("data: ")):
    list1=str1.split(" ")
    for word in list1:
        output=word[-1].upper()+word[1:-1]+word[0].upper()
        return output

out=string_f()
print("out",out)
def string_r():
    output1=string_f()
    print("output", output1[-1].lower()+output1[1:-1].upper()+output1[0].lower())
    #print("output",f"{output1[-1]}{output1[1:-1]}{output1[0]}")

string_r()

"""
data: pyhton programming
out NyhtoP
output pYHTOn
"""