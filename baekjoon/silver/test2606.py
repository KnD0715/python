from collections import deque
import sys


def infection(start):
    global count
    q = deque()
    q.append(start)
    virus[start] = 1
    while q:
        n = q.popleft()

        for v in adj_list[n]:
            if virus[v] == 0:
                q.append(v)
                virus[v] = 1
                count += 1


N = int(sys.stdin.readline())
adj_list = [[] for _ in range(N + 1)]

route = int(sys.stdin.readline())

count = 0

virus = [0] * (N + 1)

for _ in range(route):
    s, e = map(int, sys.stdin.readline().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

infection(1)
print(count)
