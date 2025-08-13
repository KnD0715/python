import sys
sys.stdin = open('input_18311.txt')


def dfs(v, N):
    visited = [0] * (N + 1)
    stack = []
    result = []

    while True:
        if visited[v] == 0:
            visited[v] = 1
            result.append(v)
        for w in adj_list[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

    return result


V, E = map(int, input().split())
route = list(map(int, input().split()))
adj_list = [[] for _ in range(V + 1)]

for i in range(E):
    v, w = route[i*2], route[i*2+1]
    adj_list[v].append(w)
    adj_list[w].append(v)

result = dfs(1, V)
print(f"#1 {'-'.join(map(str, result))}")
