import sys

sys.stdin = open('input_1219.txt')


def dfs(start, end):
    visited = [0] * 100
    stack = [start]
    visited[start] = 1

    while stack:
        v = stack.pop()
        if v == end:
            return 1

        for w in adj_list[v]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(w)

    return 0


for tc in range(1, 11):
    t, route_num = map(int, input().split())
    route = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)]
    for i in range(route_num):
        v, w = route[i * 2], route[i * 2 + 1]
        adj_list[v].append(w)

    result = dfs(0, 99)

    print(f"#{tc} {result}")
