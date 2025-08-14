import sys

sys.stdin = open('input_18389.txt')

T = int(input())
for tc in range(1, T + 1):
    modify = list(input().strip())
    stack = [0] * (len(modify) + 1)
    icp = {"(": 3, "+": 1, "-": 1, "*": 2, "/": 2}
    isp = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2}
    top = -1

    result = ''
    for x in modify:
        if x not in '(+-*/)':
            result += x

        elif x == ')':
            while stack[top] != '(':
                result += stack[top]
                top -= 1
            top -= 1

        else:
            if top == -1 or isp[stack[top]] < icp[x]:
                top += 1
                stack[top] = x

            elif isp[stack[top]] >= icp[x]:
                while top > -1 and isp[stack[top]] >= icp[x]:
                    result += stack[top]
                    top -= 1

                top += 1
                stack[top] = x

    while top > -1:
        result += stack[top]
        top -= 1

    print(f"#{tc} {result}")
