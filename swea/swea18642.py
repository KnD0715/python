import sys

sys.stdin = open('input_18642.txt')


def bfs(row):
    global result
    if sum(path) > result:
        return

    if len(path) == N:
        if sum(path) < result:
            result = sum(path)
        return

    for col in range(N):
        if visited[col]:
            continue

        else:
            path.append(factory[row][col])
            visited[col] = 1
            bfs(row + 1)
            path.pop()
            visited[col] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]

    path = []
    visited = [0] * N
    result = float('inf')

    bfs(0)

    print(f"#{tc} {result}")
