import sys

sys.stdin = open('input_18223.txt')


def max_value(num):  # 최대값 함수
    max_num = 0

    for i in num:
        if max_num < i:
            max_num = i

    return max_num


T = int(input())
for i in range(1, T + 1):
    word1 = list(input())
    word2 = list(input())

    count_list = []  # 카운트를 넣을 빈 리스트 생성

    for alphabet in word1:  # 첫 번째 단어의 알파벳 하나씩 반복
        count = 0
        for alpha in word2:  # 두 번째 단어의 알파벳 하나씩 반복
            if alphabet == alpha:  # 같으면 1 증가
                count += 1
            count_list.append(count)  # 리스트 추가

    print(f"#{i} {max_value(count_list)}")
