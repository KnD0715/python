def find_set(x):
    if x == parent[x]:
        return x

    else:
        return find_set(parent[x])


def union(x, y):
    parent[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    parent = [i for i in range(N + 1)]

    for i in range(M):
        union(num_list[i * 2], num_list[i * 2 + 1])

    result = set()

    for i in range(1, N + 1):
        result.add(find_set(i))

    print(f"#{tc} {len(result)}")