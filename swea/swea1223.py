import sys

sys.stdin = open('input_1223.txt')

for tc in range(1, 11):
    length = int(input())
    modify = list(input().strip())

    stack = [0] * (length + 1)
    top = -1
    icp = {'+': 1, '*': 2}

    fix_modify = ''

    for x in modify:
        if x not in '*+':
            fix_modify += x

        else:
            if top == -1 or icp[stack[top]] < icp[x]:
                top += 1
                stack[top] = x

            elif icp[stack[top]] >= icp[x]:
                while top > -1 and icp[stack[top]] >= icp[x]:
                    fix_modify += stack[top]
                    top -= 1

                top += 1
                stack[top] = x

    while top > -1:
        fix_modify += stack[top]
        top -= 1

    for num in fix_modify:
        if num not in "+*":
            top += 1
            stack[top] = int(num)

        else:
            if num == "+":
                num2 = stack[top]
                top -= 1
                num1 = stack[top]
                stack[top] = num1 + num2
            elif num == "*":
                num2 = stack[top]
                top -= 1
                num1 = stack[top]
                stack[top] = num1 * num2

    print(f"#{tc} {stack[top]}")
