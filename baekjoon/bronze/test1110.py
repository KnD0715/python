import sys

N = int(sys.stdin.readline())
num = N
count = 0

while True:
    first = num // 10
    second = num % 10
    third = (first + second) % 10
    num = (second * 10) + third

    count += 1
    if num == N:
        break

print(count)