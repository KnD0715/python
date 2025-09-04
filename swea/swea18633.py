import sys

sys.stdin = open('input_18633.txt')


def find(y, x):
    global start, result
    if result < start:
        return

    if y == N - 1 and x == N - 1:
        result = start
        return

    for column, row in move:
        new_column, new_row = column + y, row + x
        if 0 <= new_column < N and 0 <= new_row < N:
            start += num_list[new_row][new_column]
            find(new_column, new_row)
            start -= num_list[new_row][new_column]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]

    move = [[0, 1], [1, 0]]
    start = num_list[0][0]
    result = float('inf')

    find(0, 0)

    print(f"#{tc} {result}")
