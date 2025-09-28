def find(x):
    if parent[x] != x:
        p = parent[x]
        parent[x] = find(p)
        diff[x] += diff[p]
    return parent[x]


def union(x, y, w):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return

    if rank[rx] < rank[ry]:
        parent[rx] = ry
        diff[rx] = diff[y] - diff[x] - w

    elif rank[rx] > rank[ry]:
        parent[ry] = rx
        diff[ry] = w + diff[x] - diff[y]

    else:
        parent[ry] = rx
        diff[ry] = w + diff[x] - diff[y]
        rank[rx] += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parent = [i for i in range(N + 1)]
    diff = [0] * (N + 1)
    rank = [0] * (N + 1)
    result = []

    for _ in range(M):
        check = input().split()

        if check[0] == '!':
            a, b, w = map(int, check[1:])
            union(a, b, w)

        else:
            a, b = map(int, check[1:])
            if find(a) != find(b):
                result.append('UNKNOWN')

            else:
                result.append(str(diff[b] - diff[a]))

    print(f"#{tc}", ' '.join(result))
