import sys

T = int(sys.stdin.readline())
result = 0

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    result = a + b
    print ("Case #" + str(i + 1) + ": " + str(a) + " + " + str(b) + " = " + str(result))