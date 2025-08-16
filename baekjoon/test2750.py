import sys

T = int(sys.stdin.readline())
num_list = []
for _ in range(T):
    num = int(sys.stdin.readline())
    num_list.append(num)

for number in sorted(num_list):
    print(number)