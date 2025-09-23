import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

total = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if total == M:
                break

            if num_list[i] + num_list[j] + num_list[k] > M:
                continue
            else:
                total = max(total, num_list[i] + num_list[j] + num_list[k])

print(total)