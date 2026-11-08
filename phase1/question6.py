##Even and odd separation: Given a list of integers,
#create two separate lists: one containing even numbers and another containing odd numbers.
my_list=[1,2,3,4,5,6,7,8,9,10]
my_list_even=[]
my_list_odd=[]
for i in my_list:
    if i % 2 == 0:
        my_list_even.append(i)
    else:
        my_list_odd.append(i)
print(my_list_even)
print(my_list_odd)