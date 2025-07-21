import sys

N, X = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if lst[i] < X:
        print(lst[i], end= ' ')