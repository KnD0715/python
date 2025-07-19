import sys

N = int(sys.stdin.readline())
long = ""

for i in range(N//4):
    long += "long "

print(long + "int")