import sys
from collections import deque

def dfs(start):
    if visited_dfs[start] == 0:
        print(start, end=' ')
        visited_dfs[start] = 1

    else:
        return

    for w in adj_list[start]:
        dfs(w)

def bfs(start):
    q = deque()
    q.append(start)
    visited_bfs[start] = 1

    while q:
        v = q.popleft()
        print(v, end=' ')

        for w in adj_list[v]:
            if visited_bfs[w] == 0:
                visited_bfs[w] = 1
                q.append(w)

node, route, root = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(node + 1)]
visited_dfs = [0 for _ in range(node + 1)]
visited_bfs = [0 for _ in range(node + 1)]

for _ in range(route):
    node1, node2 = map(int, sys.stdin.readline().split())
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

for lst in adj_list:
    lst.sort()

dfs(root)
print()
bfs(root)
