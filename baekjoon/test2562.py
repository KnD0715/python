import sys
my_list = []

for i in range(9):
    my_list += list(map(int,sys.stdin.readline().split()))

max = max(my_list)
index = my_list.index(max)
index += 1

print (f"{max}\n{index}")