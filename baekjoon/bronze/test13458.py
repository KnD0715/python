import sys
import math

N = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))
A, B = map(int, sys.stdin.readline().split())

count = 0
for i in students:
    i -= A
    count += 1

    if i > 0:
        count += math.ceil(i / B)

print (count)