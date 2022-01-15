class Student:
    def __init__(self, name, usn, semester):
        self.name = name
        self.usn = usn
        self.semester = semester

    def set(self, branch):
        self.branch = branch

    def set(self, GPA, attend):
        self.grade = GPA
        self.attendance = attend

    def details(self):
        return (self.name, self.usn, self.semester, self.grade + "GPA", str(self.attendance)+"% present")


s1 = Student("Barb Palvin", "19ME069", 5)
# s1.set("MECHANICAL") gives error as latest defined method set() has two parameters
s1.set("6.9", 90)
print(s1.details())
