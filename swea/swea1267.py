from collections import deque

for tc in range(1, 11):
    V, E = map(int, input().split())
    work = list(map(int, input().split()))

    adj_list = [[] for _ in range(V + 1)]
    indegree = [0] * (V + 1)

    q = deque()
    result = []

    for i in range(E):
        s, e = work[i * 2], work[i * 2 + 1]
        adj_list[s].append(e)
        indegree[e] += 1

    for i in range(1, V + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        n = q.pop()
        result.append(n)

        for i in adj_list[n]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(f"#{tc}", ' '.join(list(map(str, result))))
