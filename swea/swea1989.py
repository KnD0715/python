import sys

sys.stdin = open('input_1989.txt')

T = int(input())
for tc in range(1, T + 1):
    word = input()
    reverse_word = word[::-1]
    if word == reverse_word:
        result = 1
    else:
        result = 0

    print(f"#{tc} {result}")
