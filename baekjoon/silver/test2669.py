import sys

arr = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for row in range(x1, x2):
        for column in range(y1, y2):
            arr[row][column] = 1

result = 0

for row in range(100):
    for column in range(100):
        if arr[row][column] == 1:
            result += 1

print(result)