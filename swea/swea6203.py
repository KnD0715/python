class Student:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def total_score(self):
        return f"국어, 영어, 수학의 총점: {self.kor + self.eng + self.math}"


kor, eng, math = map(int, input().split(','))
student = Student(kor, eng, math)

print(student.total_score())