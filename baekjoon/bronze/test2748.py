import sys

num_list = [0, 1]
num = int(sys.stdin.readline())

for i in range(2, num + 1):
    num_list.append(num_list[i - 1] + num_list[i - 2])

print (num_list[num])