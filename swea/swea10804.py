import sys

sys.stdin = open('input_10804.txt')

T = int(input())
for i in range(1, T + 1):
    word = list(input())
    reverse_word = word[::-1]  # 단어 역순

    result_list = []  # 결과 값을 넣을 빈 리스트 생성
    for alphabet in reverse_word:
        if alphabet == 'b':
            result_list.append('d')
        elif alphabet == 'd':
            result_list.append('b')
        elif alphabet == 'p':
            result_list.append('q')
        elif alphabet == 'q':
            result_list.append('p')

    print(f"#{i}", ''.join(result_list))
