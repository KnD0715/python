import sys

sys.stdin = open('input_4836.txt')

T = int(input())  # 테스트 케이스 입력

for i in range(1, T + 1):  # 테스트 케이스만큼 반복
    N = int(input())  # 반복할 횟수 입력
    arr = [[0] * 10 for _ in range(10)]  # 배열 생성
    for j in range(N):  # 반복할 횟수만큼 반복
        row1, column1, row2, column2, color = map(int, input().split())  # 색깔을 칠할 행과 열 색깔 입력
        for paint_row in range(row1, row2 + 1):  # 색깔을 칠할 행만큼 반복
            for paint_column in range(column1, column2 + 1):  # 색깔을 칠할 열만큼 반복
                arr[paint_row][paint_column] += color  # 색깔을 칠할 곳에 빨강(1), 파랑(2) 덧셈

    count = 0  # 카운트 초기 설정
    for row in range(10):  # 행의 길이만큼 반복
        for column in range(10):  # 열의 길이만큼 반복
            if arr[row][column] == 3:  # 배열 내에 보라(3)이라면
                count += 1  # 카운트 증가

    print(f"#{i} {count}")
