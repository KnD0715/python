import sys
from collections import deque


def bfs(x):
    q = deque([(x, 1)])

    while q:
        x, count = q.popleft()

        if A == x:
            return count

        if A > x:
            continue

        if x % 2 == 0:
            q.append((x // 2, count + 1))

        if str(x)[-1] == '1':
            x = int(str(x)[0:-1])
            q.append((x, count + 1))

    return -1


A, B = map(int, sys.stdin.readline().split())
print(bfs(B))
