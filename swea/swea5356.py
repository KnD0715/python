import sys

sys.stdin = open('input_5356.txt')

T = int(input())
for i in range(1, T + 1):
    word_list = [list(input()) for _ in range(5)]

    result_list = []
    for column in range(15):
        for row in range(5):
            if column < len(word_list[row]):
                result_list.append(word_list[row][column])

    print(f"#{i}", ''.join(result_list))
