import sys

num = int(sys.stdin.readline())
star = '*'
blank = ' '
for i in range(num):
    print(blank * (num - i - 1) + star * (i * 2 + 1))

for i in range(num - 1):
    print(blank * (i + 1) + star * ((num - i - 2) * 2 + 1))
