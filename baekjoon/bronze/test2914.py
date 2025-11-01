import sys

N, M = map(int, sys.stdin.readline().split())
result = 0
for i in range((N * M) - 1, 0, -1):
    if i // N == M - 1:
        result = i

    else:
        break

print(result + 1)