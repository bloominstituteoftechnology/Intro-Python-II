class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Name: {self.name}"

class Graduate(Student):
    def __init__(self, name, graduation_date):
        super().__init__(name)
        self.graduation_date = graduation_date
    def __str__(self):
        return f"Name: {self.name}\nGraduation date: {self.graduation_date}"

grad = Graduate('Gavin', 2020)
print(grad)
stud1 = Student('Test')
print(stud1)