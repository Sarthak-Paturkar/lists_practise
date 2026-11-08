##Positive and negative numbers: Take 10 integers from the user and
#create two separate lists containing positive and negative numbers. Ignore zero.
my_list=[]
list_positive=[]
list_negative=[]
for i in range(10):
    a=int(input("Enter a digit: "))
    if a>0:
        list_positive.append(a)
    elif a<0:
        list_negative.append(a)
    else:
        pass
print(list_positive)
print(list_negative)