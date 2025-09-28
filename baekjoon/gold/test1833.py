import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x

    else:
        parent[x] = y

N = int(sys.stdin.readline())

express = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
parent = [i for i in range(N + 1)]
edges = []
total = 0

for i in range(N):
    for j in range(i + 1, N):
        if express[i][j] < 0:
            total += (-express[i][j])
            union(i + 1, j + 1)

        else:
            edges.append((express[i][j], i + 1, j + 1))

edges.sort()

result = []
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        total += cost
        result.append((a, b))

print(total, len(result))
for res in result:
    print(*res)