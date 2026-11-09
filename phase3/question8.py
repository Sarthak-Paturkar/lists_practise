'''
Nested list comprehension: Given a 3 x 3 matrix 
(nested list), create a flattened list containing all its elements using list comprehension
'''
my_list=[[1,2,3],[23,23,34],[4,5,6]]
my_list1=[j for i in my_list for j in i]
print(my_list1)