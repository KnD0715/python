import sys
sys.stdin = open('input_1234.txt')

for tc in range(1, 11):
    N, password = map(str, input().split())
    password_list = list(password)
    stack = [None] * int(N)
    top = -1
    for i in password_list:
        if top == -1:
            top += 1
            stack[top] = i

        else:
            if stack[top] == i:
                top -= 1

            else:
                top += 1
                stack[top] = i

    print(f"#{tc}", ''.join(stack[:top + 1]))
