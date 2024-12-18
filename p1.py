#Using input function take two number and then swap the number

# Take input from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Display original values
print("Before swapping:")
print("First number:", num1)
print("Second number:", num2)

# Swap the numbers
num1, num2 = num2, num1

# Display swapped values
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)
