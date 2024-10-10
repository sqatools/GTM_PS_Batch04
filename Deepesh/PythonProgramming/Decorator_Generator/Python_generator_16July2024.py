"""
Generator : Generator help to handle large amount of data, to avoid crash in the code
            generator load one value at a time in the memory to handle the data efficiently.


"""

def greeting():
    return "Good Morning"
    #return "Good evening"


var1 = greeting()
print(var1)


def greeting_gen():
    yield "Good Morning"
    yield "Good Evening"
    yield "How you are ?"
    yield "Learning Python"

# data = greeting_gen()
# print(data)
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))  # StopIteration


data = greeting_gen()
for val in data:
    print(val)


def handle_list_data(list1):
    for val in list1:
        yield val**2

list_a = [4, 6, 7]*1000
square_output = handle_list_data(list_a)
print(square_output)

for val in square_output:
    print(val, end=" ")
