import sys

sys.setrecursionlimit(1_000_000)


def dfs(v):
    visited[v] = True

    for r, d in graph[v]:
        if not visited[r]:
            distance[r] = d + distance[v]
            dfs(r)

    return


N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
distance = [0] * (N + 1)
visited = [False] * (N + 1)

for _ in range(N - 1):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append([B, C])
    graph[B].append([A, C])

dfs(1)
print(max(distance))
