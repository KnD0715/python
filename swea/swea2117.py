import sys
from collections import deque

sys.stdin = open('input_2117.txt')

def count_houses_bfs(x, y, limitK):
    dist = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 0

    cnt = 0
    while q:
        r, c = q.popleft()
        if city[r][c] == 1:
            cnt += 1

        if dist[r][c] == limitK:
            continue

        for dr, dc in circuit_list:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                nd = dist[r][c] + 1
                if dist[nr][nc] == -1 or nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    q.append((nr, nc))
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N, service = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    circuit_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    result = 0
    for row in range(N):
        for column in range(N):
            for K in range(1, N + 2):
                limitK = K - 1
                count = count_houses_bfs(row, column, limitK)

                cost = K * K + (K - 1) * (K - 1)
                if count * service >= cost:
                    if result < count:
                        result = count

    print(f"#{tc} {result}")
