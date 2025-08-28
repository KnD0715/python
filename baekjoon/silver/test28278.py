import sys

T = int(sys.stdin.readline())
stack = []

for _ in range(T):
    num = list(sys.stdin.readline().split())

    if num[0] == '1':
        stack.append(num[1])

    elif num[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))

    elif num[0] == '3':
        print(len(stack))

    elif num[0] == '4':
        if stack:
            print(0)
        else:
            print(1)

    elif num[0] == '5':
        if not stack:
            print(-1)
        else:
            print(stack[-1])