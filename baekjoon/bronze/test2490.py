import sys

for i in range(3):
    yut = list(map(int, sys.stdin.readline().split()))

    if yut.count(1) == 0:
        print('D')

    elif yut.count(1) == 1:
        print('C')

    elif yut.count(1) == 2:
        print('B')

    elif yut.count(1) == 3:
        print('A')

    elif yut.count(1) == 4:
        print('E')