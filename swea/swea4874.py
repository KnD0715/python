import sys

sys.stdin = open('input_4874.txt')

T = int(input())
for tc in range(1, T + 1):
    modify = list(map(str, input().split()))
    stack = [0] * len(modify)
    top = -1

    for x in modify:
        if x not in '+-*/.':
            top += 1
            stack[top] = int(x)

        elif x == '.':
            break

        else:
            if x == '+':
                num2 = stack[top]
                top -= 1
                num1 = stack[top]
                stack[top] = num1 + num2
            elif x == '-':
                num2 = stack[top]
                top -= 1
                num1 = stack[top]
                stack[top] = num1 - num2
            elif x == '*':
                num2 = stack[top]
                top -= 1
                num1 = stack[top]
                stack[top] = num1 * num2
            elif x == '/':
                num2 = stack[top]
                top -= 1
                num1 = stack[top]
                stack[top] = int(num1 / num2)

    if top == 0:
        print(f"#{tc} {stack[top]}")

    else:
        print(f"#{tc} error")
