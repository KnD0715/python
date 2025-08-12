import sys

sys.stdin = open('input_18225.txt')

T = int(input())
for tc in range(1, T + 1):
    word = list(input())
    stack = [None] * len(word)
    top = 0

    for i in word:
        if top == 0:
            stack[top] = i
            top += 1
        else:
            if stack[top - 1] == i:
                top -= 1
            else:
                stack[top] = i
                top += 1

    print(f"#{tc} {top}")
