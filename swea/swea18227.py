import sys

sys.stdin = open('input_18227.txt')


def dfs(start, end, num):
    visited = [0] * (num + 1)
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


T = int(input())
for tc in range(1, T + 1):
    node, route = map(int, input().split())
    adj_list = [[] for _ in range(node + 1)]
    for _ in range(route):
        num1, num2 = map(int, input().split())
        adj_list[num1].append(num2)
        adj_list[num2].append(num1)

    start, end = map(int, input().split())

    result = dfs(start, end, node)
    print(f"#{tc} {result}")
