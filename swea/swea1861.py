import sys

sys.stdin = open('input_1861.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    circuit_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    result = 0
    number = 0

    for row in range(N):
        for column in range(N):
            count = 1
            start = room[row][column]
            current_row, current_col = row, column

            while True:
                moved = False
                for plus_row, plus_col in circuit_list:
                    new_row, new_col = current_row + plus_row, current_col + plus_col

                    if 0 <= new_row < N and 0 <= new_col < N:
                        if room[new_row][new_col] - 1 == room[current_row][current_col]:
                            count += 1
                            current_row, current_col = new_row, new_col
                            moved = True
                            break
                if not moved:
                    break

            if result < count:
                result = count
                number = start
            elif result == count:
                if number:
                    number = min(number, start)
                else:
                    number = start

    print(f"#{tc} {number} {result}")
