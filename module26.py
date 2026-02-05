target_string = input("Enter the string to be sorted: ")
order_string = input("Enter the order string: ")

order_dict = {char: index for index, char in enumerate(order_string)}

sorted_string = ''.join(sorted(target_string, key=lambda x: order_dict.get(x, len(order_string))))

print("Sorted string:", sorted_string)
