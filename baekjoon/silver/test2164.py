from collections import deque
import sys

N = int(sys.stdin.readline())
card_list = [i for i in range(1, N + 1)]

q = deque(card_list)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(*q)