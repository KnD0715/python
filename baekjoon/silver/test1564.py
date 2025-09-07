import sys

N = int(sys.stdin.readline())

result = 1
for i in range(1, N + 1):
    result *= i

    while result % 10 == 0:
        result //= 10

    result %= 10 ** 13
print(str(result)[-5:])