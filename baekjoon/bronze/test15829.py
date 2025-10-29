import sys

L = int(sys.stdin.readline())
r = 31
M = 1234567891

word = sys.stdin.readline().strip()

result = 0

for i in range(len(word)):
    num = ord(word[i]) - 96
    result += num * (r ** i)

print(result % M)
