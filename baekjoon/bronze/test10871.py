import sys

N, X = map(int, sys.stdin.readline().split())

my_list = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if (my_list[i] < X):
        print(my_list[i], end= ' ')