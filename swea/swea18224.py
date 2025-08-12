import sys

sys.stdin = open('input_18224.txt')

T = int(input())
for tc in range(1, T + 1):
    line = list(map(str, input()))
    stack = [None] * len(line)
    ans = 1
    top = -1

    for i in line:
        if i == '(' or i == '{':
            if top == -1:
                top += 1
                stack[top] = i
            else:
                top += 1
                stack[top] = i
        elif i == ')':
            if stack[top] == '(':
                top -= 1
            else:
                ans = 0
                break
        elif i == '}':
            if stack[top] == '{':
                top -= 1
            else:
                ans = 0
                break

    if top != -1:
        ans = 0

    print(f"#{tc} {ans}")
