##Create and display a list:
##Take 5 integers from the user, store them in a list, and display the complete list.
'''my_list=[]
for i in range(5):
    a=int(input("Enter digit: "))
    my_list.append(a)
print(my_list)'''

a=input("Enter numbers: ")
my_list=[]
b=a.split(",")
for i in b:
    my_list.append(int(i))
print(my_list)