import sys

N = int(sys.stdin.readline())
blank = ' '
star = '*'

for i in range(N):
    result = (blank * i) + (star * (N - i))
    print(result)