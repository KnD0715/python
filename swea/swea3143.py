import sys

sys.stdin = open('input_3143.txt')

T = int(input())
for tc in range(1, T + 1):
    word, pattern = input().split()

    num = len(pattern)  # 패턴 길이

    count = 0
    pattern_count = 0
    while count <= len(word) - num:  # 단어의 길이와 패턴의 길이를 뺀 만큼 반복
        if word[count:count + num] == pattern:  # 단어와 패턴의 길이가 같다면
            pattern_count += 1  # 패턴 카운트 1 증가
            count += num  # 카운트 패턴 길이만큼 증가
        else:
            count += 1

    result = len(word) - pattern_count * (num - 1)  # 단어 길이에서 패턴 횟수에 패턴 길이에 1을 뺀 값의 곱만큼 뻄

    print(f"#{tc} {result}")
