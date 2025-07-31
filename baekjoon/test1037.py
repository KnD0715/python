import sys

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

max = max(num_list)
min = min(num_list)

if len(num_list) == 1:
    print (num_list[0] ** 2)

else:
    print (max * min)
