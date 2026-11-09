'''
Filter names:
Given a list of names, create a new list containing only names having more than 5 characters.
'''
my_list=["sarthak","mohan","rohan","sam","jay","kalpesh","goat"]
my_list1=[i for i in my_list if len(i)>5 ]
print(my_list1)