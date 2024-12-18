#WAP to traverse a list of item and find particular item is present in the list or not


# List of items
items = ["apple", "banana", "cherry", "date", "fig", "grape"]

# Input: Get the item to search for
search_item = input("Enter the item to search: ")

# Flag to check if the item is found
found = False

# Traverse the list
for item in items:
    if item == search_item:
        found = True
        break

# Output the result
if found:
    print(f"{search_item} is present in the list.")
else:
    print(f"{search_item} is not present in the list.")
