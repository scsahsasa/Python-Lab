#WAP to get factorial of a number using while loop.

#Get input from the user
n = int(input("Enter a number:"))

#Initialize factorial result to 1
fact = 1

#Calculate factorial using while loop
while n > 1:
    fact *= n
    n -= 1

#Display the result
print("The factorial is:",fact)
