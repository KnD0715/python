import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

sorted_list = sorted(num_list, reverse=True)

print(sorted_list[M - 1])
