import sys

students = []

for i in range(1, 31):
    students += [i]

for j in range(28):
    homework = int(sys.stdin.readline())
    students.remove(homework)

print(min(students))
print(max(students))