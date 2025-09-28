import sys
sys.setrecursionlimit(1000000)

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

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N + 1)]

for _ in range(M):
    check, a, b = map(int, sys.stdin.readline().split())

    if check == 0:
        union(a, b)

    else:
        if find(a) == find(b):
            print("YES")

        else:
            print("NO")