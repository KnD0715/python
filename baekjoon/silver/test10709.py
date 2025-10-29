import sys

N, M = map(int, sys.stdin.readline().split())
cloud = [list(sys.stdin.readline().strip()) for _ in range(N)]
result = [[-1] * M for _ in range(N)]

for row in range(N):
    for column in range(M):
        if cloud[row][column] == 'c':
            result[row][column] = 0

        elif column > 0:
            if cloud[row][column] == '.':
                if result[row][column - 1] != -1:
                    result[row][column] = result[row][column - 1] + 1

for i in range(N):
    print(*result[i])