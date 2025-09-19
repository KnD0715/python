import sys
from collections import deque

N = int(sys.stdin.readline())
adj_list = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    node1, node2 = map(int, sys.stdin.readline().split())
    adj_list[node1].append(node2)
    adj_list[node2].append(node1)

parent = [0] * (N + 1)
q = deque([1])
parent[1] = -1

while q:
    num = q.popleft()
    for next in adj_list[num]:
        if parent[next] == 0:
            parent[next] = num
            q.append(next)

for i in range(2, N + 1):
    print(parent[i])