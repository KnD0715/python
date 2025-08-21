from collections import deque
import sys

sys.stdin = open('input_10966.txt')


def water(lst):
    visited = [[0] * M for _ in range(N)]
    distance = [[0] * M for _ in range(N)]
    Q = deque()

    for row in range(N):
        for column in range(M):
            if my_list[row][column] == 'W':
                visited[row][column] = 1
                Q.append((row, column))

    while Q:
        my_list_row, my_list_column = Q.popleft()

        for cir_row, cir_column in circuit_list:
            new_row, new_column = my_list_row + cir_row, my_list_column + cir_column

            if 0 <= new_row < N and 0 <= new_column < M and visited[new_row][new_column] == 0:
                visited[new_row][new_column] = 1
                distance[new_row][new_column] = distance[my_list_row][my_list_column] + 1
                Q.append((new_row, new_column))

    result = 0
    for row in range(N):
        for column in range(M):
            result += distance[row][column]

    return result


T = int(input())
circuit_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    my_list = [list(input()) for _ in range(N)]

    print(f"#{tc} {water(my_list)}")
