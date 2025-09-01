import sys

N, M = map(int, sys.stdin.readline().split())
num_list1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
num_list2 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result_list = []
for row in range(N):
    middle_list = []
    for column in range(M):
        middle_list.append(num_list1[row][column] + num_list2[row][column])

    result_list.append(middle_list)

for row in range(N):
    print(*result_list[row])