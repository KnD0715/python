import sys

sys.stdin = open('input_1209.txt')

for i in range(1, 11):  # 10개 케이스만큼 반복
    num = int(input())  # 번호 입력
    arr = [list(map(int, input().split())) for _ in range(100)]  # 100 x 100 배열 생성

    sum_list = []  # 줄마다 합계 값 넣을 빈 리스트 생성

    for row in range(100):  # 행마다 덧셈
        result = 0
        for column in range(100):
            result += arr[row][column]
            sum_list.append(result)

    for column in range(100):  # 열마다 덧셈
        result = 0
        for row in range(100):
            result += arr[row][column]
            sum_list.append(result)

    result = 0  # 결과 값 초기 설정
    for row_column in range(100):  # 대각선 덧셈
        result += arr[row_column][row_column]
        sum_list.append(result)

    result = 0
    for row_column in range(100):  # 반대 대각선 덧셈
        result += arr[i][100 - 1 - row_column]
        sum_list.append(result)

    max_num = 0  # 최대값 초기 설정
    for num in sum_list:
        if max_num < num:
            max_num = num

    print(f"#{i} {max_num}")
