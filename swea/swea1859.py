import sys

sys.stdin = open('input_1859.txt')

T = int(input())
for tc in range(1, T + 1):
    length = int(input())
    num_list = list(map(int, input().split()))

    profit = 0
    stack = []

    for i in range(length - 1, -1, -1):
        if not stack or stack[-1] < num_list[i]:
            stack.append(num_list[i])

        else:
            profit += stack[-1] - num_list[i]

    print(f"#{tc} {profit}")
