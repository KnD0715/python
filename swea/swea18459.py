from collections import deque
import sys

sys.stdin = open('input_18459.txt')


def bfs(s, v):
    Q.append(s)
    visited[s] = 1
    result = []
    while Q:
        q = Q.popleft()
        result.append(q)
        for w in adj_list[q]:
            if visited[w] == 0:
                Q.append(w)
                visited[w] = visited[q] + 1

    return result

node_num, route_num = map(int, input().split())
route_list = list(map(int, input().split()))
adj_list = [[] for _ in range(node_num + 1)]

for i in range(route_num):
    node1, node2 = route_list[i * 2], route_list[i * 2 + 1]
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

visited = [0] * (node_num + 1)
Q = deque()

result = bfs(1, node_num)

print(f"#1", *result)

