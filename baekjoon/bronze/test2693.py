import sys

N = int(sys.stdin.readline())

for _ in range(N):
    num_list = list(map(int, sys.stdin.readline().split()))
    num_list.sort(reverse=True)

    print(num_list[2])