#WAP to get factorial of a number using function


# Get user input
num = int(input("Enter a number: "))


# Function to calculate factorial
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)

# Check for valid input and display the result
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print("The factorial of number is:",result)




