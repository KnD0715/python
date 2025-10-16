import sys

N = int(sys.stdin.readline())
count = 1
number = 1

while number < N:
    number += count * 6
    count += 1

print(count)