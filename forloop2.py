#WAP to get factorial of a number


# Input: Get the number from the user
num = int(input("Enter a number: "))

# Initialize factorial variable
factorial = 1

# Calculate factorial
for i in range(1, num + 1):
    factorial *= i

# Output: Print the factorial
print("The factorial of number is:",factorial)
