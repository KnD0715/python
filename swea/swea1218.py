import sys

sys.stdin = open('input_1218.txt')

for tc in range(1, 11):
    length = int(input())
    bracket_list = list(input())
    stack = [None] * length

    ans = 1
    top = -1

    for i in bracket_list:
        if i == '{' or i == '(' or i == '[' or i == '<':
            if top == -1:
                top += 1
                stack[top] = i
            else:
                top += 1
                stack[top] = i

        elif i == '}':
            if stack[top] == '{':
                top -= 1
            else:
                ans = 0
                break

        elif i == ')':
            if stack[top] == '(':
                top -= 1
            else:
                ans = 0
                break

        elif i == ']':
            if stack[top] == '[':
                top -= 1
            else:
                ans = 0
                break

        elif i == '>':
            if stack[top] == '<':
                top -= 1
            else:
                ans = 0
                break

    print(f"#{tc} {ans}")
