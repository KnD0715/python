import sys
sys.stdin = open('input_20739.txt')

T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    my_list = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0
    for row in range(N):
        count_row = 0
        for column in range(M):
            if my_list[row][column] == 1:
                count_row += 1
                if max_count < count_row:
                    max_count = count_row
            else:
                count_row = 0


    for column in range(M):
        count_column = 0
        for row in range(N):
            if my_list[row][column] == 1:
                count_column += 1
                if max_count < count_column:
                    max_count = count_column

            else:
                count_column = 0

    if max_count < 2:
        max_count = 0

    print(f"#{i} {max_count}")