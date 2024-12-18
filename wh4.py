#Create a while loop to print the Fibonacci series up to n terms


# Get the number of terms from the user
n = int(input("Enter the number of terms: "))

# Initialize the first two terms of the Fibonacci series
a, b = 0, 1
count = 0  # Counter to keep track of the number of terms printed

# Start a while loop to print Fibonacci series up to n terms
while count < n:
    print(a, end=" ")
    # Update to the next term
    a, b = b, a + b
    count += 1
