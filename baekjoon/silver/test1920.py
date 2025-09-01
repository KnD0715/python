import sys

N = int(sys.stdin.readline())
num_list = set(map(int, input().split()))

M = int(sys.stdin.readline())
check_list = list(map(int, input().split()))

for i in check_list:
    print(1 if i in num_list else 0)