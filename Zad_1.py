class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if sum(self.marks) / len(self.marks) > 50:
            return True
        else:
            return False


Student_1 = Student("Jan", [30, 60, 80])
Student_2 = Student("Stanisław", [15, 20, 35])

print(Student_1.is_passed())
print(Student_2.is_passed())
