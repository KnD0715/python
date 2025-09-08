import sys
from collections import deque

sys.stdin = open('input_1953.txt')

T = int(input())
for tc in range(1, T + 1):
    q = deque()
    row, column, manhole_row, manhole_column, move = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(row)]
    visit = [[0] * column for _ in range(row)]
    count = 0

    need = {
        (-1, 0): {1, 2, 5, 6},
        (1, 0): {1, 2, 4, 7},
        (0, -1): {1, 3, 4, 5},
        (0, 1): {1, 3, 6, 7},
    }

    if tunnel[manhole_row][manhole_column] != 0:
        q.append((manhole_row, manhole_column, 1))
        visit[manhole_row][manhole_column] = 1
        count = 1

    while q:
        new_row, new_column, time = q.popleft()

        if time >= move:
            continue

        if tunnel[new_row][new_column] == 1:
            circuit_list = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        elif tunnel[new_row][new_column] == 2:
            circuit_list = [[1, 0], [-1, 0]]
        elif tunnel[new_row][new_column] == 3:
            circuit_list = [[0, 1], [0, -1]]
        elif tunnel[new_row][new_column] == 4:
            circuit_list = [[-1, 0], [0, 1]]
        elif tunnel[new_row][new_column] == 5:
            circuit_list = [[1, 0], [0, 1]]
        elif tunnel[new_row][new_column] == 6:
            circuit_list = [[1, 0], [0, -1]]
        elif tunnel[new_row][new_column] == 7:
            circuit_list = [[-1, 0], [0, -1]]
        else:
            circuit_list = []

        for check_row, check_column in circuit_list:
            nr, nc = new_row + check_row, new_column + check_column
            if 0 <= nr < row and 0 <= nc < column and visit[nr][nc] == 0 and tunnel[nr][nc] != 0:
                if tunnel[nr][nc] in need[(check_row, check_column)]:
                    visit[nr][nc] = 1
                    count += 1
                    q.append((nr, nc, time + 1))

    print(f"#{tc} {count}")
