import sys

sys.stdin = open('input_18634.txt')


def recur(cur, start, total):
    global result
    if cur == N - 1:
        result = min(result, num_list[start][0] + total)
        return
    for i in range(1, N):
        if visited[i] == 0 and start != i:
            visited[i] = 1
            recur(cur + 1, i, total + num_list[start][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]

    visited = [0 for _ in range(N)]
    result = float('inf')

    recur(0, 0, 0)

    print(f"#{tc} {result}")
