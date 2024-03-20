# create empty list
my_list = []

# append to empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# add new value to specific position (2nd)
my_list.insert(1, 15)

# extend my_list 
my_list.extend([50, 60, 70])

# remove the last element of my-list
del my_list[-1]

#sort my-list in ascending order
my_list.sort()

# find and print index value of 30
my_list.index(2)