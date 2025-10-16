import sys

N, price = map(int, sys.stdin.readline().split())
count = 0
money = [int(sys.stdin.readline()) for _ in range(N)]
money.sort(reverse=True)

for m in money:
    count += price // m
    price %= m
    if price == 0:
        break

print(count)