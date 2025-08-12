T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    my_list = [list(map(int, input().split())) for _ in range(N)]

    circuit_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    max_num = 0
    for row in range(N):
        for column in range(N):
            total = my_list[row][column]
            for cir_row, cir_column in circuit_list:
                if my_list[row][column] % 2 == 0:
                    new_row, new_column = row + cir_row * 2, column + cir_column * 2
                    if 0 <= new_row < N and 0 <= new_column < N:
                        total += my_list[new_row][new_column]

                else:
                    new_row, new_column = row + cir_row, column + cir_column
                    if 0 <= new_row < N and 0 <= new_column < N:
                        total += my_list[new_row][new_column]

            if total > max_num:
                max_num = total

    print(f"#{tc} {max_num}")