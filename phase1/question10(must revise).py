##Second-largest element:
#Find the second-largest unique element in a list without using sort(), max(), or min()
my_list = [10, 20, 30, 40, 40, 50, 50, 60]

largest = my_list[0]
second_largest = None

for i in my_list:
    if i > largest:
        second_largest = largest
        largest = i

    elif i < largest:
        if second_largest is None or i > second_largest:
            second_largest = i

if second_largest is not None:
    print("Second largest:", second_largest)
else:
    print("Second largest element does not exist.")