import sys

N = int(sys.stdin.readline())
result = 0
for i in range(1, 10):
    result = N * i
    print(str(N) + " * " + str(i) + " = " + str(result))