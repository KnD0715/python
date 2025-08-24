import sys

N, M = map(int, sys.stdin.readline().split())
basket = []

for i in range(N):
    basket += [i + 1]

for j in range(M):
    a, b = map(int, sys.stdin.readline().split())
    basket[a - 1], basket[b - 1] = basket[b - 1], basket[a - 1]

print (*basket)