import sys

num_list = []
for _ in range(5):
    num = int(sys.stdin.readline())
    num_list.append(num)
sorted_list = sorted(num_list)
print(int(sum(num_list) / 5))
print(sorted_list[2])
