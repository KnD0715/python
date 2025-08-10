T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    my_list = [list(map(int, input().split())) for _ in range(N)]

    start_row = 0
    start_column = 0
    circuit_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for row in range(N):
        for column in range(N):
            if my_list[row][column] == 2:
                start_row = row
                start_column = column

    count = N * N
    count_non_zero = 0
    attack_zone = 0

    for cir_row, cir_column in circuit_list:
                for num in range(1, N):
                    new_row = start_row + cir_row * num
                    new_column = start_column + cir_column * num
                    if 0 <= new_row < N and 0 <= new_column < N:
                        if my_list[new_row][new_column] == 0:
                            attack_zone += 1

                        else:
                            break
                    else:
                        break

    for row in range(N):
        for column in range(N):
            if my_list[row][column] != 0:
                count_non_zero += 1

    print (f"#{tc} {count - count_non_zero - attack_zone}")