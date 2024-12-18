#WAP to print triangular  pattern
'''
*                         1                       1

* *                      1 2                      2 2 

* * *                   1 2 3                     3 3 3

* * * *                1 2 3 4                    4 4 4 4
'''

# Number of rows
n = 4

# Pattern 1: Asterisk triangle
print("Pattern 1:")
for i in range(1, n + 1):
    print("* " * i)

# Pattern 2: Number triangle (increasing numbers)
print("\nPattern 2:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern 3: Number triangle (repeated numbers)
print("\nPattern 3:")
for i in range(1, n + 1):
    print(f"{i} " * i)
