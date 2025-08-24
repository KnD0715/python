import sys

sugar = int(sys.stdin.readline())

count = 0
if sugar % 5 == 0:
    print(sugar // 5)

else:
    while sugar > 0:
        sugar -= 3
        count += 1
        if sugar % 5 == 0:
            print(count + sugar // 5)
            break
        elif sugar == 1 or sugar == 2:
            print(-1)
            break
        elif sugar == 0:
            print(count)
            break