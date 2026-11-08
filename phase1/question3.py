##Find the largest and smallest: 
##Given a list of integers, find the maximum and minimum elements without using max() or min()
my_list=[10,2,34,56,-1,8,90,10,23]
max_num = my_list[0]
min_num = my_list[0]
for i in my_list:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i
print("maximum number: ",max_num)
print("minimum number: ",min_num)
