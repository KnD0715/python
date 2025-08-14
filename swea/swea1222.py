import sys

sys.stdin = open('input_1222.txt')

for tc in range(1, 11):
    length = int(input())
    calculation = list(input())
    stack = [0] * (length + 1)
    top = -1
    fix_modify = ''

    for x in calculation:
        if x not in '+':
            fix_modify += x
        else:
            if top == -1:
                top += 1
                stack[top] = x

            elif top == 0:
                fix_modify += stack[top]

    top -= 1
    for num in fix_modify:
        if num not in '+':
            top += 1
            stack[top] = int(num)

        else:
            num2 = stack[top]
            top -= 1
            num1 = stack[top]
            top -= 1
            if num == '+':
                top += 1
                stack[top] = num1 + num2
    top -= 1
    stack[top] = num1 + num2
    print(f"#{tc} {stack[top] + int(num)}")
