##Calculate the average:Take n numbers from the user,
#store them in a list, and calculate their average using sum() and len()
my_list=[]
n=int(input("enter any valu of n:"))
for i in range(n):
    my_list.append(i)
print(my_list)
print("Total sum: ",sum(my_list))
print("Avg:",sum(my_list)/2)
print("lenght: ",len(my_list))