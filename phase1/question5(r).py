##Insert an element: Create a list of 5 names. 
#Ask the user for a name and an index,
#then insert the name at the specified position using insert()
my_list = ["Amit", "Rahul", "Sneha", "Priya", "Karan"]

name = input("Enter a name: ")
index = int(input("Enter an index: "))
my_list.insert(index,name)
print(my_list)