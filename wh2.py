#Write a while loop that counts the number of digits in a given number.


# Get input from the user
n = int(input("Enter a number:"))

# Initialize count to 0
count = 0

# Loop to count digits
while n > 0:
    n //= 10   # Remove the last digit by integer division
    count += 1   # Increment the digit count


# Display the result
print("The number of digits is:", count)
