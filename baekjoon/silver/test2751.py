import sys

N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
    num = int(sys.stdin.readline())
    num_list.append(num)

for i in sorted(num_list):
    print(i)
