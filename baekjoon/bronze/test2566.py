import sys

num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
max_num = 0
max_row = 0
max_index = 0
for row in range(9):
    for column in range(9):
        if max_num <= num_list[row][column]:
            max_num = num_list[row][column]
            max_row = row + 1
            max_index = column + 1

print(max_num)
print(max_row, max_index)