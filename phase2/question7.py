'''
Find the index: Given a list of numbers and a number entered by the user, find
the index of its first occurrence using index(). Handle the case when the element does not exist
'''
my_list = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 1, 3]

a = int(input("Give a number: "))

if a in my_list:
    print("Index:", my_list.index(a))
else:
    print("Element not in the list")