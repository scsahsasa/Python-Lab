#Python program to create a tuple with different data types

# Create a tuple 
mixed_tuple = (11,33,67.78,"apple",True,90.99)

# Print the tuple
print("Tuple with different data types:", mixed_tuple)

#checking different datatypes
print("\nDatatypes of each element : ")
for i in mixed_tuple:
    print(i," : ",type(i))
