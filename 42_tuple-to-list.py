
my_tuple = (1, 2, 3)# Create a tuple


my_list = list(my_tuple)# Convert tuple to list


my_list.append(4)# Modify the list


# Convert the list back to a tuple
my_tuple = tuple(my_list)

print("Updated tuple:", my_tuple)
