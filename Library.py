#Crate a system where student attributes are added and books are given
print("---Welcome to Divyank Library---")

students = []

while True:
    student = {}

    name = input("Enter your name (Press q to quit): ")
    if name == "q":
        break
    student["Name"] = name

    fatherName = input("Enter your father's name: ")
    if fatherName == "q":
        break
    student["Father Name"] = fatherName

    course = input("Enter your course: ")
    if course == "q":
        break
    student["Course"] = course

    roll = input("Enter your roll no.: ")
    if roll == "q":
        break
    student["Roll"] = int(roll)

    students.append(student)

#Display result
print("---Student's Attributes---")
print("Name\t\tFather Name\t\tCourse\t\tRoll")

for student in students:
    print(f"{student['Name']}\t\t{student['Father Name']}\t\t\t{student['Course']}\t\t{student['Roll']}")
           