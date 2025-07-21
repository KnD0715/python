import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
max = max(lst)
min = min(lst)

print (f"{min} {max}")