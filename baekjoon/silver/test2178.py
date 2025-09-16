import sys
from collections import deque

def find(row, col):
    q = deque()
    q.append((row, col))

    while q:
        r, c = q.popleft()

        if r == N - 1 and c == M - 1:
            break

        for check_row, check_column in circuit_list:
            nr, nc = r + check_row, c + check_column

            if 0 <= nr < N and 0 <= nc < M:
                if distance[nr][nc] == 0 and maze[nr][nc] == '1':
                    q.append((nr, nc))
                    distance[nr][nc] = distance[r][c] + 1


N, M = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().strip()) for _ in range(N)]
distance = [[0] * M for _ in range(N)]

circuit_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]

distance[0][0] = 1
find(0, 0)

print(distance[N - 1][M - 1])