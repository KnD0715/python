import sys

N = list(sys.stdin.readline().strip())

N.sort(reverse=True)

for num in N:
    print(num, end='')
