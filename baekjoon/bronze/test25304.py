import sys

price = int(sys.stdin.readline())
N = int(sys.stdin.readline())
result = 0

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    result += (a * b)

if (price == result):
    print("Yes")
else:
    print("No")