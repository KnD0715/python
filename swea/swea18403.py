from collections import deque
import sys

sys.stdin = open('input_18403.txt')


def maze(y, x, N):
    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1
    while q:
        maze_row, maze_column = q.popleft()
        if maze_list[maze_row][maze_column] == '3':
            return visited[maze_row][maze_column] - 2 # 시작 칸, 도착 칸 제외

        for cir_row, cir_column in circuit_list:
            new_row, new_column = maze_row + cir_row, maze_column + cir_column
            if 0 <= new_row < N and 0 <= new_column < N and maze_list[new_row][new_column] != '1' and visited[new_row][
                new_column] == 0:
                q.append([new_row, new_column])
                visited[new_row][new_column] = visited[maze_row][maze_column] + 1

    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze_list = [list(map(str, input())) for _ in range(N)]
    circuit_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for row in range(N):
        for column in range(N):
            if maze_list[row][column] == '2':
                start_row, start_column = row, column
                break

    q = deque([(start_row, start_column)])

    result = maze(start_row, start_column, N)
    print(f"#{tc} {result}")
