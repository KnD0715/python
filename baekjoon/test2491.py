import sys

length = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

count_list = []
for count in range(1):
    cnt = 1
    for i in range(1, length):
        if num_list[i] >= num_list[i - 1]:
            cnt += 1
        else:
            count_list.append(cnt)
            cnt = 1

    count_list.append(cnt)
    cnt = 1

    for i in range(1, length):
        if num_list[i] <= num_list[i - 1]:
            cnt += 1
        else:
            count_list.append(cnt)
            cnt = 1

    count_list.append(cnt)
    cnt = 1

print(max(count_list))