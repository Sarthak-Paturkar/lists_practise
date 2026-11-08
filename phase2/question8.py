##Count occurrences: Given a list of integers, 
#find how many times each unique element appears using count()
my_list=[10,20,30,40,50,60,30]
visited=[]
for i in my_list:
    if i not in visited:
        b = my_list.count(i)
        print(f"{i} has occurred {b} times")
        visited.append(i)
