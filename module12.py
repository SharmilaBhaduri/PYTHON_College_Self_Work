student_ages = {
    "Sharmila": 20,
    "Samapti": 21,
    "Sukriti": 19,
    "Prerna": 20
}
name = input("Enter student name to get age: ")
age = student_ages.get(name, "Student not found")
print(f"{name}'s age is {age}")