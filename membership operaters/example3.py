grades = {"sandy": "A", "squidward": "B", "spongebob": "C", "patrick": "D"}

student = input ("enter a name of a student: ").lower()

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} is not in the grade book")