from collections import deque
import sys

sys.stdin = open('input_18401.txt')

T = int(input())
for tc in range(1, T + 1):
    oven_size, pizza_num = map(int, input().split())
    pizza_list = deque(enumerate(list(map(int, input().split())), 1))
    oven = deque()

    for i in range(oven_size):
        oven.append(pizza_list.popleft())

    while len(oven) > 1:

        if len(oven) < oven_size and pizza_list:
            oven.append(pizza_list.popleft())

        pizzaNumber, cheese = oven.popleft()

        if not cheese // 2:
            continue
        else:
            oven.append((pizzaNumber, cheese // 2))

    print(f"#{tc} {oven.popleft()[0]}")
