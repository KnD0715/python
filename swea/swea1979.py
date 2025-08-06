import sys

sys.stdin = open('input_1979.txt')

T = int(input())  # 테스트 케이스 입력

for i in range(1, T + 1):  # 테스트 케이스만큼 반복
    N, K = map(int, input().split())  # 배열의 수와 단어 길이 입력
    arr = [list(map(int, input().split())) for _ in range(N)]  # 배열 생성

    puzzle = 0  # 들어 갈 수 있는 단어 초기 설정
    count = 0  # 카운트 초기 설정

    for row in range(N):  # 행 길이만큼 반복
        if count == K:  # 카운트가 단어 길이와 같다면
            puzzle += 1  # puzzle 변수에 1 증가
        count = 0  # 카운트 다시 초기화
        for column in range(N):  # 열 길이만큼 반복
            if arr[row][column] == 1:  # 값이 1이면
                count += 1  # 카운트 1 증가
            else:
                if count == K:  # 값이 0이 나올시 지금까지 카운트 횟수 확인
                    puzzle += 1  # 카운트 횟수가 단어 길이와 같으면 1 증가
                count = 0  # 카운트 초기화

    for column in range(N):  # 행과 같은 원리
        if count == K:
            puzzle += 1
        count = 0
        for row in range(N):
            if arr[row][column] == 1:
                count += 1
            else:
                if count == K:
                    puzzle += 1
                count = 0
    if count == K:  # 반복문이 끝나고 남은 카운트가 단어 길이와 같으면
        puzzle += 1  # 마지막 1 증가

    print(f"#{i} {puzzle}")
