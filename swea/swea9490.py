import sys

sys.stdin = open('input_9490.txt')


def max_value(num):
    max_num = 0
    for i in num:
        if i > max_num:
            max_num = i

    return max_num


T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    balloon_list = [list(map(int, input().split())) for _ in range(N)]

    circuit_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    result_list = []
    for row in range(N):
        for column in range(M):
            total = 0
            for cir_row, cir_column in circuit_list:
                for num in range(1, balloon_list[row][column] + 1):
                    new_row, new_column = row + cir_row * num, column + cir_column * num
                    if 0 <= new_row < N and 0 <= new_column < M:
                        total += balloon_list[new_row][new_column]

            total += balloon_list[row][column]
            result_list.append(total)

    print(f"#{i} {max_value(result_list)}")
