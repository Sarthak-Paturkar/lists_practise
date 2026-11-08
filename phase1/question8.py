##Reverse indexing: Given a
#list, display its elements in reverse order using negative indexing. 
#Do not use reverse() or slicing
my_list=[10,20,30]
for i in range(1,len(my_list)+1):
    print(my_list[-i])