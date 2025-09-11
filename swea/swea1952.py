import sys

sys.stdin = open('input_1952.txt')

T = int(input())
for tc in range(1, T + 1):
    price = list(map(int, input().split()))
    month = [0] + list(map(int, input().split()))
    expensive = [0] * 13
    answer = 0

    for i in range(1, 13):
        expensive[i] = min(price[0] * month[i], price[1]) + expensive[i - 1]

        if i > 2:
            expensive[i] = min(expensive[i], price[2] + expensive[i - 3])

        answer = min(expensive[12], price[3])

    print(f"#{tc} {answer}")
