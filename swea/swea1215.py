import sys

sys.stdin = open('input_1215.txt')

for tc in range(1, 11):  # 10개 테스트 케이스
    length = int(input())  # 회문 단어 길이
    your_list = [list(input()) for _ in range(8)]

    result_list = []  # 반환할 최종 리스트 생성
    for row in range(8):  # 8x8 배열
        for column in range(8):
            middle_list = []  # 중간 리스트 생성
            for num in range(length):  # 회문 단어 길이만큼 반복
                new_row = row + num
                if 0 <= new_row < 8:  # 배열 내에서 실행
                    middle_list.append(your_list[new_row][column])
            if len(middle_list) == length:  # 회문 단어 길이와 같으면
                result_list.append(middle_list)  # 최종 리스트에 추가

    for column in range(8):
        for row in range(8):
            middle_list = []
            for num in range(length):
                new_column = column + num
                if 0 <= new_column < 8:
                    middle_list.append(your_list[row][new_column])

            if len(middle_list) == length:
                result_list.append(middle_list)

    count = 0  # 카운트 설정
    for word in result_list:  # 회문이면 카운트 1 증가
        reverse_word = word[::-1]
        if reverse_word == word:
            count += 1

    print(f"#{tc} {count}")
