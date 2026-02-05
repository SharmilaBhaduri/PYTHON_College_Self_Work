#python programming of Python Function with Arguments, and No Return Value .
def print_age(name, age):
    print(f"Hello, {name}!")
    print(f"You are {age} years old.")
    if age < 18:
        print("You're a junior.")
    elif age < 65:
        print("You're an adult.")
    else:
        print("You're a senior.")

print_age("sharmila", 19)
print_age("samaptii", 25)
print_age("sukriti", 70)