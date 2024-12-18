#Write a while loop to calculate the sum of digits of a given number.

# Get input from the user
num = int(input("Enter a number: "))

# Initialize sum to 0
sum1 = 0


# Loop to calculate the sum of digits
while num > 0:
    sum1+= num % 10  # Add the last digit to the sum
    num //= 10  # Remove the last digit by integer division

# Display the result
print("The sum of the digits is:", sum1)
