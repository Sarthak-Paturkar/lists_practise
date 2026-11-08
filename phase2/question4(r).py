## Remove all occurrences:
# Given a list, remove all occurrences of a particular number without using list comprehension
my_list = [10, 20, 20, 30, 40]
while 20 in my_list:
    my_list.remove(20)
print(my_list)