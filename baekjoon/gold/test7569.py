import sys
from collections import deque


def bfs():
    while q:
        z, x, y = q.popleft()

        for cz, cx, cy in circuit_list:
            nz = z + cz
            nx = x + cx
            ny = y + cy

            if 0 <= nz < H and 0 <= nx < M and 0 <= ny < N:
                if tomato[nz][nx][ny] == 0 and visited[nz][nx][ny] == False:
                    q.append((nz, nx, ny))
                    tomato[nz][nx][ny] = tomato[z][x][y] + 1
                    visited[nz][nx][ny] = True


N, M, H = map(int, sys.stdin.readline().split())

tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(M)] for _ in range(H)]
visited = [[[False] * N for _ in range(M)] for _ in range(H)]

circuit_list = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
q = deque()

day = 0

for height in range(H):
    for row in range(M):
        for column in range(N):
            if tomato[height][row][column] == 1:
                q.append((height, row, column))
                visited[height][row][column] = True

bfs()

for height in range(H):
    for row in range(M):
        for column in range(N):
            if tomato[height][row][column] == 0:
                print(-1)
                exit()

            else:
                day = max(day, tomato[height][row][column])

print(day - 1)
