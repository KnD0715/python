import sys

sys.stdin = open('input_12712.txt')


def max_value(num):
    max_num = 0
    for i in num:
        if max_num < i:
            max_num = i

    return max_num


T = int(input())
plus_fly_catch = [[0, 1], [0, -1], [1, 0], [-1, 0]]
x_fly_catch = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total_list = []
    for row in range(len(arr)):
        for column in range(len(arr)):
            total = 0
            for catch_row, catch_column in plus_fly_catch:
                for num in range(1, M):
                    new_row = row + catch_row * num
                    new_col = column + catch_column * num
                    if 0 <= new_row < N and 0 <= new_col < N:
                        total += arr[new_row][new_col]
            total += arr[row][column]
            total_list.append(total)
            total = 0

            for catch_row, catch_column in x_fly_catch:
                for num in range(1, M):
                    new_row = row + catch_row * num
                    new_col = column + catch_column * num
                    if 0 <= new_row < N and 0 <= new_col < N:
                        total += arr[new_row][new_col]

            total += arr[row][column]
            total_list.append(total)

    print(f"#{i} {max_value(total_list)}")
