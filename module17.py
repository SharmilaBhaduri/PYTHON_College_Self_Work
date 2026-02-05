items_set = set()

print("Enter elements for the set, one element per line. Enter 'done' to finish.")

while True:

    entry = input("Enter element: ")

    if entry.lower() == 'done':
        break

    items_set.add(entry.strip())

print("Iterating over the set:")

for item in items_set:
    print(item)