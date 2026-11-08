'''
Squares of numbers: Given a list of integers,
create a new list containing the squares of all elements using list comprehension
'''
my_list=[1,2,3,4,10,20,21,99]
my_list1=[i ** 2 for i in my_list]
print(my_list1)