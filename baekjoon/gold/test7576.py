import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

check = deque()
distance = [[0] * N for _ in range(M)]
circuit_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for row in range(M):
    for column in range(N):
        if tomato[row][column] == 1:
            check.append((row, column))
            distance[row][column] = 1

while check:
    r, c = check.popleft()

    for pr, pc in circuit_list:
        nr, nc = r + pr, c + pc

        if 0 <= nr < M and 0 <= nc < N and tomato[nr][nc] != -1 and distance[nr][nc] == 0:
            check.append((nr, nc))
            distance[nr][nc] = distance[r][c] + 1

max_day = 0
for row in range(M):
    for column in range(N):
        if tomato[row][column] != -1 and distance[row][column] == 0:
            print(-1)
            sys.exit(0)

        if max_day < distance[row][column]:
            max_day = distance[row][column]

print(max_day - 1)
