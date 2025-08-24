import sys

N = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
max = max(my_list)
min = min(my_list)

print (f"{min} {max}")