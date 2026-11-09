'''
Extract vowels: Given a string, create a list containing only its vowels using list comprehension
'''
a=input("Enter a string : ")
my_list=[i for i in a if i in "aeiou"]
print(my_list)