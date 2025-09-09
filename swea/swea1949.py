import sys

sys.stdin = open('input_1949.txt')


def max_value(arr):  # 최댓값 찾기
    max_num = 0
    for row in range(N):
        for column in range(N):
            if max_num < mountain[row][column]:
                max_num = mountain[row][column]

    return max_num


def DFS(x, y, length, drill, prev):  # x, y: 시직 좌표, length: 길이, drill: 땅 뚫었는지, prev: 이전 높이
    global result, visited
    result = max(result, length)

    for plus_row, plus_column in circuit_list:
        new_row, new_column = x + plus_row, y + plus_column

        if not (0 <= new_row < N and 0 <= new_column < N):
            continue

        if visited[new_row][new_column]:
            continue

        if mountain[new_row][new_column] < prev:
            visited[new_row][new_column] = True
            DFS(new_row, new_column, length + 1, drill, mountain[new_row][new_column])
            visited[new_row][new_column] = False

        else:
            if drill == 0:
                if mountain[new_row][new_column] - K < prev:
                    visited[new_row][new_column] = True
                    DFS(new_row, new_column, length + 1, 1, prev - 1)
                    visited[new_row][new_column] = False

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    circuit_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    high = max_value(mountain)

    result = 0

    for row in range(N):
        for column in range(N):
            if mountain[row][column] == high:
                visited = [[False] * N for _ in range(N)]
                visited[row][column] = True
                DFS(row, column, 1, 0, mountain[row][column])

    print(f"#{tc} {result}")