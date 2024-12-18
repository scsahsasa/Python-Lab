#program to copy elements 44 and 55 from the tuple into a new tuple.
#for example Tuple1 elements are: (11, 22, 33, 44, 55, 66)

# create a tuple
tuple1=(11, 22, 33, 44, 55, 66)

# Create a new tuple with the specified elements
new_tuple = (tuple1[3], tuple1[4])  # Copying elements at index 3 and 4

# Print the new tuple
print("Original tuple : ",tuple1)
print("New Tuple with copied elements:", new_tuple)
