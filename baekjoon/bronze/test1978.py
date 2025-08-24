import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

count = 0
for i in num_list:
    middle_count = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            middle_count += 1

    if middle_count == i - 2:
        count += 1

print(count)