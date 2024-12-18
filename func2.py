#WAP to find maximum among two number


# Get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Function to find the maximum of two numbers
def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Call the function and display the result
maximum = find_max(num1, num2)
print("The maximum number is:",maximum)
