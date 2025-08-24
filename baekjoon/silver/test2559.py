import sys

N, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

window_sum = sum(num_list[:K])
max_sum = window_sum

for i in range(K, N):
    window_sum += num_list[i] - num_list[i-K]
    if max_sum < window_sum:
        max_sum = window_sum

print(max_sum)
