import sys
N = int(sys.stdin.readline())

paper = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

result = 0
for row in range(100):
    for column in range(100):
        if paper[row][column] == 1:
            result += 1

print(result)
