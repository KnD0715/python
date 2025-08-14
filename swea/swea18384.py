import sys

sys.stdin = open('input_18384.txt')


def maze(y, x):
    while stack:
        maze_row, maze_column = stack.pop()
        if maze_list[maze_row][maze_column] == -1:
            continue
        maze_list[maze_row][maze_column] = -1

        for row, column in circuit_list:
            new_row, new_column = maze_row + row, maze_column + column

            if 0 <= new_row < N and 0 <= new_column < N:
                if maze_list[new_row][new_column] == 0:
                    stack.append((new_row, new_column))
                elif maze_list[new_row][new_column] == 3:
                    return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze_list = [list(map(int, input().strip())) for _ in range(N)]
    circuit_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for row in range(N):
        for column in range(N):
            if maze_list[row][column] == 2:
                start_row, start_column = row, column
                break

    stack = [[start_row, start_column]]
    print(f"#{tc} {maze(start_row, start_column)}")
