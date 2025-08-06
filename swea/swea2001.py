import sys

sys.stdin = open('input_2001.txt')

T = int(input())  # 테스트 케이스 입력
for i in range(1, T + 1):  # 테스트 케이스만큼 반복
    N, M = map(int, input().split())  # 배열의 길이와 파리 퇴치 가능 길이 입력
    arr = [list(map(int, input().split())) for _ in range(N)]  # 배열 생성

    result_list = []  # 최대로 파리를 죽일 수 있는 값을 넣을 빈 리스트 생성
    for row in range(N):  # 행 길이만큼 반복
        for column in range(N):  # 열 길이만큼 반복
            result = 0  # 파리 퇴치 값 초기 설정
            for fly_row in range(row, row + M):  # 파리 퇴치 가능구간까지 반복
                for fly_column in range(column, column + M):
                    if 0 <= fly_row < N and 0 <= fly_column < N:  # 배열의 값 안에서만 실행
                        result += arr[fly_row][fly_column]
            result_list.append(result)  # 파리 퇴치수를 리스트에 추가

    max_num = 0  # 최대값 초기 설정
    for num in result_list:  # 최대값 찾기
        if num > max_num:
            max_num = num

    print(f"#{i} {max_num}")
