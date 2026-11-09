'''
Replace negative numbers: Given a list containing positive and negative integers, 
create a new list where every negative number is replaced with zero using list comprehension
'''
my_list=[1,2,3,4,5,-6,-7,8,-10,10,-99,-11]
my_list1=[0 if i<0 else i for i in my_list]
print(my_list1)