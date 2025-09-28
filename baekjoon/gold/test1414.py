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
lan = [list(sys.stdin.readline().strip()) for _ in range(N)]
parent = [i for i in range(N + 1)]
graph = []

total = 0
for i in range(N):
    for j in range(N):
        if lan[i][j] == 0:
            graph.append((0, i + 1, j + 1))

        else:
            if ord('a') <= ord(lan[i][j]) <= ord('z'):
                graph.append((ord(lan[i][j]) - ord('a') + 1, i + 1, j + 1))
                total += (ord(lan[i][j]) - ord('a') + 1)
            elif ord('A') <= ord(lan[i][j]) <= ord('Z'):
                graph.append((ord(lan[i][j]) - ord('A') + 27, i + 1, j + 1))
                total += (ord(lan[i][j]) - ord('A') + 27)

graph.sort()
for len_line, a, b in graph:
    if find(a) != find(b):
        union(a, b)
        total -= len_line

    else:
        continue

result = True
for i in range(1, N + 1):
    if find(i) != 1:
        result = False

if result:
    print(total)

else:
    print(-1)