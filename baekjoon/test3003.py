import sys

chess = [1, 1, 2, 2, 2, 8]

pieces = list(map(int, sys.stdin.readline().split()))

result = []
for i in range(len(chess)):
    result.append(chess[i] - pieces[i])

print (*result)
