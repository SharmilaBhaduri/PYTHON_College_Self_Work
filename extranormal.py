# Initialize variables to count vowels, consonants, and blanks
vowels = 0
consonants = 0
blanks = 0

# Input string
string = input("Enter a string: ")

# Convert the string to lowercase for easier comparison
string = string.lower()

# Iterate through each character in the string
for char in string:
    # Check if the character is a vowel
    if char in "aeiou":
        vowels += 1
    # Check if the character is a consonant
    elif char.isalpha():
        consonants += 1
    # Check if the character is a blank (space)
    elif char == " ":
        blanks += 1

# Output the counts
print("Total number of vowels:", vowels)
print("Total number of consonants:", consonants)
print("Total number of blanks:", blanks)