import sys

N = int(sys.stdin.readline())
paper = [[0] * 1001 for _ in range(1001)]

for i in range(1, N + 1):
    x, y, w, h = map(int, sys.stdin.readline().split())

    for j in range(y, y + h):
        paper[j][x : x + w] = [i] * w

count = [0] * (N + 1)
for i in paper:
    for j in i:
        count[j] += 1

for i in range(1, N + 1):
    print(count[i])
