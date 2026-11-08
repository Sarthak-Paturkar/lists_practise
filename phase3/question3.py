'''
Divisible by 3 and 5: Generate a 
list of numbers between 1 and 100 that are divisible by both 3 and 5 using list comprehension
'''
my_list = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]

print(my_list)