import sys

h, m = map (int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

min = int (h * 60 + m + c)

hour = int (min // 60 % 24)
min = int (min % 60)

print (str(hour) + " " + str(min))