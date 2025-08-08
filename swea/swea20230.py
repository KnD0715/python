T = int(input())

for i in range(1, T + 1):
    N = int(input())
    balloon_list = [list(map(int, input().split())) for _ in range(N)]

    circuit_list = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    result = 0
    for row in range(N):
        for column in range(N):
            total = balloon_list[row][column]
            for cir_row, cir_column in circuit_list:
                for num in range(1, N + 1):
                    new_row = row + cir_row * num
                    new_column = column + cir_column * num
                    if 0 <= new_row < N and 0 <= new_column < N:
                        total += balloon_list[new_row][new_column]

            if total > result:
                result = total

    print (f"#{i} {result}")