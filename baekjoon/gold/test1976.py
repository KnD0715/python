import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        location = q.pop()
        for i in range(N):
            if city[location][i] and not visited[i]:
                visited[i] = True
                q.append(i)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
plan = list(map(int, sys.stdin.readline().split()))

visited = [False] * N
result = "YES"

bfs(plan[0] - 1)
for p in plan:
    if not visited[p - 1]:
        result = 'NO'
        break

print(result)