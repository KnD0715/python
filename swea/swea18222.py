import sys

sys.stdin = open('input_18222.txt')

T = int(input())
for tc in range(1, T + 1):
    N, length = map(int, input().split())
    word_list = [list(input()) for _ in range(N)]

    check_list = []  # 확인할 리스트 생성
    for row in range(N):  # 행 확인
        for column in range(N):
            middle_list = []  # 중간 리스트 생성
            for num in range(length):
                new_row = row + num
                if 0 <= new_row < N:
                    middle_list.append(word_list[new_row][column])

            if len(middle_list) == length:  # 회문 길이가 중간 리스트의 길이와 같다면
                check_list.append(middle_list)  # 체크 리스트 추가

    for column in range(N):  # 열 확인
        for row in range(N):
            middle_list = []
            for num in range(length):
                new_column = column + num
                if 0 <= new_column < N:
                    middle_list.append(word_list[row][new_column])

            if len(middle_list) == length:
                check_list.append(middle_list)

    result = ''
    for check in check_list:    # 체크리스트에서 회문 확인
        reverse_word = check[::-1]
        if reverse_word == check:
            result = check
            break

    print(f"#{tc}", ''.join(result))
