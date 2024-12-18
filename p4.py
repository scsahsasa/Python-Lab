#Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

# Take input from the user
age=int(input("Enter age:"))

# Check if the person is eligible to vote
if age>=18:
    print("Eligible for Vote!")
else:
    print("Not Eligible for Vote!")
