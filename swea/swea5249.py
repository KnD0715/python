def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])

    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx < ry:
        parents[ry] = rx

    else:
        parents[rx] = ry

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = []

    for _ in range(E):
        start, end, weight = map(int, input().split())
        edges.append((start, end, weight))

    edges.sort(key=lambda x:x[2])

    count = 0
    result = 0

    parents = [i for i in range(V + 1)]

    for u, v, w in edges:
        if find_set(u) != find_set(v):
            union(u, v)
            count += 1
            result += w

            if count == V:
                break

    print(f"#{tc} {result}")