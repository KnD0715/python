from collections import deque
import sys

sys.stdin = open('input_1226.txt')


def maze(y, x):
    while q:
        maze_row, maze_column = q.popleft()
        if maze_list[maze_row][maze_column] == -1:
            continue
        maze_list[maze_row][maze_column] = -1

        for cir_row, cir_column in circuit_list:
            new_row, new_column = maze_row + cir_row, maze_column + cir_column

            if 0 <= new_row < 16 and 0 <= new_column < 16:
                if maze_list[new_row][new_column] == '0':
                    q.append((new_row, new_column))
                elif maze_list[new_row][new_column] == '3':
                    return 1

    return 0

for _ in range(10):
    n = int(input())
    maze_list = [list(map(str, input())) for _ in range(16)]
    circuit_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    found = False
    for row in range(16):
        for column in range(16):
            if maze_list[row][column] == '2':
                start_row, start_column = row, column
                found = True
                break

        if found:
            break

    q = deque([(start_row, start_column)])

    print(f"#{n} {maze(start_row, start_column)}")
