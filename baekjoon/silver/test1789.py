import sys

N = int(sys.stdin.readline())
i = 0
total = 0

while total < N:
    i += 1
    total += i
    if total > N:
        i -= 1
        break
print(i)
