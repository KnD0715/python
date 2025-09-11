import sys
sys.stdin = open('input_1865.txt')

def work(row):
    global best
    if path:
        if success(path) <= best:
            return

    if len(path) == N:
        candidate = success(path)
        if candidate > best:
            best = candidate
        return

    for col in range(N):
        if visited[col] == 1:
            continue

        else:
            path.append(work_percent[row][col])
            visited[col] = 1
            work(row + 1)
            visited[col] = 0
            path.pop()

def success(arr):
    percent = 1
    for i in arr:
        percent *= (i / 100)

    percent *= 100
    return percent

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    work_percent = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    path = []
    best = 0.0

    work(0)
    print(f"#{tc} {best:.6f}")
