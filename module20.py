list1 = []
list2 = []

print("Enter elements for the first list, one element per line. Enter 'done' to finish.")
while True:
    entry = input("Enter element for list 1: ")
    if entry.lower() == 'done':
        break
    list1.append(entry.strip())

print("Enter elements for the second list, one element per line. Enter 'done' to finish.")
while True:
    entry = input("Enter element for list 2: ")
    if entry.lower() == 'done':
        break
    list2.append(entry.strip())

common_element_found = False
for item in list1:
    if item in list2:
        common_element_found = True
        break

if common_element_found:
    print("The two lists have at least one element in common.")
else:
    print("The two lists do not have any elements in common.")
    