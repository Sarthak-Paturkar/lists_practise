'''
Even numbers: Given a list of integers, 
create a new list containing only even numbers using list comprehension.
'''
my_list=[1,2,3,4,5,6,7,8,9,9,10,1,11,12,222,223,442,556]
my_list1=[i for i in my_list if i % 2 == 0]
print(my_list1)