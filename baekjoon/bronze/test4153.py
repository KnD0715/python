import sys

while True:
    A, B, C = map(int, sys.stdin.readline().split())
    if A == 0 & B == 0 & C == 0:
        break

    num_list = [A, B, C]
    num_list.sort()

    if (num_list[0] ** 2) + (num_list[1] ** 2) == (num_list[2] ** 2):
        print('right')

    else:
        print('wrong')