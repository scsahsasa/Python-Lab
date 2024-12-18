#WAP to check whether person can vote or not using function


# Get user input
age = int(input("Enter your age: "))


# Function to check voting eligibility
def can_vote(age):
    if age >= 18:
        return("You are eligible to vote.")
    else:
        return("You are not eligible to vote.")

# Call the function and display the result
result = can_vote(age)
print(result)
