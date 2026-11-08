'''
Sort a list: Take 10 integers from the user and sort them
in ascending order and descending order using sort()
'''
my_list=[]
for i in range(10):
    a=int(input("Enter a number: "))
    my_list.append(a)
print(my_list)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)