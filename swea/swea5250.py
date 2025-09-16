from collections import deque


def start(row, col):
    q = deque()
    q.append((row, col))

    while q:
        r, c = q.popleft()

        if r == N - 1 and c == N - 1:
            continue

        for cr, cc in circuit_list:
            nr, nc = r + cr, c + cc
            if nr == 0 and nc == 0:
                continue

            if 0 <= nr < N and 0 <= nc < N:
                if oil[nr][nc]:
                    if road[r][c] < road[nr][nc]:
                        new_val = oil[r][c] + (road[nr][nc] - road[r][c]) + 1
                        if new_val < oil[nr][nc]:
                            oil[nr][nc] = new_val
                            q.append((nr, nc))
                    else:
                        new_val = oil[r][c] + 1
                        if new_val < oil[nr][nc]:
                            oil[nr][nc] = new_val
                            q.append((nr, nc))
                else:
                    if road[r][c] < road[nr][nc]:
                        oil[nr][nc] = oil[r][c] + (road[nr][nc] - road[r][c]) + 1
                        q.append((nr, nc))
                    else:
                        oil[nr][nc] = oil[r][c] + 1
                        q.append((nr, nc))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    road = [list(map(int, input().split())) for _ in range(N)]

    oil = [[0] * N for _ in range(N)]
    circuit_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    start(0, 0)

    print(f"#{tc} {oil[N - 1][N - 1]}")
