import sys

arr = [[0] * 1001 for _ in range(1001)]

T = int(sys.stdin.readline())
for i in range(1, T + 1):
    x, y, width, height = map(int, sys.stdin.readline().split())

    for row in range(x, x + width):
        for column in range(y, y + height):
            arr[row][column] = i

for cnt in range(1, T + 1):
    result = sum(row.count(cnt) for row in arr)
    print(result)