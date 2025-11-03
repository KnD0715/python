import sys

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

N, K = map(int, sys.stdin.readline().split())

ans = factorial(N) // (factorial(N - K) * factorial(K))

print(ans)