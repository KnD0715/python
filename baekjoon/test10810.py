import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0] * N

for x in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for y in range (i, j + 1):
        basket[y - 1] = k

print (*basket)