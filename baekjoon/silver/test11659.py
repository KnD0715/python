import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    num_list[i] += num_list[i - 1]

num_list = [0] + num_list
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(num_list[j] - num_list[i - 1])