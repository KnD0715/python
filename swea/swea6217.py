class Student():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "이름: {0}".format(self.name)

class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def __repr__(self):
        return "이름: {0}, 전공: {1}".format(self.name, self.major)

student1 = Student('홍길동')
student2 = GraduateStudent('이순신', '컴퓨터')

print(student1)
print(student2)