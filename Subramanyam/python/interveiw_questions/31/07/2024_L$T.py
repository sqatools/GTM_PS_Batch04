#Rearrange the order of tuple in the list on basies of sum of tuple in des order
list1 = [(1,6),(2,4),(9,7),(5,3)]
# output=[(9, 7), (5, 3), (1, 6), (2, 4)]
sorted_list = sorted(list1, key=lambda x: sum(x), reverse=True)

print(sorted_list)

#write python program for print 100 natural number without looping
def print_natural_number9(n):
    if n<=0:
        return
    print_natural_number9(n-1)
    print(n,end=" ")

print_natural_number9(100)

# output of given dict
dict= {'a': 1, 'b':2, 'a':5}
print(dict['a'])
#output=5

# write a program for given one
a=[1,2,3]
b=[3,4,5]
c=[6,7,8]
# # Output
# # [(1, 3, 6), (2, 4, 7), (3, 5, 8)]

print(list(zip(a,b,c)))

#output of given given code

list1 = ["alfa", "bravo", "charlie", "delta", "echo"]

print(list1[10:])


# output: []
