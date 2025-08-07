import sys

sys.stdin = open('input_16268.txt')


def max_value(num):
    max_num = 0
    for i in num:
        if max_num < i:
            max_num = i
    return max_num


T = int(input())
circuit_arr = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]]    # 순회 시킬 리스트 생성

for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []   # 합계를 넣을 빈 리스트 생성

    for row in range(N):
        for column in range(M):
            result = 0
            for circuit_row, circuit_column in circuit_arr:
                new_row, new_column = row + circuit_row, column + circuit_column
                if 0 <= new_row < N and 0 <= new_column < M:
                    result += arr[new_row][new_column]
            sum_list.append(result)

    print (sum_list)

    print(f"#{i} {max_value(sum_list)}")
