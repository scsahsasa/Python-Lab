#WAP to get table of a number using function

#Get user input
num = int(input("Enter a number:"))

# Function to print the multiplication table of a number
def print_table(num):
    print(f"Multiplication Table of {num} is:")
    for i in range(1, 11):
        print(num,"*",i,"=",i*num)

print_table(num)

