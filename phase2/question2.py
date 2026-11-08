'''
Append vs Extend: Create an empty list. Append [10, 20, 30] using append(),
then create another empty list and add 
the same elements using extend(). Display and explain the difference between both outputs.
'''
my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)
my_list1=[]
my_list1.extend([10,20,30])
print(my_list1)