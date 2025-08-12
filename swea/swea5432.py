import sys

sys.stdin = open('input_5432.txt')

T = int(input())
for tc in range(1, T + 1):
    stick = list(input())
    count = 0
    stack = []

    for i in range(len(stick)):
        if stick[i] == '(':
            stack.append(stick[i])
        else:
            if stick[i - 1] == '(':
                stack.pop()
                count += len(stack)

            else:
                stack.pop()
                count += 1

    print(f"#{tc} {count}")
