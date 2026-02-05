items_set = set()

print("Enter initial elements for the set, one element per line. Enter 'done' to finish.")
while True:
    entry = input("Enter element: ")
    if entry.lower() == 'done':
        break
    items_set.add(entry.strip())

print("Enter elements to remove from the set, one element per line. Enter 'done' to finish.")
while True:
    entry = input("Enter element to remove: ")
    if entry.lower() == 'done':
        break
    item = entry.strip()
    if item in items_set:
        items_set.remove(item)
        print(f"Removed {item} from the set.")
    else:
        print(f"{item} not found in the set.")
print("The resulting set is:", items_set)
