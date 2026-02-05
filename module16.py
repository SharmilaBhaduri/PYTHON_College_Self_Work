items_set = set()

print("Enter elements for the set, one element per line. Enter 'done' to finish.")

while True:

    entry = input("Enter element: ")
    
    if entry.lower() == 'done':
        break

    items_set.add(entry.strip())

size_of_set = len(items_set)
print("The size of the set is:", size_of_set)