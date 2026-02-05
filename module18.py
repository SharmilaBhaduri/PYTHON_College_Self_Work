items_set = set()

print("Enter elements for the set, one element per line. Enter 'done' to finish.")

while True:

    entry = input("Enter element: ")

    if entry.lower() == 'done':
        break

    try:
        items_set.add(float(entry.strip()))

    except ValueError:
        print("Please enter a valid number.")

if items_set:
    max_element = max(items_set)
    min_element = min(items_set)

    print("The maximum element in the set is:", max_element)
    print("The minimum element in the set is:", min_element)

else:
    print("The set is empty.")
    