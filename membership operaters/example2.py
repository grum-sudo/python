students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter student name: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")