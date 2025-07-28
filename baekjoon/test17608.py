import sys

my_list = []
count = 1
N = int(sys.stdin.readline())
for i in range(N):
    height = int(sys.stdin.readline())
    my_list.append(height)

reversed_list = list(reversed(my_list))
reverse_num = reversed_list[0]
for i in reversed_list:
    if i > reverse_num:
        count += 1
        reverse_num = i

print (count)