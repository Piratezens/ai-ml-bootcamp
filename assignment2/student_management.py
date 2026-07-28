class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(self.name, self.roll)

students = []

students.append(Student("Ram", 1))
students.append(Student("Sita", 2))

for student in students:
    student.display()